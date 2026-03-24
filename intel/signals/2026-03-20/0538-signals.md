# Signal Engine 掃描報告
- 掃描時間：2026-03-20 05:38 (Asia/Taipei)
- 執行版本：signal-engine.prompt v1
- 輸入來源：Google News RSS、CoinDesk RSS、NYT Business RSS
- 資料可得性：中偏低（X/關鍵帳號未直連、Brave API key 缺失、Taiwan Semi 有效來源稀少）

## 評分摘要（L1/L2/L3）
- L1：0
- L2：3
- L3：2

---

## 訊號 1
- 類別：Macro / Oil
- 熱度分：74/100
- 等級：L2
- 來源：
  - NYT Business RSS（U.S. Encourages Flow of Iranian Oil While It Battles Iran）
  - Google News RSS（HBR 油價衝擊討論、Reuters/WKZO 戰事造成油氣擾動轉載）
- 命中關鍵字：oil, Iran, Hormuz, sanctions, supply disruption, OPEC
- 摘要（2-3 句）：
  油市同時存在「政策放寬供給」與「地緣衝突擾動供應」兩股力量，導致價格預期分歧但波動放大。主流來源仍持續聚焦 Hormuz 與制裁調整對供應鏈的影響。
- 判讀（1-2 句）：
  這是高敏感度宏觀波動訊號，尚未形成單邊趨勢，但風險溢價仍在。
- 反向驗證（反證/待確認項）：
  缺 OPEC 即時產量口徑與 EIA 庫存更新；需避免評論文替代硬數據。
- 建議動作（Follow-up）：
  48h 追蹤 WTI/Brent、航運保費與官方供應數據；若再有 2+ 一線來源確認實際供應中斷則升級。

## 訊號 2
- 類別：Crypto Flow
- 熱度分：68/100
- 等級：L2
- 來源：
  - Google News RSS（The Block：BTC/ETH ETF 合計約 2.19 億美元淨流出）
  - CoinDesk RSS（市場波動與資金再配置相關報導）
- 命中關鍵字：bitcoin, ethereum, ETF outflow, volatility, risk-off
- 摘要（2-3 句）：
  ETF 資金面延續「流入中斷→轉淨流出」結構，與風險資產波動上升同步。新聞面顯示機構與交易結構正在重新定價。
- 判讀（1-2 句）：
  屬中強度風險偏好收縮訊號，若連續兩日擴大淨流出，將升級為更明確的防守情境。
- 反向驗證（反證/待確認項）：
  需補發行商官方日流量與交易所未平倉數據，避免單媒體偏差。
- 建議動作（Follow-up）：
  建立 24h ETF flow + OI 聯動監控；若出現「價跌 + 淨流出擴大 + OI 下滑」則上調風險等級。

## 訊號 3
- 類別：Chinese Signal
- 熱度分：62/100
- 等級：L2
- 來源：
  - Google News RSS（Bloomberg：人民幣與政策改革敘事）
  - Google News RSS（Finimize：PBOC fixing 偏軟解讀）
- 命中關鍵字：PBOC, yuan, fixing, China economy, policy
- 摘要（2-3 句）：
  市場對人民幣與 PBOC 設定價形成「偏穩定管理但非強刺激」共識。短期偏向匯率管理與預期引導，而非總量寬鬆衝擊。
- 判讀（1-2 句）：
  目前是政策口徑管理期，對風險資產的方向性推動有限。
- 反向驗證（反證/待確認項）：
  缺 PBOC 官方公告原文與公開市場操作規模。
- 建議動作（Follow-up）：
  追蹤 CNY fix 偏離、北向資金、社融與信用脈衝；若政策工具落地再重評。

## 訊號 4
- 類別：AI Infra
- 熱度分：45/100
- 等級：L3
- 來源：
  - Google News RSS（Motley Fool / AOL / TechBuzz / DCD）
- 命中關鍵字：NVIDIA, OpenAI, data center, AI infrastructure
- 摘要（2-3 句）：
  AI 基建話題熱度仍在，但來源以二手解讀與非一線財經媒體為主。缺乏官方公告或監管文件級新訊。
- 判讀（1-2 句）：
  熱度高於信度，暫不形成交易級訊號。
- 反向驗證（反證/待確認項）：
  缺公司 IR / SEC / 一線媒體同步核證。
- 建議動作（Follow-up）：
  以 Reuters/Bloomberg + 公司公告重跑，過濾內容農場與投資導流文。

## 訊號 5
- 類別：Taiwan Semi
- 熱度分：34/100
- 等級：L3
- 來源：
  - Google News RSS（單一來源：asteriskmag.com）
- 命中關鍵字：Taiwan, chip dominance, semiconductor
- 摘要（2-3 句）：
  本輪 Taiwan Semi 在 24h 內幾乎無高可信新訊，僅見背景型長文。UMC/VIS/TSMC 直接事件訊號不足。
- 判讀（1-2 句）：
  屬資料缺口，不應硬判方向。
- 反向驗證（反證/待確認項）：
  缺交易所公告、公司新聞稿、法說與一線媒體快訊。
- 建議動作（Follow-up）：
  改走公司 IR、證交所揭露與主流終端源補件後再評分。

---

## 本輪結論
- 無 L1 訊號（未達「總分 ≥80 且跨來源確認 ≥8」門檻）。
- 補件需求：
  1) X / 關鍵帳號即時抓取管道
  2) Brave Search API key
  3) Taiwan Semi 高可信來源（IR/交易所/Reuters-Bloomberg）
