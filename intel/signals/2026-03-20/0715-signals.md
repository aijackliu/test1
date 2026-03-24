# Signal Engine 掃描報告
- 掃描時間：2026-03-20 07:15 (Asia/Taipei)
- 規格：signal-engine.prompt v1
- 來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中低（X/關鍵帳號直連缺失；Brave API key 缺失；來源噪音偏高）

## 評分總覽
- L1：0
- L2：2
- L3：3

---

## 訊號 1
- 類別：Macro / Oil
- 熱度分：74/100
- 等級：L2
- 來源：
  - NYT：U.S. encourages flow of Iranian oil
  - Google News：HBR oil shock、多家媒體油價衝擊與 OPEC/伊朗敘事
- 命中關鍵字：oil, Iran, sanctions, OPEC, oil shock, supply, Hormuz
- 摘要（2-3 句）：
  油市主軸仍是「地緣風險推升波動」與「政策釋放供給」拉扯。多來源同時出現油價衝擊敘事，但方向仍受事件 headline 主導。
- 判讀（1-2 句）：
  風險高但未形成單邊確證，仍屬事件驅動型震盪。
- 反向驗證（反證/待確認項）：
  缺 OPEC 官方產量更新與 EIA 即時庫存交叉驗證。
- 建議動作（Follow-up）：
  建立 48h 追蹤：Brent/WTI、航運保費、OPEC 聲明；若出現供應中斷硬證據再升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：63/100
- 等級：L2
- 來源：
  - Google News：The Block（BTC/ETH ETF 約 2.19 億美元淨流出）
  - Google News：Bitcoin.com（BTC ETF 淨流出）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, risk-off, flow reversal
- 摘要（2-3 句）：
  ETF 資金流由先前流入轉為淨流出，市場風險偏好降溫。消息面持續聚焦資金撤出與波動抬升。
- 判讀（1-2 句）：
  是偏空的流動性訊號，但尚未達 panic 條件。
- 反向驗證（反證/待確認項）：
  需補發行商官方 flow 表與交易所 OI/基差，避免單媒體偏差。
- 建議動作（Follow-up）：
  24h 監控 ETF 淨流、永續資金費率、OI 同步變化；連續兩日擴大才考慮升級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：56/100
- 等級：L3
- 來源：
  - Google News：Bloomberg（人民幣與中國利率市場敘事）
  - Google News：Finimize / investingLive（PBOC fixing 討論）
- 命中關鍵字：PBOC, yuan fixing, China rates, easing expectations
- 摘要（2-3 句）：
  人民幣與降息預期的討論增多，但資訊以二手市場評論為主。政策方向仍偏「口徑管理」而非強刺激落地。
- 判讀（1-2 句）：
  可觀察但交易訊號不足。
- 反向驗證（反證/待確認項）：
  缺 PBOC 官方公告、OMO 規模、社融增量數據。
- 建議動作（Follow-up）：
  等官方數據窗口再重評，現階段僅存檔。

## 訊號 4
- 類別：Taiwan Semi
- 熱度分：22/100
- 等級：L3
- 來源：
  - Google News（when:1d 查詢無有效條目返回）
- 命中關鍵字：TSMC, UMC, VIS（未形成有效新聞集合）
- 摘要（2-3 句）：
  本輪在 24h 範圍未抓到足量且可信的台灣晶圓代工即時訊號。
- 判讀（1-2 句）：
  屬資料缺口，不做方向性判斷。
- 反向驗證（反證/待確認項）：
  缺公司 IR、法說、主流財經媒體即時稿。
- 建議動作（Follow-up）：
  改由 IR/交易所揭露/Bloomberg Reuters 重跑。

## 訊號 5
- 類別：AI Infra
- 熱度分：37/100
- 等級：L3
- 來源：
  - Google News（Motley Fool/AOL/tech blogs 為主）
- 命中關鍵字：NVIDIA, OpenAI, data center, AI infrastructure
- 摘要（2-3 句）：
  AI 基建仍有熱度，但本輪多數條目屬評論與轉載，缺官方公告級新事件。
- 判讀（1-2 句）：
  噪音高於可執行訊號，暫不升級。
- 反向驗證（反證/待確認項）：
  缺公司公告/監管文件/一線記者獨立確認。
- 建議動作（Follow-up）：
  等 Tier-1 來源出現新事實點再評分。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」）。
- 主要可執行訊號為：Oil（L2）、Crypto ETF flow（L2）。
- 缺口補件：
  1) Brave API key（恢復 web_search）
  2) X 關鍵帳號直連抓取
  3) Taiwan Semi 一線來源補強（IR/Reuters/Bloomberg）
