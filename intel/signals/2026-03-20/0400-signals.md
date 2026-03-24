# Signal Engine 掃描報告
- 掃描時間：2026-03-20 04:00 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中（X 直接訊號未覆蓋；Brave API key 缺失；Reuters RSS DNS 失敗）

## 評分摘要（L1/L2/L3）
- L1：0
- L2：3
- L3：2

---

## 訊號 1
- 類別：Macro / Oil
- 熱度分：72/100
- 等級：L2
- 來源：
  - NYT Business RSS（US encourages flow of Iranian oil…）
  - Google News RSS（Fortune: oil price update；OilPrice: $150 scenario）
- 命中關鍵字：oil, Iran, sanctions, OPEC, price spike, Hormuz
- 摘要（2-3 句）：
  地緣衝突與制裁政策訊號持續推高油價預期，且市場出現「供給放寬 vs 風險溢價」雙向敘事。多來源同時出現油價劇烈波動與供應鏈不確定性描述。
- 判讀（1-2 句）：
  屬於高敏感但未完全定向的宏觀風險訊號，短期仍偏波動交易而非單邊趨勢。
- 反向驗證（反證/待確認項）：
  OPEC 官方產量與實際出口數據尚未在本輪被直接抓取；需補 EIA/IEA 即時庫存與運輸資料。
- 建議動作（Follow-up）：
  48h 追蹤 Brent/WTI、航運保費、OPEC 官方聲明；若再出現 2+ 一線媒體確認「供應中斷」再升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：66/100
- 等級：L2
- 來源：
  - Google News RSS（The Block：BTC/ETH ETF 合計約 2.19 億美元淨流出）
  - CoinDesk RSS（BTC 在油價上行背景下維持高波動）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, risk-off, volatility
- 摘要（2-3 句）：
  加密市場出現 ETF 流入趨勢中斷與短期淨流出，風險偏好下降。BTC 雖維持關鍵價位，但與油價與地緣消息耦合度提高。
- 判讀（1-2 句）：
  屬於風險資產壓力訊號，若連續兩日淨流出擴大，將轉向更明確的防守結構。
- 反向驗證（反證/待確認項）：
  需補官方 ETF 發行商淨流量表（避免單一媒體引用誤差）；鏈上 stablecoin 淨流入未核對。
- 建議動作（Follow-up）：
  建立 24h ETF flow watchlist（BTC/ETH 分開）；若出現「價格下跌 + 淨流出擴大 + 未平倉下降」再升級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：61/100
- 等級：L2
- 來源：
  - Google News RSS（SCMP：PBOC 釋出穩定資本市場訊號）
  - Google News RSS（WSJ：中國信用引擎放緩觀點）
- 命中關鍵字：PBOC, stability, capital markets, credit slowdown, China economy
- 摘要（2-3 句）：
  政策面出現「穩定市場」口徑，但基本面敘事仍偏向信用動能放緩。政策托底與成長壓力並存，市場解讀分歧。
- 判讀（1-2 句）：
  目前屬政策語氣管理階段，尚未看到可量化的強刺激落地證據。
- 反向驗證（反證/待確認項）：
  需補 PBOC 正式公告與公開市場操作規模；目前交叉來源仍以新聞轉述為主。
- 建議動作（Follow-up）：
  追蹤人民幣匯率、北向資金、信用脈衝與社融新增；若政策工具落地再重評。

## 訊號 4
- 類別：Taiwan Semi
- 熱度分：48/100
- 等級：L3
- 來源：
  - Google News RSS（MSN 轉載：TSMC 股價回落但營收仍強）
- 命中關鍵字：TSMC, stock slips, revenue growth, semiconductor
- 摘要（2-3 句）：
  台灣半導體主題在本輪來源中噪音偏高，且關鍵條目多為轉載或非目標 UMC/VIS 語義污染（SMU/非晶圓代工內容）。
- 判讀（1-2 句）：
  目前證據不足，不建議形成交易級結論。
- 反向驗證（反證/待確認項）：
  缺 TSMC/UMC/VIS 官方公告、法說或一線財經媒體同步確認。
- 建議動作（Follow-up）：
  改用精準來源（公司 IR、證交所公告、Bloomberg/Reuters）重跑。

## 訊號 5
- 類別：AI Infra
- 熱度分：44/100
- 等級：L3
- 來源：
  - Google News RSS（混合來源，含 Motley Fool/AOL/tech blogs）
- 命中關鍵字：NVIDIA, OpenAI, data center, AI infrastructure
- 摘要（2-3 句）：
  本輪 AI 基建訊號以二手評論與低權重站點為主，缺少官方公告級新事件。雖有題材熱度，但可執行資訊密度不足。
- 判讀（1-2 句）：
  熱度存在，信噪比不足；暫不升級。
- 反向驗證（反證/待確認項）：
  缺公司公告、SEC 文件或一線媒體獨立核證。
- 建議動作（Follow-up）：
  後續以公司 IR / 交易所揭露 / Reuters-Bloomberg 為主源再評估。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」門檻）。
- 需補件：
  1) Brave Search API（目前缺 key）
  2) Reuters RSS 替代入口（feeds.reuters.com DNS 無法解析）
  3) X 關鍵帳號直接抓取管道（本輪未覆蓋）
