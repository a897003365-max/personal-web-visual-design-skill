# 第三方技能与资源

本包的定制规范和主技能用于个人私有维护。本文件说明所附依赖的来源与随附许可，不将所有内容统一改授其他许可证。

| 内容 | 来源 | 随附许可 |
|---|---|---|
| Impeccable 4.1.2 本地快照 | https://github.com/pbakaus/impeccable | `skills/mds-dashboard-development/licenses/impeccable-LICENSE.txt`，Apache-2.0 |
| Impeccable 静态解析依赖 | 官方 npm 的 htmlparser2、css-select、css-tree、domutils 及其传递依赖，版本见 package-lock.json | 各自 node_modules 包内的 LICENSE／许可元数据 |
| anti-defensive-writing | 用户共享技能目录的原文快照；打包时同名 Codex 副本指纹一致 | 本地源文件未附独立许可，仅随个人私有包保存，不宣称第三方开源授权 |
| Radix Colors 3.0.0 | https://github.com/radix-ui/colors 与官方 npm `@radix-ui/colors` | `assets/radix-colors/3.0.0/LICENSE`，MIT |
| Noto Sans SC | https://fontsource.org/fonts/noto-sans-sc/about；`@fontsource-variable/noto-sans-sc@5.3.1` | `assets/fonts/noto-sans-sc/LICENSE`，OFL-1.1 |
| Barlow Semi Condensed | https://fontsource.org/fonts/barlow-semi-condensed/about；`@fontsource/barlow-semi-condensed@5.3.0` | `assets/fonts/barlow-semi-condensed/LICENSE`，OFL-1.1 |

表中 `assets/` 路径位于 `skills/mds-dashboard-development/`。字体与配色来自校验 SHA-512 integrity 的 npm 发布包；文件清单记录各文件 SHA-256。技能目录从本机已使用版本复制，未宣称与上游当前主干完全一致。

## 打包适配

- 规范正文只调整项目入口的相对链接，原条款保持不变。
- 开发清单摘取看板章节并修正项目特定的流程指代，未复制原项目的持续发布授权。
- 字体样张增加独立 HTML 外壳，将字体链接改成相对本地资源；示例值仍是排版样例。
- 定制技能入口、依赖地图和语义变量入口属于本次打包内容。
- Impeccable 原有技能、参考和脚本保持原样；新增 package.json、package-lock.json 和静态解析库以支持其完整 HTML/CSS 检测。安装使用 `--ignore-scripts`，未执行依赖的安装脚本。
