# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-19 22:45
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS（含 Reuters/CNBC/Microsoft/NVIDIA/產業媒體）
- Constraints: X 即時互動資料未接入；`web_search` 仍不可用（缺 Brave API key），熱度速度以「近時段媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：The Official Microsoft Blog、NVIDIA Newsroom、Google News RSS 聚合
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：Microsoft 與 NVIDIA 在 GTC 檔期延續釋出 AI 基建與 Physical AI 方案，屬官方高可信發布。訊號顯示供給側敘事持續偏強，但仍偏「產品/平台發布」而非財報級拐點。
- 判讀（1-2 句）：維持 L2；偏中期正向敘事，短期交易性需等待訂單/CapEx落地數據。
- 反向驗證（反證/待確認項）：缺第三方營收增量與GPU交付節奏驗證。
- 建議動作（Follow-up）：追蹤 Reuters/Bloomberg 是否補充企業採購規模與雲端資本開支拆解。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 11 + 跨來源 9 - 去雜訊 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS 聚合
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 小幅增產相關訊號持續被 Reuters/CNBC 覆蓋，供給面預期未出現新突發。此類訊號對能源與通膨預期有影響，但現階段仍是政策預期交易。
- 判讀（1-2 句）：維持 L2；偏「有方向但無新催化」狀態。
- 反向驗證（反證/待確認項）：需後續確認正式會議決議與執行率；地緣風險可能抵銷增產效應。
- 建議動作（Follow-up）：追蹤 OPEC+ 正式公告與 EIA 庫存，若出現超預期偏差再升降級。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：Reuters、Google News RSS 聚合
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技競爭與政策方向仍在主流媒體敘事中，屬中期產業風險溢價因子。對半導體鏈與地緣敏感資產有持續影響。
- 判讀（1-2 句）：方向性明確但缺新政策細則，交易可執行性有限。
- 反向驗證（反證/待確認項）：待中國官方部委公告與財政配套細節。
- 建議動作（Follow-up）：補接中國官方公告源（發改委/工信部）後重評。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 6 = 62

## Signal 4
- 類別：Taiwan Semi
- 熱度分：47/100
- 等級：L3
- 來源：Seeking Alpha、Tom's Hardware、tastylive、Google News RSS 聚合
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：TSMC CoWoS/先進封裝題材延續，但主要來源仍為評論與二手媒體，缺官方最新數字更新。內容偏舊聞再敘事。
- 判讀（1-2 句）：維持 L3 存檔觀察，暫不視為新拐點。
- 反向驗證（反證/待確認項）：待法說/IR公告提供產能與客戶訂單實證。
- 建議動作（Follow-up）：重點監控台積電 IR 與一線通訊社即時稿。
- 評分拆解：帳號權重 14 + 關鍵字 19 + 熱度速度 8 + 跨來源 7 - 去雜訊 11 = 37

## Signal 5
- 類別：Crypto Flow
- 熱度分：45/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS 聚合
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：抓取到的 crypto 訊號多為舊聞（2025Q4~2026Q1），且缺即時 ETF 淨流/交易所風險事件一手數據。訊號時效與可信交叉不足。
- 判讀（1-2 句）：不具當下執行價值，先歸檔。
- 反向驗證（反證/待確認項）：需 Coinglass/主流媒體/官方公告三方同步。
- 建議動作（Follow-up）：加接 ETF flow 結構化 API 與交易所官方公告源。
- 評分拆解：帳號權重 11 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 12 = 26

---

## 分級總結
- L1：0
- L2：3（AI Infra / Macro-Oil / Chinese Signal）
- L3：2（Taiwan Semi / Crypto Flow）

## 缺口與補件
1) 缺 X 即時互動增速資料（影響熱度速度精準度）
2) `web_search` 缺 Brave API key（影響跨來源覆蓋）
3) Taiwan Semi/Crypto 缺官方一手即時資料（IR/ETF flow/官方公告）
