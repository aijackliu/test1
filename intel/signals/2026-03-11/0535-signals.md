# Signal Engine Scan — 2026-03-11 05:35 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 05:35 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS headline scan
- Data gap: `web_search` still unavailable (missing Perplexity API key), and X stream not covered in this round.
- Quality note: stale items and low-trust repost sources were aggressively down-weighted.

## Signals

### 1) AI Infra — Oracle/OpenAI data center expansion narrative remains dominant
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Bloomberg、The Information、CNBC（皆由 Google News RSS 匯入）
- 命中關鍵字：Oracle, OpenAI, data center, expansion, Stargate, debt
- 摘要（2-3 句）：多來源持續聚焦 Oracle 與 OpenAI 在大型資料中心擴張節奏上的摩擦/調整，且連動到市場對 Oracle 資本支出與負債結構的討論。與 04:00 輪次相比，主敘事未反轉，仍屬高關注但未達官方定論。
- 判讀（1-2 句）：屬可執行的 L2 訊號，值得持續 48h 監控；但缺官方公告與財報級確認，因此暫不升 L1。
- 反向驗證（反證/待確認項）：需 Oracle / OpenAI 官方聲明、法說/IR 文件、主要賣方更新；X 上官方高權重帳號回應仍缺。
- 建議動作（Follow-up）：保持 48h 追蹤，若出現「capex guidance 下修」或「正式延期/取消」才考慮升級。
- 評分拆解：帳號權重 23 / 關鍵字 22 / 熱度速度 13 / 跨來源確認 13 / 去雜訊 -(-3) => 74

### 2) Macro / Oil — event-driven volatility, confirmation still weak
- 類別：Macro / Oil
- 熱度分：57/100
- 等級：L3
- 來源：FXStreet、Investing.com（二線來源為主）
- 命中關鍵字：WTI, Middle East tensions, CPI, inventories
- 摘要（2-3 句）：油價新聞仍聚焦地緣事件帶來的短線波動，市場等待 CPI 與庫存數據提供方向。未見一線來源形成一致的新基本面敘事。
- 判讀（1-2 句）：目前偏交易噪音，尚不足以升到 L2。
- 反向驗證（反證/待確認項）：待 Reuters/Bloomberg/WSJ + EIA 數據後再確認是否演化為趨勢。
- 建議動作（Follow-up）：數據落地後重算分數。
- 評分拆解：帳號權重 12 / 關鍵字 18 / 熱度速度 10 / 跨來源確認 7 / 去雜訊 -(-10) => 57

### 3) Crypto Flow — outflow narrative persists but source quality remains low
- 類別：Crypto Flow
- 熱度分：45/100
- 等級：L3
- 來源：MEXC、Live Bitcoin News、TradingView repost、CryptoRank
- 命中關鍵字：Bitcoin outflow, exchange supply, stablecoin outflows, liquidity
- 摘要（2-3 句）：BTC 交易所流出與流動性收縮敘事仍在，但多為交易所/二次內容來源，且舊文比例高。缺少 ETF 發行商或主流鏈上資料供應商的獨立驗證。
- 判讀（1-2 句）：可作觀察清單，不足以觸發行動級訊號。
- 反向驗證（反證/待確認項）：需補 ETF net flow、stablecoin mint/burn、交易所 reserve 序列。
- 建議動作（Follow-up）：下輪若拿到高品質數據再重評。
- 評分拆解：帳號權重 8 / 關鍵字 19 / 熱度速度 8 / 跨來源確認 6 / 去雜訊 -(-4) => 45

### 4) Taiwan Semi — no fresh multi-source catalyst
- 類別：Taiwan Semi
- 熱度分：27/100
- 等級：L3
- 來源：DigiTimes 單點更新；其餘多為舊聞
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor
- 摘要（2-3 句）：本輪仍未出現可交叉確認的新事件催化，結果多為歷史內容或泛更新頁。
- 判讀（1-2 句）：維持低訊號狀態。
- 反向驗證（反證/待確認項）：需補公司公告、法說、Focus Taiwan/台媒即時流。
- 建議動作（Follow-up）：改用 CoWoS/advanced packaging/capacity expansion 等更窄關鍵詞。
- 評分拆解：帳號權重 8 / 關鍵字 10 / 熱度速度 4 / 跨來源確認 2 / 去雜訊 -(-3) => 27

### 5) Chinese Signal — mostly stale, no fresh policy pulse
- 類別：Chinese Signal
- 熱度分：23/100
- 等級：L3
- 來源：Reuters/Bloomberg 舊聞、其他歷史條目
- 命中關鍵字：PBOC, stimulus, loans, yuan, property
- 摘要（2-3 句）：結果仍以舊聞為主，未看到當日新增且多源確認的政策脈衝。
- 判讀（1-2 句）：資料可得性不足，不能做政策轉向判定。
- 反向驗證（反證/待確認項）：需官媒/PBOC 當日公告與離岸市場即時反應。
- 建議動作（Follow-up）：下輪切換更短時間窗與官方源。
- 評分拆解：帳號權重 6 / 關鍵字 9 / 熱度速度 3 / 跨來源確認 2 / 去雜訊 -(-3) => 23

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪 **無 L1 訊號**（未觸發即時警報）。
- 最高優先追蹤維持：AI Infra（Oracle/OpenAI data center capex narrative）。

## Data Gaps & Manual Recovery
- Missing: `PERPLEXITY_API_KEY`（`web_search` 無法使用）
- Missing: X 高權重帳號流 + interaction velocity
- Manual fix: 在 Gateway 設定 `PERPLEXITY_API_KEY`（或 `tools.web.search.perplexity.apiKey`）後重跑，可提高跨來源驗證與熱度速度評分可靠度。
