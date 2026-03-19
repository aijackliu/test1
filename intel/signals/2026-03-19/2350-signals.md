# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-19 23:50
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS 聚合（Reuters/CNBC/Microsoft/NVIDIA/產業媒體）
- Constraints: `web_search` 不可用（缺 Brave API key）；X 即時互動與關鍵帳號原生流缺失，熱度速度以「近期媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：The Official Microsoft Blog、NVIDIA Newsroom、Google News RSS
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：GTC 檔期 Microsoft 與 NVIDIA 同步發布 AI 基建/Physical AI 方案，屬官方高可信訊號。現階段偏敘事強化與生態擴張，尚缺可量化財務落地資料。
- 判讀（1-2 句）：維持 L2，支持「AI 基建週期延續」但未達突發升級。
- 反向驗證（反證/待確認項）：需主流通訊社/財報補充訂單、交付、CapEx 量化指標。
- 建議動作（Follow-up）：追蹤 48h 內 Bloomberg/Reuters 後續量化報導。
- 評分拆解：26 + 22 + 11 + 9 - 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent、supply
- 摘要（2-3 句）：OPEC+ 小幅增產預期持續被主流媒體交叉覆蓋。屬供給面政策訊號，對油價短線波動與通膨預期有影響。
- 判讀（1-2 句）：仍是政策預期階段，未見新的實際執行拐點。
- 反向驗證（反證/待確認項）：正式會議結論與執行率、地緣事件衝擊可能反向抵銷。
- 建議動作（Follow-up）：等正式公告與EIA庫存資料後重評。
- 評分拆解：25 + 20 + 10 + 10 - 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技政策與中美競爭敘事延續，方向性明確。市場影響偏中期風險定價，而非即時事件衝擊。
- 判讀（1-2 句）：可納入日報跟蹤，但交易可執行性仍低。
- 反向驗證（反證/待確認項）：缺最新官方細則/資金規模與時程。
- 建議動作（Follow-up）：補中國部委公告與官方文本來源後再評。
- 評分拆解：24 + 18 + 8 + 8 - 5 = 63

## Signal 4
- 類別：Taiwan Semi
- 熱度分：43/100
- 等級：L3
- 來源：Seeking Alpha、Tom's Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 供需緊張議題持續，但可得資訊偏評論/二手產業媒體，缺少最新官方一手指引。
- 判讀（1-2 句）：屬舊主題延伸，暫不升級。
- 反向驗證（反證/待確認項）：需台積電法說或IR最新數字。
- 建議動作（Follow-up）：鎖定 TSMC IR + Reuters/Bloomberg 快訊。
- 評分拆解：15 + 20 + 8 + 6 - 6 = 43

## Signal 5
- 類別：Crypto Flow
- 熱度分：29/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓取內容時效偏舊，且缺權威即時資金流/風險事件確認，不足以形成可執行訊號。
- 判讀（1-2 句）：維持存檔觀察。
- 反向驗證（反證/待確認項）：需即時ETF流量與官方公告佐證。
- 建議動作（Follow-up）：接入 Coinglass/主流終端資料後重跑。
- 評分拆解：12 + 16 + 6 + 5 - 10 = 29

---
## 分級總結
- L1：0
- L2：3
- L3：2

## 缺口
1. 無 X 即時互動增速資料
2. `web_search` 缺 API key
3. Crypto / Taiwan Semi 缺官方一手即時量化資料
