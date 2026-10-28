# MDS 数据看板开发技能包

将用户确认的 MDS 中文电商数据看板规范打包为一个主技能入口，并附带所需技能和自托管视觉资源。规范持续追加，不固定条款总数。

## 内容

- `skills/mds-dashboard-development/`：主技能、完整规范、开发清单、MDS 更新契约及视觉资产。
- `skills/impeccable/`：当前使用的 Impeccable 4.1.2 快照，包含参考文档、脚本，以及静态 HTML/CSS 检查需要的固定解析依赖。
- `skills/anti-defensive-writing/`：用户本地文案技能，负责说明文字与交付表达。
- Radix Colors 3.0.0 六组亮／暗色板；Noto Sans SC、Barlow Semi Condensed 字体及许可证。
- `scripts/install.py`：本地安装；已有不同版本会明确停止，不覆盖。
- `scripts/validate_package.py`：文件指纹、引用、资产及基本技能结构校验。

Radix Colors 和 Fontsource 是资源来源，实际调色技能是 Impeccable。第三方来源见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 使用

在仓库根目录运行（Python 3.10+）：

```text
python scripts/validate_package.py
python scripts/install.py
```

默认安装到 `CODEX_HOME/skills`，未设置 CODEX_HOME 时使用当前用户的 `.codex/skills`。也可显式选择其他平台的技能发现目录：

```text
python scripts/install.py --target /path/to/agent/skills
```

安装会先检查全部目标；已有相同内容直接复用，主体一致但缺少文件时只补齐缺失文件，内容冲突则停止并指出目录。程序没有覆盖、删除、下载或自动发布步骤。执行 Impeccable 脚本仍需本机提供 Node.js；所附静态解析库要求 Node.js 20.19.0 或更新，已包含在包中。浏览器等外部工具按实际任务能力使用。

安装完成后，在支持技能发现的下一轮会话中使用：

```text
使用 $mds-dashboard-development 检查当前天猫看板，只读列出与规范的差异。
```

或：

```text
使用 $mds-dashboard-development 改进当前看板的表格、图例和图片灯箱，按项目流程验证。
```

主技能保留自动发现；实现、审查、规范编辑和发布的权限由当前用户请求及目标项目规则决定。调用技能不代表授权生产部署或数据写入。

## 维护

MDS 本地规范仍为规则主版本。用户确认新增条款后，更新包内规范快照、相关入口、开发清单与文件清单；已有编号保持稳定。规范正文中的项目入口已改为包内项目上下文，其余条款原样保留。

本仓库是用户于 2026-10-28 明确授权创建的个人私有技能备份，与 MDS 应用仓库的本地规范维护规则分开。包内不包含账号凭据、业务行数据、生产环境文件或完整项目运行状态。

审核更新内容后，执行 `python scripts/validate_package.py --refresh-manifest` 更新文件摘要，再执行不带选项的校验，随后打包或同步到私有仓库。该选项只更新当前包的文件摘要；修改规范或依赖版本时还须更新清单中的来源摘要。校验不要求固定条款总数。Git 保留包内文件字节，便于不同机器核对摘要。
