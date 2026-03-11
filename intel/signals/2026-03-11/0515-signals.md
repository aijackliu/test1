# Signal Engine Scan — 2026-03-11 05:15 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 05:15 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS headline scan
- Data gap: `web_search` unavailable (missing Perplexity API key), so this round still lacks X stream and engagement-velocity data.
- Change vs 04:00 run: no material delta in top headlines.

## Signals (scored)

### 1) AI Infra — Oracle/OpenAI data-center expansion adjustment narrative
- 類別：AI Infra
- 熱度分：73/100
- 等級：L2
- 來源：Bloomberg、The Information、CNBC（皆由 Google News RSS 擷取）
- 命中關鍵字：Oracle, OpenAI, data center, Stargate, expansion, debt
- 摘要（2-3 句）：多來源延續報導 Oracle 與 OpenAI 的大型資料中心擴張計畫調整，並同步出現對 Oracle backlog/資本結構的質疑報導。主題集中且跨媒體一致。
- 判讀（1-2 句）：屬 AI 基建投資節奏的重要 L2 訊號，但仍未達 L1，關鍵缺口是官方公告與即時社群高權重來源驗證。
- 反向驗證（反證/待確認項）：待 Oracle/OpenAI 官方澄清、IR 文件、法說或 SEC 相關披露。
- 建議動作（Follow-up）：維持 48h 追蹤；一旦出現官方確認（延期/縮減/capex 指引變化）可升級。
- 評分拆解：帳號權重 23 / 關鍵字 22 / 熱度速度 13 / 跨來源確認 13 / 去雜訊 -(-2) => 73

### 2) Macro/Oil — geopolitical spike but confirmation weak
- 類別：Macro / Oil
- 熱度分：57/100
- 等級：L3
- 來源：FXStreet、Investing.com（RSS）
- 命中關鍵字：WTI, Middle East tension, CPI, inventories
- 摘要（2-3 句）：油價受地緣事件催化波動，但市場仍等待 CPI/EIA 關鍵數據落地。當前屬事件驅動的短波動，不足以定義趨勢。
- 判讀（1-2 句）：未取得一線媒體與官方數據交叉確認，暫列 L3。
- 反向驗證（反證/待確認項）：待 EIA 庫存與 CPI 後重評。
- 建議動作（Follow-up）：數據發布後更新熱度速度與跨源分。
- 評分拆解：帳號權重 12 / 關鍵字 18 / 熱度速度 10 / 跨來源確認 7 / 去雜訊 -(-10) => 57

### 3) Crypto Flow — exchange outflow narrative remains noisy
- 類別：Crypto Flow
- 熱度分：45/100
- 等級：L3
- 來源：MEXC、Live Bitcoin News、TradingView repost（RSS）
- 命中關鍵字：BTC outflow, exchange reserves, stablecoin outflows
- 摘要（2-3 句）：訊號仍集中在「交易所 BTC 流出/供給收縮」敘事，但來源可信度參差，且不少屬二次轉述。
- 判讀（1-2 句）：可做觀察，不足以形成可執行高等級決策。
- 反向驗證（反證/待確認項）：需補 ETF flow（發行商/彭博終端）、鏈上權威資料、主流媒體同步報導。
- 建議動作（Follow-up）：補數據後再做升降級。
- 評分拆解：帳號權重 8 / 關鍵字 19 / 熱度速度 8 / 跨來源確認 6 / 去雜訊 -(-4) => 45

### 4) Taiwan Semi — no fresh multi-source catalyst
- 類別：Taiwan Semi
- 熱度分：27/100
- 等級：L3
- 來源：DigiTimes + mostly stale items（RSS）
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor
- 摘要（2-3 句）：本輪沒有新鮮且可交叉驗證的重大催化，結果以舊聞為主。
- 判讀（1-2 句）：資料可得性低，暫無可執行訊號。
- 反向驗證（反證/待確認項）：需補公司公告/法說與台媒即時訊。
- 建議動作（Follow-up）：下輪提升 query 精度（CoWoS/先進封裝/法說關鍵詞）。
- 評分拆解：帳號權重 8 / 關鍵字 10 / 熱度速度 4 / 跨來源確認 2 / 去雜訊 -(-3) => 27

### 5) Chinese Signal — stale feed dominated, no valid fresh pulse
- 類別：Chinese Signal
- 熱度分：24/100
- 等級：L3
- 來源：Reuters/Bloomberg old items + archived links（RSS）
- 命中關鍵字：PBOC, stimulus, loans, yuan, property
- 摘要（2-3 句）：清單仍由歷史新聞主導，未見今日可驗證政策脈衝。
- 判讀（1-2 句）：不應把「沒抓到新訊」誤判為「風險解除」。
- 反向驗證（反證/待確認項）：需補央行公告與官媒/即時通訊社流。
- 建議動作（Follow-up）：改用更窄時窗與官源白名單。
- 評分拆解：帳號權重 6 / 關鍵字 9 / 熱度速度 3 / 跨來源確認 2 / 去雜訊 -(-4) => 24

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪 **無 L1 訊號**（不觸發即時警報）。
- 最高優先維持：AI Infra（Oracle/OpenAI data center expansion）L2，繼續 48h 追蹤。

## Data Gaps
- Missing `PERPLEXITY_API_KEY` for web_search.
- Missing X/關鍵帳號即時流與互動增速。

## Manual Fix
- Gateway 設定 `PERPLEXITY_API_KEY` 或 `tools.web.search.perplexity.apiKey` 後重跑，可提升跨源確認與速度分可信度。
