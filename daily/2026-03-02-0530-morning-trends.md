# 05:30 清晨趨勢包（2026-03-02）

## 1) 核心結論（3–5 點）
- GitHub 今日熱度集中在 **AI Agent 基礎設施**（編排、沙盒、記憶、工具整合），非單一模型能力競賽。
- 熱門 repo 同時出現「陪伴型 AI（airi）」與「感測/隱私導向 AI（wifi-densepose）」，代表應用面正在往互動與現實場景分化。
- Hacker News 討論焦點落在 **MCP、生產力代理、終端/開發工具鏈**；高分題多與「AI 進入日常工程流」相關。
- 新聞來源可得性不均：The Verge 可讀但混雜即時貼文；Reuters/CNBC 在目前抓取條件下訊息受限，需標註資料缺口。
- 社群與影音來源（X/Threads/YouTube）在無登入或 JS 限制下可得資訊偏低，今日判讀信心低於技術來源（GitHub/HN）。

## 2) 分來源重點（GitHub / 社群 / 新聞 / 影音）
### GitHub
- `moeru-ai/airi`：20,619★，今日 +736。
- `ruvnet/ruflo`：17,498★，今日 +766（Claude/Codex 多代理編排定位）。
- `alibaba/OpenSandbox`：3,588★，今日 +1,179（Agent 執行沙盒基建熱度高）。
- `NevaMind-AI/memU`：12,171★，今日 +323（24/7 agent 記憶層）。
- `X-PLUG/MobileAgent`：7,781★，今日 +190（GUI agent 持續有關注）。

### 社群（Hacker News / V2EX / X / Threads）
- HN 最高熱度之一：`Microgpt`（1763 points），仍是核心討論主題。
- HN 高互動議題：`WebMCP early preview`（232 points / 130 comments）、`When does MCP make sense vs CLI?`（338 points / 217 comments）。
- HN 工程流題目升溫：`If AI writes code, should the session be part of the commit?`（116 points / 138 comments）。
- V2EX hot 分頁僅回傳站點框架資訊，未取得有效熱門主題清單。
- X / Threads：本次流程未取得可驗證即時流（資料缺口，見下節）。

### 新聞（科技 / 財經）
- The Verge 科技版可讀到 MWC 2026 裝置流：Lenovo 3D 概念機、AMD Strix Halo 筆電、Honor 可動態雲台手機等，顯示硬體端在「AI + 新形態互動」持續推進。
- Reuters 科技頁：因 JS/反爬限制，未取得可用新聞條目。
- CNBC 科技頁：僅取得頁尾與訂閱資訊，未抓到有效 headline。

### 影音（YouTube）
- YouTube Trending 頁面僅回傳「YouTube」標題，未取得影片列表（疑似動態渲染/地區與登入限制）。

## 3) 風險與盲點（資料缺口）
- **來源可得性不均**：GitHub/HN 資訊完整；V2EX/YouTube/Reuters/CNBC 受 JS、反爬、登入或版面限制影響。
- **社群偏差風險**：缺少 X/Threads 即時流時，社群樣本會偏向工程師圈（HN/GitHub）。
- **新聞交叉驗證不足**：主流財經快訊今天可用樣本不足，難做跨媒體一致性檢查。

## 4) 下一步（可執行 1–3 點）
1. 改用 browser relay（可交互）補抓 V2EX 熱門列表、YouTube Trending 影片清單、X/Threads 可見趨勢。
2. 增加一組可直接抓取的新聞備援（如 AP/BBC/FT 可讀頁），降低單一站點反爬風險。
3. 對 HN + GitHub 熱點建立「連續 3 日」追蹤欄位（stars/day、comments/day），避免單日噪音誤判。

---
資料時間：2026-03-02 13:57（Asia/Taipei）
可得性等級：中（技術來源高；社群/影音/部分新聞低）
