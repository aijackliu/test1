# AI Builders Digest — 2026-06-09

## X / Twitter

### Swyx（Latent Space / Cognition / DXTips）
Swyx 轉推並強調 METR_Evals / Cognition 推出的 FrontierCode，核心訊號很明確：AI coding 的評測標準正在從「能不能 pass tests」往「能不能交出可維護、可合併的程式碼」升級。他點出超過一半的 SWEBench 結果其實是無法 merge 的 slop，而 FrontierCode 把 rubric、code quality 與 anti-cheat 一起拉進來，代表 2026 年 agentic coding 的瓶頸已不只是解題，而是穩定把抽象目標落成可維護工作流。
來源：https://x.com/swyx/status/2064081945567580323

### Josh Woodward（Google / Google Labs / Gemini）
Josh Woodward 介紹 NotebookLM 的兩個實用更新：一是搜尋不再只限於你自己的 source files，二是能直接產生 PDF、DOCX、XLSX、PPTX 與圖表等輸出格式。這個方向很像把 NotebookLM 從「研究助理」再往「可交付產物引擎」推一步，重點不是只會整理資料，而是能把研究結果直接包裝成團隊可用文件。
來源：https://x.com/joshwoodward/status/2064046368352825492

### Boris Cherny（Anthropic / Claude Code）
Boris Cherny 談 Claude Code 上線一年後的使用方式變化：他更常用 auto mode 而不是 plan mode，並把 routines 當成日常除錯與預防性修復的一部分。這背後的訊號是，coding agent 正從「偶爾叫來幫忙的工具」變成持續在背景運作的 workflow layer，甚至讓手機成為主要互動入口之一。
來源：https://x.com/bcherny/status/2064034799711588805

### Thibault Sottiaux（OpenAI / Codex & ChatGPT）
Thibault Sottiaux 連續丟出幾個 Codex 操作介面相關貼文，最值得注意的是他直接問「有人開始寫 nested loops 了嗎？」這很像在試探新一代 agent workflow：不只是單層 prompt 呼叫，而是讓 agent 去調度 agent、把 loop 套 loop，往更高層的自動化編排走。
來源：https://x.com/thsottiaux/status/2064226958494572727

### Peter Yang（AI builder educator）
Peter Yang 抓到兩個很真實的 builder 痛點：第一，手機上的 Codex 體驗需求正在上升，代表大家開始把 AI 助手當成隨身介面，而不是桌機限定工具；第二，$200 月費訂閱用戶與企業 API 成本控管用戶，實際上在形成兩套完全不同的最佳實踐。前者偏向把模型能力用滿，後者更在意 routing、節流與 ROI。
來源：https://x.com/petergyang/status/2064204735671124073
來源：https://x.com/petergyang/status/2064063499517743417

### Aaron Levie（Box CEO）
Aaron Levie 提醒一個很重要但常被忽略的現實：再強的模型也不能取代 context。本質上，只要同一個模型要服務律師、工程師、分析師或醫療人員，instruction、domain context 與專有資料就不可能消失；也因此，真正有價值的 applied AI 仍會出現在那些能把抽象 intelligence 包成可直接上手工作流的產品層。
來源：https://x.com/levie/status/2064186766907887941

### Zara Zhang（Follow Builders）
Zara Zhang 說「新的世界可能是 Markdown、HTML、SVG」，點出一個很 builder 的方向：未來很多 AI 產物不一定是傳統 app UI，而是更輕、更可組裝的文字與圖形格式。這也呼應近期不少 agent 工具往文件、可視化與直接可交付 artefacts 靠攏的趨勢。
來源：https://x.com/zarazhangrui/status/2064108976565092706

### Nikunj Kothari（FPV Ventures）
Nikunj Kothari 對「autonomous 公司最近一波密集出現」的觀察很到位：即使加上各種 loops，last mile 仍然難，但他認為這個缺口會在接下來幾個月快速縮小。這句話的含義是，市場共識已從懷疑 agent 能不能用，轉向觀察它什麼時候能跨過最後一哩、真正吃到 production workload。
來源：https://x.com/nikunj/status/2063981835290562692

### Sam Altman（OpenAI CEO）
Sam Altman 發出 OpenAI 當前計畫連結，雖然貼文本身沒有展開細節，但它在 builders 圈的訊號仍然偏強：OpenAI 正持續把產品路線與平台整合敘事拉回到中心位置，讓外界重新以「完整系統規劃」而不只是單次模型發布來看待後續節奏。
來源：https://x.com/sama/status/2064088940932641225

## 官方部落格

### Claude Blog
**Building intelligent apps for Apple platforms with Claude in the Foundation Models framework**
Anthropic 宣布推出新的 Swift package，讓 Apple 開發者可以在 Apple 的 Foundation Models framework 裡，把 on-device model 與 Claude 串成同一條工作流：簡單任務留在本地裝置處理，遇到多步推理、程式生成、web search 或資料分析，再無縫 hand off 給 Claude。這篇最重要的不是「Claude 支援 Apple 平台」本身，而是它把 model routing 正式產品化成開發者框架：同一個 SwiftUI 體驗裡，typed output、streaming、tool calls 都能接回來，代表混合式 AI app 的工程門檻正在下降。
來源：https://claude.com/blog/claude-for-foundation-models

## Podcasts

### No Priors — Building an AI Guardian for Enterprise with Onyx Security CEO Maxim Bar Kogan
這集最有價值的主線，是把 enterprise AI 的焦慮從「員工會不會把資料貼進 chatbot」升級成「agent 已經開始替你做事，但誰來盯著它」。Onyx Security CEO Maxim Bar Kogan 的核心觀點很直接：企業現在沒辦法阻止 agent adoption，只能建立控制層，降低 agent 做出錯誤或不合法動作的機率。重點不是再多一個 human-in-the-loop，而是用更小、更專用的模型先做快速守門，只在高風險時刻才叫更強的 agent 介入，平衡成本、延遲與可靠性。

他也點出一個對 builders 很重要的結論：現有 security stack 很多時候看得到行為，卻不知道「為什麼這個 agent 現在要這樣做」，而這正是 AI 時代的新安全缺口。簡單說，未來企業要的不是更嚴的權限鎖，而是能理解 agent 意圖、歷史行為與上下文的 control plane。這跟最近整個 agent ecosystem 的方向很一致：模型能力在變強，但真正開始值錢的，是 orchestration、guardrails、context 與 governance。
來源：https://www.youtube.com/watch?v=QDsbFLEt9ro

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
