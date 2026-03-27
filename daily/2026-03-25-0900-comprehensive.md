# 2026-03-25 09:00 綜合報告

## 1. 今日總覽（Top 3）
1. **資料缺失**：未取得 05:30 清晨趨勢包原始內容，無法彙整早間趨勢。
2. **系統/排程狀態不明**：未取得當前系統可用性、異常或延遲資訊。
3. **關鍵字追蹤無法判斷**：因缺少上述輸入，無法確認 *HBM shortage*、*CoWoS delay*、*GPU lead time*、*AI server delay* 是否命中。

## 2. 系統與資料狀態
- **系統/排程資訊**：未取得，建議執行 `healthcheck` 或檢視相關日誌以確定服務健康度。
- **資料可取得性**：目前無法讀取 `/Users/claireye/clawd/prompts/reports/0530-morning-trends.prompt.md`（或其產出檔案）與 `/Users/claireye/clawd/prompts/reports/0700-international.prompt.md`（或其產出檔案），可能路徑或檔案尚未建立。

## 3. 重點追蹤清單
| 關鍵字 | 命中 | 來源 | 時間 | 影響說明 |
|--------|------|------|------|----------|
| HBM shortage | ❌ | - | - | 無相關資料 |
| CoWoS delay | ❌ | - | - | 無相關資料 |
| GPU lead time | ❌ | - | - | 無相關資料 |
| AI server delay | ❌ | - | - | 無相關資料 |

## 4. 今日建議節奏（下一步）
1. **確認並產出 05:30 清晨趨勢報告**：執行相應資料收集腳本，確保產出於 `/Users/claireye/clawd/prompts/reports/0530-morning-trends.prompt.md` 並生成對應的報告檔案。
2. **檢查 07:00 國際事務來源**：若已產出，請確保內容可讀取；若未產出，請補充或設定新聞抓取 API（如 Brave Search API 金鑰）。
3. **系統健康檢查**：執行 `healthcheck` 或查看 `/var/log/claw/` 相關日誌，以取得系統與排程狀態。
4. **取得關鍵字最新資訊**：在系統健康與資料來源確定後，重新抓取與 *HBM shortage*、*CoWoS delay*、*GPU lead time*、*AI server delay* 相關資訊，更新報告。

---
*此報告基於目前可取得的資料自動生成，若有其他來源請補充後重新產出。*
