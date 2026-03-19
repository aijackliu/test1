# Intel Signal Engine Scan
- Scan time (Asia/Taipei): 2026-03-19 21:45
- Engine: v1 (100-point scoring)
- Data sources checked: Google News RSS 聚合（Reuters/CNBC/Microsoft/NVIDIA/產業媒體）
- Constraints: X 即時互動資料缺失；`web_search`（Brave API）未配置，熱度速度以「近期跨媒體覆蓋密度」近似

## Signal 1
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：The Official Microsoft Blog、NVIDIA Newsroom、Google News RSS
- 命中關鍵字：NVIDIA、Azure AI infrastructure、Physical AI、data factory、robotics
- 摘要（2-3 句）：GTC 週期內，Microsoft 與 NVIDIA 同步發布 AI 基建與 Physical AI 方案。屬官方高可信來源，顯示生態加速整合，但短期仍偏敘事層強化。缺少可量化的新增訂單與交付節奏數據。
- 判讀（1-2 句）：AI 基建主線維持強勢，屬可追蹤但未達紅色警報。
- 反向驗證（反證/待確認項）：需第三方媒體補充 CapEx/採購數據，避免只看官方口徑。
- 建議動作（Follow-up）：48h 追蹤 Reuters/Bloomberg 是否出現企業客戶、出貨或毛利影響數字。
- 評分拆解：帳號權重 26 + 關鍵字 22 + 熱度速度 11 + 跨來源 9 - 去雜訊 6 = 74

## Signal 2
- 類別：Macro / Oil
- 熱度分：69/100
- 等級：L2
- 來源：Reuters、CNBC、Google News RSS
- 命中關鍵字：OPEC+、oil output increase、Brent crude、supply
- 摘要（2-3 句）：OPEC+ 小幅增產敘事由 Reuters 與 CNBC 重複覆蓋，供給端預期偏鬆。當前仍是政策訊號與預期交易階段，尚非已確認的供需再平衡。
- 判讀（1-2 句）：短線對油價偏壓抑，但地緣事件可快速反轉。
- 反向驗證（反證/待確認項）：等待正式會議結論與執行率資料；同步追蹤庫存與運輸風險。
- 建議動作（Follow-up）：跟進下一次 OPEC+ 官宣與 EIA 週報，若「增產不及預期」可上修等級。
- 評分拆解：帳號權重 25 + 關鍵字 20 + 熱度速度 10 + 跨來源 10 - 去雜訊 4 = 69

## Signal 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：Reuters、Google News RSS
- 命中關鍵字：China、tech race、policy、semiconductor、AI
- 摘要（2-3 句）：中國科技競賽與政策導向持續被主流媒體關注，方向上偏中長期結構訊號。對半導體供應鏈與風險溢價有潛在影響，但缺乏當日新增政策細則。
- 判讀（1-2 句）：策略面有意義，交易面仍需等待明確政策落地。
- 反向驗證（反證/待確認項）：目前缺部委級公告、補貼細則與資金規模。
- 建議動作（Follow-up）：加掛中國官方公告源（工信部/國務院）後重評。
- 評分拆解：帳號權重 24 + 關鍵字 18 + 熱度速度 8 + 跨來源 8 - 去雜訊 5 = 63

## Signal 4
- 類別：Taiwan Semi
- 熱度分：55/100
- 等級：L3
- 來源：Seeking Alpha、Tom's Hardware、Google News RSS
- 命中關鍵字：TSMC、CoWoS、advanced packaging、capacity
- 摘要（2-3 句）：CoWoS 產能瓶頸與擴產敘事延續，但可用資訊多為評論/產業媒體，時效與一手性不足。暫無新官方指引可證明趨勢再加速。
- 判讀（1-2 句）：維持灰燈，待法說/公司公告更新。
- 反向驗證（反證/待確認項）：缺台積電最新季度產能與客戶拉貨節奏數據。
- 建議動作（Follow-up）：鎖定 TSMC IR、Reuters、Bloomberg 快訊。
- 評分拆解：帳號權重 15 + 關鍵字 20 + 熱度速度 8 + 跨來源 6 - 去雜訊 6 = 43（觀察優先序上調，不改等級）

## Signal 5
- 類別：Crypto Flow
- 熱度分：49/100
- 等級：L3
- 來源：Bitcoin Magazine、dlnews、Google News RSS
- 命中關鍵字：Bitcoin ETF、crypto futures、exchange hack
- 摘要（2-3 句）：目前抓到的 crypto 條目時效性偏舊，且來源品質參差。缺乏當日 ETF 淨流與交易所風險事件的一手權威確認。
- 判讀（1-2 句）：不構成可執行即時訊號。
- 反向驗證（反證/待確認項）：需 Coinglass/彭博/路透與官方公告交叉確認。
- 建議動作（Follow-up）：接入 ETF flow 結構化資料源，降低舊聞誤判。
- 評分拆解：帳號權重 12 + 關鍵字 16 + 熱度速度 6 + 跨來源 5 - 去雜訊 10 = 29

---

## 分級總結
- L1：0
- L2：3
- L3：2

## 缺口與補件方式
1. 缺 X/社群即時增速數據 → 補接 watcher 或授權抓取輸出
2. Brave API key 未配置 → `openclaw configure --section web` 後可擴大跨來源驗證
3. Taiwan Semi/Crypto 缺一手即時數據 → 加入公司 IR 與 ETF flow/API 資料源