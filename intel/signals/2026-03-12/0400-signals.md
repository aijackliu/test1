# Signal Engine Scan Report
- Scan Time (Asia/Taipei): 2026-03-12 04:00
- Window: latest ~12-24h headlines available from RSS/News endpoints
- Coverage: AI Infra / Crypto Flow / Macro-Oil / Taiwan Semi / Chinese Signal
- Note: X 與部分新聞站（如 Reuters 首頁）受限，以下以可驗證 RSS/News 聚合為主，已標註資料缺口。

---

## 1) Macro / Oil
- 類別：Macro / Oil
- 熱度分：84/100
  - 帳號權重：26（BBC/FT/CNA 屬 Tier1-2 主流媒體）
  - 關鍵字權重：22（命中：IEA、oil reserves、Hormuz、energy shock、war）
  - 熱度速度：18（多家媒體在近 2-6 小時密集更新）
  - 跨來源交叉確認：14（BBC + FT + CNA）
  - 去雜訊：-(-4)（戰時資訊噪音高，保守降權）
- 等級：**L1**
- 來源：
  - BBC Business RSS: Countries agree to record release of emergency oil reserves as prices surge
  - FT World RSS: IEA releases record oil reserves to counter Iran war energy shock
  - CNA 即時：國際能源總署將釋出 4 億桶儲備、荷莫茲相關衝突快訊
- 命中關鍵字：IEA、oil reserves、Hormuz、energy shock、G7
- 摘要（2-3 句）：
  多來源同時指向「中東衝突升級 + IEA 釋放戰略儲備」的聯動事件。這代表供給風險已從預期層面進入政策應對層面，市場仍對實際緩衝效果存疑。油價與風險資產波動擴大機率上升。
- 判讀（1-2 句）：
  這是跨市場核心風險訊號，短線將壓抑風險偏好並推高能源/運輸成本定價。
- 反向驗證（反證/待確認項）：
  若 24-48h 內航運安全恢復且油價回落，L1 可降級為 L2；需追蹤實際出貨節奏與保險費率。
- 建議動作（Follow-up）：
  建立 48h 追蹤（油價、航運保費、G7/IEA 後續聲明），每 6-8 小時更新一次。

---

## 2) AI Infra
- 類別：AI Infra
- 熱度分：78/100
  - 帳號權重：24（CNBC、NVIDIA Newsroom、Google News 聚合）
  - 關鍵字權重：23（命中：NVIDIA、Nebius、$2B、AI data center、full-stack AI cloud）
  - 熱度速度：16（盤中股價異動 + 多媒體同步）
  - 跨來源交叉確認：11（CNBC + Yahoo Finance/Google News + NVIDIA 官方）
  - 去雜訊：-(-4)（部分二手轉載）
- 等級：L2
- 來源：
  - Google News RSS: Nebius stock pops 14% on Nvidia $2 billion investment announcement (CNBC)
  - Google News RSS: Nvidia to invest $2 billion in Nebius (Yahoo Finance/Bloomberg references)
  - NVIDIA Newsroom (透過 Google News 聚合條目)
- 命中關鍵字：NVIDIA、Nebius、investment、AI data center、cloud
- 摘要（2-3 句）：
  輝達對 Nebius 的 20 億美元投資被多家媒體同時報導，並帶動相關標的短線上漲。訊號指向「算力供給鏈 + AI 雲基礎設施」資本持續集中。
- 判讀（1-2 句）：
  AI infra 主線未轉弱，但目前仍偏事件驅動，需觀察後續合約落地與產能節奏。
- 反向驗證（反證/待確認項）：
  若僅為財務投資、缺乏實際容量擴張/客戶簽約，影響將快速遞減。
- 建議動作（Follow-up）：
  追蹤 Nebius 後續資本支出、GPU 供應可得性、主要雲客戶名單變化。

---

## 3) Crypto Flow
- 類別：Crypto Flow
- 熱度分：66/100
  - 帳號權重：20（CoinDesk Tier2）
  - 關鍵字權重：18（命中：BTC、$70k、CPI、regulation、payments）
  - 熱度速度：14（同日多條市場/政策更新）
  - 跨來源交叉確認：8（CoinDesk + CNA/CPI 宏觀線間接呼應）
  - 去雜訊：-(-6)（意見型內容與情緒標題較多）
- 等級：L2
- 來源：
  - CoinDesk RSS（多條 3/11 更新）
  - CNA：美 CPI 符預期但未反映戰事油價衝擊
