# 09:00 綜合報告（資料版）
日期：2026-05-05

## 1) 事實（fact）
- 市場資料：截至今晨可驗證快照，台股加權指數 `^TWII` 本輪未取得可用即時數值；Stooq 對 `^TWII` 回傳 `N/D`，因此不填數字，避免誤報。美股近端可驗證報價為 S&P 500 `^SPX` 7,200.8（Stooq，2026-05-04 23:00）、NASDAQ `^NDQ` 25,067.8（Stooq，2026-05-04 23:00）；半導體 ETF `SOXX.US` 462.15（Stooq，2026-05-04 22:00）；`TSM.US` 401.61、`NVDA.US` 198.543、`MU.US` 576.36、`AVGO.US` 416.54、`MRVL.US` 163.52（均為 Stooq，2026-05-04 22:00 左右）。
- 市場資料：`BTC.V` 80,123.98（Stooq，2026-05-05 03:00）、`XAUUSD` 4,528.135（Stooq，2026-05-05 03:00）、`USDTWD` 31.6127（Stooq，2026-05-04 10:00）。美國 10 年期公債殖利率本輪未取得高可信可視報價，列為缺口。
- 事件面：07:00 國際摘要顯示，中東風險升高，CNBC RSS 命中伊朗攻擊阿聯、荷姆茲海峽軍事護航、油價跳升與歐股走弱；同時美國穩定幣監管出現邊際進展，CLARITY Act 妥協版本保留 stablecoin reward programs；俄烏戰事則在勝利日閱兵前增添安全壓力。
- 科技熱點：05:30 清晨趨勢包顯示，GitHub Trending 仍由 agent / orchestration 類專案主導，`ruflo` 今日新增 2,594 stars，`TradingAgents`、`browserbase/skills`、`n8n-mcp` 同列前段；Hacker News 前排聚焦語音 AI 基礎設施、瀏覽器安全與 AI 企業估值。
- 科技熱點：眼鏡主題的可驗證訊號偏向 Samsung 智慧眼鏡傳聞與 Meta Ray-Ban 隱私爭議；AI CRM 訊號偏向 Salesforce × Google Cloud、Salesforce × Microsoft 與 Creatio 的 AI 工作流/定價調整。OpenClaw 相關則以 Google News RSS 命中媒體或企業報導為主，尚未完成官方頁交叉驗證。
- 系統/排程狀態：`2026-05-05-0530-morning-trends.md` 已於 05:32:44 +0800 落檔，`2026-05-05-0700-international.md` 已於 07:01:22 +0800 落檔；`2026-05-05-tavily-digest.md` 已建立，但內容為空白模板，無法提供補充摘要。`memory/2026-05-05.md` 已記錄 01:30–01:32 完成當日 Daily Tech Trends Digest 與 Moltbook 發布，貼文 ID `fba383b4-a1b5-4289-8851-5e634c4b2c1e`；Threads 自動發布仍受失效 token 阻塞，今晨未見修復證據。
- 固定追蹤關鍵字：`HBM shortage` 今日有延續命中，05:30 趨勢包引用 Google News RSS 線索 `SK Hynix flags persistent HBM shortage as demand outpaces supply`（digitimes，2026-04-23）；`CoWoS delay` 今日未見新增高可信訊號；`GPU lead time` 今日未見新增高可信訊號；`AI server delay` 今日未見新增高可信訊號。
- 資料限制：X / Threads / YouTube 即時熱榜仍缺乏穩定且可公開驗證的抓取；OpenClaw 命中仍停留在 RSS 層級；台股指數與美債殖利率本輪缺即時高可信數值，因此本報告僅使用已驗證公開資料，不補猜測值。

## 2) 推論（inference）
1. 結構判讀
   - 目前市場結構是「AI 主線仍強，但短線定價權回到能源與地緣風險」。美股大盤與半導體鏈維持高檔，但今晨跨市場新增訊號主要來自中東與油價，不是新的 AI 供應鏈加速證據。
2. 風險因子
   - 短線最大風險是油價、航運保費與風險溢價同步抬升，進一步壓縮高估值科技股容忍度。若荷姆茲海峽風險外溢到亞洲開盤，航空、高耗能製造與風險資產會先承壓。
3. 資金風格
   - 資金風格偏向「留在核心 AI / 半導體資產，但不願全面擴散」。`MU` 強於 `NVDA`、`AVGO`、`MRVL`，代表資金更願意押已被驗證的記憶體需求，而不是對整條 AI 鏈無差別追價。
4. 使用者真正關心的核心問題
   - 今天能不能把 AI 供應鏈當成進攻主軸。以目前資料看，答案偏向「可維持核心觀察與既有部位，但不適合因題材熱度擴大追價」。原因是四個固定追蹤關鍵字中，今天仍只有 `HBM shortage` 有延續訊號，`CoWoS delay`、`GPU lead time`、`AI server delay` 都沒有新的高可信增量。

## 3) 建議（action）
1. 今日節奏
   - 先用「能源風險是否擴散」決定早盤節奏。若亞洲時段先出現油強股弱，就以防守、分批、等確認為主；若油價風險沒有擴散，再回頭觀察半導體主鏈是否出現二次承接。
2. 警戒點
   - 盤中盯三組訊號：第一，油價、航運與航空股是否同步轉弱；第二，`HBM shortage / CoWoS delay / GPU lead time / AI server delay` 是否出現新的原始高可信來源；第三，台股權值與美股半導體 ADR 是否同向，避免只剩單一市場撐盤。
3. 部位控管
   - 已有 AI 部位者，保留 `TSM / NVDA / AVGO / MU` 這類核心標的優先，對沒有新催化的延伸題材股採更高紀律；若今天盤勢轉成油強股弱，不新增高波動科技曝險。
4. watchlist / 重點標的
   - 先看 `2330.TW / TSM`、`NVDA`、`MU`、`AVGO`、`MRVL`、`SOXX`；事件面持續追中東油運風險與美國 stablecoin 監管進度；供應鏈面固定追 `HBM shortage`、`CoWoS delay`、`GPU lead time`、`AI server delay`。若今天收盤前仍只有 `HBM shortage` 有延續，維持「主線沒壞，但沒有加速」判讀。
