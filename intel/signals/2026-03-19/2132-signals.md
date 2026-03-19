# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-19 21:32
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS (aggregated), Reuters/CNBC/Microsoft/NVIDIA/industry media headlines via feed
- Constraints: `web_search` unavailable (missing Brave API key); X/社群即時互動資料缺失，熱度速度改用「近期多家媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：
  - The Official Microsoft Blog (2026-03-16)
  - NVIDIA Newsroom (2026-03-16)
  - Google News RSS 聚合頁（2026-03-19 抓取）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：Microsoft 與 NVIDIA 在 GTC 檔期同步釋出 AI 基礎設施與 Physical AI 相關方案。訊號屬於「官方發布 + 生態協同」，屬中高可信。短期偏題材擴散，仍待企業採用與訂單落地數據驗證。
- 判讀（1-2 句）：屬於「敘事強、即時財務影響未明」的 L2 訊號，可作為 AI 基建週期延續的佐證。
- 反向驗證（反證/待確認項）：缺少第三方財務指標（新增雲端營收、實際GPU交付/價格）；目前來源偏官方口徑。
- 建議動作（Follow-up）：48h 內追蹤彭博/路透對企業採購與CapEx拆解；若出現兩家以上主流媒體量化數據，考慮升級。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 11 + 跨來源 9 - 去雜訊 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：
  - Reuters（OPEC+ 增產訊號）
  - CNBC（相同主題二次報導）
  - Google News RSS 聚合頁
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 增產相關訊息由 Reuters 與 CNBC 均有覆蓋，主題為供給面微增。屬宏觀定價中樞訊號，但目前偏政策預期，不是即時供需拐點確認。
- 判讀（1-2 句）：油價短線可能偏區間震盪，能源股與通膨預期受影響但未達突發事件級別。
- 反向驗證（反證/待確認項）：需確認正式會議結果與實際執行率；地緣風險（中東）可能反向抵銷增產影響。
- 建議動作（Follow-up）：追蹤下次 OPEC+ 正式公告與 EIA 庫存；若出現「增產落空/超預期」再調等級。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：
  - Reuters（中國科技競賽與政策面）
  - Google News RSS 聚合頁
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：Reuters 針對中國科技政策與中美競爭敘事提供持續報導。此訊號偏中期政策/產業方向，對半導體鏈與地緣風險溢價有影響。
- 判讀（1-2 句）：方向性明確但交易可執行性仍弱，需等待具體政策文件與資金安排。
- 反向驗證（反證/待確認項）：目前缺少中國官方最新細則（部委公告、財政/產業補貼具體條款）。
- 建議動作（Follow-up）：增設中國官媒/部委公告 RSS；政策文本出現後再重評。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 5 = 63

## Signal 4
- 類別：Taiwan Semi
- 熱度分：55/100
- 等級：L3
- 來源：
  - Seeking Alpha（評論）
  - Tom's Hardware（產業媒體）
  - Google News RSS 聚合頁
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：TSMC CoWoS 產能瓶頸與擴產敘事持續，但目前可見來源以評論/產業媒體為主，缺少最新官方指引更新。屬熟知主題延伸，非新拐點。
- 判讀（1-2 句）：維持灰燈觀察，等待法說/公司公告級資訊再升級。
- 反向驗證（反證/待確認項）：缺台積電最新季度法說具體數字與客戶訂單節奏。
- 建議動作（Follow-up）：鎖定 TSMC IR 與主流通訊社快訊，補齊一手來源。
- 評分拆解：帳號權重 15 + 關鍵字 20 + 熱度速度 8 + 跨來源 6 - 去雜訊 6 = 43
- 備註：因主題對市場關聯高，人工上調觀察優先序（但不改等級）

## Signal 5
- 類別：Crypto Flow
- 熱度分：49/100
- 等級：L3
- 來源：
  - Bitcoin Magazine（監管/市場內容）
  - dlnews（舊聞 hack）
  - Google News RSS 聚合頁
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：當前抓到的 crypto 內容時效性偏舊（2025-11、2026-01），且來源可信度與一致性不足。缺乏當日 ETF 淨流量與交易所風險事件的權威即時確認。
- 判讀（1-2 句）：不具即時可交易訊號，先歸檔。
- 反向驗證（反證/待確認項）：需補 Coinglass/彭博/路透即時流量與官方公告。
- 建議動作（Follow-up）：新增 ETF flow API 或可信 dashboard 作為硬資料源。
- 評分拆解：帳號權重 12 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 10 = 29

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 今日缺口與補件方式
1. 缺 X 即時互動增速（無法精算熱度速度）
   - 補件：接入 X watcher 或提供已授權社群監控輸出
2. `web_search` 缺 Brave API key
   - 補件：`openclaw configure --section web` 後重跑，可提升跨來源覆蓋
3. Crypto 與 Taiwan Semi 缺官方一手即時數據
   - 補件：加入官方 IR / 主流通訊社 / ETF flow 結構化資料源
