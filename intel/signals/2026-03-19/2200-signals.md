# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-19 22:00
- Data sources: Google News RSS（Reuters/VentureBeat/官方部落格等聚合）
- Constraint: 缺 X 即時互動資料；`web_search` 仍不可用（Brave API key 未配置）

## Signal 1
- 類別：Chinese Signal
- 熱度分：76/100
- 等級：L2
- 來源：Reuters（3/4、3/5 連續報導）+ Google News 聚合
- 命中關鍵字：China、five-year plan、AI、tech breakthroughs、semiconductor
- 摘要（2-3 句）：Reuters 連續報導中國新五年規劃將 AI 深入經濟體系，並聚焦科技突破路線。該訊號具政策中期方向性，對中資科技鏈與全球半導體競爭敘事影響較大。
- 判讀（1-2 句）：屬高可信政策框架訊號，但仍需官方細則與資金配置文件落地。
- 反向驗證（反證/待確認項）：缺中國部委正式條文、財政強度與執行時間表。
- 建議動作（Follow-up）：追蹤國務院/工信部公告與外資投行量化解讀。
- 評分拆解：帳號權重27 + 關鍵字22 + 熱度速度11 + 跨來源10 - 去雜訊-6 = 76

## Signal 2
- 類別：Macro / Oil
- 熱度分：72/100
- 等級：L2
- 來源：Reuters（3/1、3/2）+ Google News 聚合
- 命中關鍵字：OPEC+、oil output boost、Hormuz disruption、Brent crude
- 摘要（2-3 句）：Reuters 指出 OPEC+ 溫和增產同時，市場更關注 Hormuz 擾動持續時間。供給增加與地緣風險同時存在，使油價波動呈雙向拉扯。
- 判讀（1-2 句）：不是單向利空油價訊號，屬「供給與風險對沖」情境。
- 反向驗證（反證/待確認項）：需核對實際增產執行率與運輸中斷時間窗。
- 建議動作（Follow-up）：接續追 EIA 庫存、船運保費與中東地緣事件節點。
- 評分拆解：帳號權重28 + 關鍵字20 + 熱度速度10 + 跨來源9 - 去雜訊-5 = 72

## Signal 3
- 類別：AI Infra
- 熱度分：67/100
- 等級：L2
- 來源：VentureBeat（3/16）+ Google News 聚合
- 命中關鍵字：NVIDIA、Vera Rubin、AI platform、OpenAI、Anthropic、Meta
- 摘要（2-3 句）：NVIDIA 新平台消息持續被科技媒體覆蓋，且綁定多家模型公司敘事。主軸仍為 AI 基建擴張，但目前多為產品與生態口徑。
- 判讀（1-2 句）：中期偏正面，短期尚缺財務落地數據支撐（訂單/交付/毛利）。
- 反向驗證（反證/待確認項）：缺 Reuters/Bloomberg 當期供應鏈量化追蹤。
- 建議動作（Follow-up）：等主流通訊社與財報季交叉確認再評級。
- 評分拆解：帳號權重18 + 關鍵字24 + 熱度速度10 + 跨來源8 - 去雜訊-7 = 67

## Signal 4
- 類別：Taiwan Semi
- 熱度分：51/100
- 等級：L3
- 來源：產業媒體/財經聚合（非官方一手）
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能瓶頸與擴產敘事仍在，但本輪來源可信度參差，缺官方法說更新。偏舊題材延伸，非新拐點。
- 判讀（1-2 句）：暫維持灰燈，僅作背景噪音過濾。
- 反向驗證（反證/待確認項）：需 TSMC IR 或主流通訊社的一手數字。
- 建議動作（Follow-up）：等待公司公告/法說後重評。

## Signal 5
- 類別：Crypto Flow
- 熱度分：44/100
- 等級：L3
- 來源：Ledger/TradingView/其他內容站（多為舊文）
- 命中關鍵字：Bitcoin ETF、flows、exchange hack
- 摘要（2-3 句）：本輪抓取到的 crypto 內容時效性偏舊，且缺權威流量數據。無法支撐即時交易級信號。
- 判讀（1-2 句）：僅歸檔，不升級。
- 反向驗證（反證/待確認項）：缺 ETF 淨流量與交易所官方安全事件公告。
- 建議動作（Follow-up）：接入結構化 flow data 後再啟用此 watcher。

---
## 分級總結
- L1：0
- L2：3
- L3：2

## 缺口與補件
1. X 熱度增速資料缺失（影響熱度速度分）
2. Brave API key 缺失（跨來源覆蓋受限）
3. Taiwan Semi/Crypto 缺一手官方高時效資料
