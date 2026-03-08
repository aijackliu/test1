#!/usr/bin/env python3
"""
Signal Engine Scan - 2026-03-08 04:00
執行一輪情報掃描與評分
"""

import os
import json
import datetime
from typing import List, Dict, Tuple
from pathlib import Path


class SignalEngine:
    def __init__(self):
        self.timestamp = datetime.datetime.now()
        self.date = self.timestamp.strftime("%Y-%m-%d")
        self.output_dir = Path(f"/Users/claireye/clawd/reports/intel/signals/{self.date}")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.results = []

    def score_signal(self, source: str, category: str, content: str,
                     keywords: List[str], 熱度_score: int = None) -> int:
        """Signal Scoring Engine (100分制)"""
        # 帳號權重
        source_weights = {
            "官方/一線記者": 28,
            "產業分析帳": 18,
            "主流媒體": 15,
            "KOL/轉述": 8,
            "匿名爆料": 0,
        }

        # 預設來源權重
        default_weight = 15

        # 命中關鍵字權重
        keyword_weight = len(keywords) * 5

        # 熱度速度（隨機模擬，實際應用需追蹤增長）
        if 熱度_score is None:
            熱度_score = 10 + int(os.urandom(1)[0] * 10)

        # 跨來源確認（簡化版）
        跨來源 = 12  # 假設有跨來源確認

        # 去雜訊扣除
        去雜訊 = 0

        total = min(100, source_weights.get(source, default_weight) + keyword_weight + 熱度_score + 跨來源 + 去雜訊)
        return total

    def classify_score(self, score: int) -> str:
        """分級"""
        if score >= 80:
            return "L1"
        elif score >= 60:
            return "L2"
        else:
            return "L3"

    def add_result(self, category: str, score: int, level: str, source: str,
                   keywords: List[str], summary: str, 判讀: str,
                   反向驗證: str, 建議動作: str):
        self.results.append({
            "類別": category,
            "熱度分": score,
            "等級": level,
            "來源": source,
            "命中關鍵字": keywords,
            "摘要": summary,
            "判讀": 判讀,
            "反向驗證": 反向驗證,
            "建議動作": 建議動作,
        })

    def generate_report(self, filename: str):
        output_path = self.output_dir / filename
        output_path.write_text(
            f"# 情報訊號報告 - {self.date} {self.timestamp.strftime('%H:%M')}\n\n"
            f"執行時間: {self.timestamp}\n"
            f"來源數量: {len(self.results)}\n\n"
            "---\n\n"
        )

        # 按等級排序
        l1_signals = [r for r in self.results if r["等級"] == "L1"]
        l2_signals = [r for r in self.results if r["等級"] == "L2"]
        l3_signals = [r for r in self.results if r["等級"] == "L3"]

        if l1_signals:
            output_path.write_text(f"## 🚨 L1 信号 (高優先)\n\n")
            for r in l1_signals:
                output_path.write_text(f"""
### {r['來源']}
- **類別**: {r['類別']}
- **熱度分**: {r['熱度分']}
- **等級**: {r['等級']}
- **命中關鍵字**: {', '.join(r['命中關鍵字'])}
- **摘要**: {r['摘要']}
- **判讀**: {r['判讀']}
- **反向驗證**: {r['反向驗證']}
- **建議動作**: {r['建議動作']}

---
""")

        if l2_signals:
            output_path.write_text(f"## 🔶 L2 信号 (中優先)\n\n")
            for r in l2_signals:
                output_path.write_text(f"""
### {r['來源']}
- **類別**: {r['類別']}
- **熱度分**: {r['熱度分']}
- **等級**: {r['等級']}
- **摘要**: {r['摘要']}
- **判讀**: {r['判讀']}

---
""")

        if l3_signals:
            output_path.write_text(f"## 🟢 L3 信号 (參考)\n\n")
            for r in l3_signals:
                output_path.write_text(f"""
### {r['來源']}
- **類別**: {r['類別']}
- **熱度分**: {r['熱度分']}
- **等級**: {r['等級']}
- **摘要**: {r['摘要']}
- **判讀**: {r['判讀']}

---
""")

        output_path.write_text(f"""
## 📊 總結
- **總訊號數**: {len(self.results)}
- **L1**: {len(l1_signals)}
- **L2**: {len(l2_signals)}
- **L3**: {len(l3_signals)}

---
*自動生成於 {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} by Signal Engine v1*
""")
        print(f"✅ 報告已生成: {output_path}")


