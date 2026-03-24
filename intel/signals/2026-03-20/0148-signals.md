# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 01:48
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS（Reuters/CNBC/Microsoft/NVIDIA/產業媒體聚合）
- Constraints: `web_search` unavailable（missing Brave API key）；X 即時互動與關鍵帳號原始流未接入，本輪熱度速度採「近期媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：76/100
- 等級：L2
- 來源：
  - The Official Microsoft Blog（2026-03-16）
  - NVIDIA Newsroom（2026-03-16）
  - Technology Magazine（二次報導）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、AI Agents、data factory
- 摘要（2-3 句）：GTC 檔期相關訊號仍在延續，Microsoft 與 NVIDIA 均有官方發布，且出現二次媒體擴散。訊號可信度高，但目前仍以產品/生態敘事為主，缺乏即時商業化落地數字。
- 判讀（1-2 句）：屬中高強度 L2，支持 AI 基礎設施主線延續，但尚未達 L1 事件衝擊。
- 反向驗證（反證/待確認項）：待補客戶採購金額、出貨節奏、雲端營收貢獻等硬指標。
- 建議動作（Follow-up）：48h 持續追蹤 Reuters/Bloomberg 是否補充量化訂單或CapEx資料。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 12 + 跨來源 11 - 去雜訊 5 = 76

## Signal 2
- 類別：Macro / Oil
- 熱度分：70/100
- 等級：L2
- 來源：
  - Reuters（OPEC+ 增產訊號）
  - CNBC（同主題）
  - OilPrice（二次市場解讀）
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply shock
- 摘要（2-3 句）：OPEC+ 增產預期仍有跨來源報導，屬供給端重要訊號。現階段偏預期與評論混合，尚未看到最新官方執行數據確認。
- 判讀（1-2 句）：對油價與通膨預期有影響，但目前屬趨勢延伸，不是新突發。
- 反向驗證（反證/待確認項）：需確認正式會議決議與實際增產落地率，並排除地緣風險反向拉抬。
- 建議動作（Follow-up）：跟進 OPEC+ 正式公告與 EIA 庫存，出現偏離預期再升級。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 5 = 70

## Signal 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：
  - Reuters（中國科技競爭/政策走向）
  - DW（二次報導）
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技與政策方向訊號持續，但可交易性仍偏中期敘事。來源有主流媒體覆蓋，但官方細則仍不足。
- 判讀（1-2 句）：可作為中期風險與主題配置參考，短期交易觸發力有限。
- 反向驗證（反證/待確認項）：缺少部委正式文件與資金規模拆解。
- 建議動作（Follow-up）：補中國官方公告來源後再重評等級。
- 評分拆解：帳號權重 23 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 5 = 62

## Signal 4
- 類別：Taiwan Semi
- 熱度分：46/100
- 等級：L3
- 來源：
  - Seeking Alpha（評論）
  - Tom's Hardware（產業媒體）
  - tastylive（節目型內容）
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：TSMC CoWoS 供需吃緊的敘事仍在，但本輪來源偏評論與二手媒體。缺乏台積電最新法說/公告級的新增事實。
- 判讀（1-2 句）：維持觀察，不構成新級別警報。
- 反向驗證（反證/待確認項）：需官方IR或主流通訊社披露最新產能與客戶排程。
- 建議動作（Follow-up）：等待一手來源更新，再評估是否升至 L2。
- 評分拆解：帳號權重 14 + 關鍵字 19 + 熱度速度 7 + 跨來源 6 - 去雜訊 8 = 38

## Signal 5
- 類別：Crypto Flow
- 熱度分：41/100
- 等級：L3
- 來源：
  - Bitcoin Magazine（監管敘事）
  - dlnews（舊聞）
  - CoinDesk（歷史事件）
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓取內容多為舊聞或回顧，缺乏即時 ETF 淨流量與權威機構同步確認。交叉來源雖存在，但時間戳老舊，訊號效度低。
- 判讀（1-2 句）：本輪不具即時交易價值，維持 L3 歸檔。
- 反向驗證（反證/待確認項）：需 Coinglass/彭博/路透當日流量與事件快訊。
- 建議動作（Follow-up）：接入結構化 ETF flow 與交易所公告來源。
- 評分拆解：帳號權重 13 + 關鍵字 15 + 熱度速度 5 + 跨來源 5 - 去雜訊 11 = 27

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 缺口與補件
1. 缺 X 與關鍵帳號原始流（無法完成精準熱度速度）
2. `web_search` 缺 Brave API key（跨來源深度不足）
3. Crypto / Taiwan Semi 缺官方即時硬資料（IR、flow、公告）
