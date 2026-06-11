# AI Builders Digest — 2026-06-11 18:00（Asia/Taipei）

今天 builders 圈最明確的訊號：**AI coding / agent workflow 已經從「能不能用」進入「怎麼把它接進真實工作流」的階段。**

## 1) Fable / Claude 類工作流正在往「可直接產出成品」走
- Anthropic 的 Mike Krieger 在最新訪談裡談到，重點已不是第一次試模型有多驚艷，而是**如何把長上下文、背景執行、sub-agents、tool calls、視覺驗證**真正接進日常開發流程。
- Thariq 也公開示範：他用 Fable 讓模型自己剪 launch video，包含轉錄、ffmpeg、色彩調整、Figma MCP、Remotion UI 到渲染，幾乎整條鏈都由 agent 完成。
- 這代表 builder 的競爭力，正從「會不會 prompt」轉成「會不會設計 agent-native workflow」。
- 來源：
  - https://www.youtube.com/watch?v=XWpTgCvgYaE
  - https://x.com/trq212/status/2064826394589442448

## 2) Coding agent 使用量還在加速，不只是新品發布帶動
- OpenAI 的 Thibault Sottiaux 提到，**Codex 過去 48 小時 token consumption 明顯暴增，而且不是因為新產品發布**；這通常代表真實使用者正在把工具塞進更多工作流。
- Peter Yang 也提到，越用 Codex，任務野心會越來越大；這是工具跨過「玩具期」後常見的行為訊號。
- Box 的 Aaron Levie 也補刀：Fable 在 coding 與複雜知識工作上的能力跳升很明顯。
- 來源：
  - https://x.com/thsottiaux/status/2064911328087810308
  - https://x.com/petergyang/status/2064748427892945313
  - https://x.com/levie/status/2064922814688481678

## 3) 下一波不是單點工具，而是「團隊技能資產化」
- Zara Zhang 的觀察很準：未來 agency / 團隊交付物，會越來越像是**一整包給 agent 用的檔案、規則、skill**，而不是一次性素材。
- 她也進一步點出，跨部門團隊應該自己做 skills / agents，像設計團隊把品牌規範封裝成 skill，讓行銷可以直接生成更 on-brand 的產出。
- Garry Tan 轉發的 Nessie 則是另一個方向：**把 ChatGPT / Gemini / Perplexity 的記憶與上下文搬運到其他 agent 系統**，意味著 context portability 正在變成新基建。
- 來源：
  - https://x.com/zarazhangrui/status/2064843560248332577
  - https://x.com/zarazhangrui/status/2064835289559023958
  - https://x.com/garrytan/status/2064947145652994510

## 4) 基礎設施成熟度仍是主戰場：可用性、部署、存取範圍
- Gemini 今天一度 outage，之後恢復，提醒大家：模型再強，**穩定性與服務可用性**仍是企業採用的底線。
- Claude Platform 則上了 scheduled deployments 與 vault 環境變數，代表平台層正持續補齊更接近正式開發流程的能力。
- Google Labs 擴大全球 AI Ultra 5X 訂閱者對 Project Genie 的存取，表示前沿實驗產品正逐步往更廣泛付費用戶滲透。
- 來源：
  - https://x.com/joshwoodward/status/2064762269674918013
  - https://x.com/joshwoodward/status/2064869366290841716
  - https://x.com/claudeai/status/2064741184547795408
  - https://x.com/GoogleLabs/status/2064801929339752527

## 小結
**今天最值得盯的不是單一模型分數，而是：誰先把 context、skills、tooling、deploy、verification 串成一條完整工作流。** 這條鏈一旦穩，AI builder 的產能就不是加法，而是整個團隊流程被重寫。

資料概況：1 集 podcast、18 個 X builders、37 則 tweets、0 篇 blog。原始 feed 產生時間：2026-06-11T08:01:30.493Z。
