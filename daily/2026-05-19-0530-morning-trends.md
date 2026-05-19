# 2026-05-19 05:30 清晨趨勢包

資料可得性：中

## 1. 核心結論
- 開源 Agent／工具鏈仍是今晨最強主軸。GitHub Trending 前段幾乎被 openhuman、CLI-Anything、各類 agent skills 包辦。
- 社群訊號正在分化成兩條線：一條是「AI 真的開始進產品與手機端」（OpenAI Codex mobile、Salesforce × Google Cloud）；另一條是「AI 焦慮加劇」（HN 與 V2EX 都在討論 AI 對工作與公司判斷的扭曲）。
- 眼鏡／穿戴方向仍偏早期關注期。YouTube 有穩定流量，但今晨可驗證來源以內容討論為主，未抓到同等強度的官方新品公告。
- AI CRM 正從「聊天助手」往「跨系統執行」移動。Salesforce 與 Google Cloud 已把重點放在 Slack、Google Workspace、Gemini Enterprise 與 CRM 的端到端流程串接。
- AI 硬體瓶頸沒有消失。今晨有 HBM / CoWoS / GPU lead time 相關命中，但部分來源只能驗證到搜尋結果或產業文章，不能當成全面即時行情。

## 2. 分來源重點

### GitHub
- `tinyhumansai/openhuman` 登上 Trending 前列，主打「Personal AI super intelligence」，顯示個人化 AI assistant 仍是高熱題材。
- `HKUDS/CLI-Anything`、`academic-research-skills`、`scientific-agent-skills` 同時上榜，說明市場熱點不只在模型，還在 agent-native CLI 與技能封裝。
- `openclaw` GitHub 公開頁顯示主 repo 約 373k stars、Skill Directory 約 8.7k stars；OpenClaw 生態已不只是單 repo，而是工具＋技能目錄一起被消費。

### 社群
- Hacker News 前排出現兩種對比：一邊是 `WinCE64 – Windows CE 2.11 for N64` 這類硬核技術玩具；另一邊是 `I believe there are entire companies right now under AI psychosis`，代表 AI 採用已進入反思期。
- V2EX 最熱 AI 相關話題集中在「AI IDE 誰比較能用」「AI 時代程式員被分成兩類」「實習生過度依賴 AI 要不要過」，重點不是新模型，而是職場適應與能力分層。
- XCancel 可驗證訊號：OpenAI 5/14 宣布 Codex 開始預覽進入 ChatGPT 手機 App，可在手機上啟動、審核、批准 coding 任務；Anthropic 5/14 則連發地緣 AI 領導權論文與 Gates Foundation 2 億美元合作。
- Threads 可驗證公開頁：`@wjsfinance` 的 HBM 貼文（頁面時間可讀到 `2026-01-04T03:36:31Z`）主張 2026 年 HBM 產能已接近提前被訂光，記憶體正從低價零件轉成下游設計約束。

### 新聞
- Salesforce 官方部落格〈8 Ways AI Agents Are Evolving in 2026〉把焦點放在 deterministic guardrails、context engineering、MCP、headless CRM、observability，重點是讓 agent 更能在 production 落地。
- Google Cloud × Salesforce 官方新聞稿（Cloud Next '26）宣布把 Agentforce、Gemini Enterprise、Slack、Google Workspace 串成可執行的跨平台流程；其中 `Gemini-Powered Reasoning for Agentforce` 標示為 2026 年 5 月可用。
- OpenClaw 官方文件可驗證兩件事：一是 browser 已被定位成隔離式 agent-only browser；二是官方把 snapshot / stable-tab / stale-ref recovery 明確產品化，代表 browser automation 正從技巧變成標準操作層。
- 台灣產業文章《【產業洞察】2026 AI 伺服器先進封裝爆發：HBM 與 CoWoS 量測測試的台廠新戰場》提到 CoWoS 月產能目標、HBM3E/HBM4 與封裝後測試壓力，顯示瓶頸已延伸到量測與良率管理。

### 影音
- YouTube「AI open source LLM」今晨前列結果包含：`Top 10 Open Source LLMs In 2026`（3 小時前）、`Codex + Ollama = Free Unlimited Coding AI`（3 天前）、`OpenClaw Free Forever with Local LLM AI Model Setup`（1 個月前）。短期熱點仍是開源模型與本地部署。
- YouTube「AI smart glasses」前列結果集中在 `Wait... Smart Glasses are Suddenly Good?`、`The Flaw with Smart Glasses Design`、`Googles New AI Glasses Are The Future`，顯示關注點偏體驗評測與產品判斷，不是明確新品落地潮。
- YouTube「AI CRM agentic」前列結果以 `CRM Applications Reimagined with AI and Agentic Capabilities`、`How to Build AI CRM Agents that Automate your CRM` 為主，說明影音內容已開始把 CRM 從 SaaS 介面討論，轉成 agent workflow 討論。

