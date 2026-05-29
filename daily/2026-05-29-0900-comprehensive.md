# 09:00 綜合報告（資料版）
日期：2026-05-29

## 1) 事實（fact）
- 市場資料：TWSE 官方 `MI_INDEX` 2026-05-28 收盤顯示，發行量加權股價指數報 43,636.44，跌 620.36 點，跌幅 -1.40%；臺灣資訊科技指數報 85,842.60，跌幅 -1.14%。截至 2026-05-29 09:00，本報未取得可直接引用的台股當下即時盤數字。
- 市場資料：Stooq 公開頁於 2026-05-29 01:01 UTC 抓到美股前一交易日數字：S&P 500 報 7,563.60，+0.57%；Dow Jones 報 50,669.00，+0.05%；Nasdaq Composite 報 26,917.47，+0.91%。
- 市場資料：USDTWD 於 2026-05-28 10:00 報 31.4462，日變動 +0.05%（Stooq）。
- 市場資料：美國財政部 `daily_treasury_yield_curve` CSV 顯示，2026-05-28 美國 10 年期公債殖利率為 4.45%，低於 2026-05-27 的 4.48%。
- 市場資料：Stooq 公開頁於 2026-05-29 01:01 UTC 抓到，現貨金 XAUUSD 報 4,501.75 美元/盎司，日變動 +0.13%；Bitcoin 報 73,676.27 美元，日變動 -0.04%。
- 事件面：NBC News 於 2026-05-28 17:35 UTC 報導，美國與伊朗仍在互相打擊，停火壓力未形成明確降溫訊號。
- 事件面：IAPP 於 2026-05-28 16:56 UTC 指出，中國發布新的 AI ethics guidelines，香港完成 AI 與個資 compliance checks，亞洲 AI 治理節奏同步收緊。
- 事件面：Reuters 於 2026-05-28 10:33 UTC 指出，高通膨環境下，美債作為傳統避險資產的角色仍在被市場重估。
- 科技熱點：截至今早 05:30 趨勢包，GitHub 熱門專案集中在 AI agent / skills / memory / workflow tooling，包括 `Understand-Anything`、`ai-engineering-from-scratch`、`twentyhq/twenty`。
- 科技熱點：截至今早 07:00，Hacker News 高互動主題包括 `Using AI to write better code more slowly` 與 `GitHub Actions down again today`；V2EX 熱榜集中在 AI 寫碼品質、工具疲勞與折扣價格敏感。
- 科技熱點：Google Blog 已公告 Gemini 智慧眼鏡將於 2026 秋季推出；AI CRM 討論焦點集中在 Salesforce Agentforce 的收入轉化能力，而非單純概念熱度。
- 固定關鍵字：`HBM shortage` 今日有命中，05:30 趨勢包記錄 Google 搜尋結果出現 SK Hynix、TechNews、DigiTimes 等供應緊張摘要；`GPU lead time` 今日有命中，搜尋摘要提到企業級 GPU 約 12–20 週、B200 可到 3–6 個月；`CoWoS delay` 僅弱命中單一搜尋片段；`AI server delay` 今日未見新增高可信訊號。
- 系統/排程狀態：`2026-05-29-0530-morning-trends.md`、`2026-05-29-0700-international.md` 已分別於 05:37 與 07:02 生成；`2026-05-29-tavily-digest.md` 已生成但僅 163 bytes、只有空標題，代表該來源本輪未提供實質內容。
- 系統/排程狀態：`reports/moltbook_status_latest.json` 最近快照時間為 2026-03-20T04:13:03Z，非今日資料；可作長期基線，不可當成今早即時狀態。Threads 自動發布仍承接既有阻塞：Graph API token 過期、browser 備援 session 不可用。
- 資料限制：本報市場欄位以今早可驗證公開數字為主；台股 09:00 即時盤、X/Threads 即時討論、YouTube 原生播放指標未納入，避免假造同時點資料。

## 2) 推論（inference）
1. 結構判讀：隔夜美股由科技權重股帶動上行，但台股最新官方收盤仍是明顯回檔，代表市場不是全面 risk-on，而是「美國大型科技相對強、亞洲現貨資金仍偏保守」的分化結構。
2. 風險因子：短線最大外部風險仍是美伊衝突延長，其次是 AI 監管加速與開發基礎設施可靠性疑慮。利率面雖較前一日略回落到 4.45%，但還沒低到能直接解除估值壓力。
3. 資金風格：從 GitHub、HN、V2EX 到 AI CRM 訊號一致看，資金更偏向能把 AI 轉成流程、收入、品質控制的整合層，而不是無差別追逐新模型或次級題材。
4. 使用者真正關心的核心問題：AI 供應鏈瓶頸今天仍有訊號，但證據強度不平均。`HBM shortage` 與 `GPU lead time` 可列為持續壓力；`CoWoS delay` 只有弱命中；`AI server delay` 沒有新增高可信證據。因此今天不能把整條 AI 硬體鏈說成全面卡關，只能說瓶頸敘事仍在、但公開證據主要集中在記憶體與交期端。

## 3) 建議（action）
1. 今日節奏：先把「隔夜美股科技反彈」與「台股現貨是否跟上」分開看。若台股開盤後半導體/AI 伺服器鏈沒有快速承接，不要只因美股上漲就追價。
2. 警戒點：第一，看美伊衝突是否出現正式停火協調或能源運輸新消息；第二，看美國 10Y 是否重新站回 4.50% 上方；第三，若今日出現 Reuters、DigiTimes、TechNews、公司法說明確新增 `CoWoS delay`、`GPU lead time`、`AI server delay` 原文，再升級供應鏈風險判讀。
3. 部位控管：AI/半導體部位以龍頭與有現金流驗證者為主，先避免因弱證據去擴大二三線供應鏈曝險；若本來就有風險部位，今天更適合做減槓桿與集中化，不適合用單一 headline 開新槓桿。
4. watchlist / 重點標的：
   - 美股 AI 龍頭：NVDA、AVGO、MU、MRVL。
   - 平台與企業 AI：GOOGL、CRM、MSFT。
   - 台股供應鏈觀察：台積電、AI 伺服器鏈、HBM / 封裝相關概念股。
   - 指標追蹤：USD/TWD、US 10Y、Gold、BTC，以及 `HBM shortage` / `GPU lead time` 的新增原文證據。
