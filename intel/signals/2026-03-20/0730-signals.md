# Signal Engine 掃描報告
- 掃描時間：2026-03-20 07:30 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS（主）、前輪交叉基線（CoinDesk/NYT）
- 資料可得性：中偏低（X 關鍵帳號未直連；Brave API key 仍缺；台灣半導體 24h 幾乎無高品質新源）

## 評分摘要（L1/L2/L3）
- L1：0
- L2：3
- L3：2

---

## 訊號 1
- 類別：Macro / Oil
- 熱度分：78/100
- 等級：L2
- 來源：
  - Google News RSS（Reuters 經 Investing.com 轉載：美以-伊朗衝突導致油氣擾動）
  - Google News RSS（多家媒體：Hormuz 擾動、伊拉克減產、油價衝擊）
- 命中關鍵字：oil shock, Iran, Hormuz, disruption, production cut, OPEC
- 摘要（2-3 句）：
  油市仍由地緣風險主導，供應擾動敘事持續擴散，並出現產量下修與運輸路徑重配訊號。來源數量增加，但高權重一手公告仍有限。
- 判讀（1-2 句）：
  接近 L1 門檻，但「跨來源獨立一手確認」仍不足，暫維持 L2 高位。
- 反向驗證（反證/待確認項）：
  缺 OPEC 官方即時口徑與 EIA/IEA 最新庫存/出口核對。
- 建議動作（Follow-up）：
  建立 48h 事件追蹤；若再獲 2 家 Tier1 媒體獨立確認供應中斷規模，升級 L1。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：67/100
- 等級：L2
- 來源：
  - Google News RSS（多源重複：BTC/ETH ETF 流入中斷、約 2.19 億美元淨流出）
  - 前輪 CoinDesk 基線（風險資產與油價波動耦合）
- 命中關鍵字：ETF outflow, bitcoin, ethereum, risk-off, volatility
- 摘要（2-3 句）：
  加密 ETF 資金面由淨流入轉為淨流出，且新聞聚焦「趨勢中斷」。價格與宏觀風險資產波動關聯上升。
- 判讀（1-2 句）：
  目前是風險偏好收縮訊號，若連續兩個交易窗維持淨流出，將提高級別。
- 反向驗證（反證/待確認項）：
  需補發行商與交易所官方 flow 明細，避免低權重站點重複引用造成放大。
- 建議動作（Follow-up）：
  以 24h/48h 滾動表追蹤 BTC 與 ETH 各自流量與 OI 變化，確認是否進入結構性 risk-off。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：
  - Google News RSS（Bloomberg：人民幣/利率市場對政策預期調整）
  - Google News RSS（PBOC fix 與人民幣短線波動相關報導）
- 命中關鍵字：PBOC, USD/CNY fixing, yuan, easing expectation, China rates
- 摘要（2-3 句）：
  市場對中國政策寬鬆預期出現再定價，人民幣與利率敘事轉向「節奏管理」而非強刺激。屬政策預期層面的變化，不是明確落地事件。
- 判讀（1-2 句）：
  偏中性偏警戒，短線影響在 FX/利率，對風險資產傳導仍待觀察。
- 反向驗證（反證/待確認項）：
  需補 PBOC 正式公告與量化操作規模（OMO/MLF）才能判定強度。
- 建議動作（Follow-up）：
  監看 USD/CNY、CNH-CNY 價差與中國利率曲線變化，必要時做級別重評。

## 訊號 4
- 類別：AI Infra
- 熱度分：43/100
- 等級：L3
- 來源：
  - Google News RSS（多為投資評論站與低可信技術部落格）
- 命中關鍵字：NVIDIA, OpenAI, AI infrastructure, data center
- 摘要（2-3 句）：
  AI 基建話題量高但來源品質偏低，缺乏官方公告、財報補充或監管文件的新增證據。多為二手評論與標題再包裝。
- 判讀（1-2 句）：
  熱度不等於可交易訊號，暫列觀察。
- 反向驗證（反證/待確認項）：
  尚無 Tier1 一手交叉確認。
- 建議動作（Follow-up）：
  後續僅納入 Reuters/Bloomberg/公司 IR 後再重評。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：35/100
- 等級：L3
- 來源：
  - Google News RSS（本輪 query 幾乎無有效新條目）
- 命中關鍵字：TSMC, UMC, VIS, foundry
- 摘要（2-3 句）：
  台灣晶圓代工主題在 24h 內有效訊號稀缺，資料面不足以形成新判斷。
- 判讀（1-2 句）：
  目前僅能維持中性存檔，不宜推導方向。
- 反向驗證（反證/待確認項）：
  缺公司 IR、法說更新或一線財經媒體新事件。
- 建議動作（Follow-up）：
  下一輪改走公司公告與交易所揭露為主來源補件。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」）。
- 最接近 L1：Macro/Oil（78 分），需補 Tier1 一手來源與官方數據確認。
