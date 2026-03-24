# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 03:30
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS（Reuters/CNBC/Microsoft/NVIDIA/產業媒體聚合）
- Constraints: X 即時互動資料缺失；`web_search`（Brave）未配置，跨來源驗證受限

## Signal 1
- 類別：AI Infra
- 熱度分：76/100
- 等級：L2
- 來源：The Official Microsoft Blog、NVIDIA Newsroom、Technology Magazine（聚合）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、AI Agents、data factory
- 摘要（2-3 句）：Microsoft 與 NVIDIA 在 GTC 檔期釋出 AI 基建與 Physical AI 方案，且有二級媒體擴散。主題延續性高，但目前仍偏產品敘事，尚缺財務落地數據。
- 判讀（1-2 句）：屬高可信中高熱度 L2，短期偏題材驅動，等待企業採購與CapEx實證。
- 反向驗證（反證/待確認項）：缺主流通訊社對新增訂單/GPU交付量化追蹤。
- 建議動作（Follow-up）：48h 內追蹤 Reuters/Bloomberg 後續；若出現量化訂單/支出證據可升級。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 13 + 跨來源 10 - 去雜訊 5 = 76

## Signal 2
- 類別：Macro / Oil
- 熱度分：70/100
- 等級：L2
- 來源：Reuters、CNBC、OilPrice（聚合）
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 增產相關訊號由 Reuters 與 CNBC 重複確認，主軸集中於供給面小幅提升與地緣風險並存。屬可影響短期油價波動的政策訊號。
- 判讀（1-2 句）：中度可交易但非突發級，油價/通膨預期維持區間博弈。
- 反向驗證（反證/待確認項）：需等待正式決議與執行率；中東事件可能反向推升風險溢價。
- 建議動作（Follow-up）：追蹤 OPEC+ 正式會議與 EIA 庫存變化，依落地程度調級。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 11 + 跨來源 10 - 去雜訊 4 = 70

## Signal 3
- 類別：Chinese Signal
- 熱度分：64/100
- 等級：L2
- 來源：Reuters、dw.com（聚合）
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技競爭與政策導向訊號仍由 Reuters 持續報導，並有其他媒體補充中期規劃背景。對半導體供應鏈與風險偏好有結構性影響。
- 判讀（1-2 句）：方向性有效，但欠缺最新官方細則，屬政策前瞻 L2。
- 反向驗證（反證/待確認項）：缺部委正式文件、財政額度與落地節點。
- 建議動作（Follow-up）：補中國官方公告源（工信部/發改委/國務院）後重評。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 9 + 跨來源 8 - 去雜訊 5 = 64

## Signal 4
- 類別：Taiwan Semi
- 熱度分：52/100
- 等級：L3
- 來源：Seeking Alpha、Tom's Hardware、tastylive（聚合）
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：TSMC CoWoS 供需緊張敘事持續，但新增內容多屬評論與二手整理，時效偏舊。未見最新法說或公司公告級新資訊。
- 判讀（1-2 句）：延續性議題，非新拐點；維持 L3 監看。
- 反向驗證（反證/待確認項）：缺台積電一手數字（產能節奏、客戶拉貨、ASP）。
- 建議動作（Follow-up）：鎖定 TSMC IR 與主流通訊社快訊，一旦有量化更新再升級。
- 評分拆解：帳號權重 14 + 關鍵字 19 + 熱度速度 8 + 跨來源 7 - 去雜訊 6 = 42

## Signal 5
- 類別：Crypto Flow
- 熱度分：47/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、The Block（多為舊聞）
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：Crypto 條目以舊聞為主，且缺即時 ETF 流量與權威通訊社二次確認。時效與可交易性不足。
- 判讀（1-2 句）：不構成當下交易訊號，先歸檔。
- 反向驗證（反證/待確認項）：需補當日 ETF 淨流量、交易所官方公告與鏈上異常資料。
- 建議動作（Follow-up）：接入 ETF flow/交易所風險監控 API 後重跑。
- 評分拆解：帳號權重 12 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 10 = 29

---

## 分級總結
- L1：0
- L2：3
- L3：2

## 缺口與補件
1. 缺 X 互動增速數據（熱度速度僅能估算）
2. 缺 Brave web_search API key（降低交叉驗證完整度）
3. Taiwan Semi/Crypto 缺官方一手即時數據源
