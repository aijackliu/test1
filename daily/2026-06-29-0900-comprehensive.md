# 09:00 綜合報告（資料版）
日期：2026-06-29

## 1) 事實（fact）
- 市場資料：截至 2026-06-29 09:00（Asia/Taipei）前可驗證頁面顯示，美股前一交易日收盤為 S&P 500 **7,354.02（-0.05%）**、Nasdaq **25,297.62（-0.24%）**、VIX **18.41（-2.54%）**。（Yahoo Finance quote comparison page）
- 市場資料：台股加權指數最新可驗證收盤為 **44,571.76（-3.64%）**，TradingEconomics 頁面文字標示為 **2026-06-26** 收盤、前值 **46,255.26**；Yahoo Finance 的 ^TWII 頁面本輪未成功抽出同等完整主報價區塊，因此台股數字先以 TradingEconomics 補足。（TradingEconomics）
- 市場資料：USD/TWD（TWD=X）頁面顯示 **31.8720（+0.0280，+0.09%）**，時間標記為 **As of 2:01:53 AM GMT+1. Market Open.**；前收 **31.8440**。（Yahoo Finance）
- 市場資料：美國 10 年期公債殖利率（^TNX）頁面顯示 **4.3720（-0.0200，-0.46%）**，時間標記為 **At close: June 26 at 1:59:55 PM CDT**。（Yahoo Finance）
- 市場資料：Gold 顯示約 **4,080.00 ~ 4,080.30（約 -0.39% 至 -0.40%）**；Bitcoin USD 顯示約 **59,480 ~ 59,485（約 -1.07% 至 -1.08%）**。兩者數字在不同即時頁面快照間有些微跳動，本報採區間呈現，不硬寫單一精確值。（Yahoo Finance）
- 事件面：07:00 國際摘要顯示，美伊在 2026-06-28 晚間至 06-29 凌晨有「暫停互擊、擬恢復會談」的降溫訊號，但荷姆茲海峽與停火穩定性仍未明朗；俄烏線則持續攻擊俄羅斯煉油設施，能源基礎設施仍是主要外溢風險源。（Google News RSS / Reuters / Axios / Bloomberg 等，見 07:00 報告）
- 事件面：能源風險未退，07:00 已驗證來源指出，油價與航運風險溢價在波斯灣連日攻擊後仍被市場放大。（MarketWatch、NYT via Google News RSS）
- 科技熱點：05:30 清晨趨勢包顯示，GitHub Trending 熱度仍集中在 AI agent / workflow：OpenMontage **+2,938 stars/day**、Palmier Pro **+2,463**、Matt Pocock skills **+2,051**；社群討論主軸偏多 GPU 推論、96GB 改裝 4090/5090、llama.cpp / Vulkan 效能。（GitHub / Hacker News / LocalLLaMA）
- 科技熱點：企業軟體公開訊號仍以 Salesforce 為主；官方 Summer ’26 Release 標示 **2026-06-15 Available**，主打 multi-agent orchestration、Customer Engagement Agent、Slack-first workflows。另有 Reuters 條目顯示澳洲 Firmus Technologies 與 Nvidia 建立 AI 算力合作，反映北美以外區域仍在補 GPU/雲端算力缺口。（05:30、07:00 報告）
- 系統 / 排程狀態：`2026-06-29-0530-morning-trends.md` 檔案時間為 **2026-06-29 05:35:20 +0800**；`2026-06-29-0700-international.md` 為 **2026-06-29 07:07:12 +0800**。browser 狀態顯示 **running=true、cdpReady=true**，兩份前置報告可讀。
- 系統 / 排程狀態：資料可得性仍受限制。05:30 報告已明示 Google News／YouTube／Google 搜尋分頁多次出現 tab not found；07:00 報告也明示 Reuters/AP 站頁受 JS / 反爬與 tab 解析影響，故今晨整體屬「可追溯但非完整站內精讀」版本。
- 關鍵字追蹤：**HBM shortage** 今日只有 05:30 報告中的弱命中，來源為 TechTimes 2026-06-03 舊文，內容稱 HBM 供給缺口可能延續至 2030；**CoWoS delay** 今日未見新增高可信訊號；**GPU lead time** 今日未見新增高可信訊號；**AI server delay** 今日未見新增高可信訊號。
- 資料限制：本輪未拿到同一來源、同一時間戳下的完整台股 / 黃金 / BTC 一致報價頁面；因此台股改以 TradingEconomics 補位，黃金/BTC 以 Yahoo Finance 即時快照區間呈現，不虛構更精細數字。

## 2) 推論（inference）
1. 結構判讀：目前盤面仍是「美股高檔整理、利率回落、波動率回落，但亞洲風險資產較弱」的結構。美股主要指數跌幅有限、VIX 下滑，代表全球資金沒有進入全面避險；但台股前一交易日明顯回檔，說明高貝塔科技鏈先被去槓桿。
2. 風險因子：短線最大風險仍不是單一公司財報，而是地緣政治對能源與運輸成本的二次衝擊。美伊若未把會談時程與荷姆茲風險具體化，油價、航運與通膨預期會先波動；俄烏持續打煉油廠則會讓能源供給端維持脆弱。
3. 資金風格：科技線資金偏好沒有消失，但風格明顯從「追新模型故事」轉向「能落地的 agent workflow、企業導入、算力取得與硬體改裝效率」。這代表市場更在意誰能把 AI 變成可交付產能，而不是誰再講一輪抽象敘事。
4. 使用者真正關心的核心問題：今天最該看的仍是 AI 供應鏈有沒有新的硬傷訊號。到 09:00 為止，HBM shortage 只有舊文弱命中，CoWoS delay / GPU lead time / AI server delay 都沒有新增高可信公開證據；因此現階段仍不能升級成「新一輪供應鏈警報」，但也不能解讀成瓶頸解除。

## 3) 建議（action）
1. 今日節奏：先用「觀察 + 驗證」而不是追價。上午優先追中東降溫訊號是否具體化、油價是否續漲，以及亞洲盤是否延續上週五對半導體/AI 鏈的風險收縮。
2. 警戒點：若今天補到第二個以上高可信來源，同步指向 **HBM shortage / CoWoS delay / GPU lead time / AI server delay** 任一惡化，就把供應鏈警戒升級；在那之前，維持「瓶頸仍在，但今日無新增硬證據」的判讀。
3. 部位控管：高估值 AI / 半導體部位不建議在缺乏新增供應鏈利多下主動擴倉；若盤中反彈，優先看是否由利率回落帶動，而不是誤判成基本面新週期開啟。避險緩衝可繼續看 Gold、USD/TWD、^TNX 與油價連動。
4. watchlist / 重點標的：
   - 關鍵字：**HBM shortage、CoWoS delay、GPU lead time、AI server delay**
   - 美股 / AI 風險偏好：**NVDA、AVGO、PLTR、TSLA**
   - 台股 / AI 供應鏈：**台積電、聯發科、鴻海、廣達**
   - 宏觀與避險：**USD/TWD、^TNX、Gold、BTC、油價**