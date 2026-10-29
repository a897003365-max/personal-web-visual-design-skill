# 个人网页视觉设计技能包

一个可跨项目使用的个人网页视觉规范入口，适用于官网、产品界面、内容页、作品展示和数据页面。默认方向是中文清晰、标题有分量、重点醒目、信息紧凑而有留白；页面结构随目标与内容调整。

## 内容

- `skills/personal-web-visual-design/`：主技能、网页视觉规范、按需使用的数据展示规范、验收清单和视觉资产。
- `skills/impeccable/`：Impeccable 4.1.2 快照、参考文档、脚本和固定版本的 HTML/CSS 静态解析依赖。
- `skills/anti-defensive-writing/`：页面说明和交付表达技能。
- Radix Colors 3.0.0 色板，Noto Sans SC 与 Barlow Semi Condensed 字体及许可证。
- `scripts/install.py` 与 `scripts/validate_package.py`：离线安装、文件摘要、引用及资源校验。

Radix Colors 和 Fontsource 是资源来源，调色实施技能是 Impeccable。来源与许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 安装与使用

在仓库根目录运行（Python 3.10+）：

```text
python scripts/validate_package.py
python scripts/install.py
```

默认安装到 `CODEX_HOME/skills`；未设置时使用当前用户的 `.codex/skills`。其他平台可显式指定其技能发现目录：

```text
python scripts/install.py --target /path/to/agent/skills
```

安装先检查全部目标；相同文件复用，只补齐缺失文件，发现内容冲突即停止。安装器不覆盖现有版本。Impeccable 静态解析脚本需要 Node.js 20.19.0 或更新，解析依赖已在包内。浏览器能力由当前环境提供。

安装后在下一轮支持技能发现的会话中使用：

```text
使用 $personal-web-visual-design 设计当前产品官网，沿用我的配色、字体和留白规范。
```

```text
使用 $personal-web-visual-design 只读检查这个页面的视觉层级与窄屏体验。
```

```text
使用 $personal-web-visual-design 改进当前数据页面，落实表格留白、灯箱、图例显隐和默认数据标签。
```

主技能保留自动发现。一般网页读取视觉规范；页面含表格、指标或图表时才使用相应的数据展示要求。

## 维护

规范主版本位于本仓库 `skills/personal-web-visual-design/references/`。新增偏好经确认后更新对应主题、稳定锚点和验收清单，不固定条目总数，也不依赖某个业务项目的本地文档。

修改完成后执行：

```text
python scripts/validate_package.py --refresh-manifest
python scripts/validate_package.py
```

同步安装副本前比对差异并保留必要备份；第三方技能保留各自来源与许可。平台发现路径、主版本与同步方法见[维护说明](skills/personal-web-visual-design/references/maintenance.md)。

个人规范与配套技能在私有仓库维护。普通网页任务按目标项目流程交付；维护本技能不自动改写业务项目或发布网页。
