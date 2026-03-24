# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 00:45
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS 聚合（Reuters/CNBC/Microsoft/NVIDIA/產業媒體）
- Constraints: 缺 X 即時互動資料；`web_search` 仍不可用（Brave API key 未配置）

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Microsoft Blog、NVIDIA Newsroom、Google News RSS
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory
- 摘要（2-3 句）：GTC 檔期仍由 Microsoft/NVIDIA 官方訊號主導，主軸是 AI 基建與 Physical AI 生態擴張。官方可信度高，但第三方財務落地數據仍少。
- 判讀（1-2 句）：偏中高強度題材訊號，尚未達到 L1 的可交易確認。
- 反向驗證（反證/待確認項）：缺企業採購量、雲端營收拆解、交付節奏。
- 建議動作（Follow-up）：持續追蹤 Reuters/Bloomberg 是否出現量化落地報導。

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent crude
- 摘要（2-3 句）：OPEC+ 小幅增產敘事持續，主要由 Reuters 與 CNBC 交叉覆蓋。屬供給預期調整，未見最新突發催化。
- 判讀（1-2 句）：宏觀層級有效，但更像「延續訊號」非「新拐點」。
- 反向驗證（反證/待確認項）：需看正式決議與執行率，並持續觀察地緣風險反向衝擊。
- 建議動作（Follow-up）：下一輪加入 EIA 庫存與油運數據交叉。

## Signal 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、semiconductor、AI policy
- 摘要（2-3 句）：中國科技/產業政策方向的敘事延續，仍由主流媒體以宏觀視角覆蓋。對半導體估值與風險溢價有中期影響。
- 判讀（1-2 句）：方向性明確，但缺具體政策條文，交易可操作性有限。
- 反向驗證（反證/待確認項）：尚缺部委正式細則、補貼規模與時間表。
- 建議動作（Follow-up）：補接中國官方公告來源再評分。

## Signal 4
- 類別：Taiwan Semi
- 熱度分：55/100
- 等級：L3
- 來源：Seeking Alpha、Tom’s Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 供需緊張仍是舊主題延續，新增資訊密度不足。來源以評論/產業媒體為主，權威性偏弱。
- 判讀（1-2 句）：保持觀察，不升級。
- 反向驗證（反證/待確認項）：缺 TSMC 官方最新指引與客戶下單節奏。
- 建議動作（Follow-up）：等待法說或通訊社硬數據。

## Signal 5
- 類別：Crypto Flow
- 熱度分：49/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓取內容時間戳偏舊，且來源權威度與一致性不足。缺乏當日 ETF 淨流量/風險事件即時確認。
- 判讀（1-2 句）：不構成可執行即時訊號。
- 反向驗證（反證/待確認項）：需補 Coinglass/彭博/路透的當日流量與官方公告。
- 建議動作（Follow-up）：導入結構化 flow source 後重跑。

---

## 分級總結
- L1：0
- L2：3
- L3：2

## 缺口
1. 缺 X 互動增速資料（熱度速度只能近似）
2. Brave API key 缺失（`web_search` 不可用）
3. Crypto / Taiwan Semi 缺官方即時一手數據
