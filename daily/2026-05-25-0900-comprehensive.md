# 09:00 綜合報告（資料版）
日期：2026-05-25

## 1) 事實（fact）
- 市場資料
  - 台股：TWSE `發行量加權股價指數歷史資料` 顯示，最近一個可驗證收盤為 `2026-05-22`，收於 `42,267.97`，當日高低為 `42,357.60 / 41,447.92`。`2026-05-25 09:00` 當下尚無今日收盤資料。
  - 美股：Stooq 顯示 `S&P 500` 於 `2026-05-22 23:00:00` 收於 `7,473.50`，區間 `7,463.30–7,506.30`；`NASDAQ` 收於 `26,343.97`，區間 `26,309.80–26,504.55`。
  - 匯率：Stooq 顯示 `USD/TWD` 最近可驗證報價為 `2026-05-22 10:00:04`，收於 `31.4934`，區間 `31.4641–31.5532`。
  - BTC：Stooq 顯示 `BTC/USD` 於 `2026-05-25 03:01:41` 報 `77,028.02`，區間 `76,082.58–77,214.01`。
  - Gold：Stooq 顯示 `XAU/USD` 於 `2026-05-25 03:01:40` 報 `4,570.12`，區間 `4,542.50–4,579.40`。
  - 利率：本輪未取得可機器驗證的即時 `US 10Y` 精確數值；官方 Treasury 日報頁可達，但 exact row 未成功抽出，屬資料缺口。
- 事件面
  - `07:00 國際事務摘要` 顯示：BBC 於 `2026-05-24 20:26 GMT` 報導 Trump 要求美方談判代表「不要急於」與伊朗達成協議；Google News 同時反映市場已在交易「可能接近協議」情境，油價相關報導轉弱。
  - BBC 於 `2026-05-24 16:50 GMT` 報導俄羅斯對烏克蘭發動大規模攻擊，已知至少 `4` 人死亡、數十人受傷。
  - BBC 於 `2026-05-24 19:49 GMT`、Reuters 於 `2026-05-24 20:45 GMT` 指向同一方向：土耳其鎮暴警察進入主要反對派辦公室，政爭升級。
  - BBC 於 `2026-05-24 22:11 GMT` 報導，巴基斯坦俾路支省列車爆炸襲擊至少造成 `20` 人死亡。
  - 同時段系統/排程狀態：`2026-05-25-0530-morning-trends.md` 與 `2026-05-25-0700-international.md` 均已產出；`browser` 當前狀態為 `running=true / cdpReady=true`。但依 `2026-05-25` daily log，今晨 `browser` 新開動態頁快照不穩；Threads 自動發布仍受 `OAuthException code 190` 阻塞，`browser profile=user` 仍不可作為備援。
- 科技熱點
  - GitHub Trending 前排仍由 AI coding / agent infra 佔據：`Understand-Anything`（`3,987 stars today`）、`codegraph`（`2,993 stars today`）、`claude-plugins-official`（`1,179 stars today`）。
  - `VisionClaw` 的 arXiv 摘要與 GitHub README 都明示 `Meta Ray-Ban smart glasses + Gemini Live + OpenClaw` 的可穿戴代理鏈。
  - Salesforce 官方文 `8 Ways AI Agents Are Evolving in 2026`（`2026-05-01`）重點為 `deterministic guardrails`、`context engineering`、`headless CRM access`、`observability stack`。
  - TrendForce `2026-04-15` 指出：general server 關鍵零組件交期拉長，全年 server 出貨成長預估由接近 `20% YoY` 下修至約 `13% YoY`；`PCBs` 與 `CPUs` 交期已接近 `1 年`，`PMIC` 由 `21–26 週` 拉長至 `35–40 週`，`BMC` 由 `11–16 週` 拉長至 `21–26 週`；AI server `2026` 出貨仍估成長約 `28% YoY`，但 `Meta`、`AWS` 等 ASIC 專案存在出貨延遲風險。
  - 固定追蹤關鍵字：
    - `HBM shortage`：有新增公開命中。Google News RSS 近 7 日可見 Tom’s Hardware `2026-05-21` 與 Wccftech `2026-05-19` 皆直接以 HBM shortage 為題；今晨趨勢包另引 GPUnex 指出缺口可能延續至 `2028–2029`。
    - `CoWoS delay`：今日未見新增高可信訊號。可驗證到的是 TrendForce/TSMC 對 CoWoS 擴產與 roadmap 的描述，未驗證到新的 delay 事件。
    - `GPU lead time`：有既有高可信訊號，TrendForce `2026-04-15` 明示多項 server 關鍵零件 lead time 顯著拉長，`PCBs/CPUs` 接近 `1 年`；但 Google News RSS 近 7 日未見新增同級別一手命中。
    - `AI server delay`：有既有高可信訊號，TrendForce `2026-04-15` 明示 AI server 中 `ASIC-based` 專案存在 shipment delay 風險；Google News RSS 近 7 日未見新增同級別一手命中。

