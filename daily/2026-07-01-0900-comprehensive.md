# 09:00 綜合報告（資料版）
日期：2026-07-01

## 1) 事實（fact）
- 市場資料
  - 台股：本輪以 Google Finance 頁面即時抓取，`加權指數（IX0001:TPE）` 顯示為 `47,267.43`，漲幅 `+2.47%`。
  - 美股：AP News 2026-06-30 收盤資料顯示，`S&P 500` 收 `7,499.36`（`+58.93`，`+0.8%`）、`Dow Jones` 收 `52,319.20`（`+136.46`，`+0.3%`）、`Nasdaq Composite` 收 `26,213.72`（`+393.58`，`+1.5%`）、`Russell 2000` 收 `3,024.37`（`+13.95`，`+0.5%`）。
  - 利率：Trading Economics 顯示，美國 `10Y Treasury` 於 `2026-07-01` 為 `4.46%`。
  - 匯率：Google Finance 本輪抓取 `USD/TWD` 為 `31.8340`，較前值 `31.8500` 下跌 `0.05%`；Trading Economics 同日頁面顯示 `31.8320`、日變動 `+0.12%`。
  - BTC：CoinMarketCap 本輪頁面抓取 `BTC` 為 `58,240.37 USD`，`24h` 變動 `+2.53%`。
  - Gold：Trading Economics 顯示，黃金於 `2026-07-01` 為 `3,997.36 USD/t.oz`，日變動 `-0.26%`。
- 事件面
  - Reuters 2026-06-30 報導，伊朗表示不會與美國特使會面。
  - Reuters 2026-06-30 報導，Saab 與烏克蘭簽下 `25.4 億美元` Gripen 戰機合約。
  - Reuters 2026-06-30 報導，加薩援助體系接近 `breaking point`。
  - Reuters 2026-06-30 報導，美國預期不延長 `USMCA`，啟動長期倒數程序。
  - AP News 2026-06-30 報導，美股當日上漲，同時提到 AI 類股在 6 月中旬波動後再度轉強。
  - 系統/排程狀態：`2026-07-01 01:31–01:39（Asia/Taipei）` 已完成 `Daily Tech Trends Digest - 2026-07-01`；Moltbook 已補發成功，post id `bf42a276-feff-4051-bd46-5bb1ac28d0eb`；Threads 自動發布仍不可用，既有可驗證阻塞為 `Graph API token` 已於 `2026-04-11` 過期，browser 也無可用登入態。
- 科技熱點
  - OpenClaw 在 2026-06-29～06-30 的外部能見度上升，主軸為 iOS / Android app 上線與教學內容擴散。
  - AI CRM 討論重點落在 `Agentic CRM / AI Sales / 自動化營收流程`；可驗證來源包括 Salesforce Summer '26 與 Omnichat OmniClaw。
  - 固定關鍵字追蹤：`HBM shortage` 今日有延續高可信訊號（Lenovo AI server backlog `21B` 美元與 HBM 供應瓶頸連結）；`GPU lead time` 今日有延續高可信訊號（Spheron 引述 `H100 SXM5 36–52 週`、`H200 40+ 週`）；`AI server delay` 今日有延續高可信訊號（Lenovo backlog 與 HBM 缺口直接連結）；`CoWoS delay` 今日未見以此詞直述的新增高可信事件，但有 `TSMC CoWoS capacity fully allocated through at least mid-2027` 的相關供應約束證據。
- 資料限制
  - 美國財政部 `daily-treasury-rates.csv` 本輪抓取失敗（`503`），因此利率改採 Trading Economics fallback。
  - `web_search` 本輪不可用（SearXNG base URL 未配置），部分市場資料改採 browser 與可直接抓取公開頁。
  - `BTC` 使用 CoinMarketCap 頁面即時值；`USD/TWD` 同時出現 Google Finance 與 Trading Economics 兩個近似數值，顯示來源刷新時間略有差異。

## 2) 推論（inference）
1. 結構判讀
   - 目前市場主結構仍是 `AI 多頭 + 宏觀風險未退`：美股由 Nasdaq `+1.5%` 領漲，台股加權指數同步站上 `47,000` 上方，說明風險資金仍集中在科技與 AI 基建鏈。
   - 但黃金仍接近 `4,000` 美元、美債 10 年期在 `4.46%`，代表市場不是無腦 risk-on，而是成長追價與防禦配置並存。
2. 風險因子
   - 中東風險沒有結束。伊朗拒與美方特使會面、加薩人道壓力升高，代表油價雖先回落，但 headline risk 還在。
   - 利率風險沒有鬆。`10Y Treasury 4.46%` 仍在高位，若往上再推，會壓縮高估值 AI / 半導體的估值容忍度。
   - 供應鏈風險目前仍主要卡在 `HBM shortage` 與 `GPU lead time`；`CoWoS delay` 與全面性的 `AI server delay` 仍未取得更多原始公告級硬證據，不宜自行擴大解讀成整條鏈條全面惡化。
3. 資金風格
   - 資金偏向大型科技、AI infra、先進製程與記憶體瓶頸受惠股，而不是全面擴散到所有風險資產。
   - Russell 2000 雖收紅，但漲幅明顯弱於 Nasdaq，反映市場還是在買龍頭敘事，不是在買全面景氣復甦。
4. 使用者真正關心的核心問題
   - 今天真正要盯的不是「AI 題材還能不能講」，而是「AI 需求強度是否已從需求確認，進一步外溢到可量化的供應瓶頸定價權」。
   - 目前答案偏向：需求還強，且 `HBM / 高階 GPU 交期` 仍是最硬的瓶頸；但還沒有足夠證據證明 `CoWoS delay` 已經擴大成今天的主交易敘事。

## 3) 建議（action）
1. 今日節奏
   - 今天把節奏定義成「順勢看多 AI 主線，但不在高位亂追」；優先等回檔、等確認、等新數字，不用因為盤勢強就把節奏打亂。
2. 警戒點
   - 盤中持續盯三個警戒：`10Y Treasury` 是否重新往 `4.50%` 靠攏、伊朗/加薩 headline 是否再推升油價、以及 `HBM shortage / GPU lead time / CoWoS delay / AI server delay` 是否出現客戶名單或交期數字級的新證據。
3. 部位控管
   - 若手上已經偏重 AI / 半導體，今天優先控槓桿、保留現金，不把盈利部位再硬加滿。
   - 若要新增部位，優先選有訂單可見度、供給受限、能把瓶頸轉成毛利或議價權的標的；對只有題材、沒有新數字驗證的標的，維持小部位試單。
4. watchlist / 重點標的
   - 台股：`2330 TSMC`、`2454 聯發科`、HBM/封裝鏈相關標的；重點看先進封裝擴產與 AI 需求外溢。
   - 美股：`NVDA`、`AMD`、AI server / networking 鏈；重點看 GPU 交期、企業 capex 指引、以及是否出現伺服器遞延的新增硬訊號。
   - 觀察項：若今天 `CoWoS delay` 仍沒有新增客戶/交期數字，就維持「供應緊、但未證實全面延誤」的基線，不主動把它升級成主敘事。