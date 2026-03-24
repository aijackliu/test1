# Signal Engine 掃描報告
- 掃描時間：2026-03-20 12:30 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、NYT Business RSS、CoinDesk RSS
- 資料可得性：中（X/關鍵帳號直抓未覆蓋；Brave API key 仍缺）

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
  - Reuters（經 Google News：Goldman 上調油價上行風險）
  - NYT Business（油價震盪、亞洲能源供應壓力）
  - HBR/多家市場媒體（油價衝擊延伸）
- 命中關鍵字：oil shock, Iran, energy infrastructure, OPEC, supply disruption, price volatility
- 摘要（2-3 句）：
  油市持續受中東地緣風險驅動，主流來源同時描述供應鏈壓力與價格劇烈波動。NYT 已進一步指向亞洲燃油供需緊張外溢。
- 判讀（1-2 句）：
  風險仍在擴散，但方向尚未形成單邊趨勢；目前屬高波動而非確定性長趨勢。
- 反向驗證（反證/待確認項）：
  需補 OPEC 官宣增產/減產落地量、EIA/IEA 庫存即時數據。
- 建議動作（Follow-up）：
  48h 追蹤 Brent/WTI、成品油裂解價差、航運保費；若再出現「官方供應中斷」雙一線媒體確認，考慮升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：69/100
- 等級：L2
- 來源：
  - The Block（BTC/ETH ETF 合計約 2.19 億美元淨流出）
  - Google News 聚合（多來源重複引用同一流量事件）
  - CoinDesk（市場波動與政策主題升溫）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, risk-off, volatility
- 摘要（2-3 句）：
  BTC/ETH ETF 流入趨勢中斷訊號延續，風險偏好偏弱。與總體油價衝擊疊加後，市場短線更傾向防守。
- 判讀（1-2 句）：
  屬於可交易的情緒降溫訊號，但目前多為同題轉載，需防止「單一數據被多站放大」誤判。
- 反向驗證（反證/待確認項）：
  需補 ETF 發行商官方日流量與交易所資金面明細。
- 建議動作（Follow-up）：
  連續監測 2 個交易日的淨流與未平倉變化；若同時惡化再提升風險等級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：
  - marketscreener（轉引中國金融市場口徑）
  - 中國官媒/財經站點（政策偏寬鬆敘事）
  - 聚合來源（PBOC 定盤與人民幣波動）
- 命中關鍵字：PBOC, yuan, stabilise financial markets, easing track, fixing
- 摘要（2-3 句）：
  市場解讀 PBOC 釋放「穩定市場」訊號，人民幣短線呈現偏穩。政策托底敘事正在回升，但實體信用擴張證據仍不足。
- 判讀（1-2 句）：
  目前偏政策口徑管理，尚未形成高置信的增長反轉訊號。
- 反向驗證（反證/待確認項）：
  缺公開市場操作規模、社融/信貸增量的即時確認。
- 建議動作（Follow-up）：
  持續追蹤 CNH、北向資金、社融與地產融資指標。

## 訊號 4
- 類別：AI Infra
- 熱度分：56/100
- 等級：L3
- 來源：
  - NVIDIA Blog（GTC 2026 live updates）
  - Bloomberg/市場站點（AI 融資與估值消息）
- 命中關鍵字：NVIDIA, GTC, AI infrastructure, valuation, data center
- 摘要（2-3 句）：
  AI 基建仍有高關注，但本輪新增訊號以活動更新與資本市場題材為主，未看到明確「供應鏈/產能/業績」硬落地。
- 判讀（1-2 句）：
  題材熱度高但可執行密度一般，先列觀察。
- 反向驗證（反證/待確認項）：
  缺公司正式財測上修或大額確定訂單披露。
- 建議動作（Follow-up）：
  等待 GTC 後續官方公告與一線媒體交叉確認。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：51/100
- 等級：L3
- 來源：
  - 聚合媒體（MSN/AOL/simplywall.st/Globe）
  - 個別市場評論（與地緣油價衝擊連動）
- 命中關鍵字：TSMC, revenue growth, stock slips, semiconductor, Asia supply chain
- 摘要（2-3 句）：
  台灣半導體相關報導多為二手評論或轉載，信噪比不足。尚未抓到 TSMC/UMC/VIS 一手公告級變化。
- 判讀（1-2 句）：
  暫不形成高等級訊號，維持追蹤。
- 反向驗證（反證/待確認項）：
  缺 IR、法說、交易所重大訊息等硬資料。
- 建議動作（Follow-up）：
  以公司官方與一線終端媒體重跑精準查詢。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」）。
- 目前最高優先關注：Macro/Oil（L2 高位），其餘維持 L2/L3 追蹤。
- 補件需求：
  1) 啟用 Brave Search API（提升一線來源覆蓋）
  2) 建立 X 關鍵帳號直抓（加強速度分與帳號權重可信度）