## 2) 推論（inference）
1. 結構判讀
   - 現在不是「AI 需求有沒有」的問題，而是「高毛利 AI 供應鏈優先吃掉產能，其他 server 與配套零件被擠壓」的結構。這對供應鏈判讀代表：上游先進封裝、HBM、電源/管理 IC、先進製程設備仍強；通用 server 與非優先料號交付壓力更大。
2. 風險因子
   - 宏觀端短線是兩股力同時拉扯：中東若朝協議推進，油價與風險溢價有下修空間；但俄烏、土耳其、巴基斯坦三條地緣風險線同時升溫，代表避險需求不會完全消失。市場若今天亞洲盤偏強，延續性仍要看油價與美元/債券反應。
3. 資金風格
   - 從 `BTC 77,028.02`、`Gold 4,570.12` 同時維持高位，加上美股大盤仍在高檔，可讀成「風險偏好未退，但資金也在保留避險倉」。這通常不是全面 risk-on，而是偏向大型主線、確定性高的 AI/半導體資產續強，對交期長、驗證慢、量產節奏有疑問的次主線更挑剔。
4. 使用者真正關心的核心問題
   - 對 jack 來說，今天最重要的不是追新聞，而是確認：`HBM shortage / GPU lead time / AI server delay` 這三條老風險還在不在。答案是：還在，而且目前新增資料沒有推翻舊框架；`CoWoS delay` 則沒有新增高可信惡化訊號，較接近「仍緊但未見新的壞消息」。

## 3) 建議（action）
1. 今日節奏
   - 先用「供應鏈確認」而不是「題材追價」開盤。上午優先看台股 AI/半導體鏈是否由先進封裝、記憶體、電源管理、伺服器 ODM 帶動；若只是題材股普漲但權值與供應鏈核心沒表態，先視為情緒盤。
2. 警戒點
   - 盯三個即時訊號：`油價是否續跌`、`BTC 是否站穩 77k 上方`、`台股開盤後能否守住前一交易日強勢區間`。若油價轉彈、BTC 失守、台股強勢股開高走低，代表今天更像短線風險交易，不宜把早盤強勢誤判成新主升。
3. 部位控管
   - 不要把 `CoWoS delay` 當成今天的新交易主軸，因為目前沒有新增高可信惡化證據。真正該保守的是交期已拉長、出貨節奏受驗證拖慢的鏈條；若手上有依賴 general server 復甦或 ASIC 專案快速放量的部位，今天應降低預期、用反彈檢視減碼點。
4. watchlist / 重點標的
   - 上游供應鏈：`TSMC / SK hynix / Micron / Samsung`，重點看 HBM、先進封裝、CoWoS 擴產節奏有無新增公告。
   - 美股/海外鏈：`NVDA / MU / MRVL / AVGO / PLTR`，看市場是否繼續偏好有實單、有平台位階、能穿越交期問題的公司。
   - 台股鏈：優先看 `台積電 / 聯電 / 世界先進 / 力積電` 與 AI server、電源管理、封裝相關族群的量價是否同步。
   - 待補資料：`US 10Y` 即時精確值、`CoWoS delay` 一手新訊、X/Threads 原文社群訊號；這三項若中午前補到，建議再做一次午間增補版。
