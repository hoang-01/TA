# 📘 HƯỚNG DẪN HỌC TOEIC READING VỚI CLI + AI AGENT

Chào mừng bạn đến với **Không gian Ôn thi TOEIC Reading Cá nhân hóa**! 

Hệ thống này được thiết kế để bạn vừa có thể quản lý lộ trình, ghi chép lỗi sai khoa học bằng các file Markdown, vừa có công cụ CLI hỗ trợ và có thể tương tác trực tiếp với **AI Agent** trong khung chat để mổ xẻ từng câu hỏi.

---

## 🗂️ CẤU TRÚC THƯ MỤC CỦA BẠN

```
d:\TA/
├── profile.json                 # Hồ sơ điểm hiện tại, mục tiêu, ngày thi
├── ROADMAP.md                   # Lộ trình 4 giai đoạn chi tiết từ Part 5 -> Part 7
├── README.md                    # File hướng dẫn này
├── error_logs/                  # Nơi lưu trữ nhật ký câu làm sai
│   ├── TEMPLATE.md              # Mẫu phân tích lỗi chuẩn 5 bước
│   ├── sample_test_01.md        # File mẫu thực tế đã phân tích
│   └── [test_cua_ban].md        # Các file nhật ký do bạn tạo ra
├── vocab_bank/                  # Sổ tay từ vựng & Collocation
│   ├── business_collocations.md # Cụm từ thương mại ETS hay gặp nhất
│   └── my_vocab.md              # Từ vựng bạn tự tích lũy
└── scripts/
    └── toeic.py                 # Công cụ CLI hỗ trợ học tập
```

---

## 🚀 CÁC LỆNH CLI HỖ TRỢ (`scripts/toeic.py`)

Mở terminal tại thư mục `d:\TA` và sử dụng các lệnh sau:

### 1. Xem bảng điều khiển tiến độ:
```powershell
python scripts/toeic.py status
```
*Hiển thị số ngày còn lại đến kỳ thi, điểm mục tiêu, số bài test đã phân tích và số từ vựng đã nạp.*

### 2. Tạo nhật ký phân tích cho bài test mới:
```powershell
python scripts/toeic.py new-log ETS_2024_Test_02
```
*Tự động tạo ra file `error_logs/ETS_2024_Test_02.md` với ngày tháng và mẫu chuẩn để bạn điền câu sai.*

### 3. Lấy Prompt mẫu chuẩn để copy hỏi Agent:
```powershell
python scripts/toeic.py prompt part5       # Prompt chữa Part 5
python scripts/toeic.py prompt part7       # Prompt chữa Part 7
python scripts/toeic.py prompt drill       # Prompt nhờ Agent tạo bài tập luyện dạng yếu
python scripts/toeic.py prompt paraphrase  # Prompt học từ đồng nghĩa theo chủ đề
```

### 4. Thêm từ vựng/collocation mới vào sổ tay:
```powershell
python scripts/toeic.py add-vocab --word "reach an agreement" --meaning "dat duoc thoa thuan" --type "collocation" --context "Both sides reached an agreement"
```

### 5. Ôn tập từ vựng ngẫu nhiên (Flashcard):
```powershell
python scripts/toeic.py quiz
```

---

## 🔄 QUY TRÌNH HỌC TẬP 4 BƯỚC VỚI AI AGENT

### Bước 1: Làm đề có bấm giờ
* Làm đề ETS (nghiêm túc, không tra từ điển, phân bổ đúng thời gian trong [ROADMAP.md](file:///d:/TA/ROADMAP.md)).

### Bước 2: Tạo log và gom câu sai
* Chạy: `python scripts/toeic.py new-log <Ten_De>`
* Ghi nhanh mã câu làm sai hoặc câu lụi đúng vào file log vừa tạo.

### Bước 3: Đưa câu hỏi cho Agent trong khung chat này
Bạn có thể hỏi Agent bất cứ lúc nào bằng cách chat trực tiếp, ví dụ:

> *"Chữa giúp mình câu này trong đề ETS 2024 Test 1: [Dán câu hỏi + 4 đáp án]. Mình chọn A nhưng đáp án là C. Hãy phân tích cấu trúc, chỉ ra bẫy và tạo 2 câu tương tự để mình làm lại."*

Agent sẽ:
1. Bóc tách ngữ pháp câu (`S + V + O`).
2. Chỉ rõ bẫy khiến bạn chọn nhầm.
3. Cung cấp bản đồ Paraphrase (nếu là Part 7).
4. Tạo 2 câu hỏi biến thể ngay tại chỗ để bạn luyện phản xạ.

### Bước 4: Lưu từ vựng & Rút kinh nghiệm
* Dán bài học vào file nhật ký trong `error_logs/`.
* Chạy `python scripts/toeic.py add-vocab` để lưu các cụm từ mới gặp.
* Định kỳ chạy `python scripts/toeic.py quiz` để não bộ nhớ lâu.
