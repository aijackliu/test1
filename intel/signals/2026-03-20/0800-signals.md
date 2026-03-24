# Signal Engine 掃描報告
- 掃描時間：2026-03-20 08:00 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中偏低（X 直接來源缺失；高權重來源比例不足）

## 評分摘要（L1/L2/L3）
- L1：0
- L2：2
- L3：3

---

## 訊號 1
- 類別：Macro / Oil
- 熱度分：74/100
- 等級：L2
- 來源：
  - NYT Business RSS（Iranian oil sanctions / supply policy）
  - Google News RSS（HBR / TradingView / 多家油價波動相關報導）
- 命中關鍵字：oil, Iran, Hormuz, sanctions, supply, price volatility
- 摘要（2-3 句）：
  油市延續地緣政治驅動的高波動狀態，且「供給增加預期」與「航道/制裁風險」同時存在。跨來源對油價劇烈波動的敘事一致，但方向性仍分歧。
- 判讀（1-2 句）：
  這是高風險但未定向訊號，偏事件交易而非中期趨勢確認。
- 反向驗證（反證/待確認項）：
  需補 OPEC 官方產量更新與 EIA 即時庫存/出貨數據，避免評論型媒體放大。
- 建議動作（Follow-up）：
  追蹤 24-48h Brent/WTI、運費保費、OPEC 聲明；若再出現官方供應中斷證據則升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：63/100
- 等級：L2
- 來源：
  - Google News RSS（The Block：BTC/ETH ETF 轉為合計淨流出）
  - Google News RSS（多來源對 ETF flow 分歧敘事）
- 命中關鍵字：bitcoin, ethereum, ETF flows, outflows, risk-off
- 摘要（2-3 句）：
  ETF 資金流訊號呈現分歧：有來源稱延續流入，也有來源確認近期淨流出與風險偏好降溫。整體偏向「高波動＋資金轉弱」但尚未形成單邊共識。
- 判讀（1-2 句）：
  目前為黃燈，需等待官方 fund flow 資料確認方向。
- 反向驗證（反證/待確認項）：
  缺發行商/交易所官方日度流量表；現有報導含低權重站點。
- 建議動作（Follow-up）：
  建立 BTC/ETH ETF 日度對照表；若連續兩日淨流出擴大再升級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：57/100
- 等級：L3
- 來源：
  - Google News RSS（Bloomberg：人民幣長期看法）
  - Google News RSS（China Daily / Finimize / 其他轉述）
- 命中關鍵字：PBOC, yuan fixing, easing, China economy
- 摘要（2-3 句）：
  人民幣與政策寬鬆訊號持續出現，但多為市場解讀與轉述稿。政策口徑偏穩定與寬鬆傾向，惟缺乏硬落地工具細節。
- 判讀（1-2 句）：
  屬於觀察層級，暫不構成交易級強訊號。
- 反向驗證（反證/待確認項）：
  缺 PBOC 官方操作規模與社融/信貸更新交叉確認。
- 建議動作（Follow-up）：
  追蹤官方公告與匯率波動區間；資料補齊後重評。

## 訊號 4
- 類別：AI Infra
- 熱度分：46/100
- 等級：L3
- 來源：
  - Google News RSS（HPCwire / Motley Fool / AOL / Tech blog 混合）
- 命中關鍵字：NVIDIA, OpenAI, AI infrastructure, data center
- 摘要（2-3 句）：
  AI 基建題材熱度高，但本輪來源多為評論與二手站點，官方公告密度偏低。短時熱度存在，可信度結構不足。
- 判讀（1-2 句）：
  不足以形成 L2 以上行動信號。
- 反向驗證（反證/待確認項）：
  缺一線媒體與公司公告雙確認。
- 建議動作（Follow-up）：
  下輪優先抓取公司 IR、監管文件與 Reuters/Bloomberg 直源。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：35/100
- 等級：L3
- 來源：
  - Google News RSS（單一低權重條目：台灣晶片優勢背景文）
- 命中關鍵字：Taiwan chip dominance, semiconductor
- 摘要（2-3 句）：
  本輪台灣半導體直接可行情報不足，且未見 TSMC/UMC/VIS 近 24h 關鍵事件級資訊。
- 判讀（1-2 句）：
  屬資料不足，不做延伸判斷。
- 反向驗證（反證/待確認項）：
  缺公司公告、法說重點、供應鏈即時消息。
- 建議動作（Follow-up）：
  改走公司 IR 與交易所公告源重跑。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」門檻）。
- 主要風險主軸仍為 Oil/Geo 事件驅動，Crypto 次之。
- 缺口：
  1) X/關鍵帳號直連訊號
  2) Reuters/官方統計直源覆核
  3) Brave Search API key（目前不可用）
