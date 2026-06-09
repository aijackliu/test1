# 2026-06-09 05:30 清晨趨勢包

資料可得性：中
時間基準：2026-06-09 05:30（Asia/Taipei）

## 1. 核心結論（3–5 點）
- 今天清晨最清楚的主線仍是 AI 眼鏡；YouTube 搜尋前排與新聞樣本都集中在 Google / Meta / Apple 三角對照。
- OpenClaw 的新增量偏「平台化 + 企業化」：Microsoft Build 2026、Microsoft Scout、Skill Workshop 都在強化 agent 作業系統與治理能力。
- AI CRM 本輪沒有抓到同等強度的單一爆點新聞；可驗證訊號以 Salesforce Summer ’26 release 與 YouTube 教學 / demo 為主。
- Builder attention 仍集中在 skills、agent reach、personal AI infra；GitHub Trending 與 Microsoft / Salesforce 公告都在往多 agent、工作流、治理靠攏。
- 供應鏈關鍵字今天只有 `HBM shortage` 明確命中；`CoWoS delay`、`AI server delay` 未命中，`GPU lead time` 只有舊條目，不足以列為今日新訊號。

## 2. 分來源重點（GitHub / 社群 / 新聞 / 影音）

### GitHub
- `mvanhorn/last30days-skill`：34,262 stars、今日 +3,558，今天最強訊號直接落在 skill workflow。
- `RyanCodrai/turbovec`：8,684 stars、今日 +1,729；`google/skills`：12,326 stars、今日 +461。
- `Panniantong/Agent-Reach`：24,002 stars、今日 +679；`danielmiessler/Personal_AI_Infrastructure`：15,381 stars。
- 訊號解讀：開發者注意力仍在 agent skills、reach、personal infra，不是單點模型發布。

### 社群
- Hacker News 前排 AI 條目集中在 Apple / Gemini 與 agent infra：`Apple reveals new AI architecture built around Google Gemini models`（226 points，2 小時前）、`Siri AI`（241 points，3 小時前）、`MiMo-v2.5-Pro-UltraSpeed`（427 points，6 小時前）、`xAI is looking more like a datacentre REIT than a frontier lab`（294 points，6 小時前）。
- V2EX 熱帖與 AI 相關者以工具供給與職場體感為主，不是產品新聞：`国产显卡本地部署大模型`（95 回覆）、`月 base 只有 40k 的 AI 开发专家值得去吗？`（85 回覆）。
- 社群側沒有看到 AI CRM 單一熱議事件；注意力更偏 agent infra、模型效能、就業與本地部署。

### 新聞
- TechCrunch 2026-05-19：Google 在 I/O 2026 宣布與 Warby Parker、Gentle Monster 合作推出 `audio-powered smart glasses`，可與 Android / iOS 配對，並將於今年稍晚上市。
- MacRumors 2026-06-08：Apple 宣布新版 Apple Intelligence 架構，核心是與 Google 協作的 Gemini 技術；HN 同步把這條推到前排，表示「AI assistant 入口」競爭正在升溫。
- Windows Blog 2026-06-02：Build 2026 強推 `Windows Development Skills`、`Intelligent Terminal`，官方文字直接把 agent-driven workflows 納入 Windows 開發平台主線。
- Microsoft 2026-06-02：`Microsoft Scout` 定位為 always-on personal agent，官方明寫 powered by OpenClaw open-source technology，並能連到 Teams、Outlook、OneDrive、SharePoint、browser、local resources、MCP servers。
- OpenClaw docs 可驗證 `Skill Workshop` 現況：proposal-first、apply 才會 live write、scanner gated、可 rollback；平台敘事明顯從「會做事」轉向「可治理、可審核、可回滾」。
- Salesforce 2026-06-15 即將上線 Summer ’26 Release：主打 multi-agent orchestration、Slack-first workflows、Tableau MCP、Self-Service、Customer Engagement Agent。這是本輪 AI CRM 最強官方訊號，但 Google News RSS 未抓到同等密度的外部新聞擴散。

### 影音
- YouTube `AI glasses` 前排可驗證新鮮樣本包括：`AI Glasses from Meta – Buying Guides from Best Buy`（9 天前）、`Google AI Glasses vs Meta Ray-Ban: It's Not Even Close!`（2 週前）、`I Wore Google's Latest Smart Glasses. Meta Better Be Worried.`（2 週前）、`Apple’s Smart Glasses Strategy Is Brilliant`（5 天前）。
- YouTube `OpenClaw` 前排可驗證新鮮樣本包括：`2026微軟 Build 宣佈：Openclaw 接入 Windows`（4 天前）、`OpenClaw + Windows: Microsoft Build 2026`（5 天前）、`How AI Agents Run My SaaS (OpenClaw/Hermes)`（8 小時前）。
- YouTube `AI CRM` 前排仍以產品說明與導入教學為主：`What is AI CRM and How Does it Work? | Salesforce`、`AI CRM Workflows`、`Top 3 AI CRM You Must use in 2026!`、`Lark CRM | AI-Powered All-in-One CRM`。
- 影音面最明確的熱度順序是：AI 眼鏡 > OpenClaw / agent workflow > AI CRM。

