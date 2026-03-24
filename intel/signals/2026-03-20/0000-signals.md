# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 00:00
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS（聚合）＋ Reuters/CNBC/Microsoft/NVIDIA/產業媒體標題
- Constraints: X 即時互動資料未接入；`web_search`（Brave）未配置，熱度速度改用「近期媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Microsoft 官方部落格、NVIDIA Newsroom、Google News RSS
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：GTC 檔期由 Microsoft 與 NVIDIA 同步發布 AI 基建與 Physical AI 方案，屬官方高可信訊號。短線偏敘事驅動，尚缺訂單/營收轉化證據。
- 判讀（1-2 句）：為 AI 基建週期延續的正向 L2 訊號，需追蹤量化落地資料。
- 反向驗證（反證/待確認項）：缺第三方財務拆解與實際交付節奏。
- 建議動作（Follow-up）：48h 追蹤 Reuters/Bloomberg 對企業採購與CapEx量化報導。
- 評分拆解：26 + 22 + 11 + 9 - 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 增產敘事由 Reuters 與 CNBC 交叉覆蓋，屬供給側中樞訊號。現階段仍偏「政策預期」而非執行結果。
- 判讀（1-2 句）：短期對油價形成區間壓力，但地緣變數可快速反轉。
- 反向驗證（反證/待確認項）：待正式會議與實際履約率；中東地緣風險可能抵銷增產效應。
- 建議動作（Follow-up）：追蹤下次 OPEC+ 公告與 EIA 庫存數據。
- 評分拆解：25 + 20 + 10 + 10 - 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技政策與中美競爭主題持續，方向上利於解讀半導體/AI產業鏈風險溢價。訊號偏中期結構，短線可交易性有限。
- 判讀（1-2 句）：可列為風險框架觀察項，等待具體政策文本落地。
- 反向驗證（反證/待確認項）：缺官方細則（部委公告、補貼條款、資金規模）。
- 建議動作（Follow-up）：加入中國官方公告源，政策文出現後重評。
- 評分拆解：24 + 18 + 8 + 8 - 5 = 63

## Signal 4
- 類別：Taiwan Semi
- 熱度分：43/100
- 等級：L3
- 來源：Seeking Alpha、Tom's Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能緊張敘事延續，但本輪多為評論/產業媒體，缺少最新公司官方增量。偏舊題材延伸。
- 判讀（1-2 句）：維持 L3 歸檔，等待法說或公司公告級新證據。
- 反向驗證（反證/待確認項）：需補台積電最新季度指引與客戶下單節奏。
- 建議動作（Follow-up）：盯 TSMC IR 與主流通訊社即時稿。
- 評分拆解：15 + 20 + 8 + 6 - 6 = 43

## Signal 5
- 類別：Crypto Flow
- 熱度分：29/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓取內容時效偏舊，且缺少權威當日 ETF 流量與交易所風險事件更新。跨來源確認弱。
- 判讀（1-2 句）：不構成可執行即時訊號。
- 反向驗證（反證/待確認項）：需補 Coinglass/主流通訊社/官方公告的日內資料。
- 建議動作（Follow-up）：建立 ETF flow 結構化資料源。
- 評分拆解：12 + 16 + 6 + 5 - 10 = 29

---

## 分級總結
- L1：0
- L2：3
- L3：2

## 今日缺口與補件方式
1. 缺 X 即時互動增速資料（無法精算 heat velocity）
2. 缺 Brave API key（`openclaw configure --section web` 後可擴充來源）
3. Crypto / Taiwan Semi 缺官方一手即時數據（建議接 IR + 通訊社 + flow API）
