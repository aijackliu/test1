# Signal Engine 掃描報告
- 掃描時間：2026-03-20 12:45 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中（X 關鍵帳號直連未覆蓋；Brave web_search API key 仍缺）

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
  - Reuters（Iran war leaves deep, costly scar on Mideast energy）
  - NYT Business（Oil Falls and Stocks in Asia Hold Steady）
  - Google News 聚合（HBR/OilPrice 等）
- 命中關鍵字：oil, Iran, energy facilities, supply shock, OPEC, volatility
- 摘要（2-3 句）：
  油市仍受伊朗戰事與能源設施風險牽引，主流媒體描述「高波動、供應擾動、價格劇烈擺動」的結構未解除。NYT 與 Reuters 均提供獨立敘事支持，顯示事件仍在市場定價核心。
- 判讀（1-2 句）：
  已是持續性風險訊號，但尚未形成單一方向突破，因此維持 L2。
- 反向驗證（反證/待確認項）：
  尚缺 OPEC 官方即時產量調整與海運中斷量化數據；若供給端恢復速度快於預期，分數應下修。
- 建議動作（Follow-up）：
  48h 追蹤 Brent/WTI、保費與運輸路徑；若出現「供應實際中斷 + 多家 Tier1 媒體同步」即升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：67/100
- 等級：L2
- 來源：
  - Google News（Bitcoin.com News：BTC ETF 約 1.64 億美元流出）
  - Google News（FXStreet：ETF outflow 壓力）
  - CoinDesk RSS（政策與資金面波動持續）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, risk-off, volatility
- 摘要（2-3 句）：
  加密市場延續「ETF 淨流出 + 風險偏好回落」結構，短期資金面偏保守。雖非全面風險出清，但資金流向已轉弱。
- 判讀（1-2 句）：
  屬中強度壓力訊號，若連續流出天數增加，將接近 L1 邊緣。
- 反向驗證（反證/待確認項）：
  部分來源為非一線站點，需補 ETF 發行商官方日度流量表以提高可信度。
- 建議動作（Follow-up）：
  建立 BTC/ETH ETF 日度流量追蹤；觀察「價格下跌 + 流出擴大 + OI 回落」三重共振。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：
  - Google News（PBOC 穩定金融市場表態、人民幣周內走勢）
  - 聚合來源（Finimize/marketscreener）
- 命中關鍵字：PBOC, yuan, stabilise financial markets, support
- 摘要（2-3 句）：
  政策語調偏「穩市場、穩匯率」，人民幣維持相對穩定敘事。市場正在測試政策口徑是否轉化為更具體工具。
- 判讀（1-2 句）：
  目前仍屬口徑管理型訊號，未見強刺激落地證據。
- 反向驗證（反證/待確認項）：
  缺 PBOC 具體操作規模與正式公告原文交叉核驗。
- 建議動作（Follow-up）：
  追蹤 fixing、OMO 規模、跨境資金流；有量化工具落地再上調評級。

## 訊號 4
- 類別：AI Infra
- 熱度分：56/100
- 等級：L3
- 來源：
  - NVIDIA Blog（GTC 2026 live updates）
  - Bloomberg（AI 新創估值/IPO）
  - 多個二級財經站
- 命中關鍵字：NVIDIA, GTC, AI infrastructure, valuation, IPO
- 摘要（2-3 句）：
  題材熱度高，但本輪新增內容偏活動更新與資本市場敘事，缺少「跨來源確認的硬落地事件」。
- 判讀（1-2 句）：
  熱而不硬，暫維持觀察。
- 反向驗證（反證/待確認項）：
  缺企業公告/監管文件層級的新增供需數據。
- 建議動作（Follow-up）：
  等待 GTC 後續正式產品規格、出貨節點或雲廠採購數據再重評。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：45/100
- 等級：L3
- 來源：
  - Google News（MSN、simplywall.st 等二手分析）
- 命中關鍵字：TSMC, semiconductor, AI chip, stock slips
- 摘要（2-3 句）：
  台灣半導體本輪多為評論與轉載，訊號密度與可信度不足。未見官方公告級更新。
- 判讀（1-2 句）：
  無法形成交易級判斷，先歸檔。
- 反向驗證（反證/待確認項）：
  缺公司 IR、法說、交易所揭露與一線媒體同步確認。
- 建議動作（Follow-up）：
  下輪改用公司公告與一線終端來源重跑。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」）。
- 目前最接近升級的是 Macro/Oil；若供應中斷量化被 Tier1 來源同步確認，可能升至 L1。
