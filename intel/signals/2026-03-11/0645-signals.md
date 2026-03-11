# Signal Engine Scan — 2026-03-11 06:45 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 06:45 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Sources used: Google News RSS headline sweep (5 watcher buckets)
- Data gap:
  - `web_search` unavailable (missing `PERPLEXITY_API_KEY`)
  - No direct X stream + no interaction velocity telemetry
- Quality constraint: stale items and low-cred reposts were noise-deducted.

## Signal Scoring (100)

### 1) AI Infra — Oracle/OpenAI DC expansion retrenchment narrative persists
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Bloomberg, CNBC, The Information（via Google News RSS）
- 命中關鍵字：Oracle, OpenAI, flagship data center, expansion, Stargate, debt
- 摘要（2-3 句）：多個高權重媒體仍集中於「Oracle 與 OpenAI 擴建節奏調整」與「資料中心資本結構壓力」兩條主線。訊息延續上一輪，並未見明確反轉澄清。
- 判讀（1-2 句）：屬於 AI 基建資本開支節奏訊號，仍具追蹤價值，但尚未達官方公告級別。
- 反向驗證（反證/待確認項）：缺 OpenAI/Oracle 官方 IR 或監管文件；尚未補到 X 官方帳號即時回應。
- 建議動作（Follow-up）：持續 48h 追蹤公司聲明與券商 note；若出現 capex 指引/案場時程變動，升級。
- 評分拆解：帳號權重 24 / 關鍵字 22 / 熱度速度 12 / 跨來源確認 13 / 去雜訊 -(-3) => 74

### 2) Macro/Oil — event-driven volatility, awaiting hard data
- 類別：Macro / Oil
- 熱度分：57/100
- 等級：L3
- 來源：Investing.com（地區版）, FXStreet
- 命中關鍵字：CPI, oil inventories, WTI, Middle East tensions
- 摘要（2-3 句）：短線油價受地緣因素波動，但市場主要等待 CPI 與庫存數據確認。現有來源偏事件解讀，硬數據尚未落地。
- 判讀（1-2 句）：偏 headline shock，未形成可執行的中高確信趨勢訊號。
- 反向驗證（反證/待確認項）：需 Reuters/Bloomberg/EIA 原始數據確認；目前交叉來源層級不足。
- 建議動作（Follow-up）：數據發布後重算，觀察是否轉為持續趨勢。
- 評分拆解：帳號權重 11 / 關鍵字 18 / 熱度速度 11 / 跨來源確認 7 / 去雜訊 -(-10) => 57

### 3) Crypto Flow — BTC outflow narrative remains noisy
- 類別：Crypto Flow
- 熱度分：44/100
- 等級：L3
- 來源：MEXC blog, Live Bitcoin News, TradingView repost
- 命中關鍵字：BTC outflow, exchange supply, stablecoin outflow, ETF outflow run
- 摘要（2-3 句）：主題仍圍繞交易所流出與流動性收縮，但來源結構偏二手與交易所敘事。缺主流金融媒體和權威鏈上數據同步背書。
- 判讀（1-2 句）：可觀察，但目前不具決策級可靠度。
- 反向驗證（反證/待確認項）：需補 ETF 官方流量、鏈上數據供應商與主流媒體交叉確認。
- 建議動作（Follow-up）：下一輪整合 ETF/鏈上/交易所儲備三類硬數據再評分。
- 評分拆解：帳號權重 8 / 關鍵字 18 / 熱度速度 9 / 跨來源確認 5 / 去雜訊 -(-4) => 44

### 4) Taiwan Semi — no fresh multi-source catalyst
- 類別：Taiwan Semi
- 熱度分：27/100
- 等級：L3
- 來源：DigiTimes（單源新條目）+ 多數舊聞
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor
- 摘要（2-3 句）：本輪仍未見多源同日催化，結果多為舊新聞回流。缺乏法說/公告/供應鏈新事件。
- 判讀（1-2 句）：空窗期，暫不做方向性判斷。
- 反向驗證（反證/待確認項）：需補 Focus Taiwan、公司 IR、在地財經媒體即時源。
- 建議動作（Follow-up）：下輪收斂查詢至 CoWoS/先進封裝/法說關鍵詞。
- 評分拆解：帳號權重 7 / 關鍵字 10 / 熱度速度 4 / 跨來源確認 2 / 去雜訊 -(-4) => 27

### 5) Chinese Signal — no new policy pulse detected
- 類別：Chinese Signal
- 熱度分：23/100
- 等級：L3
- 來源：結果以 2025~2026 舊聞為主（Reuters/Bloomberg/WTVB 等）
- 命中關鍵字：PBOC, stimulus, loans, yuan, property
- 摘要（2-3 句）：未抓到當日新政策脈衝，輸入多為歷史新聞。當前可得資料不足以支持「新刺激」判讀。
- 判讀（1-2 句）：暫無可執行新訊號。
- 反向驗證（反證/待確認項）：需中國官媒、PBOC 官網更新與離岸市場同步反應。
- 建議動作（Follow-up）：改用窄窗口 query（24h）+ 官源優先。
- 評分拆解：帳號權重 6 / 關鍵字 9 / 熱度速度 3 / 跨來源確認 2 / 去雜訊 -(-3) => 23

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪無 L1 訊號，不觸發即時警報。
- 最高優先續追：AI Infra（Oracle/OpenAI 資料中心擴張節奏）。

## Data Gap / Recovery
- 缺 `PERPLEXITY_API_KEY` 導致無法使用 `web_search`。
- 補件方式：在 Gateway 設定 `PERPLEXITY_API_KEY`（或 `tools.web.search.perplexity.apiKey`），再重跑可提升跨來源與熱度速度評分可信度。
