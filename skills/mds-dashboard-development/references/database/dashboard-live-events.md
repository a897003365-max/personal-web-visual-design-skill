# 看板数据库变更通知与版本对账

运营总览、天猫明细与抖音明细使用 PostgreSQL 通知，经同源 SSE 按版本更新当前模块。

## 数据与事务版本

- 0060 冻结 18 张源表与主题映射：mds 8 张、maizi 10 张；0061_dashboard_versions 增加每库版本表并升级同名触发器和函数。
- public.mds_dashboard_versions 每主题一行，包含 topic、generation UUID、revision BIGINT；mds 4 行、maizi 5 行。generation 首次创建时产生，幂等升级不重置；revision 在源写入事务内递增，回滚时也回滚。
- mds 主题为 overview、tmall、tmall_product、tmall_channels；maizi 另包含 tmall_competitor、douyin，商品映射也更新对应天猫主题。向量键采用“数据库:主题”，避免两个库相同主题互相覆盖。
- 0061 使用语句级 BEFORE INSERT/UPDATE/DELETE/TRUNCATE 触发器。版本更新和 NOTIFY 与源写入同事务，提交后才可见。零行写入语句也可能推进版本。
- 函数为 SECURITY DEFINER、search_path 限定 pg_catalog，完全限定版本表和通知函数，撤销 PUBLIC EXECUTE；普通采集账号无需获得版本表写权限。
- 受监控 DML 在拿源数据行锁前，按固定顺序锁定本库 4/5 行版本元数据，避免 SKU 优先和商品优先写入与版本锁形成循环。锁随业务事务提交释放；同库受监控写事务会短暂串行，读取不受行锁阻塞。大批量维护和 TRUNCATE 应与采集错开。

## SSE 与页面确认

- /api/v1/analytics/live-events 复用 Cookie 登录、有效账号、会话版本、强制改密与页面权限。总览使用 analytics.view/manage，天猫使用 dashboard.view，抖音使用 douyin.view。
- 分别在两个库注册只读 autocommit LISTEN；全部订阅完成并取得完整版本元数据后发送 ready。版本查询使用另外的短只读事务，不占用 LISTEN 连接。
- ready、change、versions 均携带获准主题的版本向量，revision 用十进制字符串发送，避免浏览器整数精度损失。通知不含业务行、凭据或连接信息。
- 无变更通知时每 180 秒查询少量版本行，发送 versions，发现漏掉的通知；收到通知立即读取版本并发送 change，随后重新计时。首次打开和重连仍立即取得版本。
- 每 15 秒用 SSE 注释保活并重验权限，避免代理空闲超时；保活不查询版本表或业务数据。业务数据仅在页面版本落后时补读。
- 每文档共享一条 EventSource，每个日期/账号/商品筛选实例维护独立的成功已读版本。首次实例读取一次，之后只有版本不同才查数据；同版本重连只清除连接错误。
- 只在查询成功后确认开始时捕获的版本；在途出现更新版本，完成后再补读。隐藏页积累版本，恢复后只补落后部分；旧筛选和旧连接晚到响应不确认当前版本。
- 失败不推进确认版本；每个目标版本最多额外自动重试 3 次，间隔 2 秒。同版本心跳不重开耗尽预算，提示与待同步状态保留；可手动重试，或在新版本、恢复可见/联网时再次有限补读。SKU 独立记录失败，概览成功不会吞掉 SKU 失败。
- 连接错误可见，EventSource 原生重连，无业务轮询降级；最后一个读者卸载时关闭连接并取消定时器。
- 总览落后后重新查询快照，不按行 ID 缓存 payload。Nginx 关闭流缓冲并透传 X-Accel-Buffering。

## 安装与回退

- 标准 Alembic 在 mds 按 0060 → 0061 执行；外部 maizi 不运行应用迁移链。已有通知对象使用 python -B -m scripts.dashboard_notifications check|install|uninstall --database mds|maizi，写入还需精确的 --confirm-database。
- 运维命令核对数据库、源表、函数体/权限模式、触发器阶段/参数及版本表后事务升级；0061 安装/回退先用 NOWAIT 短锁检查源表，繁忙立即拒绝，不等待占锁切换。
- 预览只显式安装本功能对象，保留正式 alembic_version，不自动执行其他迁移。API 保持只读事务，不新增运行角色写权限。
- 升级前保存通知函数、触发器结构与对象状态；备份位于构建上下文之外。回退 0061 恢复 0060 通知函数和 AFTER 触发器、移除新版本表，保留源数据及原 18 个通知触发器。

## 验收

隔离 PostgreSQL 覆盖提交/回滚、漏通知对账、重连、幂等/回退、普通 writer 权限、并发 SKU/商品写入及繁忙源表拒绝升级。浏览器覆盖同版本多次心跳零业务请求、版本推进一次补读、503 有限重试与手动恢复、同版本重连不取数、筛选及展开保持。
