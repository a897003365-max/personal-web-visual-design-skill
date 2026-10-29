# 自托管视觉资产

资产仅供目标项目按需复制或接入，不会由本技能自动覆盖现有主题或页面。

| 内容 | 包内路径 | 使用方式 |
|---|---|---|
| Radix Colors 3.0.0 | `../assets/radix-colors/3.0.0/` | slate、teal、blue、amber、tomato、violet，含亮／暗色 CSS 与 LICENSE |
| Noto Sans SC 可变字体 | `../assets/fonts/noto-sans-sc/` | 通过 index.css 按 unicode-range 加载中文分片；按规范选择字重 |
| Barlow Semi Condensed | `../assets/fonts/barlow-semi-condensed/` | 提供 500、600、700 字重 CSS 及其 WOFF／WOFF2 字体 |
| 语义变量入口 | [web-theme.css](../assets/web-theme.css) | 使用 `data-personal-web` 作用域与 `--pw-*` 变量管理颜色、字体和间距 |
| 字体层级样张 | [typography-preview.html](../assets/typography-preview.html) | 使用示例内容，演示字体、数字和层级 |

完整保留相对目录后即可自托管。在容器上使用 `data-personal-web`，需应用数字字体的元素使用 `data-personal-number`。亮暗主题沿用 Radix 的 `.light`／`.dark` 或 `.light-theme`／`.dark-theme` 类，将主题类放在容器或祖先元素上。

在当前项目实际构建链、嵌入容器和图表文字中验证字体加载。样张用于核验字体与版式，示例数值不作为业务数据；具体组件行为以规范及当前任务为准。

无需为了接入这些静态资源强制新增 React、shadcn、Tailwind 或新的图表库。沿用目标项目已有组件与工具链。
