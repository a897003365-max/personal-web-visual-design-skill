---
name: personal-web-visual-design
description: "按个人网页视觉规范设计、改版和审查网站、产品界面、内容页及数据页面，统一配色、字体、留白、组件与交互细节。用于需要沿用个人审美与视觉标准的网页工作。"
---

# 个人网页视觉设计

将个人视觉偏好落实到当前网页。默认方向是中文清晰、标题有分量、重点醒目、信息紧凑而有留白。根据页面用途安排内容与表现方式，使用当前用户要求和项目已确认的品牌约束。

## 开始工作

- 读取目标项目规则、现有页面与主题，明确本次是设计、实现、局部改版还是只读审查，以及具体页面和文件范围。
- 读取[网页视觉规范](references/web-visual-standards.md)，作为配色、字体、布局、组件和响应式的主依据。
- 页面包含指标、表格或数据图表时，再读取[数据展示规范](references/data-display.md)的相关部分。官网、文章和作品展示页按自身内容组织，不因启用本技能而增加指标卡、筛选器或图表。
- 按[设计与验收清单](references/design-workflow.md#design-workflow)完成适用检查。只读审查给出有页面证据的问题与建议；规范维护按[维护说明](references/maintenance.md)执行。

## 使用配套技能与资源

- 视觉设计或改版：读取同级 [Impeccable](../impeccable/SKILL.md)，按当前任务选择其参考流程。调色默认使用 [colorize](../impeccable/reference/colorize.md)，字体用 [typeset](../impeccable/reference/typeset.md)。页面用途决定设计模式，不固定为后台或看板。
- 页面说明、注释和交付文案：读取同级 [anti-defensive-writing](../anti-defensive-writing/SKILL.md)，直接表达，克制解释。
- Radix Colors 是默认色板；Fontsource 提供 Noto Sans SC 和 Barlow Semi Condensed 的自托管字体。使用[资产说明](references/assets.md)中的本地资源与许可证。
- 个人已确认的字体、语义色、表格留白和必显数据标签要求优先于依赖技能的通用审美建议。项目明确指定其他品牌时记录本次映射和差异。
- 依赖按需加载，工具和运行时按实际环境核验。执行脚本使用当前安装目录，工作目录保持为目标项目；完整分工见[依赖地图](references/dependencies.md)。

## 必查入口

- 所有选择与筛选控件：[统一边框与组合状态](references/web-visual-standards.md#control-borders)。
- 数据页面：[表格](references/data-display.md#tables)、[必显数据标签](references/data-display.md#chart-labels)及相关图表交互。
- 内容图片与说明：[灯箱](references/web-visual-standards.md#images)、[克制注释](references/web-visual-standards.md#copy)。
- 复用目标项目现有组件、框架与主题接口；本技能负责视觉与交互，不规定业务计算、采集机制或部署架构。

## 验收与维护

- 输出实际改动、已验证结果和未完成项。提交、推送和部署按当前任务授权与项目流程执行。
- 本技能包是个人规范的主版本，规范正文、验收清单与维护流程各保留一处；入口只引用，不重复正文。
