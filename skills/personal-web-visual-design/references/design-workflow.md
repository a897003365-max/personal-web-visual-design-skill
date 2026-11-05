# 网页设计与验收清单

每次任务选择适用项。规范编辑、只读审查、设计预览和页面实现按当前请求范围执行。

<a id="design-workflow"></a>
## 设计、实施与验收

- [ ] 确认页面用途、受众、内容、现有品牌、目标尺寸及本次文件范围；读取[视觉规范](web-visual-standards.md)。
- [ ] 按页面用途组织内容，确定重点、阅读顺序、配色角色、字体层级和间距，复用当前项目已有组件与主题。
- [ ] 实施时保持同类组件对齐、边缘留白、文字与背景对比度、必要状态反馈和[克制说明](web-visual-standards.md#copy)。
- [ ] 按[边框规范的验收项](web-visual-standards.md#control-borders)检查所有原生和自定义选择／筛选控件及状态组合。
- [ ] 检查真实字体加载、长名称、大数值、键盘焦点、浮层关闭、图片灯箱及受影响的操作路径。
- [ ] 按[响应式规范](web-visual-standards.md#responsive)检查目标尺寸与承载环境，覆盖支持的亮暗主题。
- [ ] 用现有项目工具完成与改动相关的检查；检查实际呈现与交互，修复后重验受影响范围。
- [ ] 交付时说明实际改动和验证结果，区分静态检查、浏览器模拟与真机验证；列出未完成项。

<a id="data-checks"></a>
## 页面含数据展示时

- [ ] 按[数值规则](data-display.md#values)与[变化语义](data-display.md#change)核对读数，换算覆盖 `10000` 边界。
- [ ] 按[表格规则](data-display.md#tables)及其后续章节检查布局、冻结、排序分页和展开。
- [ ] 按[数据标签](data-display.md#chart-labels)、[图例](data-display.md#chart-legend)检查默认显示、显隐联动和恢复。
- [ ] 按[图形与坐标](data-display.md#chart-marks)、[图表类型](data-display.md#chart-type)核对比例及边界状态。
- [ ] 验证当前页面涉及的[日期](data-display.md#date)、[配置](data-display.md#config)、[加载刷新](data-display.md#states)操作。

## 规范维护时

- [ ] 新增偏好已获确认，写入唯一对应正文并保持锚点稳定；同步本文件及相关入口。
- [ ] 检查相对链接、资源引用和平台副本，按[维护说明](maintenance.md)验证及同步。
- [ ] 将规范更新、实际页面实现与网页发布分别记录。
