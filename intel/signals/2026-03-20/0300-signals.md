# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 03:00
- Engine: v1（100-point scoring）
- Data sources checked: Google News RSS（聚合 Reuters/CNBC/Microsoft/NVIDIA/產業媒體）
- Constraints: `web_search` 仍不可用（缺 Brave API key）；X/關鍵帳號互動速度資料缺失，熱度速度以「近期跨媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Microsoft 官方部落格、NVIDIA Newsroom、Google News RSS（2026-03-20 03:00 抓取）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：Microsoft 與 NVIDIA 在 GTC 同步發布 AI 基建/Physical AI 方案，來源為官方一手，可信度高。訊號屬「敘事強、落地數據待補」，目前仍偏中高強度主題延續。
- 判讀（1-2 句）：AI 基建循環延續訊號維持，但尚不足以升至 L1。
- 反向驗證（反證/待確認項）：缺第三方量化（雲端新增營收、GPU 實際交付節奏）。
- 建議動作（Follow-up）：48h 追蹤 Reuters/Bloomberg 是否出現採購金額、交付時程、CapEx 拆解。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 11 + 跨來源 9 - 去雜訊 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 增產預期由 Reuters 與 CNBC 交叉覆蓋，供給端訊號一致。事件仍偏政策預期，不是供需突發衝擊。
- 判讀（1-2 句）：對油價與通膨預期為中度影響，暫維持 L2。
- 反向驗證（反證/待確認項）：待正式會議結果與實際執行率；地緣風險可能反向抬升油價。
- 建議動作（Follow-up）：跟蹤 OPEC+ 正式公告與 EIA 庫存資料。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：64/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：Reuters 持續關注中國科技與政策方向，訊號偏中期結構性。對半導體供應鏈與地緣風險定價有影響，但短期可交易性有限。
- 判讀（1-2 句）：方向訊號有效，但缺政策細則，先維持 L2。
- 反向驗證（反證/待確認項）：缺部委公告、財政配套與補貼條件等硬資訊。
- 建議動作（Follow-up）：補中國官方公告源（發改委/工信部/國務院）後再重評。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 9 + 跨來源 8 - 去雜訊 5 = 64

## Signal 4
- 類別：Taiwan Semi
- 熱度分：56/100
- 等級：L3
- 來源：Seeking Alpha、Tom’s Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能瓶頸與擴產敘事延續，但以評論/產業媒體為主，缺公司最新一手公告。屬已知主題，非新拐點。
- 判讀（1-2 句）：保持灰燈觀察，等待法說或官方指引再升級。
- 反向驗證（反證/待確認項）：缺最新季度法說數字與客戶訂單能見度。
- 建議動作（Follow-up）：鎖定 TSMC IR 與主流通訊社快訊。
- 評分拆解：帳號權重 15 + 關鍵字 20 + 熱度速度 8 + 跨來源 7 - 去雜訊 6 = 44

## Signal 5
- 類別：Crypto Flow
- 熱度分：49/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓取結果以舊聞與低時效內容為主，缺當日 ETF 淨流量與權威即時來源。可用性不足，暫不形成可交易警報。
- 判讀（1-2 句）：先歸檔，等待硬數據來源補齊。
- 反向驗證（反證/待確認項）：缺 Coinglass/彭博/路透即時流量與官方公告。
- 建議動作（Follow-up）：新增 ETF flow API 與交易所官方公告監控。
- 評分拆解：帳號權重 12 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 10 = 29

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 缺口與補件方式
1. `web_search` 無 API key → 補 `openclaw configure --section web`
2. 缺 X/關鍵帳號互動增速 → 接入 watcher 資料源
3. Crypto/Taiwan Semi 缺官方即時硬數據 → 補 IR、通訊社、ETF flow 結構化來源
