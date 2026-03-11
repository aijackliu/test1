# Signal Engine Scan — 2026-03-11 06:00 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 06:00 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS headline scan
- Data gap: `web_search` still unavailable (missing Perplexity API key), therefore X 即時流與互動增速資料仍缺。
- Quality note: stale/low-trust items were downweighted.

## Signals

### 1) AI Infra — Oracle/OpenAI data center expansion pullback narrative
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Bloomberg, The Information, CNBC（皆透過 Google News RSS）
- 命中關鍵字：Oracle, OpenAI, data center, expansion, Stargate, debt
- 摘要（2-3 句）：多來源持續聚焦 Oracle 與 OpenAI 資料中心擴張節奏調整；同時有市場質疑 Oracle 在高資本支出下的財務可持續性。訊號方向與 04:00 掃描一致，屬延續而非新突發。
- 判讀（1-2 句）：AI infra capex 敘事轉弱風險仍在，但尚未達到 L1 所需的「高分 + 高交叉確認 + 更高可信即時源」。
- 反向驗證：缺正式公司公告/法說明確落地；缺 X 官方高權重帳號即時補證。
- 建議動作：持續 48h 追蹤 Oracle/OpenAI/主要 sell-side 更新。
- 評分拆解：帳號權重 24 / 關鍵字 22 / 熱度速度 12 / 跨來源確認 13 / 去雜訊 -(-3) => 74

### 2) Macro/Oil — event-driven volatility before CPI/inventory prints
- 類別：Macro / Oil
- 熱度分：56/100
- 等級：L3
- 來源：Investing.com, FXStreet（via Google News RSS）
- 命中關鍵字：WTI, CPI, oil inventories, Middle East tensions
- 摘要：油價 headline 波動仍與地緣消息連動，但市場真正定價拐點仍待 CPI 與庫存數據。缺一線媒體與官方統計交叉確證。
- 判讀：短線風險存在，尚不足升級。
- 反向驗證：待 EIA/CPI 正式數據。
- 建議動作：數據公布後重算。
- 評分拆解：帳號權重 11 / 關鍵字 18 / 熱度速度 10 / 跨來源確認 7 / 去雜訊 -(-10) => 56

### 3) Crypto Flow — BTC exchange outflow narrative remains noisy
- 類別：Crypto Flow
- 熱度分：45/100
- 等級：L3
- 來源：CryptoRank, MEXC, Live Bitcoin News（via Google News RSS）
- 命中關鍵字：Bitcoin, outflow, exchange supply, stablecoin
- 摘要：敘事延續但來源權重偏低，缺 ETF 發行商與主流鏈上數據供應商交叉確認。
- 判讀：可監控，暫不升級。
- 反向驗證：待補 ETF 淨流與鏈上資料。
- 建議動作：下輪補數據源再評分。
- 評分拆解：帳號權重 8 / 關鍵字 18 / 熱度速度 9 / 跨來源確認 6 / 去雜訊 -(-4) => 45

### 4) Taiwan Semi — no fresh actionable signal
- 類別：Taiwan Semi
- 熱度分：26/100
- 等級：L3
- 來源：DigiTimes update page + mostly stale items（via Google News RSS）
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor
- 摘要：無新鮮跨源確認的重大事件；多為舊聞或泛更新。
- 判讀：空窗期，維持低等級。
- 反向驗證：待公司公告/法說/主流台媒即時訊號。
- 建議動作：改窄關鍵詞後再掃描。
- 評分拆解：帳號權重 7 / 關鍵字 10 / 熱度速度 4 / 跨來源確認 2 / 去雜訊 -(-3) => 26

### 5) Chinese Signal — stale flow, no fresh policy pulse
- 類別：Chinese Signal
- 熱度分：23/100
- 等級：L3
- 來源：Reuters/Bloomberg older items + stale repost mix（via Google News RSS）
- 命中關鍵字：PBOC, stimulus, loans, yuan, property
- 摘要：結果仍以歷史新聞為主，未見當日可驗證政策新訊號。
- 判讀：資料可得性不足，不等於風險消失。
- 反向驗證：待 PBOC/官媒/即時 wire。
- 建議動作：下輪以官網/官媒為主源補抓。
- 評分拆解：帳號權重 6 / 關鍵字 9 / 熱度速度 3 / 跨來源確認 2 / 去雜訊 -(-3) => 23

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪 **無 L1 訊號**（不觸發即時警報）。
- 最高優先仍為 AI Infra 的 Oracle/OpenAI capex 敘事演化。

## Data Gap
- Missing: Perplexity key (`PERPLEXITY_API_KEY`) so `web_search` unavailable.
- Missing: X sources + interaction velocity.
