# Signal Engine Scan — 2026-03-11 07:45 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 07:45 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Sources: Google News RSS headline scan
- Data gap: `web_search` still unavailable (missing Perplexity API key), and this round still lacks X/engagement-velocity coverage.

## Scored Signals

### 1) AI Infra — Oracle/OpenAI data-center expansion reset narrative
- 類別：AI Infra
- 熱度分：74/100
- 等級：L2
- 來源：Bloomberg, CNBC, The Information, TechRepublic（經 Google News RSS 聚合）
- 命中關鍵字：Oracle, OpenAI, data center, expansion, Stargate, infrastructure buildout
- 摘要（2-3 句）：AI Infra 相關新聞流仍集中在 Oracle 與 OpenAI 擴建節奏調整，並延伸到供應鏈與資本支出可持續性討論。多來源同日/近兩日持續出現，屬可追蹤主題。
- 判讀（1-2 句）：為中高強度 L2，對 AI 基建敘事有實質影響，但仍缺官方公告級確認。
- 反向驗證（反證/待確認項）：缺 OpenAI/Oracle 官方聲明與財報級指引更新。
- 建議動作（Follow-up）：持續 48h 追蹤 IR/官方聲明與賣方更新。

### 2) Macro/Oil — geopolitical spike + CPI/EIA event risk
- 類別：Macro / Oil
- 熱度分：57/100
- 等級：L3
- 來源：Investing.com、FXStreet（RSS）
- 命中關鍵字：WTI, Middle East tensions, CPI, inventories
- 摘要（2-3 句）：油價短線受地緣事件驅動，市場等待 CPI 與庫存數據。主流一線來源交叉確認不足。
- 判讀（1-2 句）：偏事件性波動，未形成高可信趨勢訊號。
- 反向驗證（反證/待確認項）：需 Reuters/Bloomberg + EIA 官方數據共同確認。
- 建議動作（Follow-up）：數據落地後再評分。

### 3) Crypto Flow — exchange outflow narrative remains noisy
- 類別：Crypto Flow
- 熱度分：45/100
- 等級：L3
- 來源：MEXC、Live Bitcoin News、TradingView repost（RSS）
- 命中關鍵字：Bitcoin outflow, exchange supply, stablecoin outflows, ETF flow
- 摘要（2-3 句）：仍以交易所/二手敘事為主，缺高權重一線來源與官方流量數據。
- 判讀（1-2 句）：噪音高於訊號，暫不升級。
- 反向驗證（反證/待確認項）：需 ETF issuer flow + on-chain 主流數據供應商同步。
- 建議動作（Follow-up）：補抓 ETF/netflow 數據後重算。

### 4) Taiwan Semi — no fresh multi-source catalyst
- 類別：Taiwan Semi
- 熱度分：27/100
- 等級：L3
- 來源：DigiTimes（其餘多為舊聞）
- 命中關鍵字：TSMC, UMC, Taiwan semiconductor
- 摘要（2-3 句）：本輪未見新鮮且可交叉確認的重大催化。
- 判讀（1-2 句）：資料不足，不做方向判讀。
- 反向驗證（反證/待確認項）：需補公司公告、法說、台灣主流財經媒體新訊。
- 建議動作（Follow-up）：下輪收窄關鍵詞（CoWoS/先進封裝/稼動率）。

### 5) Chinese Signal — stale-heavy result set, no fresh pulse
- 類別：Chinese Signal
- 熱度分：23/100
- 等級：L3
- 來源：Reuters/Bloomberg 舊聞與聚合條目
- 命中關鍵字：PBOC, stimulus, loans, yuan, property
- 摘要（2-3 句）：搜尋結果仍以舊聞為主，沒有當日新政策脈衝。
- 判讀（1-2 句）：當前屬資料可得性不足，不可解讀為「無風險」。
- 反向驗證（反證/待確認項）：需補 PBOC 官網、官媒、離岸市場即時反應。
- 建議動作（Follow-up）：改採官媒/央行源優先抓取。

## Level Summary
- L1：0
- L2：1
- L3：4

## Decision
- 本輪 **無 L1 訊號**，不觸發即時警報。
- 最高優先追蹤主題：AI Infra（Oracle/OpenAI data-center narrative）。

## Quality / Gap Note
- 因 `web_search` API key 缺失，本輪仍偏 RSS headline 模式。
- 補件方式：設定 `PERPLEXITY_API_KEY`（Gateway）後重跑，可提升跨來源確認與熱度速度精度。