### 關鍵字命中
- `HBM shortage`
  - 來源：Google News RSS / Gagadget.com
  - 時間：2026-06-08 17:03 GMT
  - 摘要：標題直接寫 `Nvidia locks down Korean memory deals as HBM shortage runs through 2028`。
  - 連結：https://news.google.com/rss/articles/CBMipgFBVV95cUxQQVplb0h0Zy03S2k2ZHJSeDBkREMxM25aSmthTklZSEhvOGJ5emxhY1lnaGpKeU9lZUV2UjN5VGU4ZnYwV1BmOFlfckVhME1RVkREQlpoSlRIUFE4SW9SUVc2YzVSTDh6NEFvSUgxbG05UGdjYm96aEVFLW1BVEtLYi04SF9YOFAxTkNzajlxamdrcHlaZXA4N05BRzNFZzdGQTVLVmtn0gGrAUFVX3lxTE9ZUHFtakhMY3gtLWxxZDhYbE9USmZNV25MZE9yS3FTSzVxR295Wk5RRkwxSVN1d0JqT1l4QXRJeWtkaTlmR2xwWXZnWWN5M2JQSks4OVRWQ1BfLUVfR21LczhNYmJFZWoxaUlVS0RiWEJYa3FPcVBrNDRVN0FRZ1FZZVd0VzI3dG5uamgtckFZSDNiTlBoQTFYWkUwSUFDa2pjcnFlM1NpUVh5SQ?oc=5
- `HBM shortage`
  - 來源：Google News RSS / Tech Times
  - 時間：2026-06-03 16:57 GMT
  - 摘要：標題直接寫 `AI Memory Shortage Locked Through 2030`，將 Computex 2026 與 HBM crisis 連在一起。
  - 連結：https://news.google.com/rss/articles/CBMi1gFBVV95cUxQV05kVGJtZmhfT2FFUHZvM3pfYW9EOFpKbHJSR2FEbFpQZ1h1UHRwMEhmMzR0OU9IU0M4OXVweklUM1MxQVdtbVNtSHVIQjdleDg1Vk1jalBsVkhFZXJCekswLUh2VmFQZndSWlg3Y1RqVzduZ0JtTVNka2wxM2FfRlNQNGlHOGMwd0FyTUs5UkZINEJIelNLbm1QNG1NTk43TWRHSTJVT0RWLW9EYS1iUkUtajBaT09uek1ZM3M1VU9oQjE1dzNKNUhERlRreG1pOW1WX0Jn?oc=5
- `CoWoS delay`：今日未命中。
- `GPU lead time`：只有 2025-07-08 舊條目，今日不列命中。
- `AI server delay`：今日未命中。

## 3. 風險與盲點（資料缺口）
- YouTube 本輪穩定拿到的是搜尋結果頁，不是官方 Trending 排名或觀看增速；能判斷題材更新度，不能判斷爆量幅度。
- AI CRM 在 Google News RSS 幾乎沒有同強度新條目；目前最硬的可驗證樣本是 Salesforce 官方 release，而非多家媒體共同放大。
- OpenClaw 相關新聞樣本偏官方文件、Microsoft 生態與搜尋結果延伸，代表方向清楚，但不等於企業實際部署量。

## 4. 風險與盲點（資料缺口）
- Digitimes 的 `Google's AI glasses to boost wearable shipments to 17.5 million in 2026` 搜尋命中，但本文頁面登入受限，未能核對全文，因此不納入主結論。
- `CoWoS delay`、`AI server delay` 透過 Google News RSS 未命中；`GPU lead time` 只抓到 2025 舊文，表示這輪關鍵字追蹤可得性偏低。
- V2EX 熱榜大量被推廣帖佔據，AI 討論噪音較高；本輪只取較可辨識的 Local LLM / 職場條目作旁證。

## 5. 手動補件方式（缺什麼資料 + 如何手動取得）
- 缺：YouTube Trending 排名與 view velocity。
  - 為什麼缺：本輪可穩定驗證的是搜尋結果頁，不是完整 trending feed。
  - 如何手動取得：提供 Trending 截圖、目標影片連結或指定頻道頁，我可補成更精準的熱度排序版。
- 缺：AI CRM 當日更強的第三方新聞擴散。
  - 為什麼缺：Google News RSS 幾乎未命中，現有樣本偏官方 release / 教學影片。
  - 如何手動取得：若你有 Salesforce / HubSpot / Zoho / Lark 指定新聞連結，丟給我可補成商業決策版。
- 缺：供應鏈關鍵字全文核對。
  - 為什麼缺：目前多數只拿到 RSS 標題層級，Digitimes 又有登入牆。
  - 如何手動取得：提供原文連結、會員截圖或 PDF，我可補成供應鏈專版。

## 6. 下一步（可執行 1–3 點）
- 若要投資 / 供應鏈版，下一輪優先深挖 AI 眼鏡供應鏈、HBM shortage 延伸與台灣封裝鏈映射。
- 若要產品版，下一輪把 OpenClaw、Microsoft Scout、Salesforce Agentforce 做成一張 `always-on agent / workflow / governance` 對照表。
- 若要內容版，下一輪可直接輸出一篇「AI 眼鏡升溫、OpenClaw 平台化、AI CRM 仍在導入期」的 Threads / Moltbook 短文。