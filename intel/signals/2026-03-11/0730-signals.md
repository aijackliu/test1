# Signal Engine Scan — 2026-03-11 07:30 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 07:30 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS (`when:1d`) headline scan
- Data gap:
  - `web_search` unavailable (missing Perplexity API key)
  - X / key-account feed not available in this run
  - Taiwan Semi / Chinese Signal returned no fresh items in current query window
- Quality note: this round has weaker source quality than desired (many repost/secondary outlets), so scores are conservatively downgraded.

## Signals

### 1) AI Infra — Oracle/OpenAI datacenter plan friction remains dominant narrative
- 類別：AI Infra
- 熱度分：68/100
- 等級：L2
- 來源：Insurance Journal (reprint of Bloomberg line), TechRepublic, multiple secondary repost outlets via Google News RSS
- 命中關鍵字：Oracle, OpenAI, data center, expansion, AI infrastructure, backlog
- 摘要（2-3 句）：本時段延續「Oracle 與 OpenAI 擴張節奏調整」主線，並出現更多衍生討論（Nvidia/AMD 競爭、融資壓力、backlog 可持續性）。討論熱度高，但來源品質分散且二次轉載比例上升。
- 判讀（1-2 句）：主題仍具市場影響力，尤其對 AI capex 與供應鏈估值敘事；但缺乏新增一手披露，暫維持 L2。
- 反向驗證（反證/待確認項）：等待 Oracle/OpenAI 官方聲明、法說逐字、SEC/IR 文件；目前多為媒體敘事延伸。
- 建議動作（Follow-up）：持續 48h 追蹤，若出現官方 guidance 調整或專案時程確認，再評估升級。
- 評分拆解：帳號權重 18 / 關鍵字 22 / 熱度速度 15 / 跨來源確認 11 / 去雜訊 -(-2) => 68

### 2) Crypto Flow — ETF flow headline turns mixed, but source credibility uneven
- 類別：Crypto Flow
- 熱度分：54/100
- 等級：L3
- 來源：FinanceFeeds, TradingView repost, Dimsum Daily, MEXC/blog-style outlets
- 命中關鍵字：Bitcoin ETF inflow, outflow streak, exchange flow, funding rate
- 摘要（2-3 句）：本輪可見「BTC ETF 回流」與「ETH 壓力」並存的混合訊號，但多數條目來自二線財經站或交易導向內容平台。缺乏主流媒體與官方基金發行端同步確認。
- 判讀（1-2 句）：可視為短線情緒修復訊號，但證據鏈不完整，不足以升到 L2。
- 反向驗證（反證/待確認項）：需補 BlackRock/Fidelity 流量統計、彭博終端口徑與鏈上資料供應商交叉。
- 建議動作（Follow-up）：下一輪優先補 ETF 發行商與主流流量數據，再重算。
- 評分拆解：帳號權重 10 / 關鍵字 18 / 熱度速度 12 / 跨來源確認 8 / 去雜訊 -(-6) => 54

### 3) Macro/Oil — Awaiting scheduled data; no confirmed regime shift
- 類別：Macro / Oil
- 熱度分：42/100
- 等級：L3
- 來源：Investing.com regional feed
- 命中關鍵字：CPI, oil inventories, Wednesday data
- 摘要（2-3 句）：目前宏觀與油市主軸仍在等待 CPI 與油庫存數據釋出，市場屬「事件前觀望」。未出現多來源一致的新政策或供需衝擊信號。
- 判讀（1-2 句）：暫不構成交易級別高信號，屬前瞻提示而非已確認趨勢。
- 反向驗證（反證/待確認項）：待數據落地後檢查油價與美元/利率反應是否同向確認。
- 建議動作（Follow-up）：數據公布後立即重跑評分。
- 評分拆解：帳號權重 8 / 關鍵字 14 / 熱度速度 8 / 跨來源確認 4 / 去雜訊 -(-8) => 42

### 4) Taiwan Semi — no valid fresh signal in current window
- 類別：Taiwan Semi
- 熱度分：20/100
- 等級：L3
- 來源：本輪 query 無新項目（NO_ITEMS）
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor
- 摘要（2-3 句）：目前查詢窗口未返回可評分的新鮮條目。屬資料缺口，不代表基本面無變化。
- 判讀（1-2 句）：保持觀察，避免空白期誤判。
- 反向驗證（反證/待確認項）：下輪需改查台灣本地媒體與公司公告源。
- 建議動作（Follow-up）：改用 Focus Taiwan/工商/經濟日報關鍵詞與英文雙語查詢。
- 評分拆解：帳號權重 4 / 關鍵字 8 / 熱度速度 2 / 跨來源確認 0 / 去雜訊 -(-6) => 20

### 5) Chinese Signal — no valid fresh signal in current window
- 類別：Chinese Signal
- 熱度分：18/100
- 等級：L3
- 來源：本輪 query 無新項目（NO_ITEMS）
- 命中關鍵字：PBOC, stimulus, yuan, property
- 摘要（2-3 句）：本輪未抓到當日中國政策／信用脈衝的新鮮資訊。可得性不足，暫不下結論。
- 判讀（1-2 句）：目前無法支持任何升級信號。
- 反向驗證（反證/待確認項）：需補官媒、央行公告、Reuters/Bloomberg 即時流。
- 建議動作（Follow-up）：下輪收斂查詢到「PBOC announcement」「RMB fixing」「property easing measures」。
- 評分拆解：帳號權重 3 / 關鍵字 8 / 熱度速度 1 / 跨來源確認 0 / 去雜訊 -(-6) => 18

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪 **無 L1 訊號**（未達 ≥80 且跨來源確認 ≥8 的高可信條件）。
- 最高優先仍為 **AI Infra（Oracle/OpenAI expansion friction）L2**，持續 48h 追蹤。

## Data Gaps & Recovery
- Missing: `PERPLEXITY_API_KEY` for `web_search`
- Missing: X / key account interaction velocity
- Recovery: configure Gateway `PERPLEXITY_API_KEY` and add X feed ingestion for stronger confidence scoring.
