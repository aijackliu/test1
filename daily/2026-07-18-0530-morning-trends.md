# 05:30 清晨趨勢包｜2026-07-18

## 1. 核心結論（3–5 點）
- GitHub 今晨可驗證熱點仍偏向「AI 開發工具 / agent workflow / product telemetry」。`PostHog/posthog`、`github/copilot-sdk`、`Nutlope/hallmark` 同時在榜。
- OpenClaw × 智慧眼鏡題材仍靠影音內容延續熱度；YouTube 公開搜尋可驗證到 `Openclaw Smart Glasses are INSANE`、`Connect Rokid to Openclaw in 2 min` 等既有內容持續被檢索命中。
- 官方智慧眼鏡路線沒有驗證到今天新增公告，但 Google（2026-05-19）與 Samsung 公開頁仍明確指向「今年秋季上市」這條時間線。
- AI CRM 敘事繼續往「agent 直接進 CRM 工作流」集中；Salesforce Agentforce 官方頁仍主打 24/7 agents、builder、script、voice 等完整平台能力。
- 供應鏈關鍵瓶頸仍是 HBM／先進封裝／GPU 交期；今日可直接驗證的公開頁仍把 HBM 與 CoWoS 視為 AI 硬體供應主瓶頸，但 `AI server delay` 本輪未抓到可直接驗證原文。

## 2. 分來源重點（GitHub / 社群 / 新聞 / 影音）

### GitHub
- `codecrafters-io/build-your-own-x`：527,232 stars，今日 +1,070；雖非 AI 專案，但仍是開發者學習型內容最大流量入口。  
  來源：https://github.com/trending
- `PostHog/posthog`：36,159 stars，今日 +437；描述直接寫到 AI observability、analytics、logs 與 self-driving products。  
  來源：https://github.com/trending
- `Nutlope/hallmark`：11,929 stars，今日 +1,486；主打反 AI slop 的 design skill，反映「AI 產出治理」也成熱門分支。  
  來源：https://github.com/trending
- `github/copilot-sdk`：9,778 stars，今日 +234；顯示 agent 嵌入 app / service 的 SDK 路線仍在升溫。  
  來源：https://github.com/trending

### 社群
- Hacker News 最高互動不是新模型，而是 `AWS: Inaccurate Estimated Billing Data – $1.7 billion`：925 points、594 comments，基礎設施可觀測性與計費可信度成今天最強社群議題。  
  來源：https://news.ycombinator.com/
- HN 上 `Kimi K3, and what we can still learn from the pelican benchmark` 有 213 points、123 comments，代表開源/前沿模型評測仍有穩定關注。  
  來源：https://news.ycombinator.com/
- V2EX 熱門頁可驗證到 AI 討論仍集中在工具效果與模型實測：`推上看到有人让 K3 写了个网页版 macOS，这结果有点强啊`（77 replies）、`Kimi K3，不来个朴实无华的讨论吗？`（59 replies）。  
  來源：https://www.v2ex.com/?tab=hot
- X / Threads 本輪未完成當日時間線驗證；browser snapshot 全數 timeout，不能把搜尋片段當成已驗證樣本。  
  限制：browser timeout、公開搜尋結果不穩

### 新聞
- Google 官方頁（2026-05-19）仍是智慧眼鏡最清楚的公開路線圖：`Audio glasses are launching first, coming later this fall`，並列出導航、訊息、拍照、翻譯、多步任務。  
  來源：https://blog.google/products-and-platforms/platforms/android/android-xr-io-2026/
- Samsung Newsroom 明寫首波 intelligent eyewear collections 將於今年秋季在 select markets 推出。  
  來源：https://news.samsung.com/us/samsung-google-first-look-new-intelligent-eyewear
- Salesforce Agentforce 官方頁可直接驗證其定位為 `Build, deploy, and manage AI agents at scale`，並延伸到 Agentforce Builder、Agent Script、Agentforce Voice。  
  來源：https://www.salesforce.com/agentforce/
- Reuters tech/world 與 TSMC IR 本輪抓取失敗：Reuters 只回 `Please enable JS and disable any ad blocker`，TSMC IR 遇到 403 / Just a moment，故未納入正文事實。  
  來源限制：JS/反爬阻擋

### 影音
- YouTube 影片頁可直接驗證 `Agentic CRM Explained: How AI is Revolutionizing B2B Sales in 2026` 發佈於 2026-03-10，片長 20 分 32 秒。  
  來源：https://www.youtube.com/watch?v=XpwsUNKouhM
- `Top 3 AI CRM You Must use in 2026!` 可直接驗證發佈於 2026-04-26，片長 8 分 16 秒。  
  來源：https://www.youtube.com/watch?v=2u_rlDUxiuM
