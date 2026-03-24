# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 01:00
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS（Reuters/CNBC/Microsoft/NVIDIA/產業媒體聚合）
- Constraints: X 即時互動資料不可得；`web_search`（Brave）仍未配置，熱度速度以「近 24h 媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：76/100
- 等級：L2
- 來源：Microsoft Blog、NVIDIA Newsroom、VentureBeat（經 Google News RSS）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、Vera Rubin、OpenAI、Anthropic
- 摘要（2-3 句）：GTC 相關訊號持續延燒，Microsoft 與 NVIDIA 均有官方發布，且產業媒體追加報導新平台節點。主題延續 AI 基建與實體 AI 擴張，具中高可信與延續性。短期仍屬敘事驅動，落地強度待財務/訂單資料補足。
- 判讀（1-2 句）：AI Infra 主線未變，但尚未達到 L1 的跨來源硬數據密度。
- 反向驗證（反證/待確認項）：缺少主流通訊社對企業採購額度、GPU 交付節奏的量化核實。
- 建議動作（Follow-up）：追蹤 Reuters/Bloomberg 對雲端 CapEx 與供應鏈訂單拆解，48h 內重評。
- 評分拆解：帳號權重 27 + 關鍵字 23 + 熱度速度 12 + 跨來源 9 - 去雜訊 5 = 76

## Signal 2
- 類別：Macro / Oil
- 熱度分：70/100
- 等級：L2
- 來源：Reuters、CNBC（經 Google News RSS）
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply disruption
- 摘要（2-3 句）：OPEC+ 增產議題持續由 Reuters 與 CNBC 報導，並與地緣風險訊號（中東供應不確定）並行。市場含義偏「供給微調 vs 風險溢價」拉鋸。未見新官方決議落地，仍屬預期交易階段。
- 判讀（1-2 句）：屬可執行但非突發級訊號，維持 L2。
- 反向驗證（反證/待確認項）：正式會議決議與執行率尚未更新；EIA 庫存與運輸中斷數據需同步。
- 建議動作（Follow-up）：等 OPEC+ 正式公告 + EIA 高頻資料後再判定是否升降級。
- 評分拆解：帳號權重 25 + 關鍵字 21 + 熱度速度 10 + 跨來源 10 - 去雜訊 4 = 70

## Signal 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：Reuters（主）、DW/投行展望（二級）
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技與產業政策競賽敘事延續，Reuters 仍是最可信主來源。其他來源多屬背景分析，對「即時政策落地」證據有限。訊號對半導體與地緣風險溢價有中期影響。
- 判讀（1-2 句）：方向偏多頭/風險並存，但交易時效不足，暫維持 L2。
- 反向驗證（反證/待確認項）：缺中國官方最新部委細則、資金規模與時間表。
- 建議動作（Follow-up）：新增中國部委/官媒公告源，待一手政策文本後再評分。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 6 = 62

## Signal 4
- 類別：Taiwan Semi
- 熱度分：52/100
- 等級：L3
- 來源：Seeking Alpha、Tom’s Hardware、tastylive
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity bottleneck
- 摘要（2-3 句）：TSMC CoWoS 產能主題仍在，但可用來源以評論/產業媒體為主，且多為舊聞重述。缺乏最新 IR 或主流通訊社對新增產能與客戶拉貨節奏的量化確認。
- 判讀（1-2 句）：目前偏背景噪音，維持 L3 歸檔。
- 反向驗證（反證/待確認項）：等待公司法說、IR 文件或 Reuters/Bloomberg 新訊。
- 建議動作（Follow-up）：綁定 TSMC IR 與台系供應鏈一手公告源。
- 評分拆解：帳號權重 14 + 關鍵字 20 + 熱度速度 7 + 跨來源 6 - 去雜訊 8 = 39

## Signal 5
- 類別：Crypto Flow
- 熱度分：46/100
- 等級：L3
- 來源：Bitcoin Magazine、The Block、CoinDesk（多為舊時點）
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓取結果以歷史事件與回顧內容為主，缺當前 ETF 申贖流量與交易所風險即時資料。跨來源有，但「時效性 + 一手硬數據」不足。
- 判讀（1-2 句）：不構成即時交易訊號，維持 L3。
- 反向驗證（反證/待確認項）：需 Coinglass/交易所官方公告/主流通訊社即時驗證。
- 建議動作（Follow-up）：補 ETF flow 結構化 API，提升熱度速度與真實流量辨識。
- 評分拆解：帳號權重 13 + 關鍵字 16 + 熱度速度 6 + 跨來源 6 - 去雜訊 10 = 31

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 缺口與補件方式
1. 缺 X 互動增速數據（無法精算熱度速度）
   - 補件：接入 X watcher 或授權社群監控輸出
2. `web_search` 缺 Brave API key
   - 補件：`openclaw configure --section web`
3. Taiwan Semi / Crypto 缺即時一手硬數據
   - 補件：IR 快訊、ETF flow API、官方公告 feed
