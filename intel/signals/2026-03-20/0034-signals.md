# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 00:34
- Engine: v1（100-point scoring）
- Data sources checked: Google News RSS（aggregated）
- Constraints: X/關鍵帳號即時互動資料缺失；`web_search` 不可用（Brave API key 未配置）

## Signal 1
- 類別：AI Infra
- 熱度分：76/100
- 等級：L2
- 來源：
  - The Official Microsoft Blog（2026-03-16）
  - NVIDIA Newsroom（2026-03-16）
  - VentureBeat / Google News RSS 聚合（2026-03-19 更新）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、Vera Rubin、OpenAI、Anthropic、Meta
- 摘要（2-3 句）：GTC 檔期相關 AI 基建訊號延續，Microsoft 與 NVIDIA 仍是核心官方訊號來源。新增媒體面提及 NVIDIA Vera Rubin 平台與主要模型公司生態協作。市場敘事偏強，但尚缺實際出貨/採購量化驗證。
- 判讀（1-2 句）：屬高可信但偏「主題延續」，可維持 L2 追蹤，不足以升 L1。
- 反向驗證（反證/待確認項）：需補第三方財報/法說中的 CapEx、GPU 交付與利用率數據。
- 建議動作（Follow-up）：48h 內追蹤 Reuters/Bloomberg 是否出現量化數據與訂單驗證。
- 評分拆解：帳號權重 27 + 關鍵字 23 + 熱度速度 11 + 跨來源 9 - 去雜訊 4 = 76

## Signal 2
- 類別：Macro / Oil
- 熱度分：68/100
- 等級：L2
- 來源：
  - Reuters（OPEC+ 增產訊號）
  - CNBC（二次確認）
  - Google News RSS 聚合
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 小幅增產的既有訊號持續被主流媒體引用，屬供給面中樞訊號。由於事件時效偏舊（2 月底到 3 月初），當下更偏存量定價，而非新突發衝擊。
- 判讀（1-2 句）：維持 L2，不屬今晚新觸發風險事件。
- 反向驗證（反證/待確認項）：需正式會議執行率與最新庫存數據，否則訊號邊際效應下降。
- 建議動作（Follow-up）：對齊下次 OPEC+ 公告與 EIA 週報後再重評。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 8 + 跨來源 10 - 去雜訊 5 = 68

## Signal 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：
  - Reuters（中國科技競爭與政策敘事）
  - Google News RSS 聚合
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技政策與中美競爭仍是中期主線，Reuters 提供高可信概覽。現階段多為方向性訊號，非具體新政策落地細則。
- 判讀（1-2 句）：可列入中期監控，短期交易信號強度一般。
- 反向驗證（反證/待確認項）：缺中國部委最新原文公告與量化財政支持細節。
- 建議動作（Follow-up）：新增官媒/部委公報 RSS，待硬訊號再評級。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 7 + 跨來源 8 - 去雜訊 5 = 62

## Signal 4
- 類別：Taiwan Semi
- 熱度分：47/100
- 等級：L3
- 來源：
  - Seeking Alpha（評論）
  - Tom's Hardware（產業媒體）
  - Google News RSS 聚合
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：TSMC CoWoS 擴產與瓶頸敘事仍在，但主要來源偏評論與二手媒體，且時效偏舊。缺乏新一手公司公告。
- 判讀（1-2 句）：屬已知敘事重複，維持 L3。
- 反向驗證（反證/待確認項）：需補 TSMC IR/法說最新數字與客戶拉貨節奏。
- 建議動作（Follow-up）：關注台積電官網 IR 與主要通訊社快訊。
- 評分拆解：帳號權重 14 + 關鍵字 19 + 熱度速度 7 + 跨來源 6 - 去雜訊 9 = 37

## Signal 5
- 類別：Crypto Flow
- 熱度分：41/100
- 等級：L3
- 來源：
  - Bitcoin Magazine（監管題）
  - dlnews / CoinDesk（多為舊聞）
  - Google News RSS 聚合
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓到的 crypto 內容大多不是當日新訊，且來源品質與時效性不一致。缺 ETF 當日淨流量與交易所安全事件的一手即時確認。
- 判讀（1-2 句）：暫不構成可執行訊號，歸檔。
- 反向驗證（反證/待確認項）：需 Coinglass/主流通訊社/交易所官方公告三方交叉。
- 建議動作（Follow-up）：補結構化 ETF flow 與鏈上告警來源。
- 評分拆解：帳號權重 11 + 關鍵字 15 + 熱度速度 5 + 跨來源 5 - 去雜訊 11 = 25

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 缺口與補件方式
1. 缺 X 即時互動增速（無法精算熱度速度）
   - 補件：接入 X watcher 輸出（互動增速、轉推曲線）
2. `web_search` 無法使用（缺 API key）
   - 補件：`openclaw configure --section web`
3. 缺 Taiwan Semi/Crypto 的當日一手硬資料
   - 補件：接入官方 IR、ETF flow API、主流通訊社即時線
