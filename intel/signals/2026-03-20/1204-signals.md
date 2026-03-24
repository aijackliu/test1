# Signal Engine 掃描報告
- 掃描時間：2026-03-20 12:04 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中（X 直接訊號未覆蓋；Brave Search API 仍缺 key）

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
  - Reuters（Goldman 指出近端至 2027 油價上行風險）
  - NYT Business（亞洲航油供應緊張與出口限制）
  - Google News RSS（多家媒體同步討論油價衝擊）
- 命中關鍵字：oil shock, jet fuel shortage, Iran, supply risk, OPEC, price upside
- 摘要（2-3 句）：
  油市訊號持續惡化，從「地緣風險」擴散到「成品油供應鏈緊張」，已對亞洲航空燃料形成壓力。Reuters 與 NYT 同時提供主流來源背書，顯示風險由敘事走向實體供需。
- 判讀（1-2 句）：
  目前接近 L1 門檻，但尚缺官方產量/運輸中斷的硬數據同步確認。
- 反向驗證（反證/待確認項）：
  需補 EIA/IEA 庫存、OPEC 實際出口與運費/保險數據，確認是否為短期恐慌溢價。
- 建議動作（Follow-up）：
  建立 48h 追蹤：Brent/WTI、航油 crack spread、航運保費；若再出現 2 個一線來源確認供應中斷則升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：69/100
- 等級：L2
- 來源：
  - The Block（BTC/ETH ETF 合計約 2.19 億美元淨流出）
  - Google News RSS（多站轉述同一流出主軸）
  - CoinDesk RSS（市場波動與政策面訊號）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, risk-off, outflow streak break
- 摘要（2-3 句）：
  ETF 資金面由流入轉流出，風險資產情緒轉弱。市場多源聚焦同一筆資金流，顯示短期交易敘事明確。
- 判讀（1-2 句）：
  屬風險偏好降溫訊號，需觀察是否形成連續性流出。
- 反向驗證（反證/待確認項）：
  需補發行商官方日流量表與 CME 持倉變化，避免單日雜訊。
- 建議動作（Follow-up）：
  追蹤 24h/48h ETF 淨流、期貨基差與未平倉；若同時惡化則提高風險等級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：64/100
- 等級：L2
- 來源：
  - Bloomberg（人民幣與政策改革敘事）
  - China Daily（寬鬆政策傾向）
  - Google News RSS（LPR 維持低檔、PBOC 定價預期）
- 命中關鍵字：PBOC, yuan fixing, LPR, easing, China economy
- 摘要（2-3 句）：
  中國訊號呈現「穩增長口徑 + 匯率管理」雙軌，LPR 低檔延續顯示政策仍偏寬鬆。市場端對人民幣走勢與政策強度解讀分歧。
- 判讀（1-2 句）：
  偏政策訊號管理，尚未出現強刺激落地的硬指標共振。
- 反向驗證（反證/待確認項）：
  需補 PBOC 公開市場操作規模、社融脈衝與北向資金流。
- 建議動作（Follow-up）：
  追蹤 fixings 偏離、CNH 波動與信用脈衝；如政策工具擴大再重評。

## 訊號 4
- 類別：AI Infra
- 熱度分：56/100
- 等級：L3
- 來源：
  - NVIDIA Blog（GTC 2026 官方更新）
  - Google News RSS（多數為二手評論/投資文章）
- 命中關鍵字：NVIDIA, GTC, AI infrastructure, data center
- 摘要（2-3 句）：
  AI 基建仍有高關注度，但本輪可驗證新增資訊集中在官方活動更新，其餘多為低權重評論站。整體信噪比不足以形成交易級強訊號。
- 判讀（1-2 句）：
  題材熱但可執行資訊不足，暫列觀察。
- 反向驗證（反證/待確認項）：
  缺一線媒體對新訂單、資本開支或出貨節奏的獨立交叉驗證。
- 建議動作（Follow-up）：
  後續改以公司公告與一線財經媒體追蹤具體數字。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：35/100
- 等級：L3
- 來源：
  - Google News RSS（關鍵詞檢索未返回有效條目）
- 命中關鍵字：TSMC, UMC, VIS（命中不足）
- 摘要（2-3 句）：
  本輪在 24h 範圍內未抓到可用的台灣晶圓代工有效事件訊號，資料缺口明顯。
- 判讀（1-2 句）：
  目前無法形成可信判讀。
- 反向驗證（反證/待確認項）：
  需補公司 IR、交易所公告或 Reuters/Bloomberg 即時稿。
- 建議動作（Follow-up）：
  下輪改用精準來源清單重跑（官方公告 + 一線財經）。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」門檻）。
- 補件需求：
  1) 啟用 Brave Search API key 以提升來源覆蓋
  2) 增加 X 關鍵帳號抓取管道（目前僅 News/RSS）
  3) Taiwan Semi 改為官方/一線來源直抓
