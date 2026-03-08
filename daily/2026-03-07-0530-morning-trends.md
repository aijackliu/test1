# 05:30 清晨趨勢包（2026-03-07）

## 1) 核心結論（3–5 點）
- GitHub Trending 仍由 AI Agent/AI 應用主導，`airi` 今日新增 **2,544 stars**、`openai/skills` **582 stars**、`seomachine` **675 stars**。
- Hacker News 高互動議題集中在「就業/經濟壓力」與「AI 安全」：如就業衰退貼文 **471 分 / 331 留言**、全球暖化貼文 **841 分 / 826 留言**、Firefox 安全合作貼文 **374 分 / 111 留言**。
- 科技新聞面向顯示「AI 進入企業與資安落地」：TechCrunch/Ars 同步出現 AI 工具鏈、Firefox 漏洞挖掘、Workspace CLI 與 AI 整合。
- 財經新聞短期風險升高：CNBC RSS 顯示油價本週上漲 **35%**、美國 2 月非農 **-92,000**、失業率 **4.4%**，市場波動與避險情緒上升。
- 社群可見性不均：X/Threads/YouTube 熱門榜在本輪抓取可讀內容不足，清晨包以可驗證來源（GitHub/HN/RSS）為主。

## 2) 分來源重點（GitHub / 社群 / 新聞 / 影音）
### GitHub
- `moeru-ai/airi`：總星 **29,422**、今日 **+2,544**，自託管 AI companion 類型持續吸引開發者。
- `openai/skills`：總星 **11,858**、今日 **+582**，顯示「可組裝能力（skills）」仍是開發焦點。
- `TheCraigHewitt/seomachine`：總星 **2,093**、今日 **+675**，AI + SEO 自動化內容工作流熱度升。
- `inclusionAI/AReaL`：今日 **+348**，LLM reasoning / agent 訓練框架維持上升。

### 社群（Hacker News / V2EX / X / Threads）
- Hacker News：
  - 「Tech employment now significantly worse…」**471 分 / 331 留言**。
  - 「Global warming has accelerated significantly」**841 分 / 826 留言**。
  - 「Hardening Firefox with Anthropic's Red Team」**374 分 / 111 留言**。
- V2EX（hot API 可讀）：熱門高回覆主題偏生活與消費決策（如汽車/關係/家庭互動），技術硬核議題占比相對低。
- X：`/explore/tabs/trending` 抓取回傳「Something went wrong」，無法取得可驗證趨勢榜單。
- Threads：首頁僅取得品牌殼層文字，無法提取具體趨勢貼文。

### 新聞（科技 / 財經）
- TechCrunch：
  - 「Anthropic’s Claude found 22 vulnerabilities in Firefox over two weeks」。
  - 「Microsoft, Google, Amazon… Claude remains available to non-defense customers」。
- Ars Technica：
  - 報導 Google Workspace CLI 可與 AI 工具整合（含 OpenClaw 相關工作流）。
- CNBC RSS：
  - 油價週漲幅 **35%**（文中稱 1983 年以來期貨交易最大單週升幅）。
  - 美國 2 月非農 **-92,000**、失業率 **4.4%**。

### 影音（YouTube）
- `https://www.youtube.com/feed/trending` 本輪僅回傳「YouTube」字樣，未取得可驗證影片清單。
- 目前影音趨勢判斷不足，需改走瀏覽器互動或已登入上下文補抓。

## 3) 風險與盲點（資料缺口）
- `web_search` 工具本輪不可用（缺 Brave API key），限制了跨媒體搜尋覆蓋率。
- Reuters 網頁在本輪觸發 JS/反爬檢查（401 提示需啟用 JS），無法納入即時國際新聞交叉驗證。
- X/Threads/YouTube 熱門區對未登入或自動抓取不友善，社群與影音側存在可見性偏差。
- V2EX 使用 hot API 可取數，但社群結構偏中文生活議題，對全球技術趨勢代表性有限。

## 4) 下一步（可執行 1–3 點）
- 以 browser relay（Chrome）補抓：YouTube Trending、X Explore、Threads 搜尋頁，建立「可截圖驗證」版本。
- 新增一組穩定 RSS 來源（FT/WSJ/AP/路透替代鏡像）做財經交叉比對，降低單一媒體偏差。
- 若 06:30 前可取得社群登入態，補發「社群熱詞 TOP10 + 來源連結」增量更新版。
