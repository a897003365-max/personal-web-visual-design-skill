# 技能依赖与加载范围

本包提供一个日常入口 `personal-web-visual-design`，并附带它需要的两个完整技能目录。依赖仅在任务需要时加载。

| 依赖 | 包内路径 | 使用场景 |
|---|---|---|
| Impeccable 4.1.2 本地快照 | [SKILL.md](../../impeccable/SKILL.md) | 视觉设计与界面改进；调色使用 colorize，页面用途决定设计模式 |
| anti-defensive-writing 用户本地版本 | [SKILL.md](../../anti-defensive-writing/SKILL.md) | 页面注释、口径说明、审查及交付文案 |

Impeccable 的常用入口：[新页面](../../impeccable/reference/new-work.md)、[调色](../../impeccable/reference/colorize.md)、[操作与阅读界面](../../impeccable/reference/operate.md)、[字体](../../impeccable/reference/typeset.md)、[布局](../../impeccable/reference/layout.md)、[适配](../../impeccable/reference/adapt.md)、[检查](../../impeccable/reference/audit.md)、[收尾](../../impeccable/reference/polish.md)。官网、工具、内容页与作品页按各自目标选用流程。遵循实际脚本和工具条件，不因文件存在就声称浏览器或其他运行能力可用。

## 资源不是独立技能

- Radix Colors 是配色资源，已包含实际 CSS 和 MIT 许可证。
- Fontsource 是字体来源，已包含 Noto Sans SC、Barlow Semi Condensed 的自托管字体及许可证。
- 本包不把这两项描述成官方独立 Skill，也不需要调用外部 CDN 才能使用所附资产。

资源路径与引用方式见[资产说明](assets.md)。第三方许可位于各资产目录以及本技能的 `licenses/` 目录，仓库根 `THIRD_PARTY_NOTICES.md` 记录来源。