- `Rokid AI Glasses Style | First AI Glasses with ChatGPT & Gemini` 可直接驗證發佈於 2026-07-16，片長 1 小時 22 分 2 秒；代表 AI 眼鏡題材在近 48 小時內仍有新內容上架。  
  來源：https://www.youtube.com/watch?v=dan8uoWmQ60
- YouTube 搜尋結果可驗證 OpenClaw 相關內容簇仍存在：`Openclaw Smart Glasses are INSANE`（2026-02-28）、`Connect Rokid to Openclaw in 2 min`（2026-02-04）。  
  來源：https://www.youtube.com/results?search_query=OpenClaw+smart+glasses

## 3. 關鍵字命中
- **HBM shortage**｜SupplyICs｜2026-05-04｜明寫 2026 標準 DRAM 供應緊張的主因是 HBM3E / HBM4 擠壓產能，且 `hbm lead times 2026 stretch to 52 weeks or are entirely sold out for new customers`。  
  連結：https://supplyics.com/insights/market-intelligence/2026-hbm-dram-memory-supply-chain-analysis/
- **HBM shortage**｜Apex Component｜文內敘述 early 2026｜文中寫 Micron 2026 全年 HBM 產能已 sold out，Samsung / SK Hynix 也被描述為 full capacity allocation through 2026。  
  連結：https://apexcomponent.com/hbm-memory-shortage-2026/
- **CoWoS delay / CoWoS capacity constraint**｜SupplyICs｜2026-05-04｜文中指出 AI logic chip demand 與 advanced packaging materials demand `outstrips global CoWoS capacity`。  
  連結：https://supplyics.com/insights/market-intelligence/2026-hbm-dram-memory-supply-chain-analysis/
- **GPU lead time**｜VerticalData｜2026 年文內分析頁｜文中寫 data center GPUs 與 next-gen NVIDIA / AMD MI300 systems lead times `can extend close to a year in many cases`。  
  連結：https://verticaldata.io/ai-supply-chain-constraints-lead-times-gpu-allocation-and-the-new-reality-of-hardware-procurement/
- **AI server delay**｜今日未命中可直接驗證的公開原文。  
  限制：本輪只找到搜尋結果標題或二手分析，未取得可直接複核的原文頁。

## 4. 風險與盲點（資料缺口）
- browser 工具本輪對 GitHub / HN / V2EX / YouTube snapshot 全數 timeout，因此動態頁細節改以 `web_fetch` / `requests` 公開頁補抓。
- X / Threads 未拿到可直接驗證的當日時間線；不能把搜尋 snippets 當成今日社群樣本。
- Reuters 與 TSMC IR 都遇到 JS / 反爬阻擋，故今天新聞面缺少一手財經媒體與晶圓廠 IR 補強。
- YouTube 搜尋頁可驗證命中內容與部分影片 metadata，但未完成觀看數、留言數、排名序全面複核。
- 關鍵字命中主要來自行業分析頁，不是廠商正式產能公告；可作趨勢訊號，不宜當成公司正式指引。

## 5. 手動補件方式（缺什麼資料 + 如何手動取得）
- **缺什麼資料**：X / Threads 上 OpenClaw、智慧眼鏡、AI CRM 的當日貼文。  
  **為什麼缺**：browser timeout，公開搜尋結果又不穩。  
  **如何手動取得**：用已登入帳號開指定時間線或搜尋頁，提供截圖 / 連結，我可補成社群段落。
- **缺什麼資料**：Reuters / TSMC IR 一手新聞或法說細節。  
  **為什麼缺**：JS / 403 / anti-bot 阻擋。  
  **如何手動取得**：提供文章直連、PDF、或截圖，我可補成新聞與關鍵字交叉驗證。
- **缺什麼資料**：YouTube 影片觀看數、留言數、搜尋排序。  
  **為什麼缺**：本輪只穩定拿到標題、日期、片長。  
  **如何手動取得**：指定 3–5 支影片 URL 或提供搜尋結果截圖，我可逐支補齊完整 metadata。

## 6. 下一步（可執行 1–3 點）
- 若今天要追主線，建議先盯三件事：`OpenClaw 影音熱度是否轉成新產品/教學內容`、`Google/Samsung 智慧眼鏡秋季上市節點`、`Agentforce 是否出現新區域/新功能公告`。
- 若要做投資/供應鏈追蹤，下一輪優先補 `TSMC CoWoS / packaging` 與 `HBM allocation` 的官方或法說來源。
- 若要做內容輸出，最值得拆的是 `OpenClaw × smart glasses × AI CRM workflow` 這條交叉敘事，但需先補社群當日樣本。  
