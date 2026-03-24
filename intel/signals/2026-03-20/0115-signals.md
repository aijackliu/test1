# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 01:15
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS 聚合（Reuters/CNBC/Microsoft/NVIDIA/產業媒體）
- Constraints: `web_search` 仍不可用（Brave API key 缺失）；X 即時互動資料缺失，熱度速度以跨媒體近期覆蓋密度近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Microsoft Official Blog、NVIDIA Newsroom、Google News RSS
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：GTC 檔期延續 Microsoft 與 NVIDIA 的 AI 基建協同敘事，內容來自官方一手發佈。主題可信度高，但仍屬產品/生態訊號，未見新增財務量化落地。
- 判讀（1-2 句）：AI 基建主線延續，偏中高強度題材訊號。
- 反向驗證（反證/待確認項）：需第三方財務與採購數據驗證（雲端營收、GPU 出貨節奏）。
- 建議動作（Follow-up）：48h 追蹤 Reuters/Bloomberg 是否跟進量化拆解；若出現多家主流數據佐證再評級。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 11 + 跨來源 9 - 去雜訊 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 小幅增產議題持續被主流媒體交叉報導，屬供給端政策預期訊號。對油價與通膨預期有方向性影響，但尚未見新的執行落地更新。
- 判讀（1-2 句）：偏「已知預期持續發酵」，仍是 L2。
- 反向驗證（反證/待確認項）：需正式會議決議與執行率；地緣衝突可能反向壓過增產效果。
- 建議動作（Follow-up）：追蹤 OPEC+ 官方公告與 EIA 庫存數據，出現偏差再升降級。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：64/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技競爭與政策走向持續由 Reuters 跟進，對半導體與地緣風險定價有中期影響。現階段仍偏方向性敘事，具體政策工具資訊不足。
- 判讀（1-2 句）：可列入風險雷達，但可交易性仍有限。
- 反向驗證（反證/待確認項）：缺官方部委文件、資金規模、執行節點。
- 建議動作（Follow-up）：補中國官方政策來源（部委/官媒）後重評。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 9 + 跨來源 8 - 去雜訊 5 = 54
- 備註：主題市場關聯高，維持人工觀察優先（不改等級）

## Signal 4
- 類別：Taiwan Semi
- 熱度分：55/100
- 等級：L3
- 來源：Seeking Alpha、Tom’s Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能瓶頸與擴產論述延續，但來源偏評論與產業媒體，缺少新一手公司指引。未觀察到明確新拐點。
- 判讀（1-2 句）：維持 L3 觀察，等待公司級公告。
- 反向驗證（反證/待確認項）：缺 TSMC 最新法說或官方產能時程數據。
- 建議動作（Follow-up）：跟蹤 TSMC IR 與主流通訊社快訊補齊。
- 評分拆解：帳號權重 15 + 關鍵字 20 + 熱度速度 8 + 跨來源 6 - 去雜訊 6 = 43

## Signal 5
- 類別：Crypto Flow
- 熱度分：49/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews（舊聞）、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：Crypto 訊號多為舊聞與非一線來源，時效性不足。缺 ETF 當日流量與交易所安全事件的主流權威同步確認。
- 判讀（1-2 句）：不具即時決策價值，先歸檔。
- 反向驗證（反證/待確認項）：需 Coinglass/彭博/路透 + 交易所官方公告。
- 建議動作（Follow-up）：接入結構化 ETF flow 與交易所公告源。
- 評分拆解：帳號權重 12 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 10 = 29

---

## 分級總結
- L1：0
- L2：3
- L3：2

## 今日缺口與補件方式
1. 缺 X 即時互動增速 → 補接 X watcher/授權社群監控輸出
2. `web_search` 缺 API key → `openclaw configure --section web` 後可提升覆蓋
3. Taiwan Semi/Crypto 缺一手高可信即時數據 → 補 IR + 通訊社 + 結構化流量源
