# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 03:15
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS 聚合（Reuters/CNBC/Microsoft/NVIDIA/產業媒體）
- Constraints: `web_search`（Brave API）不可用；X 即時互動資料缺失，熱度速度以「近期媒體覆蓋密度」近似
- Note: 本輪主要來源與前一輪高度重疊（cached feed），未見明顯新增高衝擊事件

## Signal 1
- 類別：AI Infra
- 熱度分：73/100
- 等級：L2
- 來源：The Official Microsoft Blog、NVIDIA Newsroom、Google News RSS
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：GTC 檔期的 Microsoft + NVIDIA 官方發布仍為主導訊號，屬「高可信、偏敘事推進」。目前尚未看到新一輪第三方財務量化驗證，因此仍維持 L2。
- 判讀（1-2 句）：AI 基建主軸延續，但暫無升級為突發交易級事件。
- 反向驗證（反證/待確認項）：缺新增 CapEx/訂單落地指標、缺主流媒體最新追蹤數據。
- 建議動作（Follow-up）：等候 Reuters/Bloomberg 對採購與交付節奏補充；有量化數據再重評。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 10 + 跨來源 9 - 去雜訊 6 = 73

## Signal 2
- 類別：Macro / Oil
- 熱度分：68/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 增產預期仍是油市核心敘事，且有跨來源確認。惟訊息仍偏「政策/預期」層，不是最新已落地供給轉折。
- 判讀（1-2 句）：維持中度風險監控，偏宏觀定價調整而非黑天鵝。
- 反向驗證（反證/待確認項）：需正式會議結果、執行率與地緣風險變化共同驗證。
- 建議動作（Follow-up）：追下一次 OPEC+ 正式公告與 EIA 庫存。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 9 + 跨來源 10 - 去雜訊 4 = 68

## Signal 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技戰略與政策方向訊號持續，但仍偏中期敘事，缺當日可執行的新增政策細則。對半導體鏈估值與風險溢價有背景影響。
- 判讀（1-2 句）：方向有，但交易觸發器不足，維持 L2。
- 反向驗證（反證/待確認項）：缺部委公告細節與財政支持條款。
- 建議動作（Follow-up）：補接官方政策來源（部委/官媒）後再評分。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 6 = 62

## Signal 4
- 類別：Taiwan Semi
- 熱度分：54/100
- 等級：L3
- 來源：Seeking Alpha、Tom’s Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能議題仍在，但多為評論/二級媒體延續，未見台積電新官方指引。屬「舊主題延伸」非新拐點。
- 判讀（1-2 句）：維持灰燈觀察。
- 反向驗證（反證/待確認項）：缺法說最新數據、客戶拉貨節奏。
- 建議動作（Follow-up）：鎖定 TSMC IR 與一線通訊社。
- 評分拆解：帳號權重 15 + 關鍵字 20 + 熱度速度 8 + 跨來源 6 - 去雜訊 7 = 42

## Signal 5
- 類別：Crypto Flow
- 熱度分：47/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：本輪抓到的 crypto 條目時效偏舊，且來源權威性與一致性不足。缺 ETF 即時淨流與大型交易所官方公告。
- 判讀（1-2 句）：不構成即時信號，歸檔。
- 反向驗證（反證/待確認項）：需 Coinglass/彭博/路透等即時結構化資料。
- 建議動作（Follow-up）：接入 ETF flow API 與交易所公告監控。
- 評分拆解：帳號權重 12 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 11 = 28

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 今日缺口與補件方式
1. 缺 X 即時互動增速資料（熱度速度只能近似）
2. `web_search` 無 Brave API key（跨來源覆蓋受限）
3. Crypto / Taiwan Semi 缺一手即時數據（IR、ETF flow、官方公告）