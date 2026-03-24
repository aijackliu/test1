# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 02:45
- Engine: v1（100-point scoring）
- Sources checked: Google News RSS（Reuters/CNBC/Microsoft/NVIDIA/industry media headlines）
- Constraints: X 即時互動資料未接入；`web_search` 仍不可用（Brave API key 缺失），熱度速度以「近期媒體覆蓋密度」近似。

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：The Official Microsoft Blog（2026-03-16）、NVIDIA Newsroom（2026-03-16）、Google News RSS 聚合頁（2026-03-20 抓取）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：Microsoft 與 NVIDIA 在 GTC 期間同步發布 AI 基建與 Physical AI 方案。屬官方一手來源，可信度高，但目前仍偏產品敘事，缺少新增訂單與營收傳導的即時證據。
- 判讀（1-2 句）：AI infra 主線延續，屬中高強度但未達突發型交易訊號。
- 反向驗證（反證/待確認項）：缺主流財經媒體對採購規模、毛利影響與交付節奏的量化追蹤。
- 建議動作（Follow-up）：48h 內追蹤路透/彭博是否補上企業採購與 CapEx 拆解，若有雙來源量化數據再升級。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 11 + 跨來源 9 - 去雜訊 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters（OPEC+ 增產訊號）、CNBC（同主題覆蓋）、Google News RSS 聚合頁
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 增產預期持續被主流媒體覆蓋，核心仍是供給微增訊號。屬可影響油價中樞與通膨預期的政策級題材，但尚非落地確認。
- 判讀（1-2 句）：短線偏區間震盪框架，等待會議結論與執行率證實。
- 反向驗證（反證/待確認項）：地緣衝突與實際減產紀律可能抵銷紙面增產影響。
- 建議動作（Follow-up）：追蹤 OPEC+ 正式聲明與 EIA 庫存，若出現「超預期增產/落空」再重評。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：64/100
- 等級：L2
- 來源：Reuters（中國科技競賽敘事）、Google News RSS 聚合頁
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技與產業政策方向的報導延續，對半導體鏈與地緣風險溢價有中期影響。現階段仍偏方向性框架，缺少新政策細則。
- 判讀（1-2 句）：可作配置層面的風險提示，不足以觸發短線高確信交易。
- 反向驗證（反證/待確認項）：尚未取得最新部委文件、補貼條款或執行時間表。
- 建議動作（Follow-up）：補抓中國官方公告/部委 RSS，拿到條文後重算分數。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 9 + 跨來源 8 - 去雜訊 5 = 54
- 備註：因主題關聯高，人工上調關注優先序（不改等級）

## Signal 4
- 類別：Taiwan Semi
- 熱度分：43/100
- 等級：L3
- 來源：Seeking Alpha、Tom’s Hardware、Google News RSS 聚合頁
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能瓶頸敘事持續，但主要來自評論/產業媒體，缺少台積電最新法說或公司公告的增量資訊。訊號新鮮度不足。
- 判讀（1-2 句）：暫列灰燈存檔，等待官方一手更新。
- 反向驗證（反證/待確認項）：缺 TSMC 最新產能節奏、客戶排產與 ASP 影響數字。
- 建議動作（Follow-up）：鎖定 TSMC IR、法說逐字稿與 Reuters/Bloomberg 即時稿。
- 評分拆解：帳號權重 15 + 關鍵字 20 + 熱度速度 8 + 跨來源 6 - 去雜訊 6 = 43

## Signal 5
- 類別：Crypto Flow
- 熱度分：29/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews（舊聞）、Google News RSS 聚合頁
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓到的 crypto 條目多為舊資料（2025Q4~2026Q1），且來源權重偏中低，缺當日 ETF 淨流與風險事件的一手確認。
- 判讀（1-2 句）：不具即時交易價值，先歸檔。
- 反向驗證（反證/待確認項）：需補 Coinglass/交易所公告/路透即時流量數據。
- 建議動作（Follow-up）：接入 ETF flow 結構化資料源，避免被舊聞干擾。
- 評分拆解：帳號權重 12 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 10 = 29

---

## 分級總結
- L1：0
- L2：3
- L3：2

## 缺口與補件方式
1. X/社群互動增速缺失 → 影響熱度速度精度
2. Brave API key 未配置 → `web_search` 不可用，跨來源完整度受限
3. Crypto/Taiwan Semi 缺官方一手即時數據 → 需補 IR/官方公告/API
