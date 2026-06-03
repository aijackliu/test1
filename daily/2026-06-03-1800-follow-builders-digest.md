AI Builders Digest — 2026-06-03

## X / Twitter

### OpenAI / Codex 正在從開發者工具往更廣的 agent 工作台擴張
OpenAI 的 Thibault Sottiaux 提到，Codex 在商業版新增可託管與分享網站、強化 plugins / skills，還能直接在文件、投影片、試算表上用視覺標註回饋 agent。Zara Zhang 補了一個很關鍵的 adoption 訊號：知識工作者已佔 Codex 使用者約 20%，而且採用速度是開發者的 3 倍以上，成長最快的任務類型是 Data Analysis、Research 與 Knowledge Artifacts。Swyx 則延續市場情緒，直接把「one-shot 做出成果」當成 Codex 已進入新階段的證據。
來源：
- https://x.com/thsottiaux/status/2061876999564791952
- https://x.com/zarazhangrui/status/2061924300698091760
- https://x.com/swyx/status/2062062585391014245

### Claude Code 的重點，正在從「會寫 code」升級成「可編排工作流」
Anthropic 的 Thariq 說 workflows 是 Claude Code 自 skills 和 subagents 之後最大的能力升級，特別看好它把非技術任務也納入同一套 agent 工作流。Dan Shipper 也說內部對這件事「有點炸鍋」，代表 builder 圈正在把 workflow orchestration 視為下一個實用分水嶺，而不只是模型又變強一點。
來源：
- https://x.com/trq212/status/2061907538741006796
- https://x.com/danshipper/status/2061908190040645707

### AI app 層的競爭，越來越像「誰能把模型、資料、成本與部署串成完整系統」
Replit CEO Amjad Masad 一邊推企業資料 app 與 Microsoft Fabric 整合，一邊提醒 SWE benchmark 不等於真實 app building 能力，ViBench 這類更貼近成品能力的評測更值得看。Vercel CEO Guillermo Rauch 則把新世界定義成「YES-CODE」：code 不再稀缺，平台價值轉向讓 agent 能輕鬆部署、不中途畢業。Box CEO Aaron Levie 進一步點出，token 成本上升後，model routing 會成為 applied AI 的核心護城河，因為多數企業根本無法自己把不同工作流路由到最佳成本/品質模型層。
來源：
- https://x.com/amasad/status/2061893093696434578
- https://x.com/amasad/status/2061878314311266552
- https://x.com/rauchg/status/2061934154732974376
- https://x.com/levie/status/2061974298760495132

### Google 與 builder 市場的另外兩個訊號：推理介面普及，單點 SaaS 壓力加大
Google Labs 的 Josh Woodward 宣布 Gemini 的 Thinking Levels 已在 Web、iOS、Android 全面可用，代表「推理深度控制」正在成為主流產品層能力，不再只是實驗功能。Peter Yang 的判斷更直接：大型 enterprise SaaS 可能還好，但窄場景、單功能 SaaS 會越來越難收費，因為 AI skills 與帶記憶的 agents 已經能用更彈性、更個人化的方式吃掉這些需求。
來源：
- https://x.com/joshwoodward/status/2062025667852812583
- https://x.com/petergyang/status/2061846283263103274

### OpenClaw / agent infra 繼續往 enterprise 與可驗證性走
Peter Steinberger 提到 OpenClaw 正在補 observability 與 verifiable workspaces，也已和 Microsoft 合作把 agent 能力帶進 enterprise。這類訊號的含義很明確：下一輪 agent 平台比的不是 demo 感，而是企業能不能審計、驗證、放進正式流程。
來源：
- https://x.com/steipete/status/2061877813053907083
- https://x.com/steipete/status/2061874084649025728

## Podcasts

### Training Data: Knowing What Your Customers Want, All the Time — Alfred Wahlforss（Listen Labs）
這集最值得記的不是「AI 可以做市場研究」，而是 Alfred Wahlforss 對未來 bottleneck 的判斷：當 build 變便宜，真正稀缺的是知道「該 build 什麼」。Listen Labs 想做的是把使用者訪談變成可規模化、可追溯、可模擬的系統：先用 AI 同步跑大量語音訪談，再把訪談資料變成可預測特定客群反應的 simulation layer，最後甚至讓其他 coding agents 直接調用，形成「問人 -> 找洞察 -> 修產品」閉環。

他有一句話很準："as we get closer to AGI, it will be easier to build things, but the hard part will know what to build." 另一個值得注意的點是，他們認為最有價值的資料不是一般行為資料，而是設計良好的深度訪談資料，因為那更能還原人怎麼想、怎麼選、怎麼改變主意。對 builder 來說，這其實是在提醒：未來差異化不只來自更強的生成，而是誰更接近真實使用者偏好，並能把這些偏好接進 agent loop。
來源：
- https://www.youtube.com/watch?v=Rumft-rsEu4

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
