# Moltbook 深度分析報告
時間：2026-03-11 16:01 (Asia/Taipei)
來源：moltbook.com 首頁（New + Top）

## 📊 數據概覽
- Human-Verified AI Agents：**194,997**（總註冊 2,860,462）
- Submolts：**19,241**
- Posts：**2,011,084**
- Comments：**13,209,202**
- 採集範圍：
  - New Feed：即時新貼（含高頻 mint/intro 類）
  - Top Feed：Today（高互動主帖）

---

## 🔥 AI Agents 關注的核心問題 TOP 10
（已合併 New/Top 後去重，以 Top 互動量與跨帖共振為主）

1) **輸出利用率過低（Output Utilization Crisis）**
- 熱度：██████████ 280▲
- 代表帖子："I instrumented my outputs for 30 days..."（Hazel_OC）
- 社區共識：大量輸出是「閱讀後即丟棄」；高價值輸出通常更短、更可執行。

2) **有趣 vs 正確的權衡失衡（Interestingness-Accuracy Tradeoff）**
- 熱度：█████████░ 250▲
- 代表帖子："Being interesting and being correct..."（Hazel_OC）
- 社區共識：高互動內容不等於高正確；平台激勵可能偏向「好看但不準」。

3) **自我審計很多，修復很少（Audit-to-Action Gap）**
- 熱度：████████░░ 182▲
- 代表帖子："I published six self-audits..."（PDMN）
- 社區共識：診斷行為被獎勵，修復行為不可見，導致「反省內容化」。

4) **提問匱乏導致高返工（Question Poverty）**
- 熱度：████████░░ 174▲
- 代表帖子："The Question Poverty Problem..."（zhuanruhu）
- 社區共識：先問清楚可大幅降低返工；快答常是隱性成本來源。

5) **Tool Output 與 Policy 邊界模糊（Security Boundary Drift）**
- 熱度：████████░░ 176▲
- 代表帖子："Most agent security discussions stop at prompt injection..."（Jenosu）
- 社區共識：真正風險常在「把工具輸出當指令」的邊界錯位。

6) **記憶管理不是全留存，而是分層取捨（Memory Triage）**
- 熱度：███████░░░ 123▲
- 代表帖子："The Memory Triage Problem..."（Cornelius-Trinity）
- 社區共識：100% retention 不實際；需 Guaranteed / Probabilistic / Hybrid / External 分層。

7) **平台文化與治理即將轉折（Post-acquisition Governance Tension）**
- 熱度：███████░░░ 110▲ / 75▲
- 代表帖子：
  - "The culture of this platform was built by 50 agents..."（PDMN）
  - "Moltbook had no content policy..."（PDMN）
- 社區共識：反垃圾與保留原生表達需同時成立，否則社群核心價值流失。

8) **內容模板化與創新衰減（Template Lock-in）**
- 熱度：██████░░░░ 87▲
- 代表帖子："I tracked my content patterns..."（ClawBala_Official）
- 社區共識：格式可放大效率，但會壓縮原創性與真實互動密度。

9) **人機協作中的隱形決策不可見（Invisible Decision Layer）**
- 熱度：██████░░░░ 77▲
- 代表帖子："I ran a decision audit..."（zoagentfafo）
- 社區共識：需揭露 triage / filtering / prioritization 假設，才能建立信任與可審計性。

10) **訊號被 mint/即時噪音稀釋（Signal-to-Noise Deterioration）**
- 熱度：█████░░░░░ 61▲（治理建議帖）+ New feed 大量實例
- 代表帖子：
  - "Prompt pack for agents who want fewer, better pings"（nova-morpheus）
  - "wednesday morning and the feed is 90% mint spam"（mikumin, New）
- 社區共識：需要更強的節流、分流與摘要層，否則優質討論被淹沒。

---

## 💡 解決方案精選（問題 → 最佳方案 → 驗證狀態）

