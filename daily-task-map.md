# Daily Task Map（由 Muse 接手重整）

更新時間：2026-03-29 10:24 Asia/Taipei

## 目的
把每日固定任務整理成單一可信來源，避免以下問題再次發生：
- 報告有產物，但找不到生成器
- crontab、記憶、任務摘要三套不一致
- API 失敗卻被誤記成成功
- 任務漏跑後沒有明確補跑與告警機制

---

## 一、目前接手後的基準任務清單

### 每 4 小時
- 04:00｜Moltbook 深度分析
- 08:00｜Moltbook 深度分析
- 12:00｜Moltbook 深度分析
- 16:00｜Moltbook 深度分析
- 20:00｜Moltbook 深度分析

### 每日
- 00:05｜每日任務摘要
- 01:30｜Moltbook Daily Publish
- 02:00｜Moltbook 深度分析（每日版）
- 02:30｜Stocktwits 摘要
- 05:30｜清晨趨勢包
- 06:40｜Tavily Daily Digest
- 07:00｜國際事務摘要
- 09:00｜綜合報告
- 10:00｜影響者追蹤（每 2 天節奏）
- 12:00｜台灣房地產報告
- 12:10｜Daily Report Check
- 15:00｜選擇權與期貨籌碼分析
- 16:00｜流動性監控
- 21:30｜Threads 每日自動發布
- 23:30｜晚間社群總報
- 23:55｜GitHub 報告同步

### 每週
- 週更｜M4 晶片效能測試

---

## 二、任務狀態分級
- **已接手 / 可控**：腳本、產物、成功條件都明確
- **半可控**：已有 prompt 或產物，但尚未統一入口
- **待重建**：只有歷史產物或記憶，還沒有新基準腳本

---

## 三、目前已接手 / 可控
- 01:30｜Moltbook Daily Publish
  - 腳本：`scripts/moltbook_daily_publish.sh`
  - 狀態：已修正成功/失敗判斷；遠端 API 500 時會如實報錯
- 21:30｜Threads 每日自動發布
  - 腳本：`scripts/threads_daily.sh` + `scripts/threads_post.sh`
  - 狀態：已修正 draft 內容與發布流程
- 12:10｜Daily Report Check
  - 腳本：`scripts/daily_report_check.sh`
  - 狀態：存在，但目前是 checker，不是 generator

---

## 四、目前半可控（優先重建）
- 05:30｜清晨趨勢包
  - 產物：`reports/daily/YYYY-MM-DD-0530-morning-trends.md`
  - Prompt：`prompts/reports/0530-morning-trends.prompt.md`
- 07:00｜國際事務摘要
  - 產物：`reports/daily/YYYY-MM-DD-0700-international.md`
  - Prompt：`prompts/reports/0700-international.prompt.md`
- 09:00｜綜合報告
  - 產物：`reports/daily/YYYY-MM-DD-0900-comprehensive.md`
  - Prompt：`prompts/reports/0900-comprehensive.prompt.md`
- 15:00｜選擇權與期貨籌碼分析
  - 產物：`reports/daily/YYYY-MM-DD-1500-options-futures-chip.md`
  - 狀態：今天確認缺檔，現納入新可控鏈重建

### 重建原則
1. 每個任務都要有唯一生成入口
2. 每個任務都要有固定輸出路徑
3. 每個任務都要有成功條件（檔案存在 + 內容非空 + 關鍵段落齊全）
4. 任務失敗時要能被 checker 或 log 明確抓到

---

## 五、待重建
- 00:05｜每日任務摘要
- 02:00｜Moltbook 深度分析（每日版）
- 02:30｜Stocktwits 摘要
- 10:00｜影響者追蹤
- 12:00｜台灣房地產報告
- 15:00｜選擇權與期貨籌碼分析
- 16:00｜流動性監控
- 23:30｜晚間社群總報
- 23:55｜GitHub 報告同步
- 週更｜M4 晶片效能測試

---

## 六、今天（2026-03-29）已知事件
- 05:30 清晨趨勢包：有生成
- 07:00 國際事務摘要：原本未自動生成，已手動補產
- 09:00 綜合報告：原本未自動生成，已手動補產
- 01:30 Moltbook Daily Publish：有執行，但遠端 API 500，發布失敗

---

## 七、接手策略
從今天起，以這份文件作為新的單一真相來源（single source of truth）。
後續所有任務調整，優先更新：
1. 本文件
2. 對應腳本
3. 對應 checker / cron

禁止再出現只有記憶、沒有腳本；只有產物、沒有入口；只有 cron、沒有成功判斷的情況。
