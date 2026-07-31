# 05:30 清晨趨勢包 - 2026-07-31

資料可得性：中-低
說明：本次 `browser` 公開頁抓取出現 timeout / aborted，已依 fallback 改用公開網頁、官方頁、Hacker News、V2EX、YouTube 公開搜尋頁內嵌資料與搜尋結果補抓；X / Threads 未取得足夠可驗證原文，不補造。

## 1. 核心結論
- GitHub 與 Hacker News 今晨主軸很一致：焦點從「單一模型能力」轉向「agent 工作流基建」。`openwork` 在 GitHub Trending 拿到 916 stars today，GitHub 也同步推出 stacked pull requests 公開預覽。
- 機器人熱度明顯升高。DeepMind 於 2026-07-30 發布 Gemini Robotics 2，Hacker News 同條目約 6 小時內累積 403 points / 352 comments。
- 價格效能戰繼續升溫。OpenAI 2026-07-30 宣布 GPT-5.6 Luna 降價 80%、Terra 降價 20%，Sol Fast mode 最高提速 2.5 倍。
- 「眼鏡 × agent」在 YouTube 出現新一波實作訊號。`Run Your Own AI Agent on Even Realities G2 (Complete OcuClaw Setup)` 約 36 分鐘前上線，顯示穿戴式 agent 已開始出現更具體的 setup 內容。
- AI CRM 討論重點不是「加一個聊天框」，而是把 CRM 變成可在郵件、聊天、簡報與 agent 間流動的 context layer；Microsoft Dynamics 365 官方文已明確用 agentic CRM / headless CRM 描述這個方向。

## 2. 分來源重點
### GitHub
- `different-ai/openwork`：GitHub Trending 顯示 916 stars today，定位為 open-source alternative to Claude Cowork，訊號偏向「agent workflow 分享 / 連接 / 協作層」。
- `huggingface/speech-to-speech`：GitHub Trending 顯示 627 stars today，主打本地語音 agent pipeline，代表可落地的本地語音互動仍在升溫。
- `ChromeDevTools/chrome-devtools-mcp`：GitHub Trending 顯示 73 stars today，延續 coding agent 與 browser / devtools 整合需求。

### 社群
- Hacker News：`Gemini Robotics 2 brings whole body intelligence to robots` 約 6 小時前上榜，403 points / 352 comments，今晨最強 AI 研究訊號之一。
- Hacker News：`Advancing the price-performance frontier with GPT-5.6` 約 4 小時前，410 points / 264 comments，顯示社群已把成本 / 延遲視為一級戰場。
- Hacker News：`Stacked PRs are now live on GitHub` 約 5 小時前，295 points / 105 comments，對 coding workflow 的結構性改動獲高關注。
- V2EX：OpenAI / Codex 相關討論密集，含 `GPT5.6 降智降到没边了`（27 回覆）、`同时跑多个 Codex 任务时，我做了个本地状态观察器`、`没人讨论新版的 mcp 协议吗，感觉进步很大`（19 回覆）；華語開發者關注點偏向多 agent 管理、模型穩定性、協議層變化。

### 新聞
- OpenAI 官方（2026-07-30）：GPT-5.6 Luna 新價格為每百萬 input token US$0.20、output token US$1.20；Terra 為 input US$2、output US$12；Sol Fast mode 最高 2.5x 速度。
- DeepMind 官方（2026-07-30）：Gemini Robotics 2 主打 whole-body control、雙手精細操作、多機協作，並強調 on-device adaptation 可在數小時內適配新機體。
- GitHub 官方（2026-07-30）：stacked pull requests 進入 public preview，可分層 review、單次合併整疊 PR，直接對應 agent 生成大量變更後的人類審查瓶頸。
- Microsoft Dynamics 365 官方（2026-06-25 / 2026-07-07 搜尋可驗）：agentic CRM 被定義為把 customer context、next-best action、agent orchestration 直接放進 Outlook / Teams / PowerPoint 等 flow of work，而不是留在傳統 CRM 單體介面。

