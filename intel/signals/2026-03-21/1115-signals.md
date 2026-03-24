# Signal Engine Scan — 2026-03-21 11:15 (Asia/Taipei)

## 掃描設定
- Prompt: `prompts/intel/signal-engine.prompt.md`
- Sources: Reuters 為主（透過 Google News RSS 聚合），輔以跨來源標題驗證（同主題是否被 Bloomberg/CNBC 等跟進）
- Watchers: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- 時窗：近 14 天

## Signals（本輪 Top 5）

### 1) 中國房市續弱，2 月新屋價格仍下行
- 類別：Chinese Signal
- 熱度分：76/100
- 等級：L2
- 來源：
  - Reuters（2026-03-16）China's new home prices extend drop in February as recovery remains elusive
  - Bloomberg（同題跟進，跨來源）
- 命中關鍵字：China home prices, recovery elusive, property slump
- 摘要（2-3 句）：中國 2 月新屋價格續跌，顯示房市修復仍偏弱。雖有「跌幅放緩」敘事，但尚未形成明確反轉。
- 判讀（1-2 句）：內需與地方財政修復速度仍不足，對風險偏好改善有限。
- 反向驗證（反證/待確認項）：需補 3 月成交量、庫存去化與土地市場數據，確認是否為統計波動。
- 建議動作（Follow-up）：納入 48h 中國政策+房地產聯動追蹤。

### 2) 中國 LPR 按兵不動，政策觀望延續
- 類別：Chinese Signal
- 熱度分：72/100
- 等級：L2
- 來源：
  - Reuters（2026-03-19）China set to keep rates steady as Mideast war clouds inflation outlook
  - CNBC（同題）
- 命中關鍵字：LPR unchanged, PBOC, policy stance
- 摘要（2-3 句）：3 月貸款基準利率維持不變，政策端仍偏審慎。市場對大規模刺激預期再延後。
- 判讀（1-2 句）：短線偏中性偏保守，需觀察是否改採結構性工具補位。
- 反向驗證（反證/待確認項）：關注後續準財政/再貸款工具是否加碼。
- 建議動作（Follow-up）：與房市指標合併建模，監控信用脈衝拐點。

### 3) AI 基建長單仍強：Nebius x Meta（5 年最高 270 億美元）
- 類別：AI Infra
- 熱度分：70/100
- 等級：L2
- 來源：
  - Reuters（2026-03-16）Nebius signs AI infrastructure deals with Meta worth up to $27 billion over 5 years
  - Reuters（2026-03-17）後續可轉債融資 37.5 億美元
- 命中關鍵字：AI infrastructure, long-term deal, financing, Meta, Nvidia ecosystem
- 摘要（2-3 句）：AI 供應鏈出現「大單 + 融資」連動，顯示需求端仍在鎖定長期算力。資本開支與財務槓桿同步升高。
- 判讀（1-2 句）：中期需求偏強，但執行與現金流風險上升。
- 反向驗證（反證/待確認項）：需追蹤實際交付與毛利率，不可只看簽約額。
- 建議動作（Follow-up）：持續追蹤 hyperscaler 以外是否出現同量級採購。

### 4) 油價高波動：荷莫茲通行恢復後回吐漲幅
- 類別：Macro / Oil
- 熱度分：68/100
- 等級：L2
- 來源：
  - Reuters（2026-03-16）Oil prices slide 3% as some ships transit Strait of Hormuz
  - Reuters（2026-03-19）Brent up but off highs
- 命中關鍵字：Hormuz, Brent, supply risk premium, volatility
- 摘要（2-3 句）：地緣事件推高油價後，因部分航運恢復而回落。供應中斷風險溢價仍未完全消退。
- 判讀（1-2 句）：短線通膨預期仍受擾動，資產定價偏事件驅動。
- 反向驗證（反證/待確認項）：補航運保費、實際出口量與商業庫存。
- 建議動作（Follow-up）：與股債/加密風險資產做 24h 聯動監控。

### 5) 供應鏈材料風險浮現：晶片產業關注氦氣供給
- 類別：Taiwan Semi
- 熱度分：65/100
- 等級：L2
- 來源：
  - Reuters（2026-03-18）Chipmakers in Malaysia monitoring risks from helium supply disruptions
- 命中關鍵字：helium supply disruption, chip supply chain, upstream materials
- 摘要（2-3 句）：半導體供應鏈對工業氣體風險升高警覺。現階段仍屬預警，未見大規模產能衝擊。
- 判讀（1-2 句）：屬中短期脆弱點，若擴散可能壓縮先進封裝/晶圓製造彈性。
- 反向驗證（反證/待確認項）：確認主要廠商庫存週數與替代供應來源。
- 建議動作（Follow-up）：建立 helium/neon 風險雷達與台鏈曝險矩陣。

---

## L1 Gate Check
- 本輪無 L1（未達「總分 >=80 且跨來源確認 >=8」）。

## 資料缺口
- X 即時互動「增速」未直接接 API，熱度速度目前以新聞節奏替代，屬降級估算。
- 若要提升 L1 檢出率：需補關鍵帳號貼文級時間序列（轉推/回覆/引用的每小時斜率）。
