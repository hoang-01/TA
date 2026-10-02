#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TOEIC Reading CLI Assistant
Quản lý lộ trình, nhật ký sửa lỗi (Error Logs), sổ tay từ vựng và khung Prompt hỏi AI Agent.
"""

import os
import sys
import json
import random
import argparse
from datetime import datetime, date
from pathlib import Path

# Đảm bảo in UTF-8 mượt mà trên Windows console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
PROFILE_FILE = ROOT_DIR / "profile.json"
ERROR_LOGS_DIR = ROOT_DIR / "error_logs"
VOCAB_DIR = ROOT_DIR / "vocab_bank"
MY_VOCAB_FILE = VOCAB_DIR / "my_vocab.md"
COLLOCATIONS_FILE = VOCAB_DIR / "business_collocations.md"
WORDS_600_FILE = VOCAB_DIR / "toeic_600_words.json"
WORDS_600_MD = VOCAB_DIR / "toeic_600_words.md"
GRAMMAR_DIR = ROOT_DIR / "grammar_bank"
MY_GRAMMAR_FILE = GRAMMAR_DIR / "my_grammar.md"
TEMPLATE_FILE = ERROR_LOGS_DIR / "TEMPLATE.md"


def load_profile():
    if not PROFILE_FILE.exists():
        return None
    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_status(args):
    """Hiển thị tổng quan tiến độ học tập, mục tiêu và thống kê tài nguyên."""
    profile = load_profile()
    print("\n" + "=" * 62)
    print(" 🎯 BẢNG TIẾN ĐỘ ÔN THI TOEIC READING")
    print("=" * 62)

    if profile:
        target_score = profile.get("target_reading_score", 380)
        current_score = profile.get("current_reading_score", 250)
        total_target = profile.get("target_total_score", 750)
        test_date_str = profile.get("target_test_date", "")
        current_phase = profile.get("current_phase", 1)
        phase_title = profile.get("phase_titles", {}).get(str(current_phase), f"Phase {current_phase}")
        daily_time = profile.get("daily_study_time_minutes", 60)

        print(f" • Học viên:              {profile.get('user_name', 'Learner')}")
        print(f" • Điểm Reading hiện tại: {current_score} / 495")
        print(f" • Mục tiêu Reading:      {target_score} / 495 (Tổng mục tiêu: {total_target}+)")
        print(f" • Thời gian học mỗi ngày:{daily_time} phút")

        if test_date_str:
            try:
                target_date = datetime.strptime(test_date_str, "%Y-%m-%d").date()
                today = date.today()
                days_left = (target_date - today).days
                if days_left > 0:
                    print(f" • Ngày thi dự kiến:      {test_date_str} (Còn {days_left} ngày)")
                elif days_left == 0:
                    print(f" • Ngày thi dự kiến:      HÔM NAY!")
                else:
                    print(f" • Ngày thi dự kiến:      {test_date_str} (Đã qua {abs(days_left)} ngày)")
            except ValueError:
                print(f" • Ngày thi dự kiến:      {test_date_str}")

        print(f" • Giai đoạn hiện tại:    {phase_title}")
    else:
        print(" [!] Chưa tìm thấy profile.json.")

    # Thống kê Error Logs
    log_files = [f for f in ERROR_LOGS_DIR.glob("*.md") if f.name != "TEMPLATE.md"]
    total_errors_logged = 0
    for lf in log_files:
        content = lf.read_text(encoding="utf-8")
        total_errors_logged += content.count("### Câu")

    print("-" * 62)
    print(f" 📊 Thống kê nhật ký câu sai:")
    print(f" • Số đề/bài test đã log: {len(log_files)} bài")
    print(f" • Tổng số câu sai đã mổ xẻ: {total_errors_logged} câu")

    # Thống kê từ vựng cá nhân
    my_vocab_count = 0
    if MY_VOCAB_FILE.exists():
        lines = MY_VOCAB_FILE.read_text(encoding="utf-8").splitlines()
        my_vocab_count = sum(1 for l in lines if l.strip().startswith("|") and not l.strip().startswith("| :") and not l.strip().startswith("| STT"))

    # Thống kê kho 600 từ vựng cốt lõi
    words_600_total = 0
    lvl1 = lvl2 = lvl3 = 0
    if WORDS_600_FILE.exists():
        try:
            w600_data = json.loads(WORDS_600_FILE.read_text(encoding="utf-8"))
            words_600_total = len(w600_data)
            for w in w600_data:
                lvl = w.get("level", 1)
                if lvl == 1:
                    lvl1 += 1
                elif lvl == 2:
                    lvl2 += 1
                elif lvl >= 3:
                    lvl3 += 1
        except Exception:
            pass

    print(f" • Kho 600 từ vựng cốt lõi TOEIC: {words_600_total} từ (Level 1: {lvl1}, Level 2: {lvl2}, Level 3: {lvl3})")
    print(f" • Sổ tay từ vựng tích lũy riêng: {my_vocab_count} từ/cụm")

    # Thống kê kho Oxford 5000
    oxford_file = VOCAB_DIR / "oxford_5000.json"
    if oxford_file.exists():
        try:
            ox_data = json.loads(oxford_file.read_text(encoding="utf-8"))
            meta = ox_data.get("metadata", {})
            w_count = meta.get("total_words", 0)
            p_count = meta.get("total_phrases", 0)
            print(f" • Hệ sinh thái Oxford 5000™:    {w_count} từ + {p_count} cụm từ (Chuẩn CEFR A1-C1)")
        except Exception:
            pass

    # Thống kê ngữ pháp
    grammar_count = 0
    if MY_GRAMMAR_FILE.exists():
        g_lines = MY_GRAMMAR_FILE.read_text(encoding="utf-8").splitlines()
        grammar_count = sum(1 for l in g_lines if l.strip().startswith("### "))

    print(f" • Sổ tay ngữ pháp trọng điểm:   {grammar_count} chủ điểm")
    print("=" * 62 + "\n")


def cmd_new_log(args):
    """Tạo một file nhật ký chữa lỗi mới từ TEMPLATE.md."""
    test_name = args.name.strip().replace(" ", "_")
    if not test_name.endswith(".md"):
        filename = f"{test_name}.md"
    else:
        filename = test_name

    target_path = ERROR_LOGS_DIR / filename
    if target_path.exists():
        print(f"\n[!] File '{target_path.name}' đã tồn tại trong error_logs/.")
        return

    if not TEMPLATE_FILE.exists():
        print(f"\n[!] Không tìm thấy file mẫu {TEMPLATE_FILE}.")
        return

    content = TEMPLATE_FILE.read_text(encoding="utf-8")
    today_str = date.today().strftime("%Y-%m-%d")
    content = content.replace("[Ví dụ: ETS 2024 - Test 01 - Reading]", test_name.replace("_", " "))
    content = content.replace("[YYYY-MM-DD]", today_str)

    target_path.write_text(content, encoding="utf-8")
    print(f"\n[✓] Đã tạo thành công file nhật ký mới:")
    print(f"    -> {target_path}")
    print(f"    Mở file này và dán các câu bạn làm sai vào để phân tích cùng Agent!\n")


def cmd_add_vocab(args):
    """Thêm một từ/cụm từ mới vào vocab_bank/my_vocab.md."""
    if not MY_VOCAB_FILE.exists():
        print(f"\n[!] Không tìm thấy {MY_VOCAB_FILE}.")
        return

    lines = MY_VOCAB_FILE.read_text(encoding="utf-8").splitlines()
    
    # Tìm số thứ tự cao nhất hiện tại
    current_count = 0
    for l in lines:
        parts = [p.strip() for p in l.split("|") if p.strip()]
        if parts and parts[0].isdigit():
            current_count = max(current_count, int(parts[0]))
    
    new_idx = current_count + 1
    today_str = date.today().strftime("%Y-%m-%d")
    word = args.word.strip()
    pos = args.type.strip() if args.type else "phrase"
    meaning = args.meaning.strip()
    context = f"*{args.context.strip()}*" if args.context else "*-*"

    synonyms = args.synonyms.strip() if getattr(args, "synonyms", None) else "-"
    new_row = f"| {new_idx} | **{word}** | {pos} | {meaning} | {synonyms} | {context} | 1 lần | Level 1 | {today_str} |"

    with open(MY_VOCAB_FILE, "a", encoding="utf-8") as f:
        f.write(f"{new_row}\n")

    print(f"\n[✓] Đã thêm thành công vào sổ tay từ vựng cá nhân:")
    print(f"    STT {new_idx}: {word} ({pos}) - {meaning}")
    print(f"    Liên kết/Đồng nghĩa: {synonyms}")
    print(f"    Ngữ cảnh: {context}")
    print(f"    Số lần gặp: 1 lần | Mức độ: Level 1\n")


def cmd_prompt(args):
    """In ra các prompt chuẩn hóa để copy hỏi AI Agent."""
    p_type = args.type.lower()
    
    prompts = {
        "part5": """=== PROMPT CHỮA CÂU PART 5 (BÓC TÁCH CẤU TRÚC & BẪY) ===
Tôi đang giải một câu hỏi Part 5 TOEIC nhưng làm sai / phân vân. Hãy phân tích giúp tôi:

[DÁN ĐỀ BÀI VÀ 4 ĐÁP ÁN Ở ĐÂY]
- Đáp án tôi chọn: [A/B/C/D]
- Đáp án đúng theo key: [A/B/C/D]

Yêu cầu Agent phân tích theo các mục:
1. Xác định dạng câu hỏi (Từ loại / Chia thì / Giới từ / Từ vựng).
2. Phân tích cấu trúc câu (Chủ ngữ chính, vị ngữ chính, tân ngữ, thành phần bổ nghĩa).
3. Chỉ ra bẫy gây nhiễu (distractor) và tại sao đáp án tôi chọn lại sai.
4. Dịch nghĩa câu hoàn chỉnh theo ngữ cảnh công sở chuẩn.
5. Tạo 2 câu hỏi trắc nghiệm tương tự cấu trúc trên để tôi làm thử ngay.""",

        "part7": """=== PROMPT CHỮA BÀI ĐỌC PART 7 (PARAPHRASE & DẪN CHỨNG) ===
Dưới đây là một bài đọc và câu hỏi Part 7 tôi làm chưa đúng:

[DÁN ĐOẠN VĂN Ở ĐÂY]

[DÁN CÂU HỎI VÀ 4 ĐÁP ÁN Ở ĐÂY]
- Đáp án tôi chọn: [A/B/C/D]
- Đáp án đúng theo key: [A/B/C/D]

Yêu cầu Agent phân tích:
1. Định vị chính xác câu/dòng chứa chứng cứ (evidence) trong bài đọc.
2. Lập BẢNG PARAPHRASE: Chỉ ra từ ngữ trong đoạn văn được viết lại (paraphrase) sang đáp án đúng như thế nào.
3. Giải thích tại sao đáp án tôi chọn là sai (bẫy thông tin không được đề cập hay bẫy mâu thuẫn).
4. Rút ra 3 cụm từ/collocation đắt giá nhất trong bài đọc này kèm nghĩa.""",

        "drill": """=== PROMPT TẠO BÀI TẬP CỦNG CỐ CẤP TỐC (DRILL) ===
Tôi đang yếu phần [CHỦ ĐIỂM NGỮ PHÁP / DẠNG BÀI - Ví dụ: Mệnh đề phân từ rút gọn / Câu hỏi suy luận Part 7].
Hãy đóng vai chuyên gia luyện thi TOEIC ETS:
1. Tóm tắt 3 quy tắc vàng ngắn gọn nhất để giải quyết dạng này trong dưới 30 giây.
2. Tạo 5 câu trắc nghiệm format chuẩn ETS kèm 4 đáp án.
3. Cung cấp đáp án và giải thích ngắn gọn ở cuối.""",

        "paraphrase": """=== PROMPT HỌC TỪ ĐỒNG NGHĨA PARAPHRASE THEO CHỦ ĐỀ ===
