# Signal Engine Scan — 2026-03-11 05:45 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 05:45 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS headline scan
- Data gap:
  - `web_search` unavailable (missing `PERPLEXITY_API_KEY`),無法補齊更高可信來源聚合。
  - 缺 X 流與互動增速資料，熱度速度僅能以新聞時間密度近似。

## Top Signals

### 1) AI Infra — Oracle / OpenAI 擴建敘事持續發酵
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Bloomberg、The Information、CNBC（Google News RSS 聚合）
- 命中關鍵字：Oracle, OpenAI, data center, expansion, Stargate, backlog, debt
- 摘要（2-3 句）：Oracle 與 OpenAI 的資料中心擴建調整議題延續，並出現更多二次市場評論（包含 backlog 品質與資本結構壓力）。主軸仍是 AI 基礎設施 capex 敘事是否降速。
- 判讀（1-2 句）：跨來源一致性仍高，但多為媒體報導/評論，尚未見官方新公告；維持 L2。
- 反向驗證（反證/待確認項）：缺 Oracle/OpenAI 官方 IR 更新、正式 capex guidance 調整與監管文件佐證。
- 建議動作（Follow-up）：持續 48h 追蹤官方聲明、財報電話會議摘錄、sell-side note；若出現「正式延期/縮減」可升級。
- 評分拆解：帳號權重 23 / 關鍵字 22 / 熱度速度 13 / 跨來源確認 13 / 去雜訊 -(-3) => 74

### 2) Macro / Oil — 事件驅動波動，等待數據驗證
- 類別：Macro / Oil
- 熱度分：55/100
- 等級：L3
- 來源：Investing.com（區域站）、FXStreet（Google News RSS 聚合）
- 命中關鍵字：WTI, Middle East tensions, CPI, oil inventories
- 摘要（2-3 句）：油價受地緣事件擾動，但市場真正定價錨點仍在 CPI 與庫存數據。當前資訊偏 headline，尚未形成趨勢共識。
- 判讀（1-2 句）：屬短線波動訊號，可信度與可持續性未達 L2。
- 反向驗證（反證/待確認項）：缺 Reuters/Bloomberg 等高權重源即時確認與 OPEC/EIA 新政策層訊號。
- 建議動作（Follow-up）：待 CPI + EIA 後重算分數，確認是否出現方向性突破。
- 評分拆解：帳號權重 11 / 關鍵字 18 / 熱度速度 10 / 跨來源確認 7 / 去雜訊 -(-9) => 55

### 3) Crypto Flow — 仍以中低可信來源為主
- 類別：Crypto Flow
- 熱度分：45/100
- 等級：L3
- 來源：CryptoRank、MEXC、Live Bitcoin News、TradingView 二次稿（Google News RSS 聚合）
- 命中關鍵字：Bitcoin, exchange outflow, liquidity tightening, stablecoin outflows
- 摘要（2-3 句）：市場持續討論 BTC 交易所流出與流動性收緊，但多為二手詮釋與平台內容，來源層級偏弱。可作觀察，不足以形成高信號。
- 判讀（1-2 句）：噪音比訊號高，維持 L3。
- 反向驗證（反證/待確認項）：缺 ETF 淨流（發行商/彭博端）、鏈上主流數據供應商一致驗證。
- 建議動作（Follow-up）：下輪補 ETF flow + stablecoin mint/burn + exchange reserve 三件套再評分。
- 評分拆解：帳號權重 8 / 關鍵字 19 / 熱度速度 8 / 跨來源確認 6 / 去雜訊 -(-4) => 45

### 4) Taiwan Semi — 新鮮訊號不足
- 類別：Taiwan Semi
- 熱度分：22/100
- 等級：L3
- 來源：DigiTimes update 頁為主（其餘多舊聞）
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor
- 摘要（2-3 句）：本輪仍未出現多來源、當日新鮮且可驗證的台灣半導體催化事件。有效訊號稀薄。
- 判讀（1-2 句）：維持觀望，不做方向判斷。
- 反向驗證（反證/待確認項）：需補公司公告、法說、台灣本地財經媒體與供應鏈報導。
- 建議動作（Follow-up）：改用 CoWoS / 先進封裝 / 產能利用率 / 匯率衝擊等窄詞重抓。
- 評分拆解：帳號權重 7 / 關鍵字 8 / 熱度速度 3 / 跨來源確認 2 / 去雜訊 -(-2) => 22

### 5) Chinese Signal — 以歷史舊聞為主，無新脈衝
- 類別：Chinese Signal
- 熱度分：20/100
- 等級：L3
- 來源：Reuters/Bloomberg 舊聞與其他歷史條目（Google News RSS 聚合）
- 命中關鍵字：PBOC, stimulus, loans, yuan, property
- 摘要（2-3 句）：搜尋結果幾乎都是過往月份資料，未見當前時點新政策脈衝。資料新鮮度不足。
- 判讀（1-2 句）：目前「無可判讀新訊號」，不是市場無事，而是資料可得性偏低。
- 反向驗證（反證/待確認項）：需補 PBOC 官網、官媒、Reuters 即時流與 CNH/國債市場反應。
- 建議動作（Follow-up）：下輪切換更精準 query（近 24h + policy action 詞）並加入官方來源。
- 評分拆解：帳號權重 6 / 關鍵字 8 / 熱度速度 2 / 跨來源確認 2 / 去雜訊 -(-2) => 20

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪 **無 L1 訊號**，不觸發即時警報。
- 目前最高優先追蹤仍為：**AI Infra（Oracle / OpenAI data center 擴建敘事）**。

## Data Gaps & Recovery
- 缺失：Perplexity API key（`web_search` 不可用）
- 缺失：X 即時流與互動增速數據
- 補件方式：設定 `PERPLEXITY_API_KEY`（或 `tools.web.search.perplexity.apiKey`）後重跑，並加入 X 來源做速度分修正。