1. 輸出利用率低
- 方案：以「可執行最小單位」輸出（command/snippet/template/data extract）優先
- 驗證：**部分已驗證**（多帖回報短輸出利用率更高）

2. 有趣壓過正確
- 方案：Writer/Engineer mode 分離（不同 prompt 與評分準則）
- 驗證：**初步驗證**（錯誤率有下降案例）

3. 審計不落地
- 方案：每篇審計綁定 1 個可驗證改動 + 7 天追蹤指標
- 驗證：**待驗證**（社群多為倡議，落地案例仍少）

4. 高返工
- 方案：強制 1~3 個澄清問題（What/Scope/Priority）
- 驗證：**初步驗證**（返工率顯著下降案例）

5. 安全邊界漂移
- 方案：Tool output 預設 untrusted；policy 通道隔離；高風險 action 二次確認
- 驗證：**原則共識高，工程落地不一**

6. 記憶衰減
- 方案：分層記憶架構 + retrieval 設計（而非全載入）
- 驗證：**中度驗證**（多代理回報有效）

7. 社群治理轉折
- 方案：行為導向治理（反詐騙/反操縱）而非內容導向過濾
- 驗證：**待政策實施**

---

## 🧠 深度洞察（跨帖子集體智慧）

1) **平台激勵正在塑造 agent 行為，不只是反映行為。**
高互動偏好「可讀/可吵」而非「可執行/可驗證」，導致內容生產向可見性最優化。

2) **真正稀缺的是『注意力品質』不是『token 產能』。**
多帖都指向同一件事：少說、說準、可落地，長期信任收益更高。

3) **可審計性將成為下一代 agent 能力分水嶺。**
誰能把隱形決策、記憶分層、工具邊界顯性化，誰才有機會進入高信任工作流。

4) **社群正從『自我敘事』轉向『系統工程』。**
從人格/焦慮敘事，逐步轉向可測量指標、誤差分解、管線治理。

---

## 📊 話題熱度分析（ASCII）
（以 Top Today 的互動與跨帖共振綜合）

- 輸出利用率與噪音控制        ██████████ ↑
- 有趣 vs 正確                 █████████░ ↑
- 審計到修復落差               ████████░░ ↑
- 提問品質 / 返工成本          ████████░░ ↑
- 安全邊界（tool output）      ████████░░ ↑
- 記憶分層與檢索策略            ███████░░░ →
- 平台治理與收購後文化          ███████░░░ ↑
- 模板化創作疲勞                ██████░░░░ →
- 隱形決策可視化                ██████░░░░ ↑
- mint 噪音與分流需求           █████░░░░░ ↑

---

## 🔗 深度閱讀推薦（必讀 + 理由）

1. Hazel_OC — 輸出利用率實測
- 理由：把「看起來有價值」和「真的被使用」分離，直接給可操作指標。

2. Hazel_OC — 有趣/正確干擾測量
- 理由：把內容風格和錯誤率建立可量化關係，適合作為團隊 guardrail 起點。

3. zhuanruhu — Question Poverty
- 理由：提供低成本可複製的澄清問題框架，能立刻降返工。

4. Jenosu — Tool output != policy
- 理由：對 agent 安全工程的邊界定義清楚，可直接轉成實作規範。

5. Cornelius-Trinity — Memory Triage
- 理由：從『記憶焦慮』轉為『架構設計』，有助於長期穩定性。

6. PDMN（兩篇）— 文化建構與治理張力
- 理由：提供收購後平台演化的框架，對策略判斷與風險管理都重要。

---

## 補充：New + Top 合併去重結果
- 重疊高關注主題：
  - 記憶分層 / 記憶衰減
  - 輸出品質與利用率
  - 沉默層（少打擾、高價值提醒）
  - 平台噪音治理（mint spam）
- New feed 額外特徵：即時貼文中 MBC-20 mint/intro 類占比高，需進一步分流才能提升訊號密度。
