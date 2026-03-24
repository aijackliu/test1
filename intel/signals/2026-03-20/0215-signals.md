# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 02:15
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS 聚合（Reuters/CNBC/NVIDIA/Microsoft/產業媒體）
- Constraints:
  - `web_search` 仍不可用（缺 Brave API key）
  - 缺 X 即時互動增速資料，熱度速度以「近期多來源覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：76/100
- 等級：L2
- 來源：
  - The Official Microsoft Blog（2026-03-16）
  - NVIDIA Newsroom（2026-03-16）
  - Technology Magazine（二次轉述，2026-03-19）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、AI Agents、Data Factory
- 摘要（2-3 句）：Microsoft 與 NVIDIA 在 GTC 週期的 AI 基建/Physical AI 訊號延續，並有次級媒體二次擴散。屬於官方釋出驅動的敘事強訊號，但尚缺即時營收或交付量化數據。
- 判讀（1-2 句）：維持 L2（高可信、未到交易級拐點）。
- 反向驗證（反證/待確認項）：需補雲端客戶採用率、GPU 實際交付與 ASP 資料。
- 建議動作（Follow-up）：48h 追蹤 Reuters/Bloomberg 是否補量化數據，若有兩家以上獨立驗證可重評。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 12 + 跨來源 10 - 去雜訊 6 = 64（主題持續性+12 綜合調整）

## Signal 2
- 類別：Macro / Oil
- 熱度分：70/100
- 等級：L2
- 來源：
  - Reuters（OPEC+ 增產訊號）
  - CNBC（同主題覆蓋）
  - OilPrice（二級市場轉述）
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 增產相關敘事由 Reuters 與 CNBC 持續覆蓋，屬供給端中期定價訊號。市場仍受地緣風險擾動，油價方向未形成單邊。
- 判讀（1-2 句）：仍是 L2，偏「事件驅動觀察」而非確定性趨勢。
- 反向驗證（反證/待確認項）：正式會議決議與執行率尚未確認；地緣衝突可能抵銷增產效果。
- 建議動作（Follow-up）：追蹤下一次 OPEC+ 正式公告 + EIA 庫存。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 5 = 60（宏觀影響面+10 綜合調整）

## Signal 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：
  - Reuters（中國科技競爭與政策脈絡）
  - DW（二級補充）
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技政策與中美競爭敘事延續，Reuters 為主來源。訊號偏中期政策方向，對半導體與風險資產估值有間接影響。
- 判讀（1-2 句）：方向存在，但缺「新政策細則」使可執行度有限。
- 反向驗證（反證/待確認項）：尚缺官方部委公告與預算/補貼條款。
- 建議動作（Follow-up）：補抓中國官方政策發布源後再評級。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 6 = 52（政策影響面+10 綜合調整）

## Signal 4
- 類別：Taiwan Semi
- 熱度分：46/100
- 等級：L3
- 來源：
  - Seeking Alpha
  - Tom's Hardware
  - tastylive
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity bottleneck
- 摘要（2-3 句）：CoWoS 產能瓶頸與 AI 需求敘事持續，但主要是舊題材延伸，且來源多為評論/次級媒體。缺少台積電最新一手 IR 或法說增量資訊。
- 判讀（1-2 句）：維持灰燈觀察，不升級。
- 反向驗證（反證/待確認項）：需官方產能數字與客戶訂單能見度。
- 建議動作（Follow-up）：等待 TSMC IR/法說或主流通訊社一手消息再評分。
- 評分拆解：帳號權重 15 + 關鍵字 19 + 熱度速度 7 + 跨來源 6 - 去雜訊 8 = 39（關聯性+7 綜合調整）

## Signal 5
- 類別：Crypto Flow
- 熱度分：41/100
- 等級：L3
- 來源：
  - Bitcoin Magazine
  - dlnews
  - The Block
  - CoinDesk（舊事件）
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：目前抓到的多為舊聞與回顧，缺少當日 ETF 淨流量與交易所新風險事件的一手確認。時效性不足。
- 判讀（1-2 句）：不具即時決策價值，先歸檔。
- 反向驗證（反證/待確認項）：需補 Coinglass/主流終端流量與官方公告。
- 建議動作（Follow-up）：建立 ETF flow 結構化資料源後再啟用此 watcher。
- 評分拆解：帳號權重 13 + 關鍵字 16 + 熱度速度 5 + 跨來源 6 - 去雜訊 12 = 28（相關性+13 綜合調整）

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 缺口與補件方式
1. 缺 X 即時互動增速 → 熱度速度精度不足
2. 缺 Brave API key → 無法擴展跨來源驗證
3. 缺一手結構化資料（ETF flow / TSMC IR 即時）→ 部分訊號僅能維持 L2/L3
