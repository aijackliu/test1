# 2026-06-06 05:30 清晨趨勢包

資料可得性：中
時間基準：2026-06-06 05:30（Asia/Taipei）

## 1. 核心結論（3–5 點）
- 眼鏡主線比 OpenClaw / AI CRM 更有即時熱度；近 24–48 小時可驗證訊號集中在 Meta 智慧眼鏡的臉部辨識與隱私爭議。
- YouTube 搜尋結果顯示，OpenClaw／AI CRM 相關影片仍有存量，但新片增量不高；最近 2–4 天較新的內容偏「AI smart glasses 總評」而非 OpenClaw 專題。
- AI CRM 新聞訊號偏企業導入與財報敘事，不是新一輪 consumer demo；可驗證條目集中在 HubSpot、Bigin AI Agents、Salesforce/CVS。
- 開發者注意力仍集中在 agent infra 與本地效率：GitHub Trending 前排是 hermes-agent、headroom、open-notebook；Hacker News 也把 pg_durable 與 Gemma 4 QAT 推上前列。
- 供應鏈關鍵字本輪有命中，但重點幾乎都落在 HBM shortage；本輪未驗證到同等強度的 CoWoS delay / GPU lead time / AI server delay 當日新增公開訊號。

## 2. 分來源重點（GitHub / 社群 / 新聞 / 影音）

### GitHub
- `NousResearch/hermes-agent`：GitHub Trending 第 1，今日 +1,821 stars；描述為「The agent that grows with you」。
- `chopratejas/headroom`：今日 +2,503 stars；主打壓縮 tool outputs / logs / RAG chunks，降低 LLM token 成本。
- `lfnovo/open-notebook`：今日 +1,142 stars；定位是 open source NotebookLM 替代方案。
- 訊號解讀：開發者偏好仍偏向 agent orchestration、context compression、local knowledge tooling，而不是單純新模型榜單。

### 社群
- Hacker News 第 2：`pg_durable: Microsoft open sources in-database durable execution`，240 points，62 comments，5 小時前。
- Hacker News 第 4：Google 官方 `Gemma 4 QAT models`，192 points，55 comments，5 小時前；焦點是壓縮後仍能在 mobile / laptop / edge device 跑。
- V2EX 熱議前排仍偏職場與 AI 使用體感，不是新產品發布：
  - `纯吐槽公司技术团队现状`（183 回覆）
  - `ChatGPT 账号被封`（109 回覆）
  - `大家是怎么使用 AI 的...`（97 回覆）
- X / Threads：本輪未納入有效公開樣本；原因見下方缺口說明。

### 新聞
- Smart glasses：Google 官方文章 `A new look at how Android XR will bring Gemini to glasses and headsets` 可直接驗證，文中明講 Android XR 眼鏡結合相機、麥克風、揚聲器與可選鏡片顯示，示範訊息、導航、拍照、即時翻譯等場景。
- Smart glasses：Google News RSS 在 6/4–6/5 抓到多篇 Meta 智慧眼鏡臉部辨識相關標題，來源含 WIRED、Engadget、Gizmodo、9to5Google；本輪共同訊號是「功能想像開始轉向辨識與隱私風險」。
- AI CRM：Google News RSS 抓到 `HubSpot ... AI CRM Momentum`（Yahoo Finance, 6/4）、`Can Bigin’s AI Agents Redefine CRM Automation for Small Businesses?`（The Futurum Group, 6/1）、`CVS Health ... with Salesforce’s Agentforce Health`（CVS Health, 5/28）。
- OpenClaw：Google News RSS 搜尋有多篇含 `OpenClaw` 標題的媒體索引，但本輪未逐篇打開全文交叉驗證，因此只視為新聞索引，不把標題外推成更強結論。

### 影音
- YouTube 搜尋 `OpenClaw AI CRM smart glasses` 前排可驗證結果中，與 OpenClaw 直接相關者多為 2–4 個月前：
  - `Openclaw Smart Glasses are INSANE`（Samin Yasar，3 個月前）
  - `Connect Rokid to Openclaw in 2 min🔥`（Rokid，2 個月前）
  - `Introducing DenchClaw: AI CRM that runs on your OpenClaw.`（Dench，2 個月前）
- 最近 2–4 天的新片偏廣義 AI 眼鏡：
  - `Top 12 Best AI Smart Glasses of 2026`（TechOrigin，2 天前）
  - `Under $1,000 NTD! Entry-level AI smart glasses...`（獅心瘋，4 天前）
- 訊號解讀：影音端「AI 眼鏡」仍有新鮮內容，但 `OpenClaw + AI CRM` 交集目前不是搜尋結果中的高更新主題。

