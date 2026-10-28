# 自托管视觉资产

资产仅供目标项目按需复制或接入，不会由本技能自动覆盖现有主题或页面。

| 内容 | 包内路径 | 使用方式 |
|---|---|---|
| Radix Colors 3.0.0 | `../assets/radix-colors/3.0.0/` | slate、teal、blue、amber、tomato、violet，含亮／暗色 CSS 与 LICENSE |
| Noto Sans SC 可变字体 | `../assets/fonts/noto-sans-sc/` | 通过 index.css 按 unicode-range 加载中文分片；按规范选择字重 |
| Barlow Semi Condensed | `../assets/fonts/barlow-semi-condensed/` | 提供 500、600、700 字重 CSS 及其 WOFF／WOFF2 字体 |
| 语义变量入口 | [dashboard-theme.css](../assets/dashboard-theme.css) | 颜色与字体变量集中管理，组件按业务角色使用 |
| 已确认字体样张 | [typography-preview.html](../assets/typography-preview.html) | 示例数据，只作为字体与层级参考 |

完整保留相对目录后即可自托管。上线前在当前项目实际构建链、同源 iframe 和图表文字中验证字体加载；不要因 CSS 声明了字体名就认定已生效。

样张保留用户确认字体时的版式；后来确认的表格留白、数据口径和交互条款以规范正文为准。示例数值不能用作业务数据或线上验收证据。

无需为了接入这些静态资源强制新增 React、shadcn、Tailwind 或新的图表库。沿用目标项目已有组件与工具链。
