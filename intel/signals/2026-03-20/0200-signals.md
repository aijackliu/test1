# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 02:00
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS（Reuters/CNBC/Microsoft/NVIDIA/產業媒體聚合）
- Constraints: X 即時互動資料缺失；`web_search`（Brave）目前不可用，熱度速度以近期媒體覆蓋密度近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Microsoft Blog（2026-03-16）、NVIDIA Newsroom（2026-03-16）、Google News RSS 聚合（2026-03-20 抓取）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：Microsoft 與 NVIDIA 在 GTC 檔期發布 AI 基礎設施/Physical AI 方案，屬官方高可信訊號。主題延續性強，但仍偏敘事層，缺少新增訂單與財務落地數據。
- 判讀（1-2 句）：AI 基建景氣延續的 L2 訊號，暫不構成突發 L1。
- 反向驗證（反證/待確認項）：等待主流媒體或財報披露新增CapEx、GPU交付與客戶採用規模。
- 建議動作（Follow-up）：48h 追蹤 Reuters/Bloomberg 是否出現量化補強；若有跨來源財務實證可上修。
- 評分拆解：26 + 22 + 11 + 9 - 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent、supply
- 摘要（2-3 句）：OPEC+ 小幅增產敘事由 Reuters 與 CNBC 交叉覆蓋。屬供給端政策預期訊號，對油價與通膨預期有邊際影響。
- 判讀（1-2 句）：為可交易背景變數，但未達突發衝擊級。
- 反向驗證（反證/待確認項）：需等正式會議與執行率，地緣風險仍可能反向驅動油價。
- 建議動作（Follow-up）：追蹤 OPEC+ 正式公告與 EIA 庫存變化，再調整級別。
- 評分拆解：25 + 20 + 10 + 10 - 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技與政策競賽相關敘事持續，對半導體與地緣風險溢價具中期影響。當前仍偏方向訊號，缺乏新政策細節。
- 判讀（1-2 句）：中期偏多事件驅動，短線可執行性一般。
- 反向驗證（反證/待確認項）：需等待部委公告與財政配置細節。
- 建議動作（Follow-up）：增設官媒/部委一手來源 RSS，出現政策文本後重評。
- 評分拆解：24 + 18 + 8 + 8 - 5 = 63

## Signal 4
- 類別：Taiwan Semi
- 熱度分：55/100
- 等級：L3
- 來源：Seeking Alpha、Tom’s Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 瓶頸題材延續，但最新抓取仍以評論/產業媒體為主，缺乏台積電官方最新指引。屬舊主題延伸。
- 判讀（1-2 句）：先維持灰燈，等待一手財報/法說數據。
- 反向驗證（反證/待確認項）：缺官方最新季度/法說具體產能與需求節奏。
- 建議動作（Follow-up）：鎖定 TSMC IR 與主流通訊社快訊。
- 評分拆解：15 + 20 + 8 + 6 - 6 = 43（主題重要性上調觀察優先，不改等級）

## Signal 5
- 類別：Crypto Flow
- 熱度分：49/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：目前命中內容時效偏舊，且來源權威性與一致性不足。缺少當日 ETF 資金流與交易所風險事件一手確認。
- 判讀（1-2 句）：無即時可執行訊號，先存檔。
- 反向驗證（反證/待確認項）：需 Coinglass/交易所公告/主流通訊社即時流量數據。
- 建議動作（Follow-up）：補接結構化 ETF flow 與鏈上監控來源。
- 評分拆解：12 + 16 + 6 + 5 - 10 = 29

---

## 分級總結
- L1：0
- L2：3
- L3：2

## 資料缺口與補件
1. X 熱度增速資料缺失（無法精算熱度速度）
2. Brave API key 未配置（無法用 web_search 擴充交叉來源）
3. Taiwan Semi/Crypto 缺官方即時一手數據
