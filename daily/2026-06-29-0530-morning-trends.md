# 2026-06-29 05:30 清晨趨勢包

模式：Mode A（資訊彙整型）
資料可得性：中低（Google News／YouTube／Google 搜尋分頁多次出現 tab not found；社群與部分新聞頁有 JS/反爬限制）

## 1. 核心結論
- GitHub Trending 今日高熱度仍集中在 agent／自動化工作流：OpenMontage 今日 +2,938 stars、Palmier Pro +2,463、Matt Pocock skills +2,051。
- YouTube 搜尋「open source AI agents 2026」已把 OpenClaw 納入主流教學流量；結果頁可見 IBM Technology、Wagner’s TechTalk、Youri van Hofwegen 等影片。
- Hacker News 與 LocalLLaMA 同步偏向基礎設施/效能議題：HN 有 TOP500 新超算與記憶體價格資料；LocalLLaMA 高票討論集中在 96GB 改裝 4090/5090、多 GPU 推論、llama.cpp/Vulkan。
- 眼鏡線今日可驗證新聞聚焦 Meta 低價新款：TechCrunch 2026-06-23 指 Meta Glasses 起價 299 美元，且為自有品牌而非 Ray-Ban/Oakley 聯名。
- AI CRM 可驗證公開訊號以 Salesforce 為主：Summer ’26 Release 於 2026-06-15 可用，主打 multi-agent orchestration、Customer Engagement Agent、Slack-first workflows。

## 2. 分來源重點（GitHub / 社群 / 新聞 / 影音）
### GitHub
- OpenMontage：開源 agentic video production system，總星數 11,723，今日新增 2,938。
- Palmier Pro：macOS video editor built for AI，總星數 7,192，今日新增 2,463。
- codebase-memory-mcp、Matt Pocock skills、deer-flow 同步上榜，反映 agent 技能庫／長任務編排仍有高關注。

### 社群
- V2EX 熱門 AI 相關貼文可見「ClaudeCode 穩定的美國出口 IP 都能被封」「OpenAI 速率限制重置」等，焦點偏可用性/限制而非新模型。
- LocalLLaMA 日榜前列集中在 96GB 4090/5090 改裝、DeepSeek-V4-Pro、量化與多 GPU 推論；硬體擴充仍是核心話題。
- X/Threads 可得性低；本輪僅驗到 XCancel 搜尋頁，未取得足夠可驗證貼文內容，不作主證據。

### 新聞
- Salesforce Summer ’26 Release：2026-06-15 可用，主打 multi-agent orchestration、Self-Service、Customer Engagement Agent、Tableau MCP。
- Salesforce 2026-06-16 宣布未來五年投資義大利 10 億美元，官方稿稱用於 agentic AI 轉型、米蘭新辦公室與 AI 培訓。
- TechCrunch 2026-06-23：Meta 推出自有品牌 Meta Glasses，起價 299 美元，支援 Meta AI、步行導航與新增 14 種即時翻譯語言。

### 影音
- YouTube 結果頁前列為「7 new open source AI tools you need right now…」（Fireship）與「AI Agents Explained: How to Create and Use AI Agents in 2026」。
- 同頁可見 OpenClaw 相關影片：「What is OpenClaw? Inside AI Agents, LLMs and the Agentic Loop」「OpenClaw on Raspberry Pi 5…」「How to Set Up your First AI Agent in 2026」。
- 已驗到多支影片章節直接提及 OpenClaw，但未穩定取得 AI CRM／AI glasses 專用 YouTube 搜尋頁快照。

## 關鍵字命中
- HBM shortage｜TechTimes｜2026-06-03｜文中稱 HBM 供給缺口可能延續至 2030，並引用 Computex 2026 上 SK 與 Nvidia 互動作為佐證。｜https://www.techtimes.com/articles/317695/20260603/ai-memory-shortage-locked-through-2030-computex-2026-brings-agent-economy-hbm-crisis.htm
- CoWoS delay｜今日未命中（本輪已驗資料內未抓到可複核公開頁）。
- GPU lead time｜今日未命中（僅見 LocalLLaMA 硬體改裝/多 GPU 討論，未見可複核 lead time 公開頁）。
- AI server delay｜今日未命中（本輪未取得可複核新聞或公告頁）。

## 3. 風險與盲點（資料缺口）
- Google News、Google 搜尋與新開 YouTube 分頁多次回傳 tab not found，導致眼鏡／AI CRM／關鍵字新聞覆蓋不完整。
- X/Threads 仍缺穩定 primary evidence；Threads 既有登入/Token 條件不足，XCancel 只驗到搜尋入口。
- U.S. News/Reuters 路徑遭 403 反爬，無法直接複核 Reuters 原文，只能以 TechCrunch 與搜尋結果互證。

## 4. 風險與盲點（資料缺口）
- HBM shortage 命中主要來自 TechTimes 單篇與搜尋結果線索，未再補到第二家同日正式報導，可信度需人工二次複核。
- AI CRM 今日可驗公開源明顯偏 Salesforce；HubSpot / Microsoft Dynamics 365 未在本輪抓到同等可驗、同時效的公開頁。
- YouTube AI CRM 與 AI glasses 專用搜尋分頁先前已建立，但後續 snapshot 失效，故影音面仍偏 OpenClaw／agents 主題。

## 5. 手動補件方式（缺什麼資料 + 如何手動取得）
- 缺 Google News 關鍵字完整頁：在 Chrome 直接開 `https://news.google.com/search?q=HBM%20shortage%20OR%20CoWoS%20delay%20OR%20GPU%20lead%20time%20OR%20AI%20server%20delay` 後手動截前 5 則。
- 缺 AI glasses / AI CRM YouTube 搜尋頁：在 YouTube 搜 `AI glasses 2026`、`AI CRM`，各記前 3 支影片標題、頻道、上架時間。
- 缺 Reuters/官方交叉驗證：優先補抓 Meta 官方 newsroom、Microsoft Dynamics 365 blog/press、HubSpot product/blog 公告頁。

## 6. 下一步（可執行 1–3 點）
- 先補 Google News 關鍵字頁與 Meta/Microsoft/HubSpot 官方公告，提升新聞面完整度。
- 若要發外部版本，可把 OpenClaw 影音熱度與 GitHub agent 工具上榜整理成單獨一段「Agent 生態熱區」。
- 若 06:30 再跑一次，建議固定保留可用 tab，不要依賴新開 label，以降低 browser target 漂移。