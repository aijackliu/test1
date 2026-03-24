# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 00:22
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS 聚合（Reuters/CNBC/Microsoft/NVIDIA/產業媒體）
- Constraints: `web_search` 仍不可用（缺 Brave API key）；X 即時互動增速資料缺失，熱度速度以近 24h 媒體覆蓋密度替代

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Microsoft Blog、NVIDIA Newsroom、Google News RSS
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、Data Factory
- 摘要（2-3 句）：GTC 檔期內 Microsoft 與 NVIDIA 同步發布 AI 基建/Physical AI 方案，屬高可信官方訊號。市場敘事強，但尚缺第三方量化驗證（訂單、雲端收入增量）。
- 判讀（1-2 句）：中高強度題材延續，暫列 L2。
- 反向驗證（反證/待確認項）：缺彭博/路透對採購規模與交付節奏的獨立拆解。
- 建議動作（Follow-up）：48h 追蹤主流通訊社與財報口徑；若雙來源量化確認再評估升級。
- 評分拆解：26 + 22 + 11 + 9 - 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent
- 摘要（2-3 句）：OPEC+ 增產敘事持續由 Reuters/CNBC 重複確認。屬供給預期調整訊號，對油價與通膨預期有方向性影響。
- 判讀（1-2 句）：短線偏區間，不屬突發 L1 事件。
- 反向驗證（反證/待確認項）：需正式會議結果與執行率；地緣衝突可能抵銷增產效果。
- 建議動作（Follow-up）：跟進 OPEC+ 官宣與 EIA 庫存數據。
- 評分拆解：25 + 20 + 10 + 10 - 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技政策與中美競爭主題延續，Reuters 持續有中期敘事更新。方向明確，但落地交易信號不足。
- 判讀（1-2 句）：先維持 L2 觀察，等待官方政策文本細節。
- 反向驗證（反證/待確認項）：缺部委正式細則、資金與時程。
- 建議動作（Follow-up）：補中國官方公告來源，出現具體條款再重評。
- 評分拆解：24 + 18 + 8 + 8 - 5 = 63

## Signal 4
- 類別：Taiwan Semi
- 熱度分：55/100
- 等級：L3
- 來源：Seeking Alpha、Tom's Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能瓶頸敘事延續，但可得內容多為評論與二手產業媒體。缺乏最新官方指引。
- 判讀（1-2 句）：非新拐點，維持灰燈。
- 反向驗證（反證/待確認項）：需台積電法說/IR 最新數據。
- 建議動作（Follow-up）：鎖定 TSMC IR 與主流通訊社快訊。
- 評分拆解：15 + 20 + 8 + 6 - 6 = 43（主題相關性高，保留優先觀察）

## Signal 5
- 類別：Crypto Flow
- 熱度分：49/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：可見訊號多為舊聞或低即時性來源，缺當日 ETF 淨流與權威快訊確認。可執行性低。
- 判讀（1-2 句）：暫不構成交易級訊號。
- 反向驗證（反證/待確認項）：需 Coinglass/交易所公告/主流媒體即時交叉驗證。
- 建議動作（Follow-up）：接入 ETF flow 結構化資料源。
- 評分拆解：12 + 16 + 6 + 5 - 10 = 29

---
## 分級總結
- L1：0
- L2：3
- L3：2

## 缺口
1. X 即時互動增速缺失
2. Brave API key 缺失，web_search 不可用
3. Taiwan Semi / Crypto 缺官方一手即時數據