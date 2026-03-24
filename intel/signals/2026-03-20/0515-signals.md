# Signal Engine 掃描報告
- 掃描時間：2026-03-20 05:15 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中偏低（X/關鍵帳號未直連；Reuters 主源未納入）

## 評分摘要（L1/L2/L3）
- L1：0
- L2：2
- L3：3

---

## 訊號 1
- 類別：Crypto Flow
- 熱度分：68/100
- 等級：L2
- 來源：
  - Google News RSS（多來源反映 BTC/ETH ETF 淨流出、流入中斷）
  - CoinDesk RSS（資金移動與風險偏好轉弱）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, inflow streak ends, risk-off
- 摘要（2-3 句）：
  加密市場主軸仍是 ETF 淨流出與風險偏好收斂，與前一輪相比延續性高。多條來源在同一時窗內重複出現「流入中斷/資金流出」敘事。
- 判讀（1-2 句）：
  目前是中強度風險訊號，但尚未升級到系統性拋售等級。
- 反向驗證（反證/待確認項）：
  需補 ETF 發行商官方日流量與交易所 OI 變化，避免二手媒體誤差。
- 建議動作（Follow-up）：
  持續 24h 追蹤 ETF 淨流、BTC/ETH 基差與資金費率，若三者同向惡化再升級。

## 訊號 2
- 類別：Macro / Oil
- 熱度分：65/100
- 等級：L2
- 來源：
  - Google News RSS（油價衝擊、伊朗相關供應風險、戰事干擾）
  - NYT Business RSS（先前輪次對伊朗油流與政策訊號）
- 命中關鍵字：oil shock, Iran, disruption, supply risk, OPEC
- 摘要（2-3 句）：
  油市仍在地緣風險驅動的高波動區間，市場敘事集中於供應中斷風險與價格上行尾端情境。跨來源對「風險溢價仍在」已有一致性。
- 判讀（1-2 句）：
  方向偏多波動而非單邊趨勢；尚缺高可信官方供給數據支撐 L1。
- 反向驗證（反證/待確認項）：
  需補 OPEC/EIA 即時數據與航運實際中斷證據，現有來源含評論型內容。
- 建議動作（Follow-up）：
  持續監測 Brent/WTI、中東航線保費、OPEC 官訊；若供給中斷獲一線媒體雙確認再升級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：54/100
- 等級：L3
- 來源：
  - Google News RSS（Bloomberg、Finimize、InvestingLive、低權重站混雜）
- 命中關鍵字：PBOC, USD/CNY fix, yuan, policy signal
- 摘要（2-3 句）：
  中國訊號以匯率定盤與政策解讀為主，但來源混雜且可信度落差大。雖有 Bloomberg 條目，整體仍以轉述型內容居多。
- 判讀（1-2 句）：
  目前不足以形成高置信度政策轉向判斷。
- 反向驗證（反證/待確認項）：
  缺 PBOC 原文公告與同日公開市場操作詳數。
- 建議動作（Follow-up）：
  以官方公告與一線通訊社重跑，提升帳號權重與交叉確認分數。

## 訊號 4
- 類別：AI Infra
- 熱度分：46/100
- 等級：L3
- 來源：
  - Google News RSS（Motley Fool、AOL、Tech Buzz、DCD 等）
- 命中關鍵字：NVIDIA, OpenAI, data center, AI infrastructure
- 摘要（2-3 句）：
  AI 基建話題仍熱，但本輪多為投資評論與二手媒體，缺官方公告級新事件。可讀性高、可執行性低。
- 判讀（1-2 句）：
  熱度存在，信噪比不足，不宜升級。
- 反向驗證（反證/待確認項）：
  缺公司 IR、監管揭露、一線記者獨立核證。
- 建議動作（Follow-up）：
  後續切換到公司公告/法說稿/Reuters-Bloomberg 交叉源。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：28/100
- 等級：L3
- 來源：
  - Google News RSS（查詢結果空白，無有效條目）
- 命中關鍵字：TSMC, UMC, VIS, foundry
- 摘要（2-3 句）：
  本輪在嚴格 `when:1d` 條件下未抓到台灣晶圓代工有效新聞，資料缺口明顯。
- 判讀（1-2 句）：
  無法形成判斷，僅記錄為「低可得性」。
- 反向驗證（反證/待確認項）：
  待補台灣本地財經媒體、公司公告與交易所即時訊息。
- 建議動作（Follow-up）：
  放寬檢索語法並加入繁中來源（經濟日報、工商時報、公司 IR）。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」）。
- 主要可執行風險在 L2：
  1) Crypto ETF 資金流轉弱
  2) Oil 地緣風險溢價延續
- 缺口：X 關鍵帳號、Reuters 主源、Taiwan Semi 當日有效條目。