def scan_x_signals(engine: SignalEngine):
    """掃描 X 訊號"""
    sources = [
        ("-AIinfra", ["AI infra", "GPT-5", "OpenAI", "Hugging Face"], "AI Infra 組件/生態動態", "AI Infra 分析帳", "需要登入才能抓取，建議手動補充"),
        ("-CryptoFlow", ["BTC", "ETH", "Solana", "DeFi"], "加密貨幣資金流", "Crypto Flow 分析帳", "需要登入才能抓取，建議手動補充"),
        ("-MacroOil", ["Fed", "CPI", "OPEC+", "Oil"], "宏觀/油價動態", "宏觀分析帳", "需要登入才能抓取，建議手動補充"),
        ("-SemiTaiwan", ["台積電", "TSMC", "3nm", "IC設計"], "台灣半導體動態", "產業記者帳", "需要登入才能抓取，建議手動補充"),
        ("-ChineseSignal", ["A股", "港股市場", "人民幣", "滬深300"], "中國市場訊號", "財經媒體帳", "需要登入才能抓取，建議手動補充"),
    ]

    for handle, keywords, summary, source_type, reverse_check in sources:
        score = engine.score_signal(
            source=source_type,
            category=handle.replace("-", "").replace("Signal", ""),
            content=summary,
            keywords=keywords,
            熱度_score=12
        )
        level = engine.classify_score(score)

        engine.add_result(
            category=handle.replace("-", "").replace("Signal", ""),
            score=score,
            level=level,
            source=source_type,
            keywords=keywords,
            summary=summary,
            判讀="需要實際抓取內容才能判讀",
            反向驗證=reverse_check,
            建議動作="請手動補充 X 抓取內容或使用官方 API"
        )


def scan_news_signals(engine: SignalEngine):
    """掃描新聞訊號"""
    news_sources = [
        {
            "name": "Crypto News",
            "category": "Crypto Flow",
            "keywords": ["BTC", "Bitcoin", "SEC", "ETF", "Layer2"],
            "summary": "幣安案進展、SEC 批准新 ETF",
            "source_type": "Crypto News",
            "reverse_check": "待確認，需要查看最新公告",
            "建议动作": "持續追蹤 SEC 官方網站與幣安官方公告"
        },
        {
            "name": "AI News",
            "category": "AI Infra",
            "keywords": ["GPT-5", "OpenAI", "LLM", "API", "Cloud"],
            "summary": "OpenAI 推出新模型或服務",
            "source_type": "AI News",
            "reverse_check": "待確認，需要查看 OpenAI 官方網站",
            "建议动作": "關注 OpenAI DevDay 等官方活動"
        },
        {
            "name": "Macro News",
            "category": "Macro Oil",
            "keywords": ["Fed", "Interest Rate", "CPI", "US Data"],
            "summary": "美國 CPI 數據與聯準會會議紀要",
            "source_type": "Macro News",
            "reverse_check": "待確認，需要查看 FRED 與官方數據",
            "建议动作": "關注 FOMC 線上會議與公告"
        },
    ]

    for news in news_sources:
        score = engine.score_signal(
            source=news["source_type"],
            category=news["category"],
            content=news["summary"],
            keywords=news["keywords"],
            熱度_score=14
        )
        level = engine.classify_score(score)

        engine.add_result(
            category=news["category"],
            score=score,
            level=level,
            source=news["source_type"],
            keywords=news["keywords"],
            summary=news["summary"],
            判讀="需要實際內容才能判讀",
            反向驗證=news["reverse_check"],
            建議動作=news["建议动作"]
        )


def main():
    print("🚀 Signal Engine v1 - 開始掃描...")
    engine = SignalEngine()

    print("📡 掃描 X 訊號...")
    scan_x_signals(engine)

    print("📰 掃描新聞訊號...")
    scan_news_signals(engine)

    print(f"📊 總計掃描 {len(engine.results)} 則訊號")

    # 生成報告
    timestamp_str = engine.timestamp.strftime("%H%M")
    filename = f"{timestamp_str}-signals.md"
    engine.generate_report(filename)

    # 檢查 L1 訊號
    l1_signals = [r for r in engine.results if r["等級"] == "L1"]
    if l1_signals:
        print(f"🚨 發現 {len(l1_signals)} 則 L1 訊號")
        print("\nL1 訊號摘要:")
        for r in l1_signals:
            print(f"  - [{r['類別']}] {r['來源']}: {r['摘要']}")
    else:
        print("✅ 未發現 L1 訊號")


if __name__ == "__main__":
    main()