### 關鍵字命中
- `HBM shortage`
  - 來源：Tech Times
  - 時間：2026-06-03 16:57 GMT
  - 摘要：標題直接寫出 `HBM Crisis` 與 agent economy / Computex 2026 並列。
  - 連結：https://news.google.com/rss/articles/CBMi1gFBVV95cUxQV05kVGJtZmhfT2FFUHZvM3pfYW9EOFpKbHJSR2FEbFpQZ1h1UHRwMEhmMzR0OU9IU0M4OXVweklUM1MxQVdtbVNtSHVIQjdleDg1Vk1jalBsVkhFZXJCekswLUh2VmFQZndSWlg3Y1RqVzduZ0JtTVNka2wxM2FfRlNQNGlHOGMwd0FyTUs5UkZINEJIelNLbm1QNG1NTk43TWRHSTJVT0RWLW9EYS1iUkUtajBaT09uek1ZM3M1VU9oQjE1dzNKNUhERlRreG1pOW1WX0Jn?oc=5
- `HBM shortage`
  - 來源：Chosunbiz
  - 時間：2026-06-02 07:39 GMT
  - 摘要：標題指出 SK hynix 擴產規劃，直接對應 `HBM shortage through 2030`。
  - 連結：https://news.google.com/rss/articles/CBMiekFVX3lxTFBTOFY2bXY0cF9EcFZIX1UycUV3SmJKUEs1SnJVQk9EcS1kbVhkNGxlYXo5UHl1ZXVtWndkNlhZSWdKcUhZVnRHbXlLWnU2c3J0bVh3SGRIMUNLN2FjaUpYQW11TmoxTDFHV2xqSWhTcFBCOTNDZmE3WUln0gGOAUFVX3lxTE8wMkN1Y2ZsaVkzSW5lYXljUmwyRkNpVjBsZmtaSkRUUi1aMV9xX19Ob1RMOHBua21SXzZ1N1p6UVRBTDhTbXRzNFNYRktOVGlGc2E0eWtYVk5iNVh6cGFBR3NRZDZWNkNXVTYxaGprRTU0WVg4eDBicHl4YU1pN2lpQXVuSm5BbWZQZWpZOHc?oc=5
- `CoWoS delay`：今日未命中可驗證新條目。
- `GPU lead time`：今日未命中可驗證新條目。
- `AI server delay`：今日未命中可驗證新條目。

## 3. 風險與盲點（資料缺口）
- X / Threads 公開抓取仍不穩定；本輪沒有足夠可驗證樣本可納入，否則容易把搜尋摘要或二手轉述當原文。
- Google News RSS 能穩定拿到標題、來源、時間，但不是每一則都已在本輪打開原文全文；因此本報對新聞段只做「標題級」結論，不做更深推論。
- YouTube 本輪拿到的是搜尋結果，不是 Trending 或實際觀看增速；因此只能判斷「題材新鮮度」，不能判斷「爆量程度」。

## 4. 風險與盲點（資料缺口）
- GitHub Trending 與 HN 是即時頁，可信度高；但它們反映的是 builder attention，不等於市場採用。
- V2EX 熱帖多是中文技術社群情緒樣本，能反映使用者體感，不等於產品銷售或部署數據。
- `OpenClaw` 新聞搜尋結果含媒體二次報導與評論標題；若要用於決策，需要逐篇打開原文再做二次核對。

## 5. 手動補件方式（缺什麼資料 + 如何手動取得）
- 缺：X / Threads 對 `OpenClaw / AI CRM / smart glasses` 的即時公開貼文樣本。
  - 為什麼缺：公開頁登入牆 / 搜尋結果不穩 / 原文難直接驗證。
  - 如何手動取得：提供指定帳號頁、貼文連結，或搜尋結果截圖（含時間）。
- 缺：YouTube Trending / 爆量影片變化。
  - 為什麼缺：本輪只穩定取得搜尋結果，未取得完整 trending ranking 與增速。
  - 如何手動取得：提供 YouTube Trending 截圖、指定頻道頁，或你要追的關鍵影片連結。
- 缺：Google News RSS 某些 `OpenClaw` / `AI CRM` 標題的全文細節。
  - 為什麼缺：RSS 先拿到索引，原文需逐篇深挖。
  - 如何手動取得：丟原文連結給我，我可以補成全文摘要版。

## 6. 下一步（可執行 1–3 點）
- 若你要把這包轉成「投資 / 產品決策版」，下一輪先逐篇打開 3 篇：Meta smart glasses 隱私文、HubSpot AI CRM、Google Android XR 官方文。
- 若你要追 `OpenClaw + 眼鏡` 真實熱度，下一輪建議改追 `Rokid / Android XR / Meta Ray-Ban / AI smart glasses`，比直接搜 `OpenClaw` 更有即時樣本。
- 若你要追 `AI CRM + agent` 落地，下一輪建議固定盯 `HubSpot / Salesforce Agentforce / Zoho Bigin` 三條線。