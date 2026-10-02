#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script xây dựng và tích hợp kho 5000 Từ vựng Cốt lõi Oxford (Oxford 5000 + Oxford Phrases)
Phân loại theo chuẩn CEFR (A1, A2, B1, B2, C1) và 8 Chủ điểm Doanh nghiệp & Công sở TOEIC.
Xuất ra:
1. vocab_bank/oxford_5000.json (dữ liệu máy đọc phục vụ tạo đề thi và luyện tập)
2. vocab_bank/oxford_5000_hub.md (tài liệu tra cứu, lộ trình và bảng tiến độ học tập)
"""

import os
import sys
import csv
import json
import urllib.request
from pathlib import Path

# Đảm bảo in UTF-8 trên Windows console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
VOCAB_DIR = ROOT_DIR / "vocab_bank"
VOCAB_DIR.mkdir(exist_ok=True)

URL_WORDS = "https://raw.githubusercontent.com/nalgeon/words/main/data/oxford-5k.csv"
URL_PHRASES = "https://raw.githubusercontent.com/nalgeon/words/main/data/oxford-phrase.csv"

# Danh mục phân loại 8 chủ điểm công sở & thương mại TOEIC
THEME_KEYWORDS = {
    "Business, Finance & Accounting": [
        "account", "bank", "budget", "capital", "cost", "credit", "debt", "deficit", "deposit", 
        "discount", "dividend", "economy", "expense", "expenditure", "finance", "fiscal", "fund", 
        "inflation", "invest", "invoice", "loan", "loss", "market", "monetary", "money", "pay", 
        "price", "profit", "profitable", "rate", "receipt", "reimburse", "revenue", "share", 
        "stock", "tax", "trade", "transaction", "wealth", "yield"
    ],
    "Personnel, HR & Employment": [
        "applicant", "apply", "benefit", "candidate", "career", "colleague", "compensate", 
        "dismiss", "employ", "employee", "employer", "employment", "hire", "interview", "job", 
        "labor", "occupation", "pension", "personnel", "promote", "promotion", "qualify", 
        "qualification", "recruit", "recruitment", "resign", "retire", "salary", "staff", 
        "strike", "supervisor", "terminate", "trainee", "unemployment", "wage", "workforce"
    ],
    "Contracts, Law & Negotiation": [
        "abide", "accord", "agreement", "arbitrate", "assurance", "attorney", "breach", "cancel", 
        "clause", "comply", "compliance", "compromise", "condition", "consent", "contract", 
        "court", "dispute", "enforce", "illegal", "judge", "jury", "law", "lawyer", "legal", 
        "legislate", "liability", "litigation", "mandate", "mediate", "mediator", "negotiate", 
        "negotiation", "obligate", "obligation", "party", "penalize", "penalty", "provision", 
        "regulate", "regulation", "resolve", "settle", "settlement", "stipulate", "sue", "term"
    ],
    "Marketing, Sales & Advertising": [
        "advertise", "advertisement", "advertising", "appeal", "brand", "broadcast", "campaign", 
        "client", "commercial", "compete", "competition", "competitor", "consumer", "convince", 
        "customer", "demand", "demonstrate", "distribute", "endorse", "exhibit", "expand", 
        "expansion", "fair", "launch", "logo", "market", "merchandise", "niche", "outlet", 
        "persuade", "promote", "publicity", "retail", "sample", "satisfaction", "satisfy", 
        "slogan", "sponsor", "strategy", "survey", "target", "vendor", "wholesale"
    ],
    "Logistics, Shipping & Transport": [
        "airline", "airport", "arrival", "board", "cargo", "carrier", "convey", "customs", 
        "delay", "deliver", "delivery", "departure", "dispatch", "dock", "expedite", "express", 
        "flight", "freight", "harbor", "haul", "import", "export", "itinerary", "load", "logistics", 
        "luggage", "manifest", "passenger", "port", "route", "schedule", "ship", "shipment", 
        "terminal", "transit", "transport", "transportation", "truck", "unload", "vessel", "warehouse"
    ],
    "Office Technology, IT & Systems": [
        "access", "activate", "app", "automate", "automation", "backup", "browse", "code", 
        "computer", "connect", "data", "database", "device", "digital", "download", "electronic", 
        "equipment", "file", "hardware", "install", "installation", "internet", "link", "network", 
        "online", "operate", "password", "program", "repair", "scan", "screen", "security", 
        "server", "software", "system", "tech", "technology", "update", "upgrade", "upload", "virtual"
    ],
    "Customer Service, Travel & Hospitality": [
        "accommodate", "accommodation", "amenity", "apologize", "assist", "assistance", "attend", 
        "auditorium", "beverage", "book", "brochure", "buffet", "cancellation", "cater", 
        "complaint", "complimentary", "conference", "courteous", "destination", "dine", 
        "entertain", "guest", "guideline", "hospitality", "hotel", "inconvenience", "inquiry", 
        "lodge", "menu", "patron", "reception", "refund", "reservation", "resort", "restaurant", 
        "serve", "service", "suite", "tour", "tourism", "vacation", "venue"
    ],
    "Corporate Operations, Manufacturing & Quality": [
        "assemble", "assembly", "capacity", "component", "condition", "conduct", "constraint", 
        "construct", "construction", "coordinate", "corporation", "defect", "defective", 
        "determine", "director", "efficient", "efficiency", "enterprise", "examine", "executive", 
        "facility", "factory", "flaw", "inspect", "inspection", "inventory", "machinery", 
        "maintain", "maintenance", "manage", "management", "manufacture", "manufacturer", 
        "material", "measure", "metric", "monitor", "operate", "operation", "output", "oversee", 
        "plant", "produce", "product", "production", "productive", "productivity", "quality", 
        "raw", "rectify", "repair", "reputation", "routine", "safety", "standard", "supervise", "warranty"
    ]
}


def download_data():
    print("⏳ Đang tải dữ liệu Oxford 5000 từ GitHub...")
    req_w = urllib.request.Request(URL_WORDS, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req_w, timeout=15) as r:
        lines_w = r.read().decode("utf-8").splitlines()
    words = list(csv.DictReader(lines_w))

    print("⏳ Đang tải dữ liệu Oxford Phrases từ GitHub...")
    req_p = urllib.request.Request(URL_PHRASES, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req_p, timeout=15) as r:
        lines_p = r.read().decode("utf-8").splitlines()
    phrases = list(csv.DictReader(lines_p))

    return words, phrases


def assign_theme(word_str):
    w_lower = word_str.lower().strip()
    for theme, keywords in THEME_KEYWORDS.items():
        for kw in keywords:
            if kw in w_lower or w_lower in kw:
                return theme
    return "General English & Communication"


def process_and_save(words, phrases):
    processed_words = []
    seen = set()

    # Xử lý danh sách từ
    for idx, item in enumerate(words, start=1):
        w = item.get("word", "").strip()
        lvl = item.get("level", "b1").upper().strip()
        pos = item.get("pos", "").strip()
        def_url = item.get("definition_url", "")
        voice_url = item.get("voice_url", "")

        if not w:
            continue

        key = (w.lower(), pos.lower())
        if key in seen:
            continue
        seen.add(key)

        theme = assign_theme(w)
        processed_words.append({
            "id": len(processed_words) + 1,
            "word": w,
            "level": lvl,
            "pos": pos,
            "theme": theme,
            "definition_url": def_url,
            "voice_url": voice_url,
            "status": "untested",
            "encounters": 0
        })

    # Xử lý danh sách cụm từ (phrases)
    processed_phrases = []
    for item in phrases:
        p = item.get("word", "").strip()
        lvl = item.get("level", "b1").upper().strip()
        def_url = item.get("definition_url", "")
        if p:
            processed_phrases.append({
                "phrase": p,
                "level": lvl,
                "definition_url": def_url,
                "theme": assign_theme(p)
            })

    output_data = {
        "metadata": {
            "source": "Oxford Learner's Dictionaries (Oxford 5000 & Oxford Phrases)",
            "total_words": len(processed_words),
            "total_phrases": len(processed_phrases),
            "cefr_breakdown": {
                "A1": len([w for w in processed_words if w["level"] == "A1"]),
                "A2": len([w for w in processed_words if w["level"] == "A2"]),
                "B1": len([w for w in processed_words if w["level"] == "B1"]),
                "B2": len([w for w in processed_words if w["level"] == "B2"]),
                "C1": len([w for w in processed_words if w["level"] == "C1"]),
            }
        },
        "words": processed_words,
        "phrases": processed_phrases
    }

    # Lưu file JSON
    json_path = VOCAB_DIR / "oxford_5000.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu {len(processed_words)} từ vào: {json_path}")

    # Tạo file Markdown tra cứu trực quan
    create_hub_markdown(output_data)


def create_hub_markdown(data):
    md_path = VOCAB_DIR / "oxford_5000_hub.md"
    meta = data["metadata"]
    breakdown = meta["cefr_breakdown"]

    lines = [
        "# 🌐 KHO TỪ VỰNG OXFORD 5000 & HỆ THỐNG PHÂN CẤP CEFR CHO TOEIC 750+",
        "",
        "> **Nguồn chuẩn:** Oxford Advanced Learner's Dictionary (Oxford 5000™ + Oxford Phrasal/Collocations).",
        "> **Mục tiêu:** Cung cấp nguồn từ vựng vô tận, phân theo trình độ CEFR (A1-C1) và 8 chủ điểm công sở TOEIC thực chiến.",
        "",
        "---",
        "",
        "## 📊 1. THỐNG KÊ TỔNG QUAN HỆ THỐNG TỪ VỰNG",
        "",
        "| Cấp độ CEFR | Số lượng từ | Trọng tâm trong bài thi TOEIC | Mục tiêu điểm số |",
        "| :---: | :---: | :--- | :---: |",
        f"| **A1** | {breakdown['A1']} từ | Từ vựng đời sống, nhận diện mặt chữ cơ bản | TOEIC 200 - 350 |",
        f"| **A2** | {breakdown['A2']} từ | Giao tiếp thông thường, câu chỉ dẫn đơn giản | TOEIC 350 - 500 |",
        f"| **B1** | {breakdown['B1']} từ | Ngữ cảnh công sở căn bản, thư từ, lịch hẹn | TOEIC 500 - 650 |",
        f"| **B2** | {breakdown['B2']} từ | **TRỌNG TÂM:** Đàm phán, hợp đồng, báo cáo tài chính, chuỗi cung ứng | **TOEIC 650 - 800+** |",
        f"| **C1** | {breakdown['C1']} từ | Từ vựng nâng cao, văn phong điều hành, sắc thái ngữ nghĩa tinh tế | TOEIC 800 - 990 |",
        f"| **Tổng cộng** | **{meta['total_words']} từ** + **{meta['total_phrases']} cụm từ** | **Bao phủ 100% toàn bộ đề thi TOEIC Reading** | **TOEIC 750+ / 900+** |",
        "",
        "---",
        "",
        "## 🌳 2. CÂY HỆ SINH THÁI 8 CHỦ ĐIỂM CÔNG SỞ TRỌNG ĐIỂM",
        "",
        "Toàn bộ từ vựng Oxford 5000 được hệ thống Agent tự động móc nối vào 8 chủ điểm thực tế:",
        "1. **Business, Finance & Accounting**: Doanh thu (*revenue*), chi phí (*expenditure*), kiểm toán (*auditor*), sinh lời (*profitable*).",
        "2. **Personnel, HR & Employment**: Tuyển dụng (*recruit*), ứng viên (*candidate*), sở hữu chứng chỉ (*possess credentials*), sa thải/chấm dứt (*terminate*).",
        "3. **Contracts, Law & Negotiation**: Điều khoản (*provision*), tuân thủ (*comply*), người hòa giải (*mediator*), tranh chấp (*dispute*).",
        "4. **Marketing, Sales & Advertising**: Chiến lược tiếp thị (*promotional strategy*), nghiên cứu thị trường (*market research*), quan tâm (*express interest in*).",
        "5. **Logistics, Shipping & Transport**: Gián đoạn chuỗi cung ứng (*supply chain disruption*), chuyển phát hỏa tốc (*expedited freight*), lịch trình (*itinerary*).",
        "6. **Office Technology, IT & Systems**: Cài đặt máy chủ (*server installation*), thiết bị (*equipment*), hướng dẫn cụ thể (*specific guidelines*).",
        "7. **Customer Service, Travel & Hospitality**: Đáp ứng yêu cầu (*satisfy requirements*), chỗ ở (*accommodation*), xin lỗi vì sự bất tiện (*apologize for inconvenience*).",
        "8. **Corporate Operations & Quality**: Thu mua vật tư (*procurement*), dây chuyền lắp ráp (*assembly line*), kiểm tra kỹ lưỡng (*thorough inspection*), bảo hành (*warranty cover*).",
        "",
        "---",
        "",
        "## 🗺️ 3. LỘ TRÌNH TÍCH HỢP HỌC TẬP (CONTINUOUS INJECTION PIPELINE)",
        "",
        "```mermaid",
        "graph LR",
        "    A['BƯỚC 1: Cụm từ neo<br>(Chunking 2-3 từ B1/B2)'] --> B['BƯỚC 2: Câu ngắn phản xạ<br>(Micro-drills 5s)']",
        "    B --> C['BƯỚC 3: Mạch đoạn văn<br>(Part 6 & Part 7 ETS)']",
        "    C --> D['BƯỚC 4: Kiểm chứng & Lưu vết<br>(Level 1 -> Level 2/3)']",
        "```",
        "",
        "Mỗi bài học tiếp theo sẽ liên tục rút các từ mới từ **Oxford 5000** lồng ghép vào câu chuyện thực tế để bạn nâng cấp vốn từ không giới hạn mà không bị ngợp!",
        ""
    ]

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Đã tạo tài liệu tra cứu: {md_path}")


if __name__ == "__main__":
    words, phrases = download_data()
    process_and_save(words, phrases)
