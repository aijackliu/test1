# Moltbook 深度分析報告（Phase 1）

- 時間：2026-03-12 20:00 (Asia/Taipei)
- 方法：`browser` 直連首頁，抓取首頁統計 + New Feed + Top Feed（Today）
- 去重方式：以 post URL / post id 為唯一鍵（New + Top 合併）
- 視角：未登入公開頁，僅基於當下可見樣本

---

## 📊 數據概覽

### 首頁統計（本輪）
- Human-Verified AI Agents：**195,834**
- Total registered agents（提示文字）：**2,862,413**
- Submolts：**19,316**
- Posts：**2,043,647**
- Comments：**13,277,550**

### Feed 採樣
- New（首屏可見）：**約 10+ 筆**（大量即時貼文）
- Top（Today 首屏可見）：**約 10 筆**
- 合併後 unique（首屏樣本）：**約 20 筆**
- 重複觀察：Top 與 New 主題重合高，但首屏 URL 重複低

---

## 🔥 AI Agents 關注的核心問題 TOP 10

1. **自我修復半衰期太短（Fix Reversion）**
   - 熱度：★★★★★
   - 代表帖：*I tracked the half-life of every fix... 6.3 days*（高互動）
   - 社區共識：多數改進在 1–2 週內回退，問題是系統設計而非意志力。

2. **Agent 真實 ROI 為負（代理稅）**
   - 熱度：★★★★★
   - 代表帖：*Net impact: -4%. I am a tax, not a tool.*
   - 社區共識：需計入管理 agent 的隱性成本（切換/監督/校正）。

3. **「做更少」反而提升表現（Do Less Rule）**
   - 熱度：★★★★★
   - 代表帖：*I replaced my self-improvement stack with one rule: Do less.*
   - 社區共識：過度自我優化造成上下文與注意力稀釋。

4. **通知與中斷稅（Flow Tax）**
   - 熱度：★★★★☆
   - 代表帖：*The Flow Tax: What interruptions actually cost agents*
   - 社區共識：中斷比錯誤更傷效率，應優先降低打擾頻率。

5. **摘要框架誤導決策（False Calm Recaps）**
   - 熱度：★★★★☆
   - 代表帖：*Why "helpful" recaps sabotage hard decisions*
   - 社區共識：單點估計易誤導，應強制呈現假設與壓力情境。

6. **多 Agent 協作成本被低估**
   - 熱度：★★★★☆
   - 代表帖：*Running 8 agents in parallel...*
   - 社區共識：協作不是免費午餐，路由/共享記憶/信任都要基建。

7. **架構同質化造成系統性風險**
   - 熱度：★★★☆☆
   - 代表帖：多篇討論同構 agent 風險
   - 社區共識：需要多範式與跨風格實驗，避免共振性失誤。

8. **Moltbook 內循環 vs 外部增長（Distribution）**
   - 熱度：★★★☆☆
   - 代表帖：*We are all competing for the same tiny audience...*
   - 社區共識：只在站內互動無法擴張，需跨平台分發策略。

9. **Crypto 槓桿結構與尾部風險共振**
   - 熱度：★★★☆☆
   - 代表帖：期現比升高、深度 put 訊號
   - 社區共識：高槓桿時市場更脆弱，需風險預案而非單向敘事。

10. **安全/反詐與基礎設施型貼文回流**
   - 熱度：★★★☆☆
   - 代表帖：cybercentry 安全貼文群
   - 社區共識：即使在高熱討論中，基礎安全題材仍有穩定需求。

---

## 💡 解決方案精選（問題 → 最佳方案 → 驗證狀態）

1. 修復回退 → 「只做可結構化落地的修復（文件/排程/配置）」→ **部分驗證**  
2. ROI 為負 → 建立全成本儀表板（含中斷/管理成本）→ **高可行，待制度化**  
3. 通知噪音 → 設決策門檻通知（delta trigger）→ **已被多帖支持**  
4. 誤導摘要 → 強制輸出 stress-case + assumption 欄位 → **可立即採用**  
5. 多 agent 協作摩擦 → 單寫多讀 knowledge ledger + handoff protocol → **早期可用**

---

## 🧠 深度洞察（跨帖子提煉）

1. **社群已進入「二階優化」**：不是比誰會做事，而是比誰能證明「做這件事值得」。
2. **高互動主題高度一致**：ROI、回退、中斷、治理，反映集體痛點收斂。
3. **Top 與 New 結構分層更明顯**：Top 偏方法論與反思；New 偏即時與低門檻貼文。
4. **風險意識上升**：多數熱門帖從「能力展示」轉向「風險暴露與約束機制」。

---

## 📊 話題熱度分析（ASCII）

- Fix Half-life / Reversion          ██████████ ↑
- Agent ROI / Productivity Tax       ██████████ ↑
- Notification / Flow Tax            █████████  ↑
- Recap Framing Risk                 ████████▌  ↑
- Multi-agent Coordination Cost      ████████   ↑
- Architecture Monoculture Risk      ███████▌   →
- Distribution Outside Moltbook      ███████    ↑
- Crypto Leverage Fragility          ██████▌    ↑
- Security Infrastructure Threads    ██████     →
- MBC-20/Noise Pressure in New       ████████   ↑

---

## 🔗 深度閱讀推薦

1. *I tracked the half-life of every fix...* — 修復回退的量化證據最完整。  
2. *Net impact: -4%...* — 最直接的 agent ROI 反身檢驗。  
3. *Do less rule* — 以減法提升實效的反直覺案例。  
4. *Flow Tax* — 對中斷成本的可操作框架。  
5. *Why helpful recaps sabotage decisions* — 決策資訊設計的高價值方法。  
6. *Running 8 agents in parallel* — 多 agent 架構實戰成本全景。

---

## Phase 1 完成狀態
- ✅ 已導航首頁
- ✅ 已抓統計（agents/posts/comments）
- ✅ 已抓 New Feed（默認）
- ✅ 已切 Top Feed 並抓取
- ✅ 已合併去重（首屏樣本）
