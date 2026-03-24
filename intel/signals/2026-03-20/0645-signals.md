# Signal Engine 掃描報告
- 掃描時間：2026-03-20 06:45 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中偏低（X 關鍵帳號未直連；Brave API key 缺失）

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
  - NYT Business RSS（U.S. encourages flow of Iranian oil…）
  - Google News RSS（Reuters 引述戰事下油氣擾動；HBR/OilPrice 等延伸）
- 命中關鍵字：oil, Iran, Hormuz, sanctions, supply disruption, price shock
- 摘要（2-3 句）：
  油市主軸仍是「地緣衝突風險溢價」與「政策放寬供給」拉扯。Reuters/NYT 同步提供高權重敘事，顯示事件仍在發酵區。
- 判讀（1-2 句）：
  已接近 L1 門檻，但跨來源仍混入較多評論型與二手站點，未形成更高確證密度。
- 反向驗證（反證/待確認項）：
  缺 OPEC 官方最新產量與實際出口流向數據；需補 EIA 即時庫存/航運數據。
- 建議動作（Follow-up）：
  建立 48h 追蹤：Brent/WTI、保費、航運路徑與 OPEC 聲明；若再出現 2+ Tier1 獨立新增事實，升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：69/100
- 等級：L2
- 來源：
  - Google News RSS（多源提及 BTC/ETH ETF 流入中斷與淨流出）
  - CoinDesk RSS（政策與資金輪動訊號）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, risk-off, volatility
- 摘要（2-3 句）：
  ETF 資金面從連續流入轉為淨流出成為短期核心訊號，市場風險偏好降溫。Google 聚合端的數字一致性尚可，但來源權重分布偏雜。
- 判讀（1-2 句）：
  目前屬於「風險收縮但未失序」；需看連續性確認是否演變為趨勢。
- 反向驗證（反證/待確認項）：
  缺發行商官方淨流資料逐日表；鏈上 stablecoin 淨流與期貨未平倉未交叉。
- 建議動作（Follow-up）：
  24h 內追蹤 ETF 日淨流 + OI 變化；若「價跌+淨流出擴大+OI 下降」同時成立，升級風險燈號。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：
  - Google News RSS（Bloomberg：人民幣/中國利率市場預期變化）
  - Google News RSS（Finimize/InvestingLive 等對 PBOC fixing 的市場解讀）
- 命中關鍵字：PBOC, yuan fixing, China rates, easing expectations, volatility
- 摘要（2-3 句）：
  人民幣定價與寬鬆預期的訊號繼續擾動市場，主流報導偏向「政策微調而非大刺激」。市場對中國需求修復的信心仍未穩定。
- 判讀（1-2 句）：
  屬政策預期管理階段，尚未看到足以改寫風險資產定價的硬落地措施。
- 反向驗證（反證/待確認項）：
  缺 PBOC 官方公告原文與操作規模明細；部分來源為轉述型金融快訊。
- 建議動作（Follow-up）：
  追蹤 USD/CNY fix 偏離、離岸波動與北向資金；待官方工具落地後重評。

## 訊號 4
- 類別：AI Infra
- 熱度分：42/100
- 等級：L3
- 來源：
  - Google News RSS（Motley Fool/AOL/Bitget/Technetbook 等低中權重來源）
- 命中關鍵字：NVIDIA, OpenAI, AI infrastructure, data center
- 摘要（2-3 句）：
  內容以投資評論與轉述居多，缺官方公告級新增事實。高熱度但低確證，噪音高。
- 判讀（1-2 句）：
  不足以形成可執行決策信號，先列觀察。
- 反向驗證（反證/待確認項）：
  缺公司 IR/SEC/一線記者獨立驗證。
- 建議動作（Follow-up）：
  下輪改以公司公告與 Reuters/Bloomberg 主源重跑。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：35/100
- 等級：L3
- 來源：
  - Google News RSS（僅單一低權重條目：台灣晶片背景文章）
- 命中關鍵字：Taiwan chip, semiconductor
- 摘要（2-3 句）：
  本輪幾乎無即時交易相關事件，僅背景型內容。TSMC/UMC/VIS 無高可信新公告訊號。
- 判讀（1-2 句）：
  事件密度不足，暫不構成觀測升級。
- 反向驗證（反證/待確認項）：
  缺法說、營收快報、供應鏈變動等一手資料。
- 建議動作（Follow-up）：
  直接接公司 IR/證交所與主流財經線重建 watcher。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」門檻）。
- 風險主軸仍為：油市地緣風險（接近升級區）與加密資金流轉弱。
- 補件需求：
  1) Brave Search API key（恢復高品質搜尋）
  2) X 關鍵帳號直連管道（目前缺）
  3) Tier1 即時數據源（OPEC/EIA/官方公告）