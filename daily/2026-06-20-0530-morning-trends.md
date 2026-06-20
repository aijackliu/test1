# 05:30 清晨趨勢包｜2026-06-20

資料可得性：中低
更新時間：2026-06-20 05:30（Asia/Taipei）
模式：Mode A（資訊彙整型）

## 1. 核心結論
- 開源與工程圈的主線，從「單模型能力」轉向「agent 執行層 + local/open weights 可交付能力」。GitHub Trending、HN 同步出現 agent framework、open weights、local model 討論。
- 眼鏡 / 可穿戴 AI 訊號持續升溫。YouTube 搜尋前排仍由 AI smart glasses 評測與比較主導；OpenClaw × smart glasses 已有媒體示範與學術論文。
- AI CRM 主線更靠近「可控、自動化、無頭接入」。Salesforce 官方把 deterministic guardrails、MCP、Headless 360 列為 2026 關鍵方向，且 2026-06-15 已公告收購 Fin。
- 社群可驗證即時訊號偏向人才與基建。X 上 Sam Altman 2026-06-18 連發貼文歡迎 Noam Shazeer 加入 OpenAI；Threads 上 Mark Zuckerberg 2026-06-16 公布 Threads 月活 5 億。
- 供應鏈關鍵字今日未驗證到強命中；至少 CoWoS delay 在 Google News 搜尋頁顯示「There are no items to show.」，其餘關鍵字搜尋受搜尋/頁面可得性限制，不能硬下結論。

## 2. 分來源重點（GitHub / 社群 / 新聞 / 影音）

### GitHub
- `DeusData/codebase-memory-mcp`：今日 Trending 前排，主打把 codebase 索引成 persistent knowledge graph。連結：https://github.com/DeusData/codebase-memory-mcp
- `n0-computer/iroh`：模組化網路堆疊，反映 infra / agent connectivity 題材仍熱。連結：https://github.com/n0-computer/iroh
- `Panniantong/Agent-Reach`、`obra/superpowers` 也進前排，顯示 agent workflow / skills framework 仍在吸星。連結：https://github.com/Panniantong/Agent-Reach 、https://github.com/obra/superpowers

### 社群
- Hacker News 第 1 名：`GLM-5.2 is the new leading open weights model on Artificial Analysis`，4 小時前、348 points、166 comments。連結：https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index
- Hacker News 第 9 名：`Running local models is good now`，22 小時前、1408 points、546 comments。連結：https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/
- X / @sama：2026-06-18 02:02 UTC 發文歡迎 Noam Shazeer 加入 OpenAI；同串強調「10 年後終於一起工作」。連結：https://x.com/sama/status/2067427678529974740
- Threads / @zuck：2026-06-16 03:59 公布「Threads 在不到 3 年達到 5 億月活」。連結：https://www.threads.com/@zuck
- V2EX：`web_fetch` 只拿到骨架頁，browser 驗證流程不穩，今日未取得可驗證熱帖內容。

### 新聞
- Salesforce 官方部落格 `8 Ways AI Agents Are Evolving in 2026`：明列 deterministic guardrails、context engineering、MCP、Headless 360、降低延遲與 harness 為企業 agent 主線。連結：https://www.salesforce.com/blog/ai-agent-trends-2026/
- Salesforce Investor Relations：2026 年公告將收購 Fin，官方說法是把 customer agent platform 納入、加速 autonomous agents 佈局。連結：https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Fin/default.aspx
- Reuters 相關報導頁面因 JS / ad-blocker 限制無法直接抓正文；僅能以公開搜尋結果交叉驗證「約 36 億美元」這一層級訊息，未把 Reuters 內文細節當已驗證事實。
- arXiv `VisionClaw: Always-On AI Agents through Smart Glasses`：v2 提交時間 2026-04-08，描述 Meta Ray-Ban smart glasses + OpenClaw agents 的 always-on wearable agent，含實驗與部署研究。連結：https://arxiv.org/abs/2604.03486
- Heise 英文報導（2026-06）指出：開發者 Jake Ledner 以 Meta Ray-Ban Display + WhatsApp + OpenClaw/Codex 做「邊走邊 vibe coding」示範，但也明示第三方 display 權限與安全風險仍是落地限制。連結：https://www.heise.de/en/news/Vibe-Coding-on-the-Nose-Developer-Controls-OpenClaw-via-Smart-Glasses-11185272.html

### 影音
- YouTube `smart glasses AI` 搜尋前排仍是需求驗證型內容，不是單點新品爆量。前 8 筆中，1 個月內新片包含：
  - `Top 10 Best AI Smart Glasses For 2026`（1 個月前，3.8 萬次）
  - `Every AI Smartglasses Explained in 20 minutes`（1 個月前，1.5 萬次）
  - `Google AI Glasses vs Meta Ray-Ban: It's Not Even Close!`（4 週前，18 萬次）
- 舊片流量仍由大頻道吃走：MKBHD `Wait... Smart Glasses are Suddenly Good?` 累積 816 萬次，顯示題材熱度高，但新 entrants 仍靠比較 / 選購 / 教育內容切入。搜尋頁：https://www.youtube.com/results?search_query=smart+glasses+AI&sp=CAI%253D

## 3. 風險與盲點（資料缺口）
- V2EX 今日未取得可驗證熱帖清單；`web_fetch` 只回骨架頁，browser 分頁驗證失敗。
- Reuters / Reuters Technology 正文受 JS 與反廣告限制，無法直接抓取原文；今日新聞面因此偏向官方公告與二次交叉來源。
- Google News 關鍵字頁面不穩；已驗證到 `CoWoS delay` 搜尋頁顯示無結果，但 HBM shortage / GPU lead time / AI server delay 的結果頁無法穩定保留可抓取頁面。
- YouTube 為搜尋結果，不是官方 Trending；可反映主題供給與觀看量，但不能等同平台全站熱門榜。

## 4. 關鍵字命中
- HBM shortage：今日未命中（browser 搜尋分頁不穩，`web_search` 僅回廣告性結果，無可驗證原文）。
- CoWoS delay：今日未命中。已驗證 Google News 搜尋頁顯示 `There are no items to show.`
- GPU lead time：今日未命中（搜尋頁可得性不足，未取得可驗證原文）。
- AI server delay：今日未命中（搜尋頁可得性不足，未取得可驗證原文）。

## 5. 手動補件方式（缺什麼資料 + 如何手動取得）
- 缺 V2EX 熱帖：請提供 `https://www.v2ex.com/?tab=hot` 的截圖或 3–5 個熱帖連結；我可補進社群段。
- 缺 Reuters / 財經原文：請提供 Reuters 文章原連結或截圖；我可補成已驗證新聞摘要。
- 缺供應鏈關鍵字即時命中：請提供 Google News / X / 產業媒體連結（HBM shortage、CoWoS delay、GPU lead time、AI server delay 任一）；我可補成「關鍵字命中」正式區塊。
- 若要改成 YouTube 真 Trending，而非搜尋趨勢：請提供 YouTube Trending 截圖或地區頁連結。

## 6. 下一步（可執行 1–3 點）
- 先把今日主線收斂成一句話：`AI 競爭從模型分數轉向 agent 執行層、可穿戴入口與企業可控自動化。`
- 若要發社群版，可優先寫兩條：`OpenAI 人才 / open weights`、`smart glasses × OpenClaw / AI CRM`。
- 若 jack 要更可交易 / 可決策版本，我下一輪可把這份快報改成「前 3 風險 × 最小可行行動（MVA）」版。