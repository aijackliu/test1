# 05:30 清晨趨勢包｜2026-07-12

## 1. 核心結論
- AI 眼鏡今天的主線不是新硬體規格，而是 **「常時感知 / 持續錄影」帶來的隱私爭議**；Meta 相關報導密集，討論焦點已從功能轉向監管與社會接受度。
- AI CRM 主線偏向 **agentic workflow 與資料自動化**；Salesforce、Microsoft、HoneyBook、GReminders 都在強調把 AI 嵌進銷售/客戶流程，而不是單點聊天功能。
- 開發者圈早盤熱度偏 **agent skills / agent tooling / infra**；GitHub Trending 與 HN 都能看到技能庫、MCP/桌面控制、Rust/Postgres、測試與基礎設施工具同時升溫。
- YouTube 搜尋結果顯示 **OpenClaw 仍在教學與解說擴散期**，不是即時新聞期；高觀看影片集中在「是什麼／怎麼裝／工作流怎麼搭」。
- 今日資料可得性為 **中**：GitHub、HN、Google News 可驗證；V2EX 熱門頁抓取失敗、YouTube 需從頁面原始資料抽取，完整度有限。

## 2. 分來源重點

### GitHub
- `wonderwhy-er/DesktopCommanderMCP` 今日 +900 stars，主題是給 Claude/MCP 的桌面控制、檔案搜尋與 diff 編輯。
- `malisper/pgrust` 今日 +789 stars，主題是 Rust 重寫 Postgres 並通過回歸測試，代表底層資料系統仍有高關注。
- `google-labs-code/stitch-skills` 今日 +338 stars，顯示 agent skills / skill library 仍是熱門方向。
- `anthropics/claude-cookbooks` 今日 +322 stars，說明 agent/LLM 實作範例需求仍強。
- 來源：https://github.com/trending（抓取時間：2026-07-12 05:30 Asia/Taipei）

### 社群
- HN 排名前段以開發工具、資料庫、JS runtime 為主，沒有單一壓倒性 AI 新聞，市場情緒偏「實作/基建」。
- HN 第 3 則出現 `Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom`，代表 GPU 資本循環仍被技術圈持續關注。
- V2EX `?tab=hot` 本輪只抓到站點框架資訊，未回傳熱門主題清單；無法據此判讀華語社群熱點。
- 來源：HN front page、V2EX hot（抓取時間：2026-07-12 05:30 Asia/Taipei）

### 新聞
- Google News「AI smart glasses」結果密集指向 Meta：`Meta reportedly testing smart glasses with continuous recording`、`Meta tests ‘super sensing’ AI glasses...`、`Meta Still Internally Debating Privacy Of Always-On AI Glasses`。
- 同一題材還延伸到隱私保護措施：`Meta to turn off Ray-Ban AI glasses' camera if privacy light is tampered with`。
- Google News「AI CRM」結果以流程自動化與 agentic CRM 為主：`Salesforce receives double blow over an AI product`、`Salesforce Deepens Commitment to Switzerland with $1 Billion Investment to Accelerate Agentic AI Transformation`、`GReminders Launches 'AI Forms' to Automate CRM Data Extraction...`。
- Microsoft 仍在推「Agentic CRM in the flow of work」，顯示 CRM 敘事正從 SaaS 升級到工作流代理層。
- 來源：Google News 搜尋頁（抓取時間：2026-07-12 05:31 Asia/Taipei）

### 影音
- YouTube「AI smart glasses」前排可見：`Every AI Smartglasses Explained in 20 minutes`（1 個月前，約 1.9 萬觀看）、`Ray-Ban Meta vs Xiaomi AI Smart Glasses...`（1 年前，約 31 萬觀看）、`全球搶先實測 Google Android XR 智慧眼鏡...`（1 個月前，約 38 萬觀看）。
- YouTube「AI CRM」前排可見：`AI CRM Workflows: Best way to use AI in your CRM`、`Lark CRM | AI-Powered All-in-One CRM...`、`AI × CRM 成交力！... AI Agent...`；內容聚焦 lead workflow、自動分類、AI notetaker 串接。
- YouTube「OpenClaw AI」前排可見：`OpenClaw Explained in 12 Minutes (for beginners)`（約 29 萬觀看）、`How to Set Up OpenClaw in 30 Minutes`（約 3.8 萬觀看）、`The wild rise of OpenClaw...`（約 201 萬觀看）。
- 這代表 OpenClaw 在影音端的需求仍是 **教育、安裝、工作流理解**，不是單日新功能驅動。
- 來源：YouTube 搜尋結果頁原始資料抽取（抓取時間：2026-07-12 05:31 Asia/Taipei）

### 關鍵字命中
- 今日未命中（以可驗證公開頁為準）。
- 補充：關鍵字搜尋有出現二線分析站對 `HBM shortage / CoWoS / GPU lead time` 的摘要片段，但缺主流媒體或官方原始頁面交叉驗證，本報未納入正式命中。

## 3. 風險與盲點（資料缺口）
- V2EX 熱門頁只回到站點框架內容，沒有實際熱門討論列表；可能是頁面結構/反抓限制。
- YouTube 搜尋頁是高度動態頁，本輪改用原始 HTML 內嵌資料抽取；可拿到標題、部分觀看數與上架時間，但不保證排序 100% 等同登入後實際畫面。
- Google News 搜尋結果可驗證標題與相對時間，但部分文章是聚合來源，若要做深判讀，仍需逐篇打開原文。
- `web_search` 本輪狀態不穩，部分查詢回報 provider 設定錯誤；因此今天沒有把搜尋 API 當主資料源。

## 4. 手動補件方式（缺什麼資料 + 如何手動取得）
- 缺什麼：V2EX 真正的熱門討論清單。
  - 為什麼缺：公開抓取只回站點骨架。
  - 如何手動取得：打開 https://www.v2ex.com/?tab=hot ，截圖或貼上前 10 則標題。
- 缺什麼：YouTube 登入後穩定排序與最新篩選結果。
  - 為什麼缺：未直接取得互動式搜尋頁完整 DOM。
  - 如何手動取得：在 YouTube 搜尋 `AI smart glasses`、`AI CRM`、`OpenClaw AI`，切到「篩選 > 本月 / 本週」，貼前 5 支影片。
- 缺什麼：HBM shortage / CoWoS delay / GPU lead time / AI server delay 的主流媒體或官方來源。
  - 為什麼缺：本輪只有二線分析站片段，沒有足夠交叉驗證。
  - 如何手動取得：提供 Reuters / FT / TSMC / NVIDIA / 供應鏈公司原文連結，再補做命中判讀。

## 5. 下一步
- 先追 Meta AI 眼鏡的隱私線：若今天白天有更多 FT / Reuters / Meta 官方說法，可快速補成單主題快報。
- 若要落地到商業判讀，建議把 AI CRM 來源縮到 Salesforce / Microsoft / HubSpot / HoneyBook 四家官方更新，減少行銷稿噪音。
- 若 jack 要做 OpenClaw 內容或產品判斷，下一輪可改抓 YouTube 最新影片 + GitHub issue/repo 動態，分開看「認知擴散」與「產品進度」。
