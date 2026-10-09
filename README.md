# 大鲤鱼超级工作站

把 AI 服务的场景、交付方法和案例组织成可浏览的产品目录，探索“部门即服务”的业务表达。

**[在线浏览](https://hankjun.github.io/dalyu-workstation/)** · [服务场景](https://hankjun.github.io/dalyu-workstation/scenes.html) · [项目案例](https://hankjun.github.io/dalyu-workstation/cases.html)

A static service catalog and case-study website for AI-enabled business workflows.

## 项目定位

面向超级个体与中小企业，展示如何把企划、设计、运营等工作拆成服务场景、交付清单与协作流程。

公开仓库是多页面静态展示站，包含服务目录、方法论、案例和仪表盘页面。页面描述的智能体编排、算力节点和企业私域部署属于业务介绍；对应后台系统、调度服务与客户数据不包含在本仓库中。

## 可以浏览什么

- **服务场景**：按业务场景理解服务内容和交付范围。
- **项目案例**：查看品牌、直播电商和建筑汇报等案例页面。
- **方法论**：了解“小快轻准”的项目切入与交付思路。
- **产品体系**：查看浅滩、跃水、深潭、锦鲤四代命名与产品表达。
- **仪表盘与信息架构**：浏览运营展示与站点结构。

## 本地运行

需要 Git 和 Python 3；浏览站点无需安装前端依赖。

```bash
git clone https://github.com/Hankjun/dalyu-workstation.git
cd dalyu-workstation
python3 -m http.server 8877 --bind 127.0.0.1
```

打开 [http://localhost:8877](http://localhost:8877)。

## 项目结构

| 路径 | 用途 |
| --- | --- |
| `index.html` | 站点首页 |
| `scenes.html`、`scenes/` | 服务场景目录与详情 |
| `cases.html`、`cases/` | 项目案例 |
| `generations.html`、`generations/` | 产品代际说明 |
| `dashboard.html` | 仪表盘展示 |
| `pricing.html` | 定价说明 |
| `approach.html` | 交付方法论 |
| `about.html` | 关于页面 |
| `sitemap.html` | 信息架构 |
| `styles.css` | 共享样式 |
| `build_site.py` | 多页面站点生成脚本 |

## 内容维护

现有 HTML 页面可以直接用于静态部署。仓库也包含 `build_site.py`，用于生成站点内容。

生成脚本会写入页面文件。运行前先保留本地修改，并核对脚本中的内容是否与当前页面一致；生成后通过 `git diff` 审查覆盖范围，再提交。单独修改 HTML 不会自动同步回生成脚本。

## 当前范围与后续方向

这是服务产品化与信息架构的展示项目。公开页面中的项目数、节点数和定价属于站点内容，并非由该仓库实时读取的业务指标。

后续可完善案例的“问题—方案—交付物—验证”结构、内容更新记录与生成流程，逐步增加可公开复现的工作流示例。

## 反馈

欢迎通过 [Issues](https://github.com/Hankjun/dalyu-workstation/issues) 提交导航、展示和内容结构建议。请说明涉及页面与预期改善。

维护者：[Hank / 汉克](https://github.com/Hankjun)。