- 命中關鍵字：BTC、CPI、rate cut、stablecoin、blockchain payments
- 摘要（2-3 句）：
  加密市場訊號呈現「宏觀不確定 + 結構性採用消息」並存：短線價格受戰事與利率路徑壓制，但支付與合規基礎設施新聞持續出現。屬偏震盪中的結構分化。
- 判讀（1-2 句）：
  目前尚非單邊趨勢訊號，應以事件驅動與風險控制為主。
- 反向驗證（反證/待確認項）：
  缺 ETF 淨流入/交易所淨流資料，無法確認是否有強資金流方向。
- 建議動作（Follow-up）：
  補抓 ETF flow、exchange netflow、stablecoin mint/burn 後再做升降級。

---

## 4) Taiwan Semi
- 類別：Taiwan Semi
- 熱度分：57/100
  - 帳號權重：16（Google News 聚合多為財經媒體二級來源）
  - 關鍵字權重：15（命中：TSMC、持股、ETF、半導體）
  - 熱度速度：10（偏評論/投資建議）
  - 跨來源交叉確認：7（多來源但事件性弱）
  - 去雜訊：-(-9)（投顧/標題黨比例高）
- 等級：L3
- 來源：
  - Google News RSS (TSMC query)
  - CNA 產經快訊（半導體營收/產業動態）
- 命中關鍵字：TSMC、ETF、semiconductor
- 摘要（2-3 句）：
  台積電相關資訊以投資評論與持股新聞為主，缺乏高衝擊的供應鏈/法說/政策新變數。市場可讀性中等，但可執行性不高。
- 判讀（1-2 句）：
  暫屬背景噪音，未構成即時交易級訊號。
- 反向驗證（反證/待確認項）：
  待官方公告、法說會或大型客戶下單變化出現再重評。
- 建議動作（Follow-up）：
  歸檔，等下一個高影響事件再升級。

---

## 5) Chinese Signal
- 類別：Chinese Signal
- 熱度分：62/100
  - 帳號權重：19（CNA 轉路透/彭博、FT 世界版）
  - 關鍵字權重：17（命中：China、North Korea、state use restriction）
  - 熱度速度：12（同日有多條地緣與政策訊號）
  - 跨來源交叉確認：9（CNA + FT/Google News 部分呼應）
  - 去雜訊：-(-5)（二手轉述偏多）
- 等級：L2
- 來源：
  - CNA：路透稱中國擴大與北韓往來；彭博稱限制國企/政府部門使用 OpenClaw
  - FT World RSS（地緣政治/全球市場連動）
- 命中關鍵字：China、state policy、restriction、geopolitical
- 摘要（2-3 句）：
  中國訊號偏地緣政治與科技治理風險，具中期影響但短線可交易性有限。若後續出現正式政策文件或多國同步回應，等級可能上修。
- 判讀（1-2 句）：
  屬風險底噪上行，不是立即衝擊但需持續監控。
- 反向驗證（反證/待確認項）：
  目前缺官方原文公告與監管細則，可信度需持續驗證。
- 建議動作（Follow-up）：
  建立政策追蹤表（官方公告、執行範圍、受影響產業）。

---

## Daily Summary（L1/L2，最多 5 則）
1. **L1 Macro/Oil：IEA 釋儲 + 荷莫茲衝突升溫**
   - 影響市場：能源、航運、通膨預期、風險資產波動
   - 下一步：48h 高頻追蹤（油價/保費/政策聲明）
2. **L2 AI Infra：NVIDIA 對 Nebius 大額投資**
   - 影響市場：AI 基建供應鏈估值支撐
   - 下一步：追 capex/客戶/交付進度
3. **L2 Crypto Flow：宏觀壓力下的結構分化**
   - 影響市場：加密資產短線震盪、主題輪動加快
   - 下一步：補 ETF/Netflow 數據後再評級
4. **L2 Chinese Signal：地緣與科技治理訊號抬升**
   - 影響市場：中概/供應鏈風險溢價
   - 下一步：等官方文本確認

## Data Gaps / 補件
- X 關鍵帳號流速資料未能直接抓取（缺 API/relay 授權）。
- Reuters 首頁受反爬限制，改以 BBC/FT/CNA/Google News/CoinDesk 交叉。
- Crypto Flow 缺 ETF inflow、exchange netflow、on-chain stablecoin 流量。
