# 2026-06-30 05:30 清晨趨勢包

模式：Mode A（資訊彙整型）
資料可得性：中低（X/Threads 公開抓取受驗證頁／登入牆限制；Google News 與 YouTube 可讀，但部分搜尋結果偏聚合頁）

## 1. 核心結論
- GitHub Trending 今日前排同時出現隱私通訊與 agent 工具：simplex-chat 今日 +1,607 stars、agency-agents +1,425、xbtlin/ai-berkshire +1,386、video-use +967。
- Hacker News 與 LocalLLaMA 同步偏向「本地算力／agentic coding」：HN 前排有 Qwen 3.6 27B、本地 agentic coding 模型 Ornith-1.0；LocalLLaMA 高票集中在 96GB 4090/5090、多 GPU 推論、llama.cpp Vulkan。
- OpenClaw 在 YouTube 仍有穩定流量入口；搜尋前排可見 Hung-yi Lee、IBM Technology、Lex Fridman、Metics Media 等長短教學與比較影片。
- 眼鏡線可驗證公開新聞仍由 Meta 主導；Google News 結果顯示 Meta Glasses 近 19 小時仍有中文媒體追蹤，且多篇重複提到自有品牌、299 美元起。
- AI CRM 今日公開訊號偏兩極：一邊是 Salesforce/Agentforce 產品線延續曝光，另一邊是 YouTube 與 Google News 大量轉向 CRM 股價與「AI 是否吃掉 SaaS」討論。

## 2. 分來源重點（GitHub / 社群 / 新聞 / 影音）
### GitHub
- simplex-chat：Haskell 私密通訊網路，總星數 16,470，今日新增 1,607。
- agency-agents：AI agency/多角色 agent 工具集，總星數 118,769，今日新增 1,425。
- xbtlin/ai-berkshire：Claude Code / Codex 多 agent 投研框架，總星數 6,552，今日新增 1,386。
- browser-use/video-use：以 coding agents 做影片編輯，總星數 11,867，今日新增 967。

### 社群
- Hacker News 首位是〈Qwen 3.6 27B is the sweet spot for local development〉，424 points、4 小時前；同頁另有 Ornith-1.0 agentic coding、vLLM Micro-Agent、CUDA kernel 解說。
- V2EX 熱門 AI 相關貼文集中在可用性與成本：可見「DeepSeek 好贵啊」「Claude 闲置号被封」「GPT 今天早上又重置了」「OpenAI 偷偷给部分用户推送 GPT-5.6-sol」。
- LocalLLaMA 日榜前列集中在 96GB 4090/5090 改裝（405 分、269 分）、DeepSeek-V4-Pro、多 GPU inference、llama.cpp Vulkan PR。
- X/Threads 可得性低；XCancel 搜尋 `OpenClaw` 只回驗證頁，Threads 既有 tab 仍停在 Instagram 登入流程，未取得可驗證貼文內容。

### 新聞
- Google News「Meta glasses」結果前列顯示：科技產業資訊室 19 小時前仍在追蹤 Meta 自有品牌 AI 眼鏡；多家中文媒體重複提到售價 299 美元起。
- 同一搜尋頁可見 iThome、TechNews、經濟日報等 6 天內報導，關鍵描述集中在「拿掉 Ray-Ban 品牌」「Meta AI」「即時翻譯／中文支援」「26 種設計」。
- Google News「Salesforce AI CRM」結果前列混有股價新聞，但產品向可驗訊號仍是 iThome 5/26〈Salesforce Headless 360〉與 5/13〈Agentforce Operations〉。
- AI CRM 新聞面代表目前較偏 Salesforce；本輪未抓到 Microsoft Dynamics 365 或 HubSpot 同時效、同可驗度的公開新聞頁。

### 影音
- YouTube 搜尋 `OpenClaw AI agent` 前排可見：Hung-yi Lee〈Dissecting the Lobster... Featuring OpenClaw〉101 萬觀看、3 個月前；IBM Technology〈What is OpenClaw?〉22 萬觀看、2 個月前。
- 同頁另有 Metics Media〈OpenClaw vs Hermes Agent〉7.7 萬觀看、2 週前；Lex Fridman OpenClaw 專訪 128 萬觀看、4 個月前。
- YouTube 搜尋 `AI glasses 2026` 前排影片多為排行榜型內容，反覆出現 RayNeo X3 Pro、HTC VIVE Eagle、INMO Air 3、Meta Ray-Ban Display、Even Realities G2。
- YouTube 搜尋 `AI CRM` 前排同時出現金融評論與產品教學；最新可見影片是 3 天前比較 Salesforce(CRM) 與 ServiceNow(NOW) 的投資向內容。

## 關鍵字命中
- HBM shortage｜TradingKey｜5月11日｜搜尋結果前列提到「HBM 缺貨至 2028 年」與 SK 海力士股價創高。｜Google News 搜尋頁
- HBM shortage｜香港經濟日報 HKET｜28 天前｜搜尋結果提到記憶體短缺恐持續至 2030 年。｜Google News 搜尋頁
- CoWoS delay｜今日未命中（Google News 精確搜尋 `"CoWoS delay"` 無結果）。
- GPU lead time｜今日未命中（未取得可複核公開結果；web_fetch 只拿到 Google News 原始 HTML 骨架，browser 新分頁亦不穩）。
- AI server delay｜今日未命中（Google News 精確搜尋 `"AI server delay"` 無結果）。

## 3. 風險與盲點（資料缺口）
- X/Threads 這輪沒有拿到 primary evidence；XCancel 被驗證頁攔下，Threads 仍缺可用登入態。
- Google News 關鍵字命中偏少，且 HBM shortage 命中多為 5 月／近 28 天舊聞，不代表今天新事件。
- AI CRM 新聞搜尋頁混入大量股價/評論稿，產品層面的新增資訊密度不高。

## 4. 風險與盲點（資料缺口）
- `GPU lead time` 的 browser 新分頁出現 target 不穩；改用 web_fetch 只拿到原始 HTML/CSS，無法當成可驗證正文。
- YouTube `AI glasses 2026` 搜尋前排多為排行榜影片，屬二手整理，不等同官方發表或出貨數據。
- GitHub Trending 可驗的是星數與排名，不能直接推導實際商業採用。

## 5. 手動補件方式（缺什麼資料 + 如何手動取得）
- 缺 X/Threads 原生貼文：請在 Chrome 直接提供 OpenClaw / AI glasses / AI CRM 指定貼文網址或帳號頁截圖。
- 缺 GPU lead time 可驗新聞：請手動開 `https://news.google.com/search?q=%22GPU%20lead%20time%22`，截前 5 則或貼原文連結。
- 缺 AI CRM 官方補強：優先補 Salesforce 官方 release note、HubSpot blog、Microsoft Dynamics 365 blog 的 6 月更新頁。

## 6. 下一步（可執行 1–3 點）
- 先補官方頁：Meta Newsroom / Meta Store、Salesforce release notes，讓眼鏡與 AI CRM 從聚合新聞升級成官方證據。
- 若要做對外版本，可把 OpenClaw YouTube 熱度與 GitHub agent 工具榜整合成「Agent 生態能見度」單段。
- 若 06:30 再跑一次，建議固定用既有 Google News / YouTube tab，避免新開分頁 target 漂移。