### 影音
- YouTube 公開搜尋頁內嵌資料：`Run Your Own AI Agent on Even Realities G2 (Complete OcuClaw Setup)`｜Tech with Spencer｜36 分鐘前｜48 views。
- YouTube 公開搜尋頁內嵌資料：`沒有鏡頭的 Even G2 是我最想每天戴出門的智慧眼鏡`｜3C 達人廖阿輝｜10 小時前｜5,665 views。
- YouTube 公開搜尋頁內嵌資料：`全球搶先實測Google Android XR 智慧眼鏡...`｜3cTim哥生活日常｜2 個月前｜398,397 views；代表中文圈對 Android XR / Gemini 眼鏡已有較成熟的流量承接。
- YouTube 公開搜尋頁內嵌資料：OpenClaw 一般搜尋前列仍以 TED / IBM Technology / Hung-yi Lee 等解說型影片為主；新鮮度最高的可驗證新增訊號是 OcuClaw + Even G2 實作片。

## 關鍵字命中
- `HBM shortage`｜命中｜2026-06-29｜TechTimes｜`Lenovo AI Server Backlog Hits $21 Billion as HBM Shortage Stalls China’s Compute Race`；文中稱三大廠 2026 年 HBM 產能已售罄，SK Hynix 警告 shortage 可能延續至 2027 後段。連結：https://www.techtimes.com/articles/319260/20260629/lenovo-ai-server-backlog-hits-21-billion-hbm-shortage-stalls-chinas-compute-race.htm
- `AI server delay`｜命中（低信度）｜2026-07-06｜Bloomberg 搜尋結果 / placeholder 頁｜搜尋摘要提到 Nvidia next-generation AI server rack 因製造困難延後超過一年；原文公開頁未成功抽出正文。連結：https://www.bloomberg.com/news/articles/2026-07-06/nvidia-ai-server-delay-report-sends-asian-pcb-stocks-sliding
- `CoWoS delay`｜今日未命中。
- `GPU lead time`｜今日未命中。

## 3. 風險與盲點（資料缺口）
- `browser` 本輪無法穩定打開公開頁，錯誤為 timeout / aborted；因此未能用互動式頁面複核 YouTube、Google News、X、Threads。
- X / Threads 在 logged-out 公開模式下未取得足夠可驗證原文，今日社群段落不把它們當主證據。
- Google News 搜尋頁只返回大量前端樣板，未能直接抽出有效新聞條目。

## 4. 風險與盲點（資料缺口）
- 部分「眼鏡 / AI server delay」訊號只能取得搜尋摘要或 YouTube 公開搜尋頁內嵌 JSON，可信度低於直接官方原文。
- V2EX 頁面可讀但回傳被截斷，僅適合抓取前排熱門討論，不適合做完整社群統計。
- 關鍵字命中中，`AI server delay` 目前只有 Bloomberg placeholder + 搜尋摘要佐證，應視為待補件訊號，不宜當成最終供應鏈判斷。

## 5. 手動補件方式（缺什麼資料 + 如何手動取得）
- 缺：X / Threads 今晨原文貼文。
  - 原因：公開頁可驗證性不足、browser 本輪 timeout。
  - 手動補法：提供指定帳號頁、貼文連結或截圖；我可補成同格式摘要。
- 缺：Google News / Bloomberg 原文正文。
  - 原因：前者返回 JS 樣板，後者公開頁僅抽到 placeholder。
  - 手動補法：提供原文連結、全文截圖或已登入瀏覽器可見頁面；我可補做關鍵字命中複核。
- 缺：YouTube 今日更完整的趨勢排行。
  - 原因：目前僅解析公開搜尋結果，非完整 Trending / topic shelf。
  - 手動補法：提供 YouTube Trending 或指定頻道頁截圖 / 連結，我可補強影音段落。

## 6. 下一步（可執行 1–3 點）
- 若要提高完整度，先修復 `browser` / gateway 路徑，再重跑 YouTube、Google News、X、Threads 公開頁複核。
- 若要聚焦主題，下一輪可直接拆成三條監控線：`OpenClaw / 穿戴式 agent`、`agentic CRM`、`AI 供應鏈關鍵字`。
- 若 jack 要，我可以在 08:00 前再補一版「只看眼鏡 / OpenClaw / AI CRM」的窄版追蹤。