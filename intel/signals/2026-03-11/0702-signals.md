# Signal Engine Scan — 2026-03-11 07:02 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 07:02 Asia/Taipei
- Coverage requested: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS (when:1d)
- Data gap:
  1) `web_search` still unavailable (missing Perplexity API key)
  2) No X stream / key-account velocity signals
  3) Taiwan Semi & Chinese Signal query returned near-empty fresh results this round

---

## Top Signals

### 1) AI Infra — Oracle/OpenAI DC expansion narrative still dominant
- 類別：AI Infra
- 熱度分：68/100
- 等級：L2
- 來源：Insurance Journal (pick-up of Bloomberg line), TechRepublic, PYMNTS, Mint, Stocktwits/24-7 WallSt repost stream
- 命中關鍵字：Oracle, OpenAI, data center, expansion, Nvidia, AMD, antitrust, backlog
- 摘要（2-3 句）：AI Infra 討論依然集中在 Oracle 與 OpenAI 擴張計畫變動，以及 Nvidia 在供應鏈談判權力的爭議敘事。內容有延續性，但來源品質兩極（部分高可信原始線索被大量二次轉述包圍）。
- 判讀（1-2 句）：屬於「中高關注但尚未升級」訊號；市場敘事有擴散，但可驗證的新事實增量有限。
- 反向驗證（反證/待確認項）：缺官方公告/IR 檔；需確認是否只是同一則原始新聞的多站轉載。
- 建議動作（Follow-up）：追蹤 Oracle/OpenAI 官方聲明與財報電話會議文字稿，若出現 capex 指引變化才考慮升級。
- 評分拆解：帳號權重 18 / 關鍵字 22 / 熱度速度 13 / 跨來源確認 10 / 去雜訊 -(-5) => 68

### 2) Crypto Flow — ETF flow headlines improve, but source quality uneven
- 類別：Crypto Flow
- 熱度分：61/100
- 等級：L2
- 來源：FinanceFeeds, TradingView repost ecosystem, MEXC/blog 類來源
- 命中關鍵字：Bitcoin ETF inflow, outflow streak, Ethereum outflows, funding rate
- 摘要（2-3 句）：本輪出現「美國比特幣 ETF 轉正流入」相關新鮮標題，且與前期 outflow 敘事形成反轉。另有 ETH funding rate 轉負與 ETF 出流並行，顯示資金在 BTC/ETH 間結構分化。
- 判讀（1-2 句）：可作為交易層面的二級訊號，但來源仍混雜，需要 ETF 發行商與主流數據平台核實。
- 反向驗證（反證/待確認項）：尚缺 Bloomberg/Reuters 或發行商官方流量表；部分數字可能來自未審核二手來源。
- 建議動作（Follow-up）：下一輪補抓 BlackRock/Fidelity/Bitwise 公開流量與鏈上供給變化，重算級別。
- 評分拆解：帳號權重 13 / 關鍵字 21 / 熱度速度 14 / 跨來源確認 9 / 去雜訊 -(-4) => 61

### 3) Macro / Oil — event watch only (pre-data)
- 類別：Macro / Oil
- 熱度分：41/100
- 等級：L3
- 來源：Investing.com Australia
- 命中關鍵字：CPI, oil inventories
- 摘要（2-3 句）：宏觀油價相關結果僅見「數據將公布」型前瞻內容，缺乏新政策或新供需衝擊事件。屬於等待數據落地前的低可交易性訊號。
- 判讀（1-2 句）：暫不形成高優先級情報，待數據公布後再重評。
- 反向驗證（反證/待確認項）：缺 EIA/OPEC/主流媒體當日實際數據報導。
- 建議動作（Follow-up）：CPI 與 EIA 公布後立即重跑。
- 評分拆解：帳號權重 8 / 關鍵字 15 / 熱度速度 6 / 跨來源確認 4 / 去雜訊 -(-8) => 41

### 4) Taiwan Semi — no qualified fresh signal
- 類別：Taiwan Semi
- 熱度分：12/100
- 等級：L3
- 來源：本輪 RSS 無有效新鮮條目
- 命中關鍵字：TSMC, UMC（未形成新事件）
- 摘要（2-3 句）：此輪未抓到可用的新鮮半導體台灣鏈重大事件。
- 判讀（1-2 句）：資料不足，不代表風險消失。
- 反向驗證（反證/待確認項）：需補本地財經媒體、公司公告、法說會來源。
- 建議動作（Follow-up）：改查中英雙語 query（台積電/聯電/CoWoS/先進封裝）。

### 5) Chinese Signal — no qualified fresh signal
- 類別：Chinese Signal
- 熱度分：10/100
- 等級：L3
- 來源：本輪 RSS 無有效新鮮條目
- 命中關鍵字：PBOC, stimulus, yuan（未形成新事件）
- 摘要（2-3 句）：本輪未見當日可交叉確認的中國政策新脈衝。
- 判讀（1-2 句）：屬資料可得性偏低狀態。
- 反向驗證（反證/待確認項）：需補人民銀行公告與 Reuters 即時稿。
- 建議動作（Follow-up）：下輪聚焦「PBOC + MLF/RRR + property support」精準檢索。

---

## Level Summary
- L1：0
- L2：2
- L3：3

## Decision
- 本輪 **無 L1 訊號**（未達 80 分且跨來源確認門檻不足）。
- 需重點追蹤：AI Infra（Oracle/OpenAI）與 Crypto Flow（ETF 流向反轉）。

## Data Gaps & Recovery
- Missing: `PERPLEXITY_API_KEY` → `web_search` unavailable
- Missing: X 關鍵帳號流與互動增速
- Manual recovery:
  1) 在 Gateway 設定 `PERPLEXITY_API_KEY`
  2) 下一輪加入 X 官方/記者名單監控
  3) 補 ETF 發行商官方流量來源做交叉驗證
