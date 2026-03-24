# Signal Engine 掃描報告
- 掃描時間：2026-03-20 08:15 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、Reuters（經 Google News 聚合）、CoinDesk RSS、NYT Business RSS
- 資料可得性：中（X/關鍵帳號直連未覆蓋；Brave API key 仍缺）

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
  - Reuters（US may remove sanctions on Iranian oil stranded in tankers）
  - Reuters（Brent up but off highs）
  - NYT（U.S. Encourages Flow of Iranian Oil While It Battles Iran）
- 命中關鍵字：oil, Iran, sanctions, Brent, Hormuz, supply disruption
- 摘要（2-3 句）：
  油市主軸維持在「中東地緣風險 vs 美國鬆綁伊朗油流向」的拉扯。Reuters 與 NYT 均出現高權重政策與價格敘事，顯示風險溢價仍在但已出現政策緩衝訊號。
- 判讀（1-2 句）：
  這是偏高等級的波動訊號，但尚未形成單邊供應中斷共識，因此未進 L1。
- 反向驗證（反證/待確認項）：
  需補 OPEC 實際增產/出口與油輪運力數據，確認是否只是 headline-driven volatility。
- 建議動作（Follow-up）：
  48h 追蹤 Brent、Dubai、航運保費與 OPEC 官方口徑；若出現「供應中斷被 2+ 一線來源確認」升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：67/100
- 等級：L2
- 來源：
  - The Block（BTC/ETH ETF 合計約 2.19 億美元淨流出）
  - 多個二級來源（Mitrade / LiveBitcoinNews）重複引用同一組流量敘事
- 命中關鍵字：bitcoin, ethereum, ETF outflow, inflow streak ends, risk-off
- 摘要（2-3 句）：
  ETF 連續流入中斷並轉為淨流出，是本輪加密風險偏好降溫的核心訊號。雖然轉述量高，但高權重一手來源仍偏少。
- 判讀（1-2 句）：
  屬可交易但需謹慎的二級訊號，現階段偏「風險收縮」而非結構反轉。
- 反向驗證（反證/待確認項）：
  尚缺發行商官方日流量表與鏈上穩定幣淨流入交叉驗證。
- 建議動作（Follow-up）：
  監控連續 2 日 ETF 淨流出與 BTC 持續跌破關鍵位的共振條件；觸發後再升級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：
  - Bloomberg（Yuan rally / policy reform 相關敘事）
  - China Daily（貨幣政策偏寬）
  - Finimize（PBOC fixing 偏軟）
- 命中關鍵字：PBOC, yuan fixing, easing, China economy, policy
- 摘要（2-3 句）：
  人民幣與政策口徑呈現「穩中偏寬」訊號，市場焦點集中在 fixing 與後續寬鬆節奏。來源間方向一致，但官方量化工具落地仍有限。
- 判讀（1-2 句）：
  目前仍是政策預期交易，尚未達到強政策衝擊等級。
- 反向驗證（反證/待確認項）：
  缺 PBOC 公開市場操作規模與社融脈衝最新數據。
- 建議動作（Follow-up）：
  追蹤 USD/CNY fix 偏離幅度、北向資金與中國利率曲線，確認是否轉為實質政策行情。

## 訊號 4
- 類別：AI Infra
- 熱度分：46/100
- 等級：L3
- 來源：
  - Google News 聚合（The Motley Fool / AOL / TechBuzz 等低至中權重）
- 命中關鍵字：NVIDIA, OpenAI, data center, AI stocks
- 摘要（2-3 句）：
  本輪 AI 基建多為投資評論與二手消息，缺少官方公告或一線媒體新事件。雜訊比例高，無法形成高置信訊號。
- 判讀（1-2 句）：
  熱度有、可執行性不足，暫列觀察。
- 反向驗證（反證/待確認項）：
  缺 SEC 文件、公司 IR、Reuters/Bloomberg 獨立確認。
- 建議動作（Follow-up）：
  改用公司官方與一線財經源重跑，降低內容農場干擾。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：31/100
- 等級：L3
- 來源：
  - Google News RSS（本輪查詢幾乎無有效新條目）
- 命中關鍵字：TSMC, UMC, VIS, foundry
- 摘要（2-3 句）：
  台灣晶圓代工在本輪 `when:1d` 條件下未抓到可用新訊號，顯示當前資料空窗或查詢需改寫。
- 判讀（1-2 句）：
  證據不足，不應產生方向性結論。
- 反向驗證（反證/待確認項）：
  缺公司公告、法說會重點、主流財經媒體同步報導。
- 建議動作（Follow-up）：
  下輪改採「公司名 + revenue/capex/guidance」精準 query 與官方 IR 來源。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」）。
- 目前最接近 L1：Macro/Oil（78 分），但仍缺供應中斷的高置信實證。
- 補件需求：
  1) X / 關鍵帳號 direct feed
  2) Brave Search API key
  3) 台灣半導體官方/一線財經來源的精準抓取管道
