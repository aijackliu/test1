# Signal Engine 掃描報告
- 掃描時間：2026-03-20 11:00 (Asia/Taipei)
- 任務版本：signal-engine.prompt v1
- 資料來源：Google News RSS、Reuters（經 Google News 聚合）、CoinDesk RSS、NYT Business RSS
- 資料可得性：中（X 直連缺失；Brave API key 仍未配置；台灣半導體近24h命中不足）

## 評分總覽
- L1：0
- L2：3
- L3：2

---

## 訊號 1
- 類別：Macro / Oil
- 熱度分：78/100
- 等級：L2
- 來源：Reuters（Iran war leaves deep, costly scar on Mideast energy）、HBR、TradingView/OilPrice（市場延伸解讀）
- 命中關鍵字：Iran, oil shock, energy infrastructure, OPEC, Hormuz, price spike
- 摘要（2-3句）：
  中東衝突延續，主流媒體與市場解讀同時放大能源供應與成本衝擊。油價上行敘事持續，且風險事件仍在演化階段。
- 判讀（1-2句）：
  事件驅動明確，但目前更像高波動 regime，而非已確認的單向趨勢延續。
- 反向驗證（反證/待確認項）：
  缺少 OPEC 官方即時產量與航運中斷硬數據；多數次級來源為情境推演。
- 建議動作（Follow-up）：
  48h 追蹤 Brent/WTI、航運保費、OPEC 聲明；若再出現兩家以上一線媒體確認供應實際中斷，升級 L1 候選。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：67/100
- 等級：L2
- 來源：Google News 聚合（ETF 流出相關多篇）、CoinDesk（市場與政策面更新）
- 命中關鍵字：Bitcoin, Ethereum, ETF outflow, inflow streak ends, volatility
- 摘要（2-3句）：
  市場聚焦 BTC/ETH ETF 流入動能中斷與短期淨流出，風險偏好轉弱。多來源皆指向「資金節奏放慢 + 波動抬升」。
- 判讀（1-2句）：
  屬風險資產壓力訊號，但缺少發行商官方流量報表作最終確認。
- 反向驗證（反證/待確認項）：
  來源多為二次報導與交易平台內容，需補 ETF 官方統計以避免口徑偏差。
- 建議動作（Follow-up）：
  監控 24h/48h 淨流量與 OI 變化；若連續兩日擴大流出且價格失守關鍵位，提升風險等級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：Google News（China Holds LPR Rates at Record Lows for 10th Month）
- 命中關鍵字：PBOC, LPR, record lows, China economy, stimulus
- 摘要（2-3句）：
  中國利率維持低位但未加碼寬鬆，市場解讀偏「穩定優先、刺激保留」。政策訊號偏中性，對風險資產支撐有限。
- 判讀（1-2句）：
  目前是政策觀望訊號，尚不足以觸發風險偏好明顯反轉。
- 反向驗證（反證/待確認項）：
  缺 PBOC 操作細節與社融/信用脈衝同步強化證據。
- 建議動作（Follow-up）：
  追蹤人民幣、北向資金、社融與信貸新增；若出現工具落地再重評。

## 訊號 4
- 類別：AI Infra
- 熱度分：55/100
- 等級：L3
- 來源：NVIDIA Blog（GTC live updates）+ 多篇投資媒體/二線站
- 命中關鍵字：NVIDIA, GTC, AI infrastructure, data center
- 摘要（2-3句）：
  AI 基建主題熱度高，但可交易的新事實主要集中在活動更新，其他多為投資評論與二手解讀。
- 判讀（1-2句）：
  熱度足、信噪比一般，暫不升級。
- 反向驗證（反證/待確認項）：
  缺一線媒體對重大新合作/訂單的獨立交叉確認。
- 建議動作（Follow-up）：
  等待 GTC 官宣落地（產品規格、客戶名單、供應鏈時程）後重跑評分。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：25/100
- 等級：L3
- 來源：Google News RSS（近24h幾乎無有效命中）
- 命中關鍵字：TSMC, UMC, VIS（命中不足）
- 摘要（2-3句）：
  本輪在 24h 視窗內缺乏高品質、可交叉驗證的台灣晶圓代工新事件。
- 判讀（1-2句）：
  資料缺口型低分，不代表風險消失。
- 反向驗證（反證/待確認項）：
  缺公司 IR、公文揭露與一線媒體追蹤。
- 建議動作（Follow-up）：
  下輪改用公司公告/交易所揭露/Bloomberg-Reuters 精準追蹤。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」）。
- 主要可執行重點：油市地緣風險（L2）與加密 ETF 流向轉弱（L2）。
- 缺口與補件：
  1) 啟用 Brave API 以提升來源覆蓋
  2) 補 X 關鍵帳號直接訊號
  3) 強化台灣半導體一線來源抓取