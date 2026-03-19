# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-19 22:30
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS（Reuters/CNBC/Microsoft/NVIDIA/產業媒體聚合）
- Constraints: `web_search` 仍不可用（Brave API key 缺失）；X 即時互動數據缺失，熱度速度以媒體覆蓋密度近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Microsoft Official Blog（2026-03-16）、NVIDIA Newsroom（2026-03-16）、Google News RSS（2026-03-19 22:30 抓取）
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：GTC 檔期中 Microsoft 與 NVIDIA 同步釋出 AI 基建與 Physical AI 方案，來源屬官方高可信。訊號偏「敘事擴張」而非即時財務落地，仍需第三方營收與採購證據。
- 判讀（1-2 句）：維持 L2，代表題材延續但尚非事件驅動拐點。
- 反向驗證（反證/待確認項）：缺少雲端訂單、GPU 交付與 CapEx 實測數字。
- 建議動作（Follow-up）：追蹤 Reuters/Bloomberg 是否出現企業採購量化資訊。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 11 + 跨來源 9 - 去雜訊 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters（OPEC+ 增產訊號）、CNBC（二次確認）、Google News RSS
- 命中關鍵字：OPEC+、oil output、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 供給微增預期持續被主流媒體引用，構成宏觀價格區間影響。訊號有效但仍屬政策預期，未見最新正式決議更新。
- 判讀（1-2 句）：短線偏區間震盪，尚未升級為突發級別。
- 反向驗證（反證/待確認項）：需會議決議與執行率落地，另受中東地緣風險反向擾動。
- 建議動作（Follow-up）：跟進正式公報與 EIA 庫存資料。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：Reuters（中國科技競賽與政策敘事）、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技政策與中美競逐敘事持續，對半導體鏈估值折溢價具中期影響。可見度高但可交易細節仍不足。
- 判讀（1-2 句）：方向明確、執行性偏弱，暫留 L2。
- 反向驗證（反證/待確認項）：缺最新部委正式條文與資金配置細則。
- 建議動作（Follow-up）：補中國官方公告源後重評。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 5 = 63

## Signal 4
- 類別：Taiwan Semi
- 熱度分：55/100
- 等級：L3
- 來源：Seeking Alpha、Tom’s Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能緊張敘事延續，但主要來自評論與產業媒體，缺台積電最新一手指引。屬舊主題延伸而非新拐點。
- 判讀（1-2 句）：維持 L3 觀察。
- 反向驗證（反證/待確認項）：缺法說/IR 即時數字與客戶拉貨節奏。
- 建議動作（Follow-up）：等待 TSMC IR/主流通訊社一手訊號。
- 評分拆解：帳號權重 15 + 關鍵字 20 + 熱度速度 8 + 跨來源 6 - 去雜訊 6 = 43（市場關聯高，僅提高觀察優先級）

## Signal 5
- 類別：Crypto Flow
- 熱度分：49/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews（舊聞）、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：本輪抓取內容時效性偏舊，且來源權威性不夠集中。未取得當日 ETF 淨流與交易所風險的權威即時資料。
- 判讀（1-2 句）：不具即時交易價值，維持歸檔。
- 反向驗證（反證/待確認項）：需補 Coinglass/彭博/路透或官方公告。
- 建議動作（Follow-up）：接入 ETF flow 結構化資料源後再評分。
- 評分拆解：帳號權重 12 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 10 = 29

---

## 分級總結
- L1：0
- L2：3
- L3：2

## 缺口與補件方式
1. 缺 X 即時互動增速 → 接入 X watcher/API
2. `web_search` 不可用 → 補 Brave API key (`openclaw configure --section web`)
3. Taiwan Semi / Crypto 缺一手硬資料 → 補 IR + 通訊社 + ETF flow API
