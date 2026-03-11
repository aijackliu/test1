# Signal Engine Scan — 2026-03-11 22:15 Asia/Taipei

## Scan Status
- Prompt: `/Users/claireye/clawd/prompts/intel/signal-engine.prompt.md`
- Run time: 2026-03-11 22:15 Asia/Taipei
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Data sources used: Google News RSS headline scan
- Data gap: `web_search` unavailable (missing Perplexity API key); no X velocity data.

### AI Infra
- 類別：AI Infra
- 熱度分：87/100
- 等級：L1
- 來源：Bloomberg.com, CNBC, Rolling Out
- 命中關鍵字：oracle, openai, data center, stargate, nvidia, debt
- 摘要（2-3 句）：本輪抓取 8 則 headline，跨來源 7。主要敘事：Nvidia to Invest $2 Billion in AI Data Center Specialist Nebius - Bloomberg.com / Oracle is building yesterday’s data centers with tomorrow’s debt - CNBC。
- 判讀（1-2 句）：RSS headline 初判，需高權重來源補強。
- 反向驗證（反證/待確認項）：缺 X 即時流與互動增速。
- 建議動作（Follow-up）：下一輪補官方來源與財報/公告。
- 評分拆解：帳號權重 27 / 關鍵字 25 / 熱度速度 20 / 跨來源確認 15 / 去雜訊 0 => 87

### Crypto Flow
- 類別：Crypto Flow
- 熱度分：54/100
- 等級：L3
- 來源：CryptoRank, The Block, TradingView
- 命中關鍵字：bitcoin, etf, outflow, exchange, stablecoin, liquidity
- 摘要（2-3 句）：本輪抓取 8 則 headline，跨來源 7。主要敘事：Trump says the Iran conflict is “very complete” — oil plunges and Bitcoin snaps back above $70k - CryptoRank / The year in data: 5 charts that show how crypto changed in 2025 - The Block。
- 判讀（1-2 句）：RSS headline 初判，需高權重來源補強。
- 反向驗證（反證/待確認項）：缺 X 即時流與互動增速。
- 建議動作（Follow-up）：下一輪補官方來源與財報/公告。
- 評分拆解：帳號權重 8 / 關鍵字 25 / 熱度速度 14 / 跨來源確認 15 / 去雜訊 -8 => 54

### Macro / Oil
- 類別：Macro / Oil
- 熱度分：66/100
- 等級：L2
- 來源：Investing.com Australia, ING THINK economic and financial analysis | ING THINK, FOREX.com
- 命中關鍵字：oil, wti, brent, inventory, cpi, fed
- 摘要（2-3 句）：本輪抓取 8 則 headline，跨來源 6。主要敘事：CPI data, oil inventories among economic data due Wednesday By Investing.com - Investing.com Australia / The Commodities Feed: Oil in wait-and-see mode ahead of Trump Vs. Putin - ING THINK economic and financial analysis | ING THINK。
- 判讀（1-2 句）：RSS headline 初判，需高權重來源補強。
- 反向驗證（反證/待確認項）：缺 X 即時流與互動增速。
- 建議動作（Follow-up）：下一輪補官方來源與財報/公告。
- 評分拆解：帳號權重 18 / 關鍵字 25 / 熱度速度 8 / 跨來源確認 15 / 去雜訊 0 => 66

### Taiwan Semi
- 類別：Taiwan Semi
- 熱度分：66/100
- 等級：L2
- 來源：digitimes, Tech in Asia, Bloomberg.com
- 命中關鍵字：tsmc, umc, semiconductor
- 摘要（2-3 句）：本輪抓取 8 則 headline，跨來源 8。主要敘事：TSMC updates - digitimes / Taiwan’s UMC beats TSMC with 11% stock gain - Tech in Asia。
- 判讀（1-2 句）：RSS headline 初判，需高權重來源補強。
- 反向驗證（反證/待確認項）：缺 X 即時流與互動增速。
- 建議動作（Follow-up）：下一輪補官方來源與財報/公告。
- 評分拆解：帳號權重 27 / 關鍵字 16 / 熱度速度 8 / 跨來源確認 15 / 去雜訊 0 => 66

### Chinese Signal
- 類別：Chinese Signal
- 熱度分：70/100
- 等級：L2
- 來源：WKZO, Reuters, Bloomberg.com
- 命中關鍵字：pboc, stimulus, yuan, loan, credit
- 摘要（2-3 句）：本輪抓取 8 則 headline，跨來源 7。主要敘事：China’s December new bank loans beat forecast as stimulus juices credit demand - WKZO / China's November new loans miss forecast as housing slump persists - Reuters。
- 判讀（1-2 句）：RSS headline 初判，需高權重來源補強。
- 反向驗證（反證/待確認項）：缺 X 即時流與互動增速。
- 建議動作（Follow-up）：下一輪補官方來源與財報/公告。
- 評分拆解：帳號權重 27 / 關鍵字 22 / 熱度速度 6 / 跨來源確認 15 / 去雜訊 0 => 70

## Level Summary
- L1：1
- L2：3
- L3：1

## Alert
- 本輪有 L1 訊號，需立即啟動 48h 追蹤。

## Data Gaps & Manual Recovery
- Missing: `PERPLEXITY_API_KEY` for `web_search`
- Missing: X source coverage and interaction velocity metrics
- Manual fix: set key in Gateway and rerun.