Tôi muốn tích lũy các cặp Paraphrase thông dụng nhất trong Part 7 TOEIC về chủ đề: [CHỦ ĐỀ: Tuyển dụng / Đặt phòng khách sạn / Hoãn chuyến bay / Hợp đồng thương mại].
Hãy liệt kê 7-10 cặp Paraphrase (Cách bài đọc viết -> Cách đáp án viết lại) hay xuất hiện trong đề thi ETS gần đây kèm ví dụ."""
    }

    if p_type in prompts:
        print("\n" + prompts[p_type] + "\n")
    else:
        print(f"\n[!] Loại prompt không hợp lệ. Hãy chọn: {list(prompts.keys())}\n")


def cmd_quiz(args):
    """Trắc nghiệm nhanh 3-5 từ vựng ngẫu nhiên từ sổ tay hoặc kho 600 từ."""
    vocab_items = []
    source = getattr(args, "source", "all")
    lesson_filter = getattr(args, "lesson", None)

    # 1. Lấy từ my_vocab.md (nếu source là personal hoặc all)
    if source in ("personal", "all") and MY_VOCAB_FILE.exists():
        lines = MY_VOCAB_FILE.read_text(encoding="utf-8").splitlines()
        for l in lines:
            parts = [p.strip() for p in l.split("|") if p.strip()]
            if parts and parts[0].isdigit() and len(parts) >= 5:
                vocab_items.append({
                    "word": parts[1].replace("*", ""),
                    "pos": parts[2],
                    "meaning": parts[3],
                    "context": parts[5].replace("*", "") if len(parts) >= 6 else parts[4].replace("*", ""),
                    "source": "Sổ tay cá nhân"
                })

    # 2. Lấy từ toeic_600_words.json (nếu source là 600 hoặc all)
    if source in ("600", "all") and WORDS_600_FILE.exists():
        try:
            w600_data = json.loads(WORDS_600_FILE.read_text(encoding="utf-8"))
            for item in w600_data:
                if lesson_filter is not None and item.get("lesson_id") != lesson_filter:
                    continue
                vocab_items.append({
                    "word": item["word"],
                    "pos": item["pos"],
                    "meaning": item["meaning"],
                    "context": item["example"],
                    "source": f"Lesson {item['lesson_id']}: {item['lesson_name']}"
                })
        except Exception:
            pass

    if not vocab_items:
        print("\n[!] Không tìm thấy từ vựng phù hợp với bộ lọc.\n")
        return

    sample_size = min(len(vocab_items), getattr(args, "num", 4))
    selected = random.sample(vocab_items, sample_size)

    print("\n" + "=" * 62)
    print(f" 🧠 MINI FLASHCARD QUIZ (Nguồn: {source.upper()} | {len(vocab_items)} từ)")
    print("=" * 62)

    for i, item in enumerate(selected, 1):
        print(f"\nCâu {i}: Từ/Cụm từ:  \033[1m{item['word']}\033[0m ({item['pos']})")
        print(f"       Nguồn:         {item['source']}")
        print(f"       Ngữ cảnh:      {item['context']}")
        input("       -> Bấm [Enter] để lật đáp án...")
        print(f"       => NGHĨA:      \033[32m{item['meaning']}\033[0m")
        print("-" * 62)

    print("\n[✓] Hoàn thành buổi ôn tập từ vựng nhanh!\n")


def main():
    parser = argparse.ArgumentParser(
        description="TOEIC Reading CLI Assistant - Công cụ hỗ trợ ôn thi TOEIC Reading cá nhân hóa.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python scripts/toeic.py status
  python scripts/toeic.py new-log ETS_2024_Test_02
  python scripts/toeic.py prompt part5
  python scripts/toeic.py prompt part7
  python scripts/toeic.py add-vocab --word "obligated" --type "adj" --meaning "co nghia vu lam gi" --context "obligated to pay"
  python scripts/toeic.py quiz
        """
    )
    subparsers = parser.add_subparsers(dest="command", help="Lệnh chức năng")

    # Command: status
    p_status = subparsers.add_parser("status", help="Xem bảng điều khiển tiến độ và thống kê")
    p_status.set_defaults(func=cmd_status)

    # Command: new-log
    p_newlog = subparsers.add_parser("new-log", help="Tạo file nhật ký câu sai mới cho một bài test")
    p_newlog.add_argument("name", help="Tên bài test (vd: ETS_2024_Test_02)")
    p_newlog.set_defaults(func=cmd_new_log)

    # Command: add-vocab
    p_vocab = subparsers.add_parser("add-vocab", help="Thêm từ vựng/collocation mới vào sổ tay cá nhân")
    p_vocab.add_argument("--word", required=True, help="Từ hoặc cụm từ tiếng Anh")
    p_vocab.add_argument("--meaning", required=True, help="Nghĩa tiếng Việt")
    p_vocab.add_argument("--type", default="phrase", help="Loại từ (v, n, adj, adv, phrase...)")
    p_vocab.add_argument("--synonyms", default="", help="Từ đồng nghĩa hoặc nhóm từ liên kết cây")
    p_vocab.add_argument("--context", default="", help="Câu hoặc cụm ngữ cảnh thực tế")
    p_vocab.set_defaults(func=cmd_add_vocab)

    # Command: prompt
    p_prompt = subparsers.add_parser("prompt", help="Sinh khung prompt chuẩn để hỏi Agent")
    p_prompt.add_argument("type", choices=["part5", "part7", "drill", "paraphrase"], help="Loại prompt cần sinh")
    p_prompt.set_defaults(func=cmd_prompt)

    # Command: quiz
    p_quiz = subparsers.add_parser("quiz", help="Ôn tập nhanh từ vựng bằng mini flashcard")
    p_quiz.add_argument("--source", choices=["personal", "600", "all"], default="all", help="Nguồn từ vựng ôn tập (personal: sổ tay cá nhân, 600: kho 600 từ, all: cả hai)")
    p_quiz.add_argument("--lesson", type=int, default=None, help="Lọc theo bài học trong kho 600 từ (1 - 50)")
    p_quiz.add_argument("--num", type=int, default=4, help="Số lượng từ cần ôn tập (mặc định: 4)")
    p_quiz.set_defaults(func=cmd_quiz)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
