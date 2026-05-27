# 09:00 綜合報告（資料版）
日期：2026-05-27

## 1) 事實（fact）
- 市場資料
  - 台股：Stooq `^TWSE` 顯示，`2026-05-27 03:00:35 CEST`（頁面內時間）加權指數為 `44,502.78`，日內高低 `44,502.78 / 43,842.26`，較前值 `43,525.37` 上漲 `+977.41`（`+2.25%`）。
  - 美股：Stooq `^SPX` 顯示，`2026-05-26 23:00:00` 收 `7,519.10`，高低 `7,539.10 / 7,501.10`，較前值 `7,473.50` 上漲 `+45.60`（`+0.61%`）。
  - 美股：Stooq `^NDQ` 顯示，`2026-05-26 23:00:00` 收 `26,656.18`，高低 `26,725.29 / 26,520.30`，較前值 `26,343.97` 上漲 `+312.21`（`+1.19%`）。
  - 匯率：Stooq `USDTWD` 顯示，`2026-05-26 10:00:04` 為 `31.4594`，日內高低 `31.5160 / 31.4079`。
  - 利率：CNBC `US10Y` 顯示，`9:01 PM EDT` 美國 10 年債殖利率為 `4.481%`，日內高低 `4.485% / 4.477%`，前收 `4.491%`。
  - BTC：Stooq `BTC.V` 顯示，`2026-05-27 03:00:59` 報 `75,992.32`，日內高低 `76,020.31 / 75,594.73`。
  - Gold：Stooq `GC.F` 顯示，`2026-05-27 03:00:57` 報 `4,548.20` 美元/盎司，日內高低 `4,560.15 / 4,532.00`。
- 事件面
  - `07:00 國際事務摘要` 顯示，Google 搜尋結果頁可見 Reuters 線索：Micron 於 `2026-05-26 10:11 AM PDT` 一度站上 `1 兆美元市值`；Qualcomm 與 ByteDance 傳出 AI 晶片合作，時間標記 `2026-05-26 7:55 AM PDT`；EU 衛星頻譜方案與德國對 EU 資本市場聯盟妥協訊號也在同日 Reuters 線索中出現。
  - 同份摘要顯示，Hacker News 前排可驗證高互動條目包含 `GitHub Actions down again today`（約 `274 points / 153 comments`）與 `Using AI to write better code more slowly`（約 `814 points / 321 comments`）。
  - 系統/排程狀態：`2026-05-27-0530-morning-trends.md` 於 `05:35` 已生成，`2026-05-27-0700-international.md` 於 `07:05` 已生成；`browser` 狀態為 `running=true`、`cdpReady=true`。
  - 系統異常：`logs/tavily_daily_digest.log` 顯示今日 `tavily_search.py` 仍出現 `TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'`，因此 `2026-05-27-tavily-digest.md` 只有空骨架。`memory/2026-05-27.md` 另記錄 Threads 自動發布仍受 `OAuthException code 190` 阻塞。
- 科技熱點
  - `05:30 清晨趨勢包` 顯示，GitHub Trending 前排仍由 AI agent / AI engineering 基建主導，包括 `Understand-Anything`（`4,721 stars today`）、`ECC`（`1,912 stars today`）、`ai-engineering-from-scratch`（`2,169 stars today`）、`knowledge-work-plugins`（`1,698 stars today`）。
  - `VisionClaw` 的 arXiv 摘要與 GitHub 倉庫都明示 `Meta Ray-Ban smart glasses + OpenClaw AI agents`；同份 05:30 報告記錄 GitHub 星數為 `2,320`。
  - Salesforce 官方文 `8 Ways AI Agents Are Evolving in 2026`（頁面日期 `2026-05-01`）明列 `deterministic guardrails`、`context engineering`、`headless CRM`、`observability`。
  - 固定追蹤關鍵字：
    - `HBM shortage`：有命中。`05:30` 報告引用 GPUnex，指出 HBM 已成 GPU 供應瓶頸，缺口可能延續到 `2028–2029`。
    - `CoWoS delay`：今日未見新增高可信訊號。
    - `GPU lead time`：有命中。`05:30` 報告引用 Igor’sLAB / TrendForce 整理，指出 `PCBs and CPUs` lead time 已接近 `1 year`。
    - `AI server delay`：有命中。同一來源指出 `entire server platforms are delayed`，且 `2026` 全球 server 成長預估由接近 `20%` 下修至約 `13%`。
- 資料限制
  - Reuters 直頁需 JS，本輪主要依 Google 搜尋結果頁可見標題與時間線索引用，未直接擷取 Reuters 完整內文。
  - X / Threads 仍缺穩定原文層級資料；`CoWoS delay` 沒有補到 Reuters / TrendForce / TSMC / 法說等一手新證據。

## 2) 推論（inference）
1. 結構判讀
   - 今天結構偏明確：股指、Nasdaq、Micron 線索、GitHub Trending 與企業 AI 治理題材一起指向「AI 主線仍強，但資金更集中在可交付的基建、記憶體、企業導入與可靠性工具鏈」，不是全面擴散式 risk-on。
2. 風險因子
   - 眼前最大風險不是需求消失，而是交付與基礎設施摩擦：`HBM shortage`、`GPU lead time`、`AI server delay` 都還在；同時 `GitHub Actions` 再度成為高互動議題，說明市場開始把「能不能穩定運轉」看得和「有沒有 AI 故事」一樣重要。
3. 資金風格
   - `S&P 500` 與 `Nasdaq` 同步走高，但 `US10Y 4.481%` 仍在不低水位、`Gold 4,548.20` 也未明顯回落，代表資金風格更像「核心成長資產續抱 + 宏觀避險尚未撤」，高 beta 題材仍需靠基本面與交付節奏支撐。
4. 使用者真正關心的核心問題
   - 供應鏈框架今天沒有被推翻：`HBM shortage` 與 `AI server delay` 仍是有效壓力，`GPU lead time` 有延長證據，但 `CoWoS delay` 今天沒有新增高可信惡化訊號。換句話說，今天可以繼續沿用「AI 需求強、交付受限」的判讀，但不該把 `CoWoS delay` 當成新增利空放大交易。

## 3) 建議（action）
1. 今日節奏
   - 先把今天定義成「驗證強勢盤」：早上優先觀察台股 AI／半導體權值與伺服器鏈是否量價同步，若只有題材股衝、權值不跟，先別把盤勢當成全面擴散行情。
2. 警戒點
   - 盯四個點：`台股 44,500` 附近能否站穩、`US10Y` 是否重新上拐、`BTC 75.6k` 是否失守、以及是否出現新的 `CoWoS delay` 一手來源。若其中兩項同時轉弱，今天就該把強勢視為短打而非趨勢延伸。
3. 部位控管
   - 對吃交付節奏的部位維持紀律，不要用未驗證的 `CoWoS delay` 自己加戲；真正要保守的是依賴 HBM 緩解、AI server 快速出貨、或基礎設施零中斷假設的持股與供應鏈敘事。
4. watchlist / 重點標的
   - 上游供應鏈：`TSMC / SK hynix / Micron / Samsung`，看 HBM 與先進封裝擴產節奏。
   - 美股核心：`NVDA / MU / MRVL / AVGO / GOOGL / PLTR`，看資金是否繼續集中在平台級與基建級受益股。
   - 台股鏈：`台積電 / 聯電 / 世界先進 / 力積電`，以及 AI server、電源管理、封裝與散熱族群。
   - 系統面 watchlist：修 `tavily_search.py` 的 Python 相容性問題、確認 Threads token 更新進度，避免後續情報與發布鏈路持續掉資料。