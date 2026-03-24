# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-20 03:45
- Engine: v1 (100-point scoring)
- Inputs checked: Google News RSS（AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal）
- Constraints:
  - X 即時互動資料不可得（熱度速度以「近期媒體覆蓋密度」替代）
  - `web_search` 仍不可用（Brave API key 缺失）

## Signal 1
- 類別：Macro / Oil
- 熱度分：77/100
- 等級：L2
- 來源：CNBC、NYTimes、OilPrice（同主題聚合）
- 命中關鍵字：OPEC+、oil output、Brent crude、Iran conflict
- 摘要（2-3 句）：OPEC+ 增產預期與中東衝突風險同時出現，形成供給增加 vs 風險溢價拉扯。多來源有一致主題，但仍以媒體報導為主，缺正式會議落地細節。
- 判讀（1-2 句）：這是高關聯但未定案的宏觀訊號，足以維持 L2 警戒，尚未達 L1。
- 反向驗證（反證/待確認項）：需官方公告與實際執行率；若地緣升級，增產影響可能被抵銷。
- 建議動作（Follow-up）：追蹤下一次 OPEC+ 正式決議與EIA庫存資料。
- 評分拆解：帳號權重 22 + 關鍵字 23 + 熱度速度 13 + 跨來源 12 - 去雜訊 7 = 63
- 註：因跨主題衝突性高，人工風險優先序上調（不改分級）

## Signal 2
- 類別：AI Infra
- 熱度分：71/100
- 等級：L2
- 來源：VentureBeat、Microsoft/Azure 既有發布、Google News 聚合
- 命中關鍵字：NVIDIA、AI platform、Azure、OpenAI、Anthropic
- 摘要（2-3 句）：AI 基建敘事延續，重點仍在 NVIDIA 新平台與雲端生態協作。訊號偏產業敘事擴散，真實財務影響需由訂單/CapEx佐證。
- 判讀（1-2 句）：屬「題材強、硬數據弱」的標準 L2。
- 反向驗證（反證/待確認項）：缺主流通訊社最新企業採購量化數據與交付節奏。
- 建議動作（Follow-up）：補抓 Reuters/Bloomberg 對 hyperscaler 資本開支拆解。
- 評分拆解：帳號權重 19 + 關鍵字 22 + 熱度速度 12 + 跨來源 10 - 去雜訊 8 = 55

## Signal 3
- 類別：Chinese Signal
- 熱度分：66/100
- 等級：L2
- 來源：Reuters、DW、Google News 聚合
- 命中關鍵字：China、policy、tech race、semiconductor、five-year plan
- 摘要（2-3 句）：中國科技與政策方向訊號持續，但多為政策框架層面，交易層可執行性仍有限。Reuters 提供較高可信背景，但缺最新部委細則。
- 判讀（1-2 句）：中期方向明確、短期落地不明，維持 L2。
- 反向驗證（反證/待確認項）：需官方文件與資金配置細節。
- 建議動作（Follow-up）：接入中國官方公告源後再做升降級。
- 評分拆解：帳號權重 23 + 關鍵字 19 + 熱度速度 9 + 跨來源 9 - 去雜訊 6 = 54

## Signal 4
- 類別：Taiwan Semi
- 熱度分：52/100
- 等級：L3
- 來源：Seeking Alpha、Tom's Hardware、DigiTimes（聚合）
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 供需緊張敘事持續，但多為舊文與評論型來源。尚未看到新一輪官方指引更新。
- 判讀（1-2 句）：可持續觀察但非新拐點，維持 L3。
- 反向驗證（反證/待確認項）：需台積電IR/法說一手數據。
- 建議動作（Follow-up）：鎖定 TSMC 官方公告及一線通訊社快訊。
- 評分拆解：帳號權重 14 + 關鍵字 21 + 熱度速度 8 + 跨來源 7 - 去雜訊 8 = 42

## Signal 5
- 類別：Crypto Flow
- 熱度分：41/100
- 等級：L3
- 來源：Ledger、TradingView、CryptoSlate（多為舊文/回顧）
- 命中關鍵字：Bitcoin ETF、crypto hack、flows
- 摘要（2-3 句）：抓到內容大多非即時（2025 回顧型），缺少當日 ETF 淨流與交易所事件一手確認。訊號時效性與可信度不足。
- 判讀（1-2 句）：不具可執行性，歸檔處理。
- 反向驗證（反證/待確認項）：需即時 ETF flow（例如官方/主流數據平台）與交易所公告。
- 建議動作（Follow-up）：接入結構化 flow 資料源後重跑。
- 評分拆解：帳號權重 10 + 關鍵字 15 + 熱度速度 6 + 跨來源 6 - 去雜訊 11 = 26

---

## 分級總結
- L1：0
- L2：3（Macro/Oil、AI Infra、Chinese Signal）
- L3：2（Taiwan Semi、Crypto Flow）

## 結論
本輪**無 L1 訊號**。

## 缺口與補件
1. 缺 X/社群即時互動增速資料 → 補接 watcher 或授權社群監控輸出
2. `web_search` 缺 Brave API key → `openclaw configure --section web`
3. Crypto/Taiwan Semi 缺官方一手更新 → 補官方IR、通訊社與結構化數據源
