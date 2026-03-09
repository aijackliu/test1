# Signal Engine Scan — 2026-03-09 14:30 (Asia/Taipei)

## Scan Scope
- Sources checked: NYT Technology RSS, CoinDesk RSS, SCMP China RSS, FT World RSS
- Watcher categories: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data caveat: X/關鍵帳號即時互動增速未取得；FT RSS 僅回傳 content-id（標題缺失），可用性受限。

---

## Signal 1
- 類別：Macro / Oil + Crypto Flow
- 熱度分：79/100
  - 帳號權重：20（CoinDesk 市場線 + SCMP 地緣報導）
  - 關鍵字權重：24（oil, crude surge, Iran escalation, bitcoin, liquidation）
  - 熱度速度：18（連續數小時多篇更新）
  - 跨來源交叉確認：12（CoinDesk + SCMP）
  - 去雜訊：- - -
- 等級：L2
- 來源：
  - CoinDesk: oil futures surge 20% past $110…
  - CoinDesk: oil shorts on Hyperliquid wiped out… $40M liquidations
  - CoinDesk: bitcoin tumbles below $66k as oil prices explode higher
  - SCMP: How will the Iran turmoil affect China and its Middle East ties?
- 命中關鍵字：oil, crude, Iran escalation, liquidation, bitcoin
- 摘要（2-3 句）：油價與地緣衝突敘事快速升溫，且已出現加密衍生品清算事件，代表風險資產正在被被動去槓桿。SCMP 的中東-中國關係報導提供事件背景，強化「非單一市場噪音」判定。
- 判讀（1-2 句）：屬高強度風險傳導訊號，但仍需更多主流財經媒體與即時行情 API 完整交叉，暫維持 L2。
- 反向驗證（反證/待確認項）：需補 Brent/WTI 即時曲線、DXY、US10Y 與現貨 ETF 資金流。
- 建議動作（Follow-up）：啟動 24-48h 追蹤，重點監測油價是否站穩高檔與 BTC 是否持續破位。

## Signal 2
- 類別：Crypto Flow
- 熱度分：71/100
  - 帳號權重：18
  - 關鍵字權重：21（downside, meltdown odds, bitcoin）
  - 熱度速度：17
  - 跨來源交叉確認：8（CoinDesk 多文 + 宏觀敘事）
  - 去雜訊：-3（仍偏單媒體）
- 等級：L2
- 來源：CoinDesk（多篇連續市場稿）
- 命中關鍵字：bitcoin downside, market meltdown odds, volatility
- 摘要（2-3 句）：CoinDesk 在短時間內連續發布偏空稿，市場敘事從「回調」轉向「更深下行風險」。若油價維持高檔，可能繼續壓制風險偏好。
- 判讀（1-2 句）：交易面偏空強化，但沒有足夠跨媒體與鏈上數據，不升 L1。
- 反向驗證（反證/待確認項）：補交易所淨流、funding rate、OI 與 ETF 淨流。
- 建議動作（Follow-up）：與 Signal 1 併軌追蹤，避免重複告警。

## Signal 3
- 類別：Chinese Signal
- 熱度分：61/100
  - 帳號權重：17（SCMP）
  - 關鍵字權重：19（critical minerals, supply chains, China）
  - 熱度速度：13
  - 跨來源交叉確認：7（SCMP + FT world headline stream 但標題缺失）
  - 去雜訊：- - -
- 等級：L2
- 來源：
  - SCMP: Why China’s critical mineral dominance is still disrupting US supply chains
  - SCMP: China’s CPI keeps rising after holiday spending surge
- 命中關鍵字：critical minerals, supply chain, China CPI
- 摘要（2-3 句）：中國關鍵礦物主導與供應鏈摩擦持續，疊加內需與通膨訊號，對全球製造成本與政策博弈仍有拉扯。雖非即時風險爆點，但具中期資產定價意義。
- 判讀（1-2 句）：屬慢變量風險，適合納入日報/週報而非即時警報。
- 反向驗證（反證/待確認項）：需補官方數據全文、主要經濟體政策回應。
- 建議動作（Follow-up）：放入週報主題聚類（資源地緣化）。

## Signal 4
- 類別：AI Infra
- 熱度分：64/100
  - 帳號權重：20（NYT）
  - 關鍵字權重：17（AI, data centers, supply chain risk）
  - 熱度速度：10
  - 跨來源交叉確認：8
  - 去雜訊：- - -
- 等級：L2
- 來源：NYT（OpenAI/Anthropic/Pentagon、AI data centers）
- 命中關鍵字：AI data centers, supply chain risk, OpenAI, Anthropic
- 摘要（2-3 句）：AI 基建需求仍高、政策與供應風險敘事同步存在。這對算力供應鏈是「需求強、摩擦大」的延續訊號。
- 判讀（1-2 句）：尚未形成新的突發催化，維持 L2 觀察。
- 反向驗證（反證/待確認項）：待公司公告/法說驗證實際交付影響。
- 建議動作（Follow-up）：追蹤 HBM/CoWoS/lead-time 一手指標。

---

## Level Summary
- L1：0
- L2：4
- L3：0

## Data Gaps
1. X 關鍵帳號互動增速缺失，velocity 分數採新聞密度代理。
2. Taiwan Semi 本輪無新一手事件（公司公告/法說）。
3. FT feed 標題缺失，交叉證據品質有限。

## Conclusion
- 本輪無 L1 訊號。
- 最強主軸：中東升溫帶動油價急升，透過去槓桿機制傳導至加密與風險資產。