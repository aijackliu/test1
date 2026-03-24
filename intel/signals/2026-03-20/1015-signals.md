# Signal Engine 掃描報告
- 掃描時間：2026-03-20 10:15 (Asia/Taipei)
- 任務來源：`prompts/intel/signal-engine.prompt.md`
- 輸入來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中（X 直連缺失、Brave Search API key 缺失）

## 評分總覽
- L1：0
- L2：3
- L3：2

---

## 訊號 1
- 類別：Macro / Oil
- 熱度分：76/100
- 等級：L2
- 來源：
  - Google News RSS（Reuters/Investing 轉載：US-Israeli war 對油氣供應中斷）
  - Google News RSS（HBR/Business Insider：油價衝擊持續擴散）
- 命中關鍵字：oil shock, Iran, Hormuz, disruption, OPEC, supply
- 摘要（2-3 句）：
  油價衝擊敘事從即時新聞延伸到宏觀評論層，顯示市場把事件風險由短訊號轉為中短期定價主線。供應端干擾與風險溢價仍在同時升溫。
- 判讀（1-2 句）：
  風險高但方向尚未單邊確認，屬高波動 regime。
- 反向驗證（反證/待確認項）：
  尚缺 OPEC 官方產量調整與 EIA 即時庫存同步驗證。
- 建議動作（Follow-up）：
  追蹤 24–48h Brent/WTI、航運保費、OPEC 官方聲明；若再有 2 個 Tier1 媒體獨立確認實體供應中斷，再評估升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：69/100
- 等級：L2
- 來源：
  - Google News RSS（The Block：BTC/ETH ETF 合計約 2.19 億美元流出）
  - CoinDesk RSS（資金與監管議題並行，市場波動維持高位）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, risk-off, volatility
- 摘要（2-3 句）：
  ETF 淨流量由連續流入轉為顯著流出，短線風險偏好轉弱。政策端與資金端訊號混合，導致市場缺乏單一驅動。
- 判讀（1-2 句）：
  屬「偏空但未破位」結構，重點看是否延續第二天淨流出。
- 反向驗證（反證/待確認項）：
  多數轉載來源為二手摘要，需補 ETF 發行商官方日流量表。
- 建議動作（Follow-up）：
  建立 BTC/ETH 分流追蹤；若「價格走弱 + 流出擴大 + 未平倉下降」同時成立，升級為更高風險等級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：63/100
- 等級：L2
- 來源：
  - Google News RSS（Bloomberg：長期人民幣政策改革敘事）
  - Google News RSS（China Daily：油價衝擊下寬鬆路徑訊號）
- 命中關鍵字：PBOC, yuan, easing, policy reform, China economy
- 摘要（2-3 句）：
  中國訊號由「短期維穩」擴展到「中期政策調整」敘事，但目前仍偏口徑與預期管理。市場對人民幣與寬鬆節奏的分歧仍大。
- 判讀（1-2 句）：
  可觀察但不構成立即交易級催化。
- 反向驗證（反證/待確認項）：
  缺 PBOC 正式公告文件與操作規模明細。
- 建議動作（Follow-up）：
  追蹤 USD/CNY 中間價偏離、公開市場操作、北向資金流向。

## 訊號 4
- 類別：AI Infra
- 熱度分：57/100
- 等級：L3
- 來源：
  - Google News RSS（NVIDIA GTC 2026 Live Updates，NVIDIA 官方）
  - 其他多為二手評論站（Motley Fool/AOL/tech blogs）
- 命中關鍵字：NVIDIA, GTC, AI infrastructure, data center
- 摘要（2-3 句）：
  有官方活動熱點，但跨來源可驗證的「新落地交易/供應鏈變化」不足。大量內容屬投資評論與轉述，信噪比偏低。
- 判讀（1-2 句）：
  熱度高、可執行性中低，暫列觀察。
- 反向驗證（反證/待確認項）：
  需補 Tier1 媒體或公司正式揭露（合約、capex、出貨節奏）。
- 建議動作（Follow-up）：
  待 GTC 官方完整稿與財報口徑後重評。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：35/100
- 等級：L3
- 來源：
  - Google News RSS（`TSMC UMC Vanguard Semiconductor when:1d` 回傳空頻道）
- 命中關鍵字：TSMC, UMC, VIS（命中不足）
- 摘要（2-3 句）：
  本輪在 24h 視窗內未抓到可用的台灣晶圓代工高可信訊號，資料缺口明顯。
- 判讀（1-2 句）：
  無法形成有效評分結論。
- 反向驗證（反證/待確認項）：
  缺公司 IR、交易所公告、Reuters/Bloomberg 即時條目。
- 建議動作（Follow-up）：
  下輪改用公司公告源與台股即時新聞源重跑。

---

## 本輪結論
- **無 L1 訊號**（未達「總分≥80 且跨來源確認≥8」）。
- 目前最高風險簇：Macro/Oil（L2，高波動）。
- 主要缺口：
  1) Brave Search API key 缺失
  2) X 關鍵帳號直抓未覆蓋
  3) Taiwan Semi 在 24h 視窗資料稀疏