## 3. 關鍵字命中
- **HBM shortage｜命中**
  - 來源：Threads 公開頁 `@wjsfinance`
  - 時間：2026-01-04T03:36:31Z（頁面可讀）
  - 摘要：貼文主張 2026 年 HBM 產能幾乎提前被訂光，記憶體正在變成下游產品設計與 AI 體驗上限的核心約束。
  - 連結：https://www.threads.com/@wjsfinance/post/DTEuvgRks_K/
- **CoWoS delay｜部分命中**
  - 來源：JZTEK 產業文章
  - 時間：今晨抓取於 2026-05-19 05:33（Asia/Taipei）
  - 摘要：文章未直接寫出「delay」，但明確把 CoWoS 良率、封裝後測試與量產時程列為 AI 伺服器量產關鍵瓶頸。
  - 連結：https://jztek.com.tw/%E3%80%90%E7%94%A2%E6%A5%AD%E6%B4%9E%E5%AF%9F%E3%80%912026-ai-%E4%BC%BA%E6%9C%8D%E5%99%A8%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%E7%88%86%E7%99%BC%EF%BC%9Ahbm-%E8%88%87-cowos-%E9%87%8F%E6%B8%AC%E6%B8%AC/
- **GPU lead time｜命中（搜尋結果層級）**
  - 來源：Google 搜尋結果 → Fusion Worldwide
  - 時間：今晨抓取於 2026-05-19 05:33（Asia/Taipei）
  - 摘要：搜尋結果摘要顯示 Blackwell 價格上升 15–23%，lead times 延長至 3–7 個月；但原文頁面被 access restriction 擋下，未完成原文複核。
  - 連結：https://www.fusionww.com/insights/gpu-shortage-and-price-increases-in-2026
- **AI server delay｜今日未命中**
  - 目前未抓到可直接驗證、且明確使用此關鍵詞的公開來源。

## 4. 風險與盲點（資料缺口）
- Reuters 科技/商業頁面被 JS／anti-bot 擋下，只回 `Please enable JS`，因此今晨新聞段落偏向官方公告與可讀公開頁。
- XCancel 用 `web_fetch` 取文失敗（403），改以 browser 公開頁驗證；可讀到貼文內容，但抓取穩定性不如官方 API。
- Threads 雖有部分公開頁可讀，但今晨只完成單篇 HBM 貼文驗證；更廣泛的 Threads 趨勢仍不足。
- YouTube 結果可讀，但屬搜尋結果頁，不等於平台總榜；能驗證的是「查詢下的可見熱門結果」，不是全站 trending。
- 智慧眼鏡方向今晨沒有同等強度的官方新品新聞，只能保守寫成「內容關注持續」，不能擴寫成新一波正式發布潮。

## 5. 手動補件方式（缺什麼資料 + 如何手動取得）
- 缺：Reuters / 一線媒體即時科技與財經原文。
  - 原因：JS 渲染與反爬限制。
  - 手動補法：提供文章連結或截圖，我可補成更完整的新聞段落。
- 缺：Threads 更完整的 AI / 眼鏡 / CRM 討論面。
  - 原因：公開搜尋可得性有限，且不是所有貼文都能穩定開啟。
  - 手動補法：提供指定帳號、關鍵字或貼文連結，我可再做二次整理。
- 缺：YouTube 全站 trending 與中文區分眾榜單對照。
  - 原因：今晨只做主題搜尋結果驗證。
  - 手動補法：若你要更像「榜單監控」，可指定頻道清單或提供 trending 截圖。

## 6. 下一步（可執行 1–3 點）
- 把今晨主軸收斂成一句話：**Agent 開始進入手機端與企業流程，但硬體供應鏈與組織治理仍是落地上限。**
- 若要延伸成對外貼文，最值得寫的角度是：**OpenAI 手機端 Codex、Salesforce × Google Cloud、OpenClaw browser automation，三條線都在指向「agent 從 demo 走向操作層」。**
- 若要做投資／產業版追蹤，建議今天補抓：HBM / CoWoS / GPU 交期的一線原文，否則硬體段落仍應維持「中等可得性」標記。