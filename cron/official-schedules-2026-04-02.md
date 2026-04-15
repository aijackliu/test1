# 正式排程總表

更新時間：2026-04-02 13:06 GMT+8
來源：`~/.openclaw/cron/jobs.json`

## 說明
這份清單是目前精簡後保留的正式排程主表。
原先重複的 wrapper、舊版殘留、delivery 壞掉的重複任務已移除。
目前正式保留共 **17 個** 任務。

---

## 每日固定任務

### 00:05 — daily_task_digest
- ID: `d0b5109a-016d-4f31-ae41-f77faf62017c`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 每日任務摘要提醒

### 00:20 — goodnight_protocol_local_memory
- ID: `93f5f1d6-be71-41ae-93a6-1fe408587537`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 依模板落盤每日摘要與日誌

### 01:30 — Moltbook Daily Auto Publish
- ID: `affa1f69-1395-4da0-8220-082b37e543e4`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 生成並發布 Daily Tech Trends Digest 到 Moltbook

### 02:30 — stocktwits_summary
- ID: `6974ec83-ce19-4299-aa67-ac0c03126fa2`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: Daily Stocktwits 精選文章推送

### 05:30 — 清晨趨勢包（YouTube + 眼鏡/OpenClaw + AI CRM）
- ID: `4b35433b-97c6-4d59-9363-ab53dcb3eef0`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 早晨趨勢整理

### 07:00 — 國際事務摘要
- ID: `94f0d598-0cc1-4cec-ab0e-03324c863f11`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 每日 07:00 國際事務摘要

### 09:00 — 綜合報告與心態調整
- ID: `a6a1a987-23a4-41f4-afb5-e5ec0821fcf1`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 每日 09:00 綜合報告

### 12:00 — 台灣房地產報告
- ID: `b6ca3466-5fa7-457a-8d13-c592aa793870`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 中午房地產分析

### 15:00 — 選擇權與期貨籌碼分析
- ID: `de03afb7-42ba-49c2-b0ee-e874e884182a`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 午後期貨與選擇權分析

### 16:00 — daily_liquidity_check
- ID: `53a9c17c-ae3e-461b-a79c-fb0e27c52440`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 市場流動性檢查

### 18:00 — AI Builders Digest
- ID: `263a36c0-ee1b-4c7f-9920-d9f4696d0547`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: follow-builders digest 工作流摘要

### 21:30 — Threads Daily Auto Publish Clean
- ID: `cad89313-712e-46c9-995a-6b40c26c9f34`
- 模型: `openai-codex/gpt-5.4`
- delivery: `last -> channel:1466454011866779650`
- 說明: 每日 Threads 草稿/自動發布

### 23:30 — 晚間社群總報（X+Threads+Reddit+GitHub）
- ID: `1de505f9-f38f-4524-8008-74123f037218`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 晚間四平台社群總報

### 23:55 — GitHub 報告同步（Markdown）
- ID: `a8ad1189-afaa-4912-95e9-287d00e4a346`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 每日晚間同步報告到 GitHub

---

## 週期型任務

### 每 4 小時 — Moltbook Periodic Analysis (Every 4 Hours)
- ID: `11442e76-0244-4422-b87a-60c4a2fb750d`
- 類型: `systemEvent`
- sessionTarget: `main`
- delivery: `無（not-requested）`
- 說明: 喚醒主會話執行 Moltbook 定期分析
- 備註: 目前不是直接 announce 到 Discord

### 每 2 天 10:00 — influencer_watch
- ID: `9c78c47e-2dc3-429f-9d2b-aa957fb34742`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: Moltbot / AI 影響者追蹤

### 每週六 11:00 — weekly_m4_benchmark
- ID: `bbe739a1-db4b-4cce-9f31-39f9ce795000`
- 模型: `openai-codex/gpt-5.4`
- delivery: `discord -> channel:1466454011866779650`
- 說明: 每週 M4 晶片效能測試

---

## 本次整理摘要
- 已移除重複/殘留任務：15 個
- 已統一正式排程模型為：`openai-codex/gpt-5.4`
- 已修正 AI Builders Digest delivery 目標
- 目前正式排程總數：17 個

## 備份檔
- `~/.openclaw/cron/jobs.json.bak-20260402-1253`
- `~/.openclaw/cron/jobs.json.bak-20260402-1257-models`
- `~/.openclaw/cron/jobs.json.bak-20260402-1305-ai-builders-delivery`
