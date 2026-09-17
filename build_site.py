# -*- coding: utf-8 -*-
"""生成大鲤鱼超级工作站多页面站点（19 页 + 信息架构图）"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
for d in ("generations", "cases", "scenes"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)

NAV = [
    ("index.html", "首页", "home"),
    ("generations.html", "水深四代", "gen"),
    ("dashboard.html", "仪表盘", "dash"),
    ("cases.html", "案例", "cases"),
    ("scenes.html", "场景目录", "scenes"),
    ("pricing.html", "定价", "price"),
    ("approach.html", "方法论", "appr"),
    ("about.html", "关于", "about"),
]

def head(title, prefix=""):
    return '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="大鲤鱼超级工作站——部门即服务（DaaS），专注小快轻准的 AI 项目运营。水深四代：浅滩·跃水·深潭·锦鲤。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=JetBrains+Mono:wght@400;500;600&family=Noto+Serif+SC:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" href="%sfavicon.png">
<link rel="stylesheet" href="%sstyles.css">
</head>
<body>
<div class="brandline"></div>
''' % (title, prefix, prefix)

def nav_html(active_key, prefix="", crumb=None):
    links = []
    for href, label, key in NAV:
        if key == active_key:
            cls = ' class="active"'
        elif href in ("index.html", "about.html"):
            cls = ""
        else:
            cls = ' class="opt"'
        links.append('<a href="%s%s"%s>%s</a>' % (prefix, href, cls, label))
    crumb_html = ""
    if crumb:
        crumb_html = '<div class="breadcrumb">%s</div>' % crumb
    return '''<nav>
  <div class="nav-inner">
    <a class="wordmark" href="%sindex.html">
      <img class="ip-avatar" src="%ssuper-assistant-avatar.png" alt="大鲤鱼超级助手">
      <div><div class="t1">大鲤鱼超级工作站</div><div class="t2">共享虾塘 · DALIYU</div></div>
    </a>
    <div class="nav-links">%s <span class="gen-badge">深潭 Gen 3</span></div>
  </div>
</nav>''' % (prefix, prefix, "".join(links)), crumb_html

def page_hero(title, lede, prefix="", crumb=None, active="home"):
    n, c = nav_html(active, prefix, crumb)
    lede_html = ('<p class="lede">%s</p>' % lede) if lede else ""
    return n + '''
<header class="page-hero"><div class="wrap inner">
%s
<h1>%s</h1>%s
</div></header>''' % (c, title, lede_html)

def footer(prefix=""):
    return '''
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
          <img class="ip-avatar" style="width:44px;height:44px;border-radius:12px;" src="%(p)ssuper-assistant-avatar.png" alt="大鲤鱼超级助手">
          <div class="co" style="margin-bottom:0;">无锡大鲤鱼文化科技发展有限公司</div>
        </div>
        <p>长三角「人工智能 + 电商」数智化转型服务商。建设运营江苏直播电商产业创新服务基地（无锡市级直播电商基地），国家高新技术企业、科技型中小企业。</p>
      </div>
      <div class="foot-col"><h4>四大业务主线</h4><ul>
        <li><a href="%(p)sabout.html">AI + 电子商务与新零售</a></li>
        <li><a href="%(p)sabout.html">AI + 企业服务与经营管理</a></li>
        <li><a href="%(p)sabout.html">AI + 内容创作与品牌传播</a></li>
        <li><a href="%(p)sabout.html">AI + 组织协同与流程重构</a></li>
      </ul></div>
      <div class="foot-col"><h4>站点导航</h4><ul>
        <li><a href="%(p)sgenerations.html">水深四代 · 命名体系</a></li>
        <li><a href="%(p)sscenes.html">场景目录 · 24 场景</a></li>
        <li><a href="%(p)scases.html">项目案例</a></li>
        <li><a href="%(p)ssitemap.html">信息架构图</a></li>
        <li><a href="%(p)soperations.html">运营仪表盘（旧版）</a></li>
      </ul></div>
    </div>
    <div class="copyright">大鲤鱼超级工作站 · 共享虾塘 · 深潭 Gen 3（DLY-DEEP-G3）· 水深四代：浅滩 · 跃水 · 深潭 · 锦鲤 · DALIYU BASE © 2026 · <a href="%(p)ssitemap.html">站点地图</a></div>
  </div>
</footer>
</body></html>''' % {"p": prefix}

def kpi_row():
    return '''<div class="kpi-row">
  <div class="kpi"><div class="num t">4</div><div class="lbl">算力节点</div></div>
  <div class="kpi"><div class="num t">22+</div><div class="lbl">智能体</div></div>
  <div class="kpi"><div class="num g">24</div><div class="lbl">可售场景</div></div>
  <div class="kpi"><div class="num g">73</div><div class="lbl">实战项目</div></div>
  <div class="kpi"><div class="num c">3</div><div class="lbl">智能体层级</div></div>
  <div class="kpi"><div class="num c">¥99</div><div class="lbl">次卡起</div></div>
</div>'''

def cta(prefix=""):
    return '''<section class="block" style="padding-top:0;"><div class="wrap">
<div class="cta-band">
  <h2>从一个具体问题开始</h2>
  <p class="sub">先做 AI 诊断，找到最小可切入的场景，再谈要不要一起做塘。</p>
  <div class="cta-contact">
    <span class="item">联系人 <b>超级助手</b></span>
    <span class="item">电话 <b>133 2790 8793</b></span>
    <span class="item">定位 <b>长三角 · 无锡</b></span>
  </div>
</div></div></section>'''

GENERATIONS = [
    ("shoal", "浅滩", "Shoal", "GEN 1 · 历史", "~2026.04", False, "早期单机探索，V3 → V4 架构设计阶段。在岸边试水，验证单点能力。",
     "第一代，从一台机器开始。验证 AI 能不能在本地跑通、能不能稳定交付单个任务。架构上经历了 V3 → V4 的重新设计，为后续多设备协同埋下伏笔。"),
    ("leap", "跃水", "Leap", "GEN 2 · 上一代", "2026.06", False, "4 机 + 云 + 移动多态协同，试运营接单，四档定价体系成型。",
     "从单机跃迁为多态协同：本地 4 台 + 云端弹性 + 移动端随叫随到。定价从高端结构调整为四档体系（次卡 ¥99 起 → 标准 ¥1,999/月），以次卡做破冰漏斗。内部代号 DLY-DEEP-G2。"),
    ("deep", "深潭", "Deep", "GEN 3 · 当前 ●", "DLY-DEEP-G3", True, "集群化、企业级私有部署。部门即服务（DaaS），24 个可售场景，2–5 万/年起。",
     "当前世代。定位从「22+ 智能体平台」收口为「企业 AI 组织改造 / 部门即服务」。三大场景包：品牌资产包（沉淀层）/ 获客增长包（流量层）/ 产品造势包（事件层）。计费三层骨架（基座 / 人力 / 场景）× 三种模式（菜单式 / 包年整包 / 建设-运营两段式）。"),
    ("koi", "锦鲤", "Koi", "GEN 4 · 远景", "DLY-DEEP-G4", False, "自运转生态、对外赋能——从「帮客户做塘」走向「教客户造塘」。",
     "远景世代。当交付能力、工具链、案例库沉淀到一定密度，工作站从「对外承接」转向「对外赋能」：把做塘的方法、工具、标准开放出去，让客户和伙伴自己建塘。"),
]

CASES = [
    ("zhongyu-jiuyi", "中域玖壹 · 仓鼠云仓", "GEO · 第一曲线客户",
     "大鲤鱼 OPC 社区第一曲线客户项目，对接人陈总。为中域玖壹（仓鼠云仓）提供 AI 落地解决方案，推进 GEO（生成式引擎优化）落地。",
     "【背景】中域玖壹（仓鼠云仓）寻求 AI 落地与线上可见度提升。\n【交付】完成完整客户案例 + 海外事业调研报告；参考文旅行业 GEO 报告完善方案；引用每经 AI 智库《GEO 红皮书 2026》。\n【进展】2026-06-11 完成案例与调研，进入实质性合作推进，苏州会面待确认时间。",
     ["GEO 落地", "客户案例", "海外调研", "第一曲线"]),
    ("gaosi-geo", "高思控制 GEO 评测", "GEO 评测 · 无锡",
     "为江苏高思控制系统（热处理气氛控制/碳势控制，德国 Millivolt 技术合作）评测品牌在国内主流 AI 智能体中的可见度，输出优化路线图。",
     "【背景】高思控制 = 无锡热处理气氛控制方案商，产品 EndoMate RX 发生器 / gauss MES™。需求：评测品牌在主流 AI 智能体（GEO）中的可见度。\n【结论】综合 AIVO 65/100（品牌词 90、决策词 78、知识源 55、歧义控制 50）；智谱清言、360 AI 搜索均正面推荐；核心问题：缺百科/知乎/公众号/榜单/软文五大信源，同名品牌污染。\n【交付】可视化评测报告（HTML + MD + PDF）+ 证据快照 + P0 落地五项（建百科/知乎/公众号/榜单申报/官网结构化）。",
     ["AIVO 65/100", "评测报告", "优化路线图", "GEO"]),
    ("ppt-assistant", "建筑汇报 PPT 助手", "产品化 · 交付管理",
     "Claude 暖调展示页 + 咨询表单定价引擎 + HTML 预览生成器，核心差异化在「咨询 → 定价 → 按页反馈」的交付链。",
     "【定位】把 PPT 制作从「卖模板」升级为「卖交付管理」。\n【能力】咨询表单定价引擎 + HTML 预览生成器（8 种页面类型）+ 按页反馈交付链。\n【差异化】竞品只做生成，不做交付管理——这是「咨询 → 定价 → 按页反馈」的完整闭环。",
     ["定价引擎", "8 种页面", "交付链", "无竞品"]),
    ("live-ecommerce-ai", "直播电商 AI 智能体方案", "行业方案 · 直播电商",
     "面向江苏直播电商产业创新服务基地的行业方案，覆盖数字人直播、短视频生产、智能营销与 AIGC 内容生产，挂靠 Deep3.0 行业包。",
     "【范围】8 大模块 × 32 子场景，覆盖 AI 数字人直播、数字人口播短视频、3D 数字人交互、智能营销、AIGC 内容生产。\n【载体】江苏直播电商产业创新服务基地（无锡市级直播电商基地）。\n【挂靠】作为 Deep3.0 行业包 + 技能商店 SKU + OPC 赛道，不新增独立概念。",
     ["8 模块", "32 子场景", "数字人", "行业包"]),
]

SCENE_LINES = {
    "brand": ("品牌沉淀线", "8 个场景 · 沉淀层", "把「品牌」从概念变成持续产出、可衡量的资产。", [
        ("B-01", "品牌公众号全年运营", "¥36,000/年", "品牌公众号年度内容全托管——选题→写作→排版→发布→复盘", "全年150篇原创推文 · 选题日历 · 排版+头图 · 阅读数据月报 · 季度复盘", "选题/写作/排版/数据分析 4 常驻", "FDE 0.2FTE", "有公众号但缺持续产出能力的品牌"),
        ("B-02", "品牌叙事升级（系列长文）", "¥28,000", "系统化重建品牌叙事体系——创始人故事、源起、哲学、案例", "叙事框架文档 · 6-10篇品牌长文 · 故事线时间轴 · 可复用模板", "定位/叙事/调研 3 专项", "方案师 0.2 + FDE 0.1", "有产品没故事的品牌"),
        ("B-03", "品牌 IP 设计全案", "¥32,000", "从0到1打造品牌IP角色——设定、人格、视觉、话术、应用体系", "IP设定文档 · 视觉形象+表情包 · 话术体系 · 应用指南 · 首发6篇", "IP创作/视觉/话术 3 专项", "方案师 0.3 + FDE 0.2", "人格化需求强的品牌"),
        ("B-04", "内容日历 + 热点策略", "¥15,000/年", "年度内容节奏设计——热点日历+节点策略+内容排期", "年度策略报告 · 12月选题日历 · 热点清单 · 内容SOP · 12份节点包", "选题/热点监控 2 周期", "FDE 0.1", "有产能缺系统排期的客户"),
        ("B-05", "品牌视觉规范手册", "¥12,000", "品牌视觉体系规范化——从散乱到统一", "色/字体/Logo规范 · 应用示例 · 视觉资产库 · 设计模板包", "视觉/规范 2 专项", "FDE 0.1", "多品牌需视觉统一的客户"),
        ("B-06", "品牌声量监测", "¥9,600/年", "持续追踪品牌全网提及量、声量趋势和竞品对标", "月度声量报告 · 竞品对标 · 热点预警 · 季度健康度", "舆情/竞品/数据 3 常驻", "FDE 0.05", "成长期或舆情敏感品牌"),
        ("B-07", "品牌定位 + 战略梳理", "¥22,000", "用「三问框架」梳理品牌定位——你是谁/为谁/凭什么", "定位矩阵 · 竞争卡位 · 价值主张 · 传播层级 · 竞品对比", "定位/调研/竞争 3 专项", "方案师 0.3", "新品牌/转型期/融资期"),
        ("B-08", "品牌资产库搭建", "¥8,000", "从散乱到有序——品牌内容资产的系统化归档、可检索", "分类体系 · 命名规范 · 资产初始化 · 检索目录 · 维护SOP", "知识库/分类 2 专项", "FDE 0.1", "资产积累多年但无系统的客户"),
    ]),
    "growth": ("获客增长线", "10 个场景 · 流量层", "用 AI + 内容矩阵，系统化降低获客成本、提升线索质量。", [
        ("G-01", "公众号矩阵获客", "¥48,000/年", "以获客为目标的公众号内容矩阵——有转化设计的内容", "主号+子号矩阵 · 每周8-12篇 · 获客钩子 · 转化追踪 · 月复盘", "写作×2/选题/排版/数据 5 常驻", "FDE 0.3 + OPC 0.2", "公众号是核心渠道的B2B/B2C"),
        ("G-02", "小红书 / 短视频矩阵获客", "¥42,000/年", "小红书+短视频的获客内容矩阵——爆款+评论区+私信转化", "账号定位 · 每周10-15条 · 评论区SOP · 私信路径 · 数据周报", "写作/脚本/视觉/数据 4 常驻", "FDE 0.3 + OPC 0.2", "目标客户在小红书活跃的品牌"),
        ("G-03", "GEO（AI 搜索）获客", "¥36,000/年", "针对 AI 搜索引擎的内容优化——让 AI 在回答时「提到你」", "关键词矩阵 · 结构化内容包 · Schema部署 · 月报 · 迭代建议", "SEO/GEO/内容/数据 3 常驻", "FDE 0.2 + 方案师 0.1", "想布局 AI 搜索红利的品牌（蓝海）"),
        ("G-04", "私域搭建 + 运营", "¥48,000/年", "从0到1搭建私域体系——企微/社群/SOP/内容/复购全链路", "私域架构 · 入池SOP · 社群日历 · 朋友圈 · 复购策略 · 看板", "私域/社群/内容/数据 4 常驻", "FDE 0.3 + OPC 0.2", "有客户基础缺私域体系的品牌"),
        ("G-05", "多平台矩阵获客（全域）", "¥84,000/年", "全平台内容矩阵——公众号+小红书+知乎+抖音+B站一盘分发", "全平台策略 · 每周20-30条 · 分发自动化 · 跨平台仪表盘 · ROI对比", "全平台写作集群 8-10 + 数据", "FDE 0.5 + OPC 0.3", "扩张期需全域覆盖的品牌（旗舰）"),
        ("G-06", "投放优化 + 素材生产", "¥60,000/年", "AI 辅助投放——素材批量生产+A/B测试+ROI优化", "投放策略 · 每月50+素材 · A/B测试 · 复盘 · 迭代", "投放素材/数据/视觉 3 常驻", "FDE 0.3 + 方案师 0.2", "有预算缺素材产能的客户"),
        ("G-07", "KOL / KOC 矩阵合作", "¥36,000/年", "达人筛选→触达→合作SOP→效果追踪全流程管理", "达人画像 · 季度50+清单 · 触达SOP · Brief模板 · 台账", "筛选/触达/数据 3 周期", "方案师 0.2 + FDE 0.2", "需达人背书无BD团队的品牌"),
        ("G-08", "SEO 内容体系", "¥24,000/年", "传统搜索引擎的内容优化和排名提升", "200+关键词 · 每周4-6篇 · 站内优化 · 月排名报告 · 竞品分析", "SEO/内容/数据 3 常驻", "FDE 0.15", "百度是重要来源的B2B客户"),
        ("G-09", "获客管道诊断 + 优化", "¥15,000", "从线索到成交的全链路诊断——找到漏斗最大漏点", "全链路诊断报告 · 漏点定位 · 优化方案 · 漏斗看板模板", "诊断/数据 2 专项", "方案师 0.3", "获客遇瓶颈不知问题在哪（入口场景）"),
        ("G-10", "直播获客运营", "¥42,000/年", "用直播间做获客——持续获取有质量的线索", "直播策略 · 场次脚本 · 话术库 · 数据复盘 · 私域引流", "策划/脚本/数据 3 常驻", "FDE 0.3 + OPC 0.2", "适合直播获客的教育/咨询/本地"),
    ]),
    "product": ("产品造势线", "6 个场景 · 事件层", "把产品发布 / 事件营销从一次性消耗，变成可传播的资产。", [
        ("P-01", "产品发布会全套", "¥48,000–78,000", "从策划到复盘的产品发布会全案——内容/物料/传播全包", "策划方案 · 发布内容 · 物料 · 传播内容 · 邀约清单 · 复盘报告", "策划/内容/视觉/传播 4 专项", "方案师 0.5 + FDE 0.3 + OPC 0.3", "重要产品上线/品牌升级节点客户"),
        ("P-02", "产品 SKU 体系设计", "¥22,000", "把「做什么生意」变成「卖什么东西」——系统化SKU设计", "SKU清单 · 定价矩阵 · 产品定义 · 上下架SOP · 竞品对标", "产品/定价/竞品 3 专项", "方案师 0.3", "产品线散乱/定价随意的客户"),
        ("P-03", "服务交付 SOP 设计", "¥28,000", "让服务从「因人而异」变成「可复制、可培训、可规模化」", "流程地图 · 环节SOP · 沟通模板 · 质控体系 · 培训手册", "流程/文档/知识库 3 专项", "方案师 0.3 + FDE 0.2", "扩张期服务型公司"),
        ("P-04", "标杆案例包装", "¥18,000/个", "把一次成功交付变成可传播的「标杆案例」", "采访素材 · 标准文档 · 多形态输出 · 分发策略 · 效果追踪", "采访/写作/视觉/分发 4 专项", "FDE 0.2 + OPC 0.2", "有成功交付缺案例包装的公司"),
        ("P-05", "线上活动 / 裂变营销全案", "¥22,000–38,000", "设计一个能「自己长」的活动——裂变机制+内容+数据", "活动方案 · 页文案视觉 · 裂变素材 · 执行SOP · 复盘报告", "策划/文案/视觉/数据 4 专项", "方案师 0.3 + FDE 0.2", "有增长需求的品牌"),
        ("P-06", "产品路线图 + 竞品监测", "¥24,000/年", "产品迭代方向和竞品动态的持续追踪", "3-6-12月路线图 · 月竞品报告 · 趋势简报 · 机会点 · 季度复盘", "竞品/趋势/数据 3 常驻", "方案师 0.15", "竞争激烈需持续迭代的产品型公司"),
    ]),
}

# ============================================================
def build_index():
    ports = [
        ("gen", "水深四代 · 命名体系", "generations.html", "浅滩 · 跃水 · 深潭 · 锦鲤，版本号本身在讲产品故事。"),
        ("dash", "项目仪表盘", "dashboard.html", "4 台节点、22+ 智能体、三层水域、五步交付法，一处看清。"),
        ("cases", "项目案例", "cases.html", "中域玖壹、高思控制、PPT 助手、直播电商——真实交付。"),
        ("scenes", "场景目录", "scenes.html", "24 个可售场景，菜单式选购，精确到篇数、件数、频率。"),
        ("price", "定价体系", "pricing.html", "从一顿饭钱（¥99 次卡）到部门即服务（2-5 万/年）。"),
        ("appr", "方法论 · 小快轻准", "approach.html", "小·快·轻·准——把 AI 做得更小、更快、更轻、更准。"),
        ("about", "关于 · 联系", "about.html", "公司介绍、四大业务主线、全链路服务与联系方式。"),
        ("sitemap", "信息架构图", "sitemap.html", "整站信息架构全景，一眼看懂体系与层级。"),
    ]
    cards = "".join('<a class="portal-card" href="%s"><div class="tag">§ %s</div><h3>%s</h3><p>%s</p><span class="go">进入 →</span></a>' % (u, tag, t, d) for tag, t, u, d in ports)
    n, _ = nav_html("home")
    body = n + '''
<div class="wrap hero-ip">
  <div class="hero-ip-text">
    <div class="eyebrow">无锡大鲤鱼文化科技发展有限公司 · DALIYU BASE</div>
    <h1>大鲤鱼超级工作站<span class="en">Department as a Service — 部门即服务</span></h1>
    <p class="lede">把企划、设计、运营等部门能力，变成<strong style="color:var(--text);">可购买、可交付、可复用</strong>的服务。私域部署在基地，22+ 智能体编排 + 超级个体 + 交付工程师协同。</p>
    <p class="tagline">让 AI 真正长在创业者的日常里。</p>
  </div>
  <div class="hero-ip-img"><img src="super-assistant.png" alt="大鲤鱼超级助手 IP 形象"></div>
</div>'''
    body += '''<section class="block" style="padding-top:0;"><div class="wrap">
<div class="eyebrow"><span class="sec-no">§</span>部门即服务 · 深潭 Gen 3</div>
<h2 class="h">小快轻准的 AI 项目运营</h2>
<p class="sub">为中小企业做「小快轻准」的 AI 项目落地，从一顿饭钱的次卡，到部门即服务的整包。</p>
%s
<div class="grid g4" style="margin-top:40px;">%s</div>
</div></section>''' % (kpi_row(), cards)
    body += cta()
    return head("大鲤鱼超级工作站 · 共享虾塘 · 深潭 Gen 3") + body + footer()

def build_generations_index():
    cards = "".join('<a class="gen-card%s" href="generations/%s.html"><div class="gen-tag"><span class="gen-dot"></span>%s</div><div class="gen-name">%s</div><div class="gen-en">%s</div><p class="gen-desc">%s</p><div class="gen-era">%s</div></a>' % (" current" if cur else "", slug, tag, name, en, desc, era) for slug, name, en, tag, era, cur, desc, _ in GENERATIONS)
    body = page_hero("水深四代 · 命名体系", "客户记不住 V2.0，但记得住「鱼往深水游」。四代水深，每一代都是一次能力跃迁。", active="gen")
    body += '<section class="block"><div class="wrap"><div class="grid g4">%s</div></div></section>' % cards
    body += cta()
    return head("水深四代 · 大鲤鱼超级工作站") + body + footer()

def build_generation_detail(slug):
    for s, name, en, tag, era, cur, desc, full in GENERATIONS:
        if s == slug:
            break
    p = "../"
    gid = "1" if slug == "shoal" else "2" if slug == "leap" else "3" if slug == "deep" else "4"
    body = page_hero("水深四代 · %s" % name, full, p, crumb='<a href="%sindex.html">首页</a><span class="sep">/</span><a href="%sgenerations.html">水深四代</a><span class="sep">/</span>%s' % (p, p, name), active="gen")
    badge = '<span class="badge gold">当前世代</span>' if cur else '<span class="badge">%s</span>' % tag
    body += '''<section class="block"><div class="wrap">
<div class="badge-row">%s <span class="badge coral">%s</span></div>
<div class="card" style="margin-bottom:16px;">
<h3 style="font-family:var(--serif);font-size:26px;">%s <span style="font-family:var(--display);font-style:italic;color:var(--teal);font-size:18px;">%s</span></h3>
<p style="font-size:15px;color:var(--text);margin:8px 0 16px;">%s</p>
</div>
<div class="card"><h3>升级触发线</h3>
<div class="spec-row"><span class="k">内部代号</span><span class="v">DLY-DEEP-G%s</span></div>
<div class="spec-row"><span class="k">状态</span><span class="v">%s</span></div>
<div class="spec-row"><span class="k">时代</span><span class="v">%s</span></div>
</div>
<div style="margin-top:16px;"><a class="btn btn-ghost" href="%sgenerations.html">← 回到水深四代总览</a></div>
</div></section>''' % (badge, era, name, en, desc, gid, tag, era, p)
    body += cta(p)
    return head("水深四代 · %s · 大鲤鱼超级工作站" % name, p) + body + footer(p)

def build_dashboard():
    body = page_hero("项目仪表盘", "一处看清，我们有什么、怎么干。", active="dash")
    body += '''<section class="block"><div class="wrap">
%s
<div class="grid g2" style="margin-top:20px;">
<div class="card"><h3>硬件节点</h3>
<div class="spec-row"><span class="k">基地 · 主机 1 号</span><span class="v">本地算力</span></div>
<div class="spec-row"><span class="k">基地 · 主机 2 号</span><span class="v">本地算力</span></div>
<div class="spec-row"><span class="k">基地 · 主机 3 号</span><span class="v">本地算力</span></div>
<div class="spec-row"><span class="k">汉克个人 Mac</span><span class="v">移动协同</span></div>
<div class="spec-row"><span class="k">多台云主机</span><span class="v">云端弹性</span></div>
</div>
<div class="card"><h3>智能体三层架构</h3>
<div class="spec-row"><span class="k">旗舰云模型</span><span class="v">3 款</span></div>
<div class="spec-row"><span class="k">派系小龙虾</span><span class="v">15 款</span></div>
<div class="spec-row"><span class="k">涌现式框架</span><span class="v">4+ 款</span></div>
</div>
<div class="card"><h3>三层水域配置</h3>
<div class="spec-row"><span class="k">塘底 · 本地 4 台</span><span class="v">私有部署</span></div>
<div class="spec-row"><span class="k">流水 · 云 N 台</span><span class="v">弹性扩展</span></div>
<div class="spec-row"><span class="k">浮游 · 移动 2 端</span><span class="v">随叫随到</span></div>
</div>
<div class="card"><h3>交付团队</h3>
<div class="spec-row"><span class="k">方案师</span><span class="v">诊断策划</span></div>
<div class="spec-row"><span class="k">FDE 交付工程师</span><span class="v">落地执行</span></div>
<div class="spec-row"><span class="k">OPC 超级个体</span><span class="v">专项承接</span></div>
</div>
</div>
<div class="flow" style="margin-top:20px;">
<div class="flow-step"><div class="idx">01</div><h4>前测诊断</h4><p>AI 应用成熟度评估，找到最小可切入的问题。</p></div>
<div class="flow-step"><div class="idx">02</div><h4>方案签约</h4><p>场景级菜单式方案，先跑通一个场景再谈组合。</p></div>
<div class="flow-step"><div class="idx">03</div><h4>入驻生产</h4><p>智能体编排 + 人工把关，按周按件交付。</p></div>
<div class="flow-step"><div class="idx">04</div><h4>持续运营</h4><p>数据复盘、场景增购，从一单长成长期关系。</p></div>
<div class="flow-step"><div class="idx">05</div><h4>月度复盘</h4><p>结果交付 + 下月路线，客户看得见每一分投入。</p></div>
</div>
</div></section>''' % kpi_row()
    body += cta()
    return head("项目仪表盘 · 大鲤鱼超级工作站") + body + footer()

def build_cases_index():
    cards = "".join('<a class="portal-card" href="cases/%s.html"><div class="tag">%s</div><h3>%s</h3><p>%s</p><span class="go">查看详情 →</span></a>' % (slug, tag, name, short) for slug, name, tag, short, _, _ in CASES)
    body = page_hero("项目案例", "不是演示，是真实交付。每个都跑在真实经营现场。", active="cases")
    body += '<section class="block"><div class="wrap"><div class="grid g2">%s</div></div></section>' % cards
    body += cta()
    return head("项目案例 · 大鲤鱼超级工作站") + body + footer()

def build_case_detail(slug):
    for s, name, tag, short, full, tags in CASES:
        if s == slug:
            break
    p = "../"
    tgs = "".join('<span class="badge">%s</span>' % t for t in tags)
    body = page_hero(name, short, p, crumb='<a href="%sindex.html">首页</a><span class="sep">/</span><a href="%scases.html">项目案例</a><span class="sep">/</span>%s' % (p, p, name), active="cases")
    body += '''<section class="block"><div class="wrap">
<div class="badge-row"><span class="badge gold">%s</span> %s</div>
<div class="card"><p style="font-size:14.5px;color:var(--text-2);line-height:1.9;white-space:pre-line;">%s</p></div>
<div style="margin-top:16px;"><a class="btn btn-ghost" href="%scases.html">← 回到案例列表</a></div>
</div></section>''' % (tag, tgs, full, p)
    body += cta(p)
    return head("%s · 大鲤鱼超级工作站" % name, p) + body + footer(p)

def build_scenes_index():
    cols = ""
    for key in ("brand", "growth", "product"):
        title, count, note, items = SCENE_LINES[key]
        rows = "".join('<div class="scene-item"><span class="n">%s %s</span><span class="p%s">%s</span></div>' % (code, nm, (" coral" if key == "growth" and code == "G-03" else ""), price) for code, nm, price, _, _, _, _, _ in items)
        cols += '<div class="card"><h3 style="font-size:16px;margin-bottom:2px;">%s</h3><div style="font-family:var(--mono);font-size:11px;color:var(--text-3);margin-bottom:12px;">%s</div>%s<p style="font-size:12px;color:var(--text-3);margin-top:12px;">%s</p><a style="display:inline-block;margin-top:10px;font-size:12.5px;color:var(--teal);" href="scenes/%s.html">查看完整字段 →</a></div>' % (title, count, rows, note, key)
    body = page_hero("场景目录 · 24 个可售场景", "以前卖「套餐」，客户不知道里面有什么；现在卖「菜单」，客户自己选。", active="scenes")
    body += '<section class="block"><div class="wrap"><div class="grid g3">%s</div></div></section>' % cols
    body += cta()
    return head("场景目录 · 大鲤鱼超级工作站") + body + footer()

def build_scene_line(key):
    title, count, note, items = SCENE_LINES[key]
    p = "../"
    details = ""
    for code, nm, price, one, deliver, agent, labor, client in items:
        details += '''<div class="scene-detail">
<div class="code">%s</div>
<h3>%s</h3>
<div class="price-tag">%s</div>
<p class="one">%s</p>
<div class="field"><b>交付物</b>%s</div>
<div class="field"><b>智能体</b>%s</div>
<div class="field"><b>人工</b>%s</div>
<div class="field"><b>适用客户</b>%s</div>
</div>''' % (code, nm, price, one, deliver, agent, labor, client)
    body = page_hero(title, note, p, crumb='<a href="%sindex.html">首页</a><span class="sep">/</span><a href="%sscenes.html">场景目录</a><span class="sep">/</span>%s' % (p, p, title), active="scenes")
    body += '<section class="block"><div class="wrap">%s<div style="margin-top:16px;"><a class="btn btn-ghost" href="%sscenes.html">← 回到场景目录</a></div></div></section>' % (details, p)
    body += cta(p)
    return head("%s · 场景目录 · 大鲤鱼超级工作站" % title, p) + body + footer(p)

def build_pricing():
    body = page_hero("定价体系", "定价锚点不是「AI 工具值多少钱」，而是「客户自己做这件事要花多少钱」。", active="price")
    body += '''<section class="block"><div class="wrap">
<div class="grid g4">
<div class="price-card"><div class="pname">次卡 · 破冰漏斗</div><div class="pnum">¥99</div><div class="punit">起</div><p class="pdesc">10 次 ¥99 / 50 次 ¥399 / 100 次 ¥699 / 300 次 ¥1799，12 个月有效，余额可抵扣月卡。</p></div>
<div class="price-card"><div class="pname">体验版 · 个人尝鲜</div><div class="pnum">¥999</div><div class="punit">/月</div><p class="pdesc">7 天试用，适合个人 / 超级个体跑通第一个 AI 场景。</p></div>
<div class="price-card hot"><div class="pname">标准版 · 主推档</div><div class="pnum">¥1,999</div><div class="punit">/月</div><p class="pdesc">超级个体 / 小团队，3 天试用。年付 9 折、季付 95 折。</p></div>
<div class="price-card"><div class="pname">定制版 · 企业团队</div><div class="pnum">面议</div><div class="punit">&nbsp;</div><p class="pdesc">企业团队差异化定制，按场景与规模评估报价。</p></div>
</div>
<div class="note-box" style="margin-top:20px;">
<strong>深潭 Gen 3 · 部门即服务：</strong>2–5 万/年起，三大场景包（品牌资产包 · 沉淀层 / 获客增长包 · 流量层 / 产品造势包 · 事件层）。计费三层骨架（基座 / 人力 / 场景）× 三种模式（菜单式 / 包年整包 / 建设–运营两段式）。<br><br>
<strong>关键：</strong>永远不和「雇一个人多少钱」比，和「客户自己做这件事的投入」比——自己做看似更便宜，但做不出来、做不持续。详见 <a href="scenes.html">场景目录</a>。
</div>
</div></section>'''
    body += cta()
    return head("定价体系 · 大鲤鱼超级工作站") + body + footer()

def build_approach():
    body = page_hero("方法论 · 小快轻准", "不把 AI 讲得更大，而是把 AI 做得更小、更快、更轻、更准——创始人吴俊原话定义。", active="appr")
    body += '''<section class="block"><div class="wrap">
<div class="grid g4">
<div class="card"><h3 style="font-family:var(--serif);font-size:40px;color:var(--teal);line-height:1;">小</h3><p style="font-weight:600;color:var(--text);margin:8px 0 4px;">颗粒度小</p><p>能从一个具体问题开始。不卖大而全的平台，先卖一个能立刻见效的场景。</p></div>
<div class="card"><h3 style="font-family:var(--serif);font-size:40px;color:var(--teal);line-height:1;">快</h3><p style="font-weight:600;color:var(--text);margin:8px 0 4px;">响应快</p><p>快速形成方案、工具和行动。工单「能勾别写」，当面成单、快速交付。</p></div>
<div class="card"><h3 style="font-family:var(--serif);font-size:40px;color:var(--teal);line-height:1;">轻</h3><p style="font-weight:600;color:var(--text);margin:8px 0 4px;">部署轻</p><p>不让中小企业背上复杂系统负担。MVP 先做表格 + 文档 + 微信群。</p></div>
<div class="card"><h3 style="font-family:var(--serif);font-size:40px;color:var(--teal);line-height:1;">准</h3><p style="font-weight:600;color:var(--text);margin:8px 0 4px;">场景准</p><p>必须落在经营现场。24 个场景精确到篇数、件数、频率。</p></div>
</div>
<h2 class="h" style="margin-top:52px;">四步交付法</h2>
<p class="sub">前测 → 方案 → 生产 → 复盘，每一步都有明确交付与负责人。</p>
<div class="flow">
<div class="flow-step"><div class="idx">01</div><h4>前测</h4><p>诊断现状，定位最小场景。</p></div>
<div class="flow-step"><div class="idx">02</div><h4>方案</h4><p>菜单式方案，明确交付物与定价。</p></div>
<div class="flow-step"><div class="idx">03</div><h4>生产</h4><p>智能体编排 + 人工把关，按周交付。</p></div>
<div class="flow-step"><div class="idx">04</div><h4>复盘</h4><p>数据复盘，驱动下一轮增购。</p></div>
</div>
</div></section>'''
    body += cta()
    return head("方法论 · 小快轻准 · 大鲤鱼超级工作站") + body + footer()

def build_about():
    body = page_hero("关于 · 联系", "无锡大鲤鱼文化科技发展有限公司——长三角「人工智能 + 电商」数智化转型服务商。", active="about")
    body += '''<section class="block"><div class="wrap">
<div class="card" style="margin-bottom:16px;">
<p style="font-size:14.5px;color:var(--text-2);line-height:1.9;">无锡大鲤鱼文化科技发展有限公司成立于 2021 年 8 月，定位为长三角「人工智能 + 电商」数智化转型服务商。公司建设运营江苏直播电商产业创新服务基地（无锡市级直播电商基地），获认定为国家高新技术企业、科技型中小企业。</p>
<p style="font-size:14.5px;color:var(--text-2);line-height:1.9;margin-top:12px;">公司以 AI 应用研发、智能体编排与行业交付能力为基础，重点布局 AI 数字人、AI 数字员工、智能营销与 AIGC 内容生产，为中小企业及政企客户提供从 AI 诊断、方案规划、工具部署、流程重构到持续运营与结果交付的全链路数智化转型服务。</p>
</div>
<div class="grid g2">
<div class="card"><h3>四大业务主线</h3>
<div class="spec-row"><span class="k">AI + 电子商务与新零售</span></div>
<div class="spec-row"><span class="k">AI + 企业服务与经营管理</span></div>
<div class="spec-row"><span class="k">AI + 内容创作与品牌传播</span></div>
<div class="spec-row"><span class="k">AI + 组织协同与流程重构</span></div>
</div>
<div class="card"><h3>服务链路</h3>
<div class="spec-row"><span class="k">AI 诊断</span><span class="v">→ 方案规划</span></div>
<div class="spec-row"><span class="k">工具部署</span><span class="v">→ 流程重构</span></div>
<div class="spec-row"><span class="k">持续运营</span><span class="v">→ 结果交付</span></div>
</div>
</div>
</div></section>'''
    body += cta()
    return head("关于 · 大鲤鱼超级工作站") + body + footer()

def build_sitemap():
    lvl1 = [
        ("generations.html", "水深四代", "命名体系"),
        ("dashboard.html", "项目仪表盘", "算力与流程"),
        ("cases.html", "项目案例", "4 个案例"),
        ("scenes.html", "场景目录", "24 场景"),
        ("pricing.html", "定价体系", "四档 + DaaS"),
        ("approach.html", "方法论", "小快轻准"),
        ("about.html", "关于·联系", "公司与服务"),
    ]
    lvl2 = {
        "generations.html": [("generations/shoal.html", "浅滩 Gen1"), ("generations/leap.html", "跃水 Gen2"), ("generations/deep.html", "深潭 Gen3"), ("generations/koi.html", "锦鲤 Gen4")],
        "cases.html": [("cases/zhongyu-jiuyi.html", "中域玖壹"), ("cases/gaosi-geo.html", "高思控制"), ("cases/ppt-assistant.html", "PPT 助手"), ("cases/live-ecommerce-ai.html", "直播电商")],
        "scenes.html": [("scenes/brand.html", "品牌沉淀线"), ("scenes/growth.html", "获客增长线"), ("scenes/product.html", "产品造势线")],
        "dashboard.html": [], "pricing.html": [], "approach.html": [], "about.html": [],
    }
    def node(href, title, desc, cls=""):
        return '<a class="ia-node %s" href="%s"><div class="t">%s</div><div class="d">%s</div></a>' % (cls, href, title, desc)
    cols = ""
    for href, title, desc in lvl1:
        children = lvl2.get(href, [])
        child_html = ""
        if children:
            c_links = "".join('<div class="child">%s</div>' % node(ch, ct, "", "") for ch, ct in children)
            child_html = '<div class="ia-children">%s</div>' % c_links
        cols += '<div class="ia-col">%s%s</div>' % (node(href, title, desc), child_html)
    body = page_hero("信息架构图", "整站信息架构全景——三级结构，每个节点都可点击进入对应页面。", active="home")
    body += '''<section class="block"><div class="wrap">
<div class="ia-root">
<img class="ip-inline" src="super-assistant.png" alt="大鲤鱼超级助手">
%s
<div class="ia-connector-v"></div>
<div class="ia-level">%s</div>
</div>
<div class="ia-legend">
<span class="lg"><span class="sw root"></span>首页（根）</span>
<span class="lg"><span class="sw page"></span>一级页面</span>
<span class="lg"><span class="sw detail"></span>二级 / 详情页</span>
</div>
</div></section>''' % (node("index.html", "大鲤鱼超级工作站", "首页 · 部门即服务", "root"), cols)
    body += cta()
    return head("信息架构图 · 大鲤鱼超级工作站") + body + footer()

# ============================================================
def w(path, content):
    with open(os.path.join(OUT, path), "w", encoding="utf-8") as f:
        f.write(content)
    print("WROTE", path)

w("index.html", build_index())
w("generations.html", build_generations_index())
w("dashboard.html", build_dashboard())
w("cases.html", build_cases_index())
w("scenes.html", build_scenes_index())
w("pricing.html", build_pricing())
w("approach.html", build_approach())
w("about.html", build_about())
w("sitemap.html", build_sitemap())
for slug, _, _, _, _, _, _, _ in GENERATIONS:
    w("generations/%s.html" % slug, build_generation_detail(slug))
for slug, _, _, _, _, _ in CASES:
    w("cases/%s.html" % slug, build_case_detail(slug))
for key in SCENE_LINES:
    w("scenes/%s.html" % key, build_scene_line(key))

print("DONE: 19 pages generated")
