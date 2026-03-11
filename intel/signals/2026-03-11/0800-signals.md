# Signal Engine Scan — 2026-03-11 08:00 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 08:00 Asia/Taipei
- Coverage target: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS（近 24h）
- Data gap:
  - `web_search` 仍不可用（缺 `PERPLEXITY_API_KEY`）
  - 未納入 X 即時流與互動增速（velocity）
  - Taiwan Semi / Chinese Signal 在本輪近 24h RSS 幾乎無有效新條目

## Top Signals

### 1) AI Infra — Oracle / OpenAI 資料中心擴張調整（延續）
- 類別：AI Infra
- 熱度分：69/100
- 等級：L2
- 來源：Insurance Journal 轉載 Bloomberg、CNBC 轉載鏈、其他二級媒體（Google News RSS 聚合）
- 命中關鍵字：Oracle, OpenAI, data center, expansion, Nvidia, backlog
- 摘要（2-3 句）：本輪仍以「Oracle 與 OpenAI 擴張調整」為主軸，並外溢到 Nvidia/AMD 競爭敘事。雖然話題持續熱，但新增來源品質偏混雜，可信度分佈不均。
- 判讀（1-2 句）：屬於「高討論、未完全定錨」的 L2；對 AI 基建資本開支敘事仍有壓力。
- 反向驗證（反證/待確認項）：缺官方公告與一手財報/IR 更新；大量二次轉載可能放大同一事件。
- 建議動作（Follow-up）：追官方聲明與主流一線媒體原文；若出現正式 capex 或時程調整再評估升級。
- 評分拆解：帳號權重 20 / 關鍵字 22 / 熱度速度 13 / 跨來源確認 10 / 去雜訊 -(-4) => 69

### 2) Crypto Flow — ETF 流向轉正 vs altcoin 資金分化
- 類別：Crypto Flow
- 熱度分：57/100
- 等級：L3
- 來源：FinanceFeeds、TradingView 二級內容、MEXC/區塊鏈媒體（Google News RSS）
- 命中關鍵字：Bitcoin ETF inflows, outflow streak, Ethereum outflows, funding rate
- 摘要（2-3 句）：可見「BTC ETF 淨流回正」與「ETH/alt 資金面偏弱」的分化訊號，但來源多為二級媒體與交易平台內容。尚未形成高可信、多源獨立驗證。
- 判讀（1-2 句）：方向可追蹤，但目前訊號強度不足，維持 L3。
- 反向驗證（反證/待確認項）：需補 ETF 發行商官方流量資料與一線媒體交叉確認。
- 建議動作（Follow-up）：下一輪補抓官方 ETF 日流量、主要交易所儲備與 stablecoin mint/burn。
- 評分拆解：帳號權重 11 / 關鍵字 18 / 熱度速度 11 / 跨來源確認 7 / 去雜訊 -(-10) => 57

### 3) Macro / Oil — 靜待 CPI + 庫存，事件不足
- 類別：Macro / Oil
- 熱度分：41/100
- 等級：L3
- 來源：Investing.com 區域版（Google News RSS）
- 命中關鍵字：CPI, oil inventories
- 摘要（2-3 句）：本輪僅抓到行事曆型事件提醒，缺乏新增實質催化（如 EIA 意外值、OPEC 政策新表述）。
- 判讀（1-2 句）：屬低資訊密度，暫不形成可交易級訊號。
- 反向驗證（反證/待確認項）：等待實際數據公布後再重新評分。
- 建議動作（Follow-up）：CPI/EIA 落地後即時重跑。
- 評分拆解：帳號權重 10 / 關鍵字 14 / 熱度速度 6 / 跨來源確認 3 / 去雜訊 -(-8) => 41

### 4) Taiwan Semi — 資料不足
- 類別：Taiwan Semi
- 熱度分：18/100
- 等級：L3
- 來源：本輪近 24h RSS 無有效新鮮高可信條目
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor
- 摘要（2-3 句）：無可用新訊。
- 判讀（1-2 句）：資料可得性不足，不代表基本面無變化。
- 反向驗證（反證/待確認項）：需補台媒財經線、公司公告、法說與供應鏈來源。
- 建議動作（Follow-up）：下輪改精準 query（CoWoS/先進封裝/法說）並擴充來源。

### 5) Chinese Signal — 資料不足
- 類別：Chinese Signal
- 熱度分：16/100
- 等級：L3
- 來源：本輪近 24h RSS 無有效新鮮高可信條目
- 命中關鍵字：PBOC, stimulus, yuan, property
- 摘要（2-3 句）：未抓到當日新政策脈衝。
- 判讀（1-2 句）：暫無有效新訊。
- 反向驗證（反證/待確認項）：需補 PBOC 官網、官媒與 Reuters 即時流。
- 建議動作（Follow-up）：下一輪改窄詞並加入官源。

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪 **無 L1 訊號**，不觸發即時警報。
- 當前最高優先追蹤：AI Infra（Oracle/OpenAI 擴張調整）

## Data Gaps & Manual Recovery
- 缺口：`PERPLEXITY_API_KEY` 導致 `web_search` 無法用，降低來源品質與交叉確認能力。
- 補件方式：在 Gateway 設定 `PERPLEXITY_API_KEY` 或 `tools.web.search.perplexity.apiKey`，再重跑可提升 L1 檢出可靠度。
