# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 01:35
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS（Reuters/CNBC/Microsoft/NVIDIA/產業媒體聚合）
- Constraints: `web_search` 尚不可用（Brave API key 缺失）；X 即時互動數據缺失，熱度速度以「近期媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：76/100
- 等級：L2
- 來源：
  - The Official Microsoft Blog（2026-03-16）
  - NVIDIA Newsroom（2026-03-16）
  - Technology Magazine（2026-03-19）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、AI agents、data factory
- 摘要（2-3 句）：GTC 週期內 Microsoft 與 NVIDIA 的官方發布持續被二線科技媒體轉載，AI 基礎設施與 Physical AI 主題熱度延續。訊號可信度高，但仍偏產品與生態敘事。短期對市場影響以情緒面為主。
- 判讀（1-2 句）：維持 L2，屬「趨勢延續」而非「新拐點」。
- 反向驗證（反證/待確認項）：尚缺第三方量化指標（新增雲端AI收入、GPU交付節奏、企業採購數據）。
- 建議動作（Follow-up）：48h 內追蹤 Reuters/Bloomberg 對 CapEx 與訂單落地的量化報導。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 12 + 跨來源 10 - 去雜訊 6 = 76

## Signal 2
- 類別：Macro / Oil
- 熱度分：68/100
- 等級：L2
- 來源：
  - Reuters（OPEC+ 增產訊號）
  - CNBC（相近主題二次報導）
  - OilPrice（二級補充）
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 增產議題仍由主流財經媒體持續覆蓋，市場聚焦供給端對油價中樞的壓力。訊號屬政策預期，尚未見最新執行數據。
- 判讀（1-2 句）：維持 L2，對通膨預期與能源板塊偏中度影響。
- 反向驗證（反證/待確認項）：需等待正式決議與執行率；地緣衝突可能對沖增產效應。
- 建議動作（Follow-up）：追蹤 OPEC+ 正式公告與 EIA 庫存後再重評。
- 評分拆解：帳號權重 24 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 6 = 68

## Signal 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：
  - Reuters（中美科技競賽與政策敘事）
  - DW（宏觀政策背景）
- 命中關鍵字：China、policy、tech race、semiconductor、AI
- 摘要（2-3 句）：中國科技政策與競賽主題維持媒體能見度，對半導體與區域風險溢價有持續影響。現階段仍以敘事與框架性分析為主。
- 判讀（1-2 句）：方向明確但交易可執行性有限，暫列 L2 觀察。
- 反向驗證（反證/待確認項）：缺少最新部委細則與具體資金規模。
- 建議動作（Follow-up）：補抓中國官方公告源，出現可量化政策後再升降級。
- 評分拆解：帳號權重 23 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 5 = 62

## Signal 4
- 類別：Taiwan Semi
- 熱度分：47/100
- 等級：L3
- 來源：
  - Seeking Alpha（評論）
  - Tom's Hardware（產業媒體）
  - tastylive（市場評論）
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity bottleneck
- 摘要（2-3 句）：台積 CoWoS 產能緊張敘事持續，但本輪新增資訊多為舊聞/評論重述。缺少近期法說或公司公告級更新。
- 判讀（1-2 句）：維持 L3 歸檔，等待一手資訊再評分。
- 反向驗證（反證/待確認項）：無最新 IR 量化數據與客戶投片節奏。
- 建議動作（Follow-up）：鎖定台積 IR、法說逐字稿、主流通訊社快訊。
- 評分拆解：帳號權重 14 + 關鍵字 19 + 熱度速度 7 + 跨來源 6 - 去雜訊 9 = 37

## Signal 5
- 類別：Crypto Flow
- 熱度分：42/100
- 等級：L3
- 來源：
  - Bitcoin Magazine（泰國ETF規則）
  - CoinDesk（歷史事件延伸）
  - dlnews / The Block（多為舊聞）
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：Crypto feed 仍以舊資料為主，缺乏當日 ETF 資金流與交易所風險的權威即時訊號。可讀性有但可交易性不足。
- 判讀（1-2 句）：維持 L3，僅存檔回顧。
- 反向驗證（反證/待確認項）：缺 Coinglass/彭博/路透即時資金流與官方公告。
- 建議動作（Follow-up）：新增 ETF flow 結構化來源後重跑。
- 評分拆解：帳號權重 11 + 關鍵字 16 + 熱度速度 5 + 跨來源 5 - 去雜訊 11 = 26

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 缺口與補件方式
1. 缺 X 即時互動增速（無法精算熱度速度）
   - 補件：接入 X watcher 或授權社群監控來源
2. Brave web_search API key 缺失
   - 補件：`openclaw configure --section web`
3. Taiwan Semi / Crypto 缺官方一手即時資料
   - 補件：IR 公告、主流通訊社即時流、ETF flow 結構化數據
