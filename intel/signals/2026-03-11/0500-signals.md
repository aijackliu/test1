# Signal Engine Scan — 2026-03-11 05:00 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 05:00 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS (last ~24h focus)
- Data gap:
  1) `web_search` unavailable (missing Perplexity API key)
  2) X / key-account stream unavailable in this run
  3) Taiwan Semi / Chinese Signal had no fresh items returned in this scan window

## Signals

### 1) AI Infra — Oracle/OpenAI DC expansion reset remains dominant
- 類別：AI Infra
- 熱度分：68/100
- 等級：L2
- 來源：Insurance Journal reprint of Reuters/Bloomberg thread (headline), TechRepublic, PYMNTS, Mint
- 命中關鍵字：Oracle, OpenAI, data center, expansion, Nvidia, AMD, antitrust
- 摘要（2-3 句）：AI infra 話題持續集中在 Oracle 與 OpenAI 資料中心擴張調整，以及 Nvidia/AMD 在關鍵交易中的競爭爭議。這輪新增來源多為二級媒體與轉述，核心敘事未見根本反轉。
- 判讀（1-2 句）：主題仍具市場影響力，但一線來源密度較上一輪弱，信號維持 L2。
- 反向驗證（反證/待確認項）：需官方 IR、財報電話會或監管文件證實項目節奏與競爭指控；目前多為外部報導與評論。
- 建議動作（Follow-up）：持續 48h 追蹤；若出現 Oracle/OpenAI 官方定調或監管調查落地，重新評級。
- 評分拆解：帳號權重 18 / 關鍵字 22 / 熱度速度 13 / 跨來源確認 11 / 去雜訊 -(-4) => 68

### 2) Crypto Flow — ETF flow turned positive, but source quality mixed
- 類別：Crypto Flow
- 熱度分：57/100
- 等級：L3
- 來源：FinanceFeeds, CryptoRank, MEXC, Dimsum Daily
- 命中關鍵字：Bitcoin ETF inflows, outflow streak, Ethereum outflows, oil shock
- 摘要（2-3 句）：出現「美國 BTC ETF 淨流入回正」的敘事，同時伴隨地緣風險與 ETH 資金流出相關報導。訊號方向有可追蹤價值，但來源以非頂級財經媒體為主。
- 判讀（1-2 句）：尚不足以作為高置信度資金流拐點，暫列 L3 觀察。
- 反向驗證（反證/待確認項）：需 ETF 發行商官方日流量表、彭博/路透或鏈上主流資料商交叉驗證。
- 建議動作（Follow-up）：下輪補官方 ETF flow 與主要交易所儲備變化後重算。
- 評分拆解：帳號權重 10 / 關鍵字 20 / 熱度速度 12 / 跨來源確認 8 / 去雜訊 -(-7) => 57

### 3) Macro / Oil — calendar-driven watch, not confirmed trend
- 類別：Macro / Oil
- 熱度分：42/100
- 等級：L3
- 來源：Investing.com Nigeria
- 命中關鍵字：CPI, oil inventories
- 摘要（2-3 句）：本輪宏觀油市只抓到「數據日曆預告」型內容，缺乏多來源即時事件更新。暫無可確認的新政策或供需突變。
- 判讀（1-2 句）：偏事件前觀望，不構成可交易級別新訊號。
- 反向驗證（反證/待確認項）：待 CPI 與 EIA 數據正式公布及主流媒體解讀。
- 建議動作（Follow-up）：數據公布後再掃描與評分。
- 評分拆解：帳號權重 8 / 關鍵字 14 / 熱度速度 6 / 跨來源確認 3 / 去雜訊 -(-11) => 42

### 4) Taiwan Semi — no fresh signal returned
- 類別：Taiwan Semi
- 熱度分：12/100
- 等級：L3
- 來源：本輪 RSS 無新項目
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor（查詢詞）
- 摘要（2-3 句）：當前掃描窗口未回傳新鮮台灣半導體相關新聞項。
- 判讀（1-2 句）：資料不足，非市場無事。
- 反向驗證（反證/待確認項）：需改查 Focus Taiwan、工商/經濟、公司公告與法說素材。
- 建議動作（Follow-up）：下輪改用來源定向查詢。

### 5) Chinese Signal — no fresh signal returned
- 類別：Chinese Signal
- 熱度分：10/100
- 等級：L3
- 來源：本輪 RSS 無新項目
- 命中關鍵字：PBOC, stimulus, yuan, property（查詢詞）
- 摘要（2-3 句）：本輪查詢未抓到新的中國政策訊號條目。
- 判讀（1-2 句）：資料可得性不足，暫不判斷政策轉向。
- 反向驗證（反證/待確認項）：需補官媒、央行公告與 Reuters 即時流。
- 建議動作（Follow-up）：下輪改 narrow query + source allowlist。

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪無 L1，**不觸發即時警報**。
- 最高優先追蹤維持：AI Infra（Oracle/OpenAI 資料中心擴張敘事）。

## Data Gaps & Fix
- `web_search` 無法使用：缺 `PERPLEXITY_API_KEY`
- 缺 X/關鍵帳號互動增速資料
- 修復方式：於 Gateway 設定 `PERPLEXITY_API_KEY` 或 `tools.web.search.perplexity.apiKey`，再執行下一輪以提升交叉確認品質。
