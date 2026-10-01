#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script xây dựng trọn bộ 600 Từ Vựng Cốt Lõi TOEIC (Barron's / IIG 600 Essential Words for the TOEIC)
Bao gồm đầy đủ 50 bài x 12 từ = 600 từ vựng chia theo 10 chủ điểm công sở chuẩn ETS.
Toàn bộ từ vựng được gán Level 1 mặc định theo Mastery Progression System.
Xuất ra 2 định dạng:
1. vocab_bank/toeic_600_words.json (dữ liệu máy đọc phục vụ ra đề & CLI)
2. vocab_bank/toeic_600_words.md (sổ tay tra cứu trực quan theo từng Unit/Lesson)
"""

import json
import sys
from pathlib import Path

# Đảm bảo in UTF-8 mượt mà trên Windows console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
VOCAB_DIR = ROOT_DIR / "vocab_bank"
VOCAB_DIR.mkdir(exist_ok=True)

LESSONS_DATA = [
    # =========================================================================
    # UNIT 1: GENERAL BUSINESS (Bài 1 - 5)
    # =========================================================================
    {
        "category": "General Business",
        "lesson_id": 1,
        "lesson_name": "Contracts (Hợp đồng)",
        "words": [
            ("abide by", "v phrase", "tuân thủ theo", "comply with, adhere to, follow", "Both parties agreed to abide by the judge's decision."),
            ("agreement", "n", "hợp đồng, sự thỏa thuận", "contract, arrangement, pact", "According to the agreement, payment is due on Friday."),
            ("assurance", "n", "sự cam đoan, bảo đảm", "guarantee, pledge, confidence", "He gave his assurance that the project would finish on time."),
            ("cancellation", "n", "sự hủy bỏ", "annulment, termination, voiding", "The hotel charges a penalty for late cancellation."),
            ("determine", "v", "xác định, quyết định", "decide, establish, figure out", "We need to determine the exact cause of the delivery delay."),
            ("engage", "v", "tham gia, cam kết", "participate, involve, commit", "The company engaged in negotiations with overseas suppliers."),
            ("establish", "v", "thiết lập, thành lập", "set up, institute, found", "They established a new branch in Tokyo last year."),
            ("obligate", "v", "bắt buộc, ép buộc", "require, bind, compel", "The contract obligates the contractor to finish by June."),
            ("party", "n", "bên (trong hợp đồng)", "participant, signatory, side", "Both parties must sign the contract before it takes effect."),
            ("provision", "n", "điều khoản hợp đồng", "clause, condition, stipulation", "Under the provisions of the agreement, fees are nonrefundable."),
            ("resolve", "v", "giải quyết (tranh chấp)", "settle, solve, sort out", "The mediator helped resolve the contract dispute."),
            ("specific", "adj", "cụ thể, rõ ràng", "particular, precise, explicit", "Please provide specific details regarding your inquiry.")
        ]
    },
    {
        "category": "General Business",
        "lesson_id": 2,
        "lesson_name": "Marketing (Tiếp thị)",
        "words": [
            ("attract", "v", "thu hút, hấp dẫn", "draw, appeal to, entice", "The trade show attracted thousands of potential clients."),
            ("compare", "v", "so sánh", "contrast, balance, weigh", "Consumers compare prices before making a major purchase."),
            ("competition", "n", "sự cạnh tranh, đối thủ", "rivalry, competitors, contest", "Competition in the telecommunications sector is fierce."),
            ("consume", "v", "tiêu thụ, tiêu dùng", "use up, absorb, deplete", "The manufacturing facility consumes vast amounts of electricity."),
            ("convince", "v", "thuyết phục", "persuade, assure, sway", "The sales agent convinced the client to sign the agreement."),
            ("currently", "adv", "hiện tại, hiện nay", "presently, right now, at present", "We are currently reviewing all vendor proposals."),
            ("fad", "n", "mốt nhất thời, xu hướng ngắn", "craze, trend, fashion", "The marketing director warned that the product might just be a fad."),
            ("inspire", "v", "truyền cảm hứng", "motivate, encourage, stimulate", "The CEO's keynote speech inspired the entire sales staff."),
            ("market", "v/n", "tiếp thị / thị trường", "promote, advertise / marketplace", "They plan to market the new smartphone globally."),
            ("persuasion", "n", "sự thuyết phục", "convincing, influence, coaxing", "Effective persuasion is an essential marketing skill."),
            ("productive", "adj", "năng suất, hiệu quả", "fruitful, constructive, efficient", "The morning brainstorming session was highly productive."),
            ("satisfaction", "n", "sự hài lòng", "contentment, pleasure, fulfillment", "Customer satisfaction remains our primary objective.")
        ]
    },
    {
        "category": "General Business",
        "lesson_id": 3,
        "lesson_name": "Warranties (Bảo hành)",
        "words": [
            ("characteristic", "adj/n", "đặc trưng, đặc tính", "typical, representative / trait, feature", "Reliability is the key characteristic of our engines."),
            ("consequence", "n", "hậu quả, kết quả", "result, outcome, repercussion", "The consequence of failing to inspect the machines was severe."),
            ("consider", "v", "cân nhắc, xem xét", "think about, evaluate, deliberate", "The committee is considering several replacement options."),
            ("cover", "v", "bảo hiểm, chi trả, bao gồm", "include, insure, shield", "The standard warranty covers parts and labor for one year."),
            ("expiration", "n", "sự hết hạn", "termination, end, lapse", "Check the expiration date on the coupon before using it."),
            ("frequently", "adv", "thường xuyên", "regularly, often, repeatedly", "Train schedules are frequently updated on the website."),
            ("imply", "v", "ngụ ý, hàm ý", "suggest, hint, indicate", "The report implies that further budget cuts will be necessary."),
            ("promise", "v/n", "hứa hẹn / lời hứa", "pledge, guarantee, assure", "The manufacturer promised to replace any defective components."),
            ("protect", "v", "bảo vệ", "guard, shield, defend", "Proper packaging protects goods from damage during transit."),
            ("reputation", "n", "danh tiếng, uy tín", "standing, fame, prestige", "The firm has built a solid reputation for punctuality."),
            ("require", "v", "yêu cầu, đòi hỏi", "demand, necessitate, mandate", "Safety regulations require all workers to wear helmets."),
            ("vary", "v", "thay đổi, khác nhau", "differ, alter, fluctuate", "Delivery fees vary depending on the destination.")
        ]
    },
    {
        "category": "General Business",
        "lesson_id": 4,
        "lesson_name": "Business Planning (Kế hoạch kinh doanh)",
        "words": [
            ("address", "v", "giải quyết, xử lý", "deal with, tackle, handle", "Management convened to address employee concerns."),
            ("avoid", "v", "tránh, né tránh", "steer clear of, evade, prevent", "To avoid delays, submit your application at least two weeks early."),
            ("demonstrate", "v", "chứng minh, giải thích", "show, prove, illustrate", "The pilot test demonstrated the effectiveness of the software."),
            ("develop", "v", "phát triển, mở rộng", "expand, cultivate, advance", "The company aims to develop new overseas markets."),
            ("evaluate", "v", "đánh giá, định giá", "assess, appraise, rate", "Supervisors evaluate staff performance annually."),
            ("gather", "v", "thu thập, tập hợp", "collect, assemble, amass", "The analysts gathered market data from several sources."),
            ("offer", "v/n", "cung cấp, đưa ra đề xuất", "provide, propose / proposal, bid", "The hotel offers complimentary shuttle services."),
            ("primarily", "adv", "chủ yếu, căn bản", "chiefly, mainly, predominantly", "The seminar is aimed primarily at junior accountants."),
            ("risk", "n/v", "rủi ro, mạo hiểm", "hazard, peril, danger / jeopardize", "Expanding too quickly carries significant financial risk."),
            ("strategy", "n", "chiến lược", "plan, tactic, scheme", "Our pricing strategy helped boost domestic sales."),
            ("strong", "adj", "mạnh mẽ, vững chắc", "robust, solid, powerful", "The company reported strong financial growth in Q3."),
            ("substitute", "v/n", "thay thế / vật thay thế", "replace, swap / alternative, surrogate", "The technician substituted a durable metal part for the plastic one.")
        ]
    },
    {
        "category": "General Business",
        "lesson_id": 5,
        "lesson_name": "Conferences (Hội thảo)",
        "words": [
            ("accommodate", "v", "đáp ứng (yêu cầu), chứa (người)", "house, fulfill, cater to, hold", "The ballroom can accommodate up to 400 attendees."),
            ("arrangement", "n", "sự sắp xếp, thu xếp", "preparation, setup, planning", "Special travel arrangements have been made for the keynote speaker."),
            ("association", "n", "hiệp hội, tổ chức", "organization, society, alliance", "She is an active member of the Medical Writers Association."),
            ("attend", "v", "tham dự, có mặt", "be present at, go to", "Over 200 delegates attended the regional symposium."),
            ("get in touch", "phrase", "liên lạc với", "contact, reach out to, communicate with", "Please get in touch with our coordinator if you need assistance."),
            ("hold", "v", "tổ chức (sự kiện)", "host, conduct, convene", "The annual general meeting will be held next Thursday."),
            ("location", "n", "địa điểm, vị trí", "venue, site, place", "The convention center is an ideal location for international summits."),
            ("overcrowded", "adj", "quá đông đúc", "congested, packed, jam-packed", "The auditorium was overcrowded due to high turnout."),
            ("register", "v", "đăng ký", "enroll, sign up, record", "Participants must register online before the deadline."),
            ("select", "v/adj", "lựa chọn / chọn lọc, ưu tú", "choose, pick / exclusive, choice", "The committee selected three finalists for the interview."),
            ("session", "n", "phiên họp, buổi hội thảo", "meeting, assembly, period", "The afternoon breakout session will begin at 2:00 P.M."),
            ("take part in", "phrase", "tham gia vào", "participate in, join, partake in", "All staff are encouraged to take part in the charity run.")
        ]
    },

    # =========================================================================
    # UNIT 2: OFFICE ISSUES (Bài 6 - 10)
    # =========================================================================
    {
        "category": "Office Issues",
        "lesson_id": 6,
        "lesson_name": "Computers and the Internet (Máy tính & Mạng)",
        "words": [
            ("access", "v/n", "truy cập / quyền truy cập", "admittance, entry / enter, retrieve", "Authorized staff can access the database remotely."),
            ("allocate", "v", "phân bổ, cấp phát", "assign, designate, apportion", "The IT director allocated additional server space for backups."),
            ("compatible", "adj", "tương thích", "suitable, adaptable, consistent", "Make sure the software is fully compatible with Windows 11."),
            ("delete", "v", "xóa bỏ", "remove, erase, wipe", "Accidentally deleted files can often be retrieved from the archives."),
            ("display", "v/n", "hiển thị / màn hình, trưng bày", "exhibit, show / screen", "The dashboard displays real-time production statistics."),
            ("duplicate", "v/n", "sao chép / bản sao", "copy, replicate / clone", "Please duplicate these financial statements for the committee."),
            ("failure", "n", "sự cố, thất bại", "breakdown, malfunction, collapse", "The power failure disrupted assembly operations for two hours."),
            ("figure out", "v phrase", "tìm ra, hiểu ra", "solve, decipher, comprehend", "Technicians worked overnight to figure out the network glitch."),
            ("ignore", "v", "phớt lờ, bỏ qua", "disregard, overlook, neglect", "Do not ignore warning messages displayed on your terminal."),
            ("search", "v/n", "tìm kiếm", "seek, look for, investigate / lookup", "Use the intranet portal to search for internal policy documents."),
            ("shut down", "v phrase", "tắt máy, ngừng hoạt động", "power off, close, halt", "Remember to shut down your workstation before leaving."),
            ("warning", "n", "cảnh báo", "caution, alert, notice", "The monitor flashed a low-disk warning alert.")
        ]
    },
    {
        "category": "Office Issues",
        "lesson_id": 7,
        "lesson_name": "Office Technology (Công nghệ văn phòng)",
        "words": [
            ("affordable", "adj", "giá cả phải chăng", "economical, reasonably priced, inexpensive", "The company provides affordable ergonomic office chairs."),
            ("as needed", "phrase", "khi cần thiết", "when necessary, as required", "External technical consultants will be brought in as needed."),
            ("be in charge of", "phrase", "chịu trách nhiệm về", "responsible for, manage, head", "Ms. Davis is in charge of organizing the global symposium."),
            ("capacity", "n", "công suất, sức chứa", "volume, capability, size", "The new data center operates at maximum processing capacity."),
            ("durable", "adj", "bền bỉ, dùng lâu", "sturdy, long-lasting, resilient", "Heavy-duty machinery requires durable steel components."),
            ("initiative", "n", "sáng kiến, sự chủ động", "enterprise, lead, novelty", "Employees who take the initiative are prioritized for promotions."),
            ("physically", "adv", "về mặt thể chất/vật lý", "bodily, tangibly, manually", "Documents must be physically filed in the records vault."),
            ("provider", "n", "nhà cung cấp", "supplier, vendor, purveyor", "Select an internet service provider with high reliability ratings."),
            ("recur", "v", "tái diễn, lặp lại", "repeat, happen again, return", "Software patches were installed so the error would not recur."),
            ("reduction", "n", "sự giảm bớt", "decrease, cutback, drop", "The firm achieved a 15 percent reduction in operating costs."),
            ("stay on top of", "phrase", "nắm bắt kịp thời", "keep informed, monitor, master", "Project managers must stay on top of emerging industry trends."),
            ("stock", "v/n", "tích trữ / hàng tồn kho", "inventory, supply / store, keep", "The supply closet is fully stocked with printer cartridges.")
        ]
    },
    {
        "category": "Office Issues",
        "lesson_id": 8,
        "lesson_name": "Office Procedures (Quy trình văn phòng)",
        "words": [
            ("appreciate", "v", "đánh giá cao, cảm kích", "value, recognize, esteem", "We appreciate your prompt feedback on the draft proposal."),
            ("be made of", "phrase", "được làm từ", "consist of, composed of", "The ergonomic desk is made of recycled oak."),
            ("bring in", "v phrase", "thu hút, mang lại, thuê", "generate, introduce, hire", "The new marketing campaign brought in three major corporate accounts."),
            ("casually", "adv", "bình thường, không trang trọng", "informally, casually", "Employees may dress casually on Fridays."),
            ("code", "n", "bộ quy tắc, quy chuẩn", "rules, regulations, standard", "All personnel must adhere strictly to the corporate ethics code."),
            ("expose", "v", "tiếp xúc, phơi bày", "subject to, uncover, introduce", "The workshop exposes employees to cutting-edge AI technologies."),
            ("glimpse", "n/v", "cái nhìn lướt qua", "peek, brief look, glance", "The presentation provides a fascinating glimpse into future projects."),
            ("out of", "phrase", "hết, cạn kiệt", "depleted, lacking, short of", "The copier is out of toner again."),
            ("outdated", "adj", "lỗi thời, lạc hậu", "obsolete, antiquated, old-fashioned", "Our database software is outdated and needs an immediate upgrade."),
            ("practice", "n/v", "thói quen, quy chuẩn thực hành", "custom, routine, standard habit", "It is standard company practice to verify vendor invoices twice."),
            ("reinforce", "v", "củng cố, tăng cường", "strengthen, fortify, bolster", "Regular training reinforces corporate security protocols."),
            ("verbally", "adv", "bằng lời nói, miệng", "orally, by word of mouth", "The supervisor confirmed the approval verbally before emailing it.")
        ]
    },
    {
        "category": "Office Issues",
        "lesson_id": 9,
        "lesson_name": "Electronics (Thiết bị điện tử)",
        "words": [
            ("disk", "n", "đĩa lưu trữ dữ liệu", "hard drive, storage medium", "Backup copies were transferred to an external disk."),
            ("facilitate", "v", "tạo điều kiện thuận lợi", "ease, enable, assist, expedite", "Automated workflows facilitate rapid invoice processing."),
            ("network", "n/v", "mạng lưới / kết nối mạng", "web, system / connect, socialize", "The engineering network links all regional satellite offices."),
            ("popularity", "n", "sự phổ biến, ưa chuộng", "favor, acceptance, renown", "The popularity of electric vehicles has surged recently."),
            ("process", "n/v", "quy trình / xử lý", "procedure, workflow / handle, treat", "The processing of passport applications takes two weeks."),
            ("replace", "v", "thay thế", "substitute, exchange, take the place of", "Technicians will replace outdated cables this weekend."),
            ("revolution", "n", "cuộc cách mạng, đột phá", "transformation, breakthrough, upheaval", "Cloud computing sparked a revolution in remote work."),
            ("sharp", "adj/adv", "sắc bén, rõ rệt, đúng giờ", "keen, acute, distinct / promptly", "The meeting begins at 9:00 A.M. sharp."),
            ("skill", "n", "kỹ năng, chuyên môn", "expertise, ability, competence", "Effective communication is a crucial leadership skill."),
            ("software", "n", "phần mềm", "program, application, system", "Our accounting software was updated last night."),
            ("store", "v/n", "lưu trữ / cửa hàng", "keep, archive / shop, outlet", "Sensitive records are securely stored in the cloud."),
            ("technically", "adv", "về mặt kỹ thuật", "strictly, scientifically, mechanically", "The software is technically sound but lacks a friendly UI.")
        ]
    },
    {
        "category": "Office Issues",
        "lesson_id": 10,
        "lesson_name": "Correspondence (Thư tín & Văn bản)",
        "words": [
            ("assemble", "v", "tập hợp, lắp ráp", "gather, collect, bring together", "All staff assembled in the auditorium for the announcement."),
            ("beforehand", "adv", "trước, sẵn sàng trước", "in advance, earlier, ahead of time", "Please review the agenda beforehand so meetings run smoothly."),
            ("complication", "n", "sự phức tạp, rắc rối", "difficulty, obstacle, snag", "Supply chain complications resulted in late shipment delivery."),
            ("courier", "n", "người chuyển phát nhanh", "messenger, carrier, dispatch", "Confidential contracts should be delivered via bonded courier."),
            ("express", "adj/v", "hỏa tốc / bày tỏ", "fast, expedited / voice, articulate", "Choose express freight if you require guaranteed next-day arrival."),
            ("fold", "v", "gấp lại", "bend, crease, tuck", "Fold the letter neatly before placing it inside the official envelope."),
            ("layout", "n", "bố cục, trình bày", "design, arrangement, format", "The graphic designer revamped the newsletter's visual layout."),
            ("mention", "v/n", "đề cập đến", "state, refer to, remark", "The memo mentions that office renovation begins next Monday."),
            ("petition", "n/v", "đơn kiến nghị", "appeal, formal request, plea", "Staff submitted a petition requesting flexible telecommuting options."),
            ("proof", "n", "bản in thử, bằng chứng", "evidence, draft copy, verification", "Check the printer's proof carefully for typographical errors."),
            ("proofread", "v", "đọc và sửa lỗi bản in", "check, review, correct", "Always proofread important emails before sending them to clients."),
            ("revise", "v", "chỉnh sửa, sửa đổi", "modify, amend, alter, update", "The author revised the financial summary based on client feedback.")
        ]
    },

    # =========================================================================
    # UNIT 3: PERSONNEL (Bài 11 - 15)
    # =========================================================================
    {
        "category": "Personnel",
        "lesson_id": 11,
        "lesson_name": "Job Advertising and Recruiting (Tuyển dụng)",
        "words": [
            ("abundant", "adj", "dồi dào, phong phú", "plentiful, ample, copious", "There is an abundant supply of skilled programmers in the region."),
            ("accomplish", "v", "hoàn thành, đạt được", "achieve, fulfill, complete", "The engineering team accomplished all milestone deliverables on time."),
            ("bring together", "v phrase", "tập hợp, quy tụ", "unite, assemble, gather", "The annual conference brings together top researchers worldwide."),
            ("candidate", "n", "ứng viên", "applicant, contender, nominee", "She is the most qualified candidate for the senior analyst role."),
            ("commensurate", "adj", "tương xứng với", "proportionate, equal, corresponding", "Salary will be commensurate with experience and credentials."),
            ("match", "v/n", "phù hợp, tương xứng", "fit, correspond, complement", "Her technical skills match our current vacancy requirements."),
            ("profile", "n", "hồ sơ năng lực", "summary, background, dossier", "Review the corporate profile before your interview with management."),
            ("qualification", "n", "trình độ chuyên môn, văn bằng", "credentials, eligibility, certificates", "Applicants must meet all educational qualifications listed."),
            ("recruit", "v/n", "tuyển dụng / tân binh", "hire, employ / newcomer, inductee", "Our human resources department actively recruits top college graduates."),
            ("submit", "v", "nộp, đệ trình", "hand in, turn in, present", "Resumes must be submitted online before 5:00 P.M. on Friday."),
            ("time-consuming", "adj", "tốn nhiều thời gian", "lengthy, arduous, slow", "Sorting through hundreds of resumes by hand is time-consuming."),
            ("update", "v/n", "cập nhật / thông tin mới", "modernize, renew / latest report", "Please update your online resume before submitting the application.")
        ]
    },
    {
        "category": "Personnel",
        "lesson_id": 12,
        "lesson_name": "Applying and Interviewing (Ứng tuyển & Phỏng vấn)",
        "words": [
            ("ability", "n", "khả năng, năng lực", "capability, skill, aptitude", "He demonstrated an exceptional ability to manage tight deadlines."),
            ("apply", "v", "ứng tuyển, áp dụng", "request, seek / implement, utilize", "Qualified professionals are encouraged to apply for the opening."),
            ("background", "n", "lý lịch, nền tảng", "experience, history, education", "She possesses a strong academic background in corporate finance."),
            ("call in", "v phrase", "mời đến, gọi tới", "invite, summon, ask in", "Five shortlisted applicants were called in for second-round interviews."),
            ("confidence", "n", "sự tự tin, tin tưởng", "assurance, certainty, faith", "His poise during the presentation inspired investor confidence."),
            ("constantly", "adv", "liên tục, không ngừng", "continuously, persistently, perpetually", "Technology requirements in digital marketing evolve constantly."),
            ("expert", "n/adj", "chuyên gia / tinh thông", "specialist, authority / masterly, adept", "Consult an expert auditor before finalizing your tax return."),
            ("follow up", "v phrase", "theo dõi, liên hệ lại", "check back, pursue, continue", "Follow up with the hiring manager via a polite thank-you email."),
            ("hesitant", "adj", "ngập ngừng, do dự", "reluctant, uncertain, tentative", "Do not be hesitant to ask questions during the orientation."),
            ("present", "v", "trình bày, xuất trình", "exhibit, showcase, introduce", "Each candidate will present a five-minute case study solution."),
            ("weakly", "adv", "yếu ớt, thiếu thuyết phục", "poorly, faintly, inadequately", "The proposal was argued weakly and failed to secure funding."),
            ("conduct", "v/n", "tiến hành, điều hành / hạnh kiểm", "carry out, manage, administer / behavior", "The panel will conduct interviews throughout next Wednesday.")
        ]
    },
    {
        "category": "Personnel",
        "lesson_id": 13,
        "lesson_name": "Hiring and Training (Tuyển mộ & Đào tạo)",
        "words": [
            ("basis", "n", "nền tảng, cơ sở", "foundation, ground, principle", "Reviews are conducted on a quarterly basis."),
            ("compensate", "v", "đền bù, trả thù lao", "remunerate, repay, reimburse", "Workers will be compensated for weekend overtime hours."),
            ("delicately", "adv", "tế nhị, khéo léo", "tactfully, sensitively, carefully", "Salary negotiations should be handled delicately."),
            ("eligible", "adj", "đủ điều kiện, xứng đáng", "qualified, entitled, suitable", "Employees with one year of service are eligible for tuition aid."),
            ("flexibly", "adv", "linh hoạt", "adaptably, pliably", "Managers should schedule shifts flexibly to accommodate staff needs."),
            ("hire", "v/n", "thuê, tuyển dụng / nhân viên mới", "employ, take on / new recruit", "The firm hired an experienced logistics manager."),
            ("keep up with", "phrase", "bắt kịp, theo kịp", "stay abreast of, match pace with", "Staff attend regular webinars to keep up with industry standards."),
            ("look up to", "phrase", "kính trọng, noi gương", "admire, respect, venerate", "Junior engineers look up to the senior systems architect."),
            ("mentor", "n/v", "người hướng dẫn / dẫn dắt", "advisor, guide, coach / train", "Each new recruit is paired with a seasoned mentor."),
            ("on track", "phrase", "đúng tiến độ", "on schedule, progressing well", "The orientation program remains on track to conclude by Friday."),
            ("reject", "v", "từ chối, bác bỏ", "turn down, decline, dismiss", "Applications lacking proper transcripts will be automatically rejected."),
            ("set up", "v phrase", "thiết lập, cài đặt", "establish, arrange, configure", "The technician set up individual workstation accounts.")
        ]
    },
    {
        "category": "Personnel",
        "lesson_id": 14,
        "lesson_name": "Salaries and Benefits (Lương bổng & Phúc lợi)",
        "words": [
            ("benefit", "n/v", "phúc lợi / hưởng lợi", "perk, advantage / gain, profit", "Comprehensive health insurance is an attractive corporate benefit."),
            ("dedicated", "adj", "tận tụy, cống hiến", "committed, devoted, steadfast", "The award honors dedicated service to community welfare."),
            ("negotiate", "v", "đàm phán, thương lượng", "bargain, confer, arbitrate", "The union met with management to negotiate healthcare benefits."),
            ("raise", "n/v", "tăng lương / nâng lên", "increase, bump / elevate, boost", "Outstanding quarterly performance earned her a substantial raise."),
            ("retire", "v", "nghỉ hưu", "step down, leave work, withdraw", "Mr. Gomez plans to retire after 35 dedicated years at the bank."),
            ("vested", "adj", "được trao quyền, chính thức", "entitled, secured, fixed", "Employees become fully vested in the pension fund after five years."),
            ("wage", "n", "tiền công (theo giờ/tuần)", "pay, hourly earnings, remuneration", "The government raised the minimum wage beginning this month."),
            ("merit", "n", "công lao, sự xứng đáng", "worth, excellence, value", "Promotions are determined strictly on professional merit."),
            ("look forward to", "phrase", "mong đợi, trông ngóng (+ V-ing)", "anticipate, await eagerly", "We look forward to welcoming the new branch manager next week."),
            ("loyal", "adj", "trung thành", "faithful, devoted, dependable", "The firm rewards loyal clients with exclusive quarterly discounts."),
            ("promote", "v", "thăng chức, quảng bá", "elevate, advance / market, publicize", "She was promoted to vice president of global procurement."),
            ("severance", "n", "tiền trợ cấp thôi việc", "severance pay, termination benefit", "Laid-off workers received three months of severance pay.")
        ]
    },
    {
        "category": "Personnel",
        "lesson_id": 15,
        "lesson_name": "Promotions, Pensions, and Awards (Thăng tiến & Khen thưởng)",
        "words": [
            ("achievement", "n", "thành tựu, thành tích", "accomplishment, success, triumph", "Hitting the yearly sales target was a milestone achievement."),
            ("contribute", "v", "đóng góp, cống hiến", "donate, add to, furnish", "All team members contributed valuable insights to the campaign."),
            ("dedication", "n", "sự cống hiến, tận tâm", "commitment, devotion, adherence", "Her unwavering dedication earned the respect of colleagues."),
            ("obviously", "adv", "rõ ràng, hiển nhiên", "clearly, evidently, plainly", "The new software is obviously superior to the legacy tool."),
            ("recognition", "n", "sự công nhận, tôn vinh", "acknowledgment, tribute, acclaim", "He received a plaque in recognition of his safety leadership."),
            ("value", "v/n", "coi trọng / giá trị", "appreciate, cherish / worth, price", "Our organization values innovative thinking and ethical conduct."),
            ("award", "n/v", "giải thưởng / trao thưởng", "prize, honor / bestow, grant", "The board awarded the contract to the lowest qualified bidder."),
            ("criterion", "n", "tiêu chí đánh giá (số nhiều: criteria)", "standard, benchmark, yardstick", "Academic record is only one criterion used during candidate selection."),
            ("pension", "n", "lương hưu", "retirement fund, annuity", "Retirees depend on monthly pension payouts to cover living costs."),
            ("tenure", "n", "thâm niên công tác, nhiệm kỳ", "term, incumbency, period", "During his 10-year tenure, corporate revenues tripled."),
            ("stand out", "v phrase", "nổi bật, xuất sắc", "distinguish oneself, excel", "Her exceptional problem-solving skills make her stand out."),
            ("evaluate", "v", "đánh giá nhân sự", "appraise, assess, review", "Supervisors evaluate staff performance on an annual basis.")
        ]
    },

    # =========================================================================
    # UNIT 4: PURCHASING (Bài 16 - 20)
    # =========================================================================
    {
        "category": "Purchasing",
        "lesson_id": 16,
        "lesson_name": "Shopping (Mua sắm)",
        "words": [
            ("bargain", "n/v", "món hời / mặc cả", "good deal / negotiate, haggle", "The purchasing officer struck an exceptional bargain on paper supplies."),
            ("bear", "v", "chịu đựng, gánh vác", "endure, shoulder, tolerate", "The company will bear all travel expenses for the keynote speaker."),
            ("behavior", "n", "hành vi tiêu dùng", "conduct, manner, demeanor", "Surveys help analyze consumer shopping behavior online."),
            ("checkout", "n", "quầy thanh toán", "counter, cashier, payment point", "Self-service checkouts help reduce customer wait times."),
            ("comfort", "n/v", "sự thoải mái / an ủi", "ease, relief, solace / soothe", "Ergonomic seating provides comfort during long workdays."),
            ("expand", "v", "mở rộng", "enlarge, broaden, extend", "The retail chain plans to expand into three neighboring countries."),
            ("explore", "v", "khám phá, thăm dò", "investigate, survey, examine", "Management is exploring alternative logistics routes."),
            ("item", "n", "món hàng, khoản mục", "product, article, piece, entry", "Every item on the invoice must be audited before payment."),
            ("mandatory", "adj", "bắt buộc", "compulsory, obligatory, required", "Attendance at the workplace safety workshop is mandatory."),
            ("merchandise", "n", "hàng hóa", "goods, commodities, stock, wares", "Damaged merchandise should be returned within 30 days."),
            ("strictly", "adv", "nghiêm ngặt, khắt khe", "rigorously, firmly, stringently", "Deadlines for grant submissions will be strictly enforced."),
            ("trend", "n", "xu hướng", "tendency, drift, pattern", "Consumer trends indicate growing demand for eco-friendly goods.")
        ]
    },
    {
        "category": "Purchasing",
        "lesson_id": 17,
        "lesson_name": "Ordering Supplies (Đặt mua vật tư)",
        "words": [
            ("diversify", "v", "đa dạng hóa", "expand, vary, branch out", "Companies should diversify their supplier base to minimize disruption."),
            ("enterprise", "n", "doanh nghiệp, tập đoàn", "business, corporation, venture", "Small-scale enterprises account for the majority of local hiring."),
            ("essentially", "adv", "về cơ bản, thực chất", "fundamentally, primarily, basically", "The two proposed logistics strategies are essentially identical."),
            ("everyday", "adj", "hàng ngày, thường nhật", "routine, daily, commonplace", "Pen and paper remain everyday office essentials."),
            ("function", "v/n", "hoạt động, vận hành / chức năng", "operate, work / role, purpose", "The printer failed to function properly after the paper jam."),
            ("maintain", "v", "duy trì, bảo dưỡng", "preserve, keep up, service", "Regular maintenance helps maintain vehicle efficiency."),
            ("obtain", "v", "đạt được, thu thập được", "acquire, procure, secure", "You must obtain written authorization before placing the order."),
            ("prerequisite", "n/adj", "điều kiện tiên quyết", "requirement, precondition / requisite", "Basic computer literacy is a prerequisite for this administrative role."),
            ("quality", "n/adj", "chất lượng / hảo hạng", "standard, caliber / premium", "The factory is renowned for producing high quality textiles."),
            ("smooth", "adj", "trôi chảy, êm thấm", "seamless, trouble-free, fluid", "Careful planning ensured a smooth transition to the new headquarters."),
            ("source", "n/v", "nguồn gốc / tìm kiếm nguồn", "origin, supplier / procure, seek", "Local farms are the primary source of our restaurant's produce."),
            ("stationery", "n", "văn phòng phẩm", "office supplies, writing materials", "The clerk submitted a requisition form for office stationery.")
        ]
    },
    {
        "category": "Purchasing",
        "lesson_id": 18,
        "lesson_name": "Shipping (Giao nhận vận chuyển)",
        "words": [
            ("accurately", "adv", "chính xác", "precisely, correctly, exactingly", "Packages must be weighed accurately to calculate postage."),
            ("carrier", "n", "hãng vận chuyển, bên chuyên chở", "transporter, courier, shipper", "We selected an insured freight carrier for international delivery."),
            ("catalog", "n/v", "danh mục sản phẩm", "directory, inventory / classify", "Browse our autumn catalog for the latest industrial tools."),
            ("fulfill", "v", "hoàn thành, đáp ứng đơn", "execute, satisfy, complete", "The warehouse fulfilled all backlogged customer orders by noon."),
            ("integral", "adj", "không thể thiếu, cốt lõi", "essential, vital, fundamental", "Efficient logistics is an integral part of our supply chain strategy."),
            ("inventory", "n", "hàng tồn kho, bản kiểm kê", "stock, supply, goods list", "Quarterly inventory audits help detect shrinkage early."),
            ("minimize", "v", "giảm thiểu đến mức tối đa", "reduce, curtail, diminish", "Optimizing truck routes helps minimize fuel consumption."),
            ("on hand", "phrase", "có sẵn trong kho", "in stock, available, present", "Keep sufficient spare parts on hand for emergency repairs."),
            ("receive", "v", "nhận được", "accept, get, obtain", "The dock manager signed for the crates upon receiving them."),
            ("ship", "v", "giao hàng, vận chuyển", "dispatch, transport, send", "All orders placed before 3:00 P.M. are shipped the same day."),
            ("sufficiently", "adv", "đủ, thỏa đáng", "adequately, enough, amply", "Make sure the fragile glassware is sufficiently padded."),
            ("supply", "n/v", "nguồn cung / cung cấp", "provision, stock / provide, furnish", "Disruptions at the port threatened our fuel supply.")
        ]
    },
    {
        "category": "Purchasing",
        "lesson_id": 19,
        "lesson_name": "Invoices (Hóa đơn thanh toán)",
        "words": [
            ("charge", "v/n", "tính phí / khoản phí", "bill, levy / fee, cost", "The supplier will charge a five percent restocking fee."),
            ("compile", "v", "tổng hợp, thu thập", "assemble, gather, collate", "The accountant compiled financial records for the annual tax audit."),
            ("customer", "n", "khách hàng", "client, patron, buyer", "Prompt email replies enhance customer satisfaction."),
            ("discount", "n/v", "khoản chiết khấu / giảm giá", "deduction, concession / reduce", "Bulk purchases qualify for a 10 percent volume discount."),
            ("dispute", "n/v", "tranh chấp / khiếu nại", "controversy, quarrel / contest", "The billing department quickly resolved the billing dispute."),
            ("efficient", "adj", "hiệu quả, tiết kiệm thời gian", "effective, streamlined, productive", "An automated invoicing process is highly efficient."),
            ("estimate", "v/n", "ước tính / bảng dự toán", "calculate, appraise / quote, appraisal", "The mechanic provided a written estimate for the repair work."),
            ("impose", "v", "áp đặt (thuế/phí)", "levy, enforce, inflict", "The local municipality imposed a tax on single-use plastics."),
            ("mistake", "n", "sai sót, lỗi", "error, blunder, inaccuracy", "Proofread the invoice to ensure there are no calculation mistakes."),
            ("promptly", "adv", "ngay lập tức, đúng hạn", "immediately, swiftly, punctually", "Invoices must be paid promptly within 30 days of receipt."),
            ("rectify", "v", "sửa chữa, khắc phục sai sót", "correct, fix, remedy", "Customer support acted swiftly to rectify the shipping error."),
            ("terms", "n", "điều khoản thanh toán", "conditions, stipulations, provisions", "The contract terms specify net-30 payment via wire transfer.")
        ]
    },
    {
        "category": "Purchasing",
        "lesson_id": 20,
        "lesson_name": "Inventory (Kiểm kê kho bãi)",
        "words": [
            ("adjustment", "n", "sự điều chỉnh", "modification, alteration, tweak", "Warehouse staff made an inventory adjustment for broken items."),
            ("automatically", "adv", "tự động", "spontaneously, mechanically", "The system automatically reorders supplies when stock drops below ten."),
            ("crucial", "adj", "cực kỳ quan trọng, sống còn", "critical, vital, essential", "Accurate data entry is crucial during warehouse audits."),
            ("discrepancy", "n", "sự chênh lệch, sai khác", "inconsistency, divergence, disparity", "Auditors noticed a discrepancy between the ledger and physical stock."),
            ("disturb", "v", "làm phiền, xáo trộn", "interrupt, disrupt, agitate", "Do not disturb boxes labeled for immediate hazardous inspection."),
            ("liability", "n", "trách nhiệm pháp lý, khoản nợ", "obligation, debt, accountability", "The carrier disclaimed liability for goods damaged in transit."),
            ("reflect", "v", "phản ánh", "show, indicate, demonstrate", "The revised quarterly report reflects our actual operating costs."),
            ("run out of", "phrase", "hết sạch, cạn kiệt", "deplete, exhaust, use up", "The assembly line halted when workers ran out of bolts."),
            ("scan", "v", "quét mã vạch, rà soát", "read electronically, inspect, check", "Workers scan barcodes to update inventory records instantaneously."),
            ("subtract", "v", "trừ đi, khấu trừ", "deduct, take away, remove", "Subtract the discount from the subtotal before calculating sales tax."),
            ("tedious", "adj", "buồn tẻ, tẻ nhạt", "monotonous, dull, boring", "Manual inventory counting can be extremely tedious."),
            ("verify", "v", "xác minh, kiểm tra lại", "confirm, validate, authenticate", "Always verify shipping addresses before dispatching freight.")
        ]
    },

    # =========================================================================
    # UNIT 5: FINANCING AND BUDGETING (Bài 21 - 25)
    # =========================================================================
    {
        "category": "Financing & Budgeting",
        "lesson_id": 21,
        "lesson_name": "Banking (Ngân hàng)",
        "words": [
            ("accept", "v", "chấp nhận", "agree to, approve, receive", "Most local retailers accept all major credit cards."),
            ("balance", "n/v", "số dư tài khoản / cân đối", "remainder, equilibrium / equalize", "Check your bank account balance before authorizing the transfer."),
            ("borrow", "v", "vay, mượn", "take on loan, obtain on credit", "The small startup borrowed funds to purchase production tooling."),
            ("cautious", "adj", "cẩn trọng, dè dặt", "careful, prudent, wary", "Financial planners advise taking a cautious approach during recessions."),
            ("deduct", "v", "khấu trừ", "subtract, take off, withhold", "Payroll taxes will be deducted automatically from your gross pay."),
            ("dividend", "n", "cổ tức", "share of profits, return, payout", "Stockholders were pleased with the generous quarterly dividend."),
            ("down payment", "n phrase", "tiền đặt cọc, trả trước", "deposit, upfront installment", "Buyers must put down a 20 percent down payment on the commercial site."),
            ("mortgage", "n/v", "khoản thế chấp / thế chấp", "home loan / pledge, encumber", "The company refinanced its property mortgage at a lower interest rate."),
            ("restrict", "v", "hạn chế, giới hạn", "limit, constrain, confine", "Security regulations restrict visitor access to the executive floor."),
            ("signature", "n", "chữ ký", "endorsement, autograph", "Your authorized signature is required on the loan application form."),
            ("take out", "v phrase", "rút tiền, vay mượn", "withdraw, secure (loan)", "She decided to take out a commercial loan to expand her clinic."),
            ("transaction", "n", "giao dịch ngân hàng", "deal, business operation, transfer", "A small service charge applies to foreign currency transactions.")
        ]
    },
    {
        "category": "Financing & Budgeting",
        "lesson_id": 22,
        "lesson_name": "Accounting (Kế toán)",
        "words": [
            ("accounting", "n", "ngành kế toán, sự hạch toán", "bookkeeping, financial auditing", "Proper accounting practices ensure full compliance with tax codes."),
            ("accumulate", "v", "tích lũy, dồn lại", "amass, build up, collect", "Unpaid interest can accumulate rapidly over several months."),
            ("asset", "n", "tài sản", "resource, property, holding", "Patents and trademarks represent valuable intangible corporate assets."),
            ("audit", "n/v", "cuộc kiểm toán / kiểm toán", "examination, inspection / scrutinize", "An independent firm was hired to audit the corporation's books."),
            ("budget", "n/v", "ngân sách / lập ngân sách", "financial plan / allocate, plan", "Marketing expenses exceeded our initial Q2 budget."),
            ("build up", "v phrase", "tích tụ, xây dựng lên", "accumulate, develop, expand", "The firm built up substantial cash reserves to withstand market shocks."),
            ("client", "n", "khách hàng", "customer, patron, purchaser", "The accounting firm advises over 500 corporate clients."),
            ("debt", "n", "khoản nợ", "obligation, liability, deficit", "The CFO outlined a plan to pay down high-interest bank debt."),
            ("outstanding", "adj", "chưa thanh toán / xuất sắc", "unpaid, overdue / exceptional", "Please settle all outstanding invoices before the close of business."),
            ("profitable", "adj", "sinh lời, có lãi", "lucrative, gainful, cost-effective", "Divesting the failing branch made the overall company more profitable."),
            ("reconcile", "v", "đối chiếu (sổ sách)", "settle, square, harmonize", "Accountants work hard each month to reconcile bank statements."),
            ("turnover", "n", "doanh thu / tỷ lệ luân chuyển", "revenue, volume / attrition rate", "High employee turnover can significantly harm company productivity.")
        ]
    },
    {
        "category": "Financing & Budgeting",
        "lesson_id": 23,
        "lesson_name": "Investments (Đầu tư)",
        "words": [
            ("aggressive", "adj", "táo bạo, xông xáo", "assertive, bold, ambitious", "The firm adopted an aggressive strategy to capture market share."),
            ("commit", "v", "cam kết, ủy thác vốn", "pledge, dedicate, allocate", "Management committed five million dollars to the clean energy project."),
            ("conservative", "adj", "thận trọng, bảo thủ", "cautious, moderate, prudent", "Our investment fund takes a conservative approach to bond assets."),
            ("fund", "n/v", "quỹ tiền tệ / tài trợ vốn", "capital, reserve / finance, subsidize", "Venture capital funded the development of the prototype device."),
            ("invest", "v", "đầu tư", "put money into, venture, sink", "It is wise to invest in renewable energy technologies early."),
            ("long-term", "adj", "dài hạn", "extended, enduring, lasting", "Real estate is generally regarded as a solid long-term investment."),
            ("portfolio", "n", "danh mục đầu tư", "holdings, investments profile", "A diversified portfolio helps hedge against sudden stock volatility."),
            ("pull out", "v phrase", "rút vốn, thoái lui", "withdraw, retreat, back out", "Investors pulled out after regulatory authorities announced an inquiry."),
            ("resource", "n", "nguồn lực, tài nguyên", "asset, capability, capital", "Human resources are vital to the sustained success of any enterprise."),
            ("return", "n", "lợi nhuận thu về", "yield, profit, gain, dividend", "The investment yielded a 12 percent annual return on equity."),
            ("wisely", "adv", "khôn ngoan, sáng suốt", "prudently, judiciously, smartly", "She invested her annual performance bonus wisely."),
            ("yield", "v/n", "sinh ra, mang lại / sản lượng, lợi suất", "produce, generate / profit, return", "High-yield municipal bonds attract risk-tolerant retail investors.")
        ]
    },
    {
        "category": "Financing & Budgeting",
        "lesson_id": 24,
        "lesson_name": "Taxes (Thuế vụ)",
        "words": [
            ("calculate", "v", "tính toán", "compute, reckon, figure", "Software makes it easy to calculate payroll withholding taxes."),
            ("deadline", "n", "hạn chót", "due date, cutoff point", "The federal deadline for filing corporate taxes is April 15."),
            ("file", "v", "nộp đơn, nộp hồ sơ", "submit, register, lodge", "Eligible taxpayers can file their annual returns electronically."),
            ("fill out", "v phrase", "điền thông tin vào mẫu", "complete, furnish, write in", "Please fill out all required fields on the tax declaration form."),
            ("give up", "v phrase", "từ bỏ", "surrender, abandon, relinquish", "Do not give up claiming legitimate business deductible expenses."),
            ("joint", "adj", "chung, liên đới", "shared, mutual, collective", "Spouses may choose to file a joint income tax return."),
            ("owe", "v", "nợ (tiền/thuế)", "be indebted to, have a debt of", "The audit revealed that the contractor owed additional back taxes."),
            ("penalty", "n", "tiền phạt, hình phạt", "fine, forfeiture, sanction", "Late tax filings incur an automatic financial penalty."),
            ("preparation", "n", "sự chuẩn bị", "readiness, arrangement, work", "Careful preparation reduces errors during tax season audits."),
            ("refund", "n/v", "tiền hoàn lại / hoàn tiền", "reimbursement, rebate / repay", "Taxpayers who overpaid receive a government refund check."),
            ("spouse", "n", "vợ hoặc chồng", "partner, husband/wife, mate", "Include your spouse's income if filing taxes jointly."),
            ("withhold", "v", "khấu trừ lại, giữ lại", "deduct, retain, hold back", "Employers must withhold state and federal income taxes from paychecks.")
        ]
    },
    {
        "category": "Financing & Budgeting",
        "lesson_id": 25,
        "lesson_name": "Financial Statements (Báo cáo tài chính)",
        "words": [
            ("desire", "v/n", "khao khát, mong muốn", "wish, want, crave / ambition", "The executive expressed a strong desire to cut operational overhead."),
            ("detail", "n/v", "chi tiết / trình bày chi tiết", "particular, specification / specify", "The balance sheet details all company liabilities and assets."),
            ("forecast", "v/n", "dự báo (kinh tế/doanh thu)", "predict, project / projection", "Analysts forecast steady revenue growth across the next three fiscal years."),
            ("level", "n", "mức độ, cấp độ", "standard, echelon, tier", "Production reached its highest level since before the pandemic."),
            ("overall", "adj/adv", "tổng thể, nhìn chung", "general, comprehensive / on the whole", "The CFO reported an overall increase in operating profit margins."),
            ("perspective", "n", "góc nhìn, quan điểm", "viewpoint, angle, outlook", "Historical financial data provides perspective on market fluctuations."),
            ("projected", "adj", "dự kiến, phóng chiếu", "estimated, predicted, anticipated", "Projected earnings for Q4 exceed prior analyst expectations."),
            ("realistic", "adj", "thực tế, khả thi", "feasible, pragmatic, sensible", "Management set realistic sales targets for the new sales recruits."),
            ("target", "n/v", "mục tiêu / nhắm đến", "goal, objective / aim, focus", "The marketing team met its quarterly subscription target."),
            ("translation", "n", "sự chuyển đổi, chuyển ngữ", "conversion, transformation, rendering", "Currency translation differences affected consolidated net income."),
            ("typically", "adv", "thông thường, điển hình", "ordinarily, customarily, normally", "Year-end financial audits typically take around six weeks."),
            ("unprecedented", "adj", "chưa từng có tiền lệ", "groundbreaking, extraordinary, unmatched", "The technology firm experienced unprecedented demand for AI chips.")
        ]
    },

    # =========================================================================
    # UNIT 6: MANAGEMENT ISSUES (Bài 26 - 30)
    # =========================================================================
    {
        "category": "Management Issues",
        "lesson_id": 26,
        "lesson_name": "Property and Departments (Mặt bằng & Phòng ban)",
        "words": [
            ("adjacent", "adj", "liền kề, sát bên", "adjoining, neighboring, next to", "The conference hall is adjacent to the executive dining room."),
            ("collaborate", "v", "hợp tác, phối hợp", "work together, cooperate, team up", "Marketing and engineering collaborated to launch the application."),
            ("concentrate", "v", "tập trung", "focus, center, zero in", "Noise cancellation booths help workers concentrate on complex tasks."),
            ("conducive", "adj", "thuận lợi cho, có ích cho", "favorable, helpful, beneficial to", "A quiet workspace is conducive to creative problem-solving."),
            ("disrupt", "v", "gây gián đoạn, làm đảo lộn", "interrupt, disturb, disorganize", "Office remodeling work will temporarily disrupt daily operations."),
            ("hamper", "v", "gây cản trở, làm vướng", "hinder, impede, obstruct", "Supply chain bottlenecks hampered product assembly lines."),
            ("inconsiderately", "adv", "thiếu chu đáo, bất lịch sự", "thoughtlessly, heedlessly", "Parking inconsiderately in fire lanes is strictly forbidden."),
            ("lobby", "n/v", "tiền sảnh / vận động hành lang", "foyer, reception / advocate", "Visitors must register at the reception desk in the lobby."),
            ("move up", "v phrase", "thăng tiến, đẩy sớm", "advance, promote, reschedule earlier", "He moved up rapidly through corporate ranks due to diligence."),
            ("open to", "phrase", "cởi mở, sẵn sàng tiếp thu", "receptive to, willing to consider", "Management is open to adopting flexible working hours."),
            ("opt", "v", "lựa chọn, quyết định", "choose, select, decide on", "Many telecommuters opt for co-working facilities near home."),
            ("scrutiny", "n", "sự xem xét kỹ lưỡng, kiểm soát gắt gao", "inspection, examination, audit", "Public companies face rigorous regulatory scrutiny.")
        ]
    },
    {
        "category": "Management Issues",
        "lesson_id": 27,
        "lesson_name": "Board Meetings and Committees (Họp HĐQT & Ủy ban)",
        "words": [
            ("adhere to", "v phrase", "tuân thủ, giữ đúng", "abide by, comply with, follow", "All committee members must adhere strictly to meeting bylaws."),
            ("agenda", "n", "chương trình nghị sự", "schedule, program, timetable", "The first item on today's agenda is approving the annual budget."),
            ("bring up", "v phrase", "nêu ra, đề cập", "mention, introduce, broach", "The treasurer brought up several issues regarding cash liquidity."),
            ("conclude", "v", "kết luận, kết thúc", "finish, wrap up, deduce", "The chairperson concluded the meeting promptly at 5:00 P.M."),
            ("go ahead", "v phrase / n", "tiến hành / sự cho phép", "proceed, move forward / green light", "Management gave the go ahead to break ground on the warehouse."),
            ("goal", "n", "mục tiêu", "objective, aim, target", "Our primary strategic goal is improving delivery turnaround time."),
            ("lengthy", "adj", "dài dòng, lê thê", "prolonged, protracted, long", "The lengthy discussion delayed the board's final voting procedure."),
            ("matter", "n/v", "vấn đề / có ý nghĩa quan trọng", "issue, subject, topic / count", "Let us resolve this personnel matter before moving to financial items."),
            ("periodically", "adv", "định kỳ, theo chu kỳ", "regularly, recurrently, at intervals", "Board committee charters should be reviewed periodically."),
            ("priority", "n", "sự ưu tiên", "precedence, urgency, preference", "Customer safety is the airline's utmost operational priority."),
            ("progress", "n/v", "tiến độ / tiến triển", "advancement, development / advance", "The project director gave a positive progress report to the committee."),
            ("waste", "v/n", "lãng phí / rác thải, hao phí", "squander, misuse / loss, scrap", "Inefficient administrative workflows waste valuable staff hours.")
        ]
    },
    {
        "category": "Management Issues",
        "lesson_id": 28,
        "lesson_name": "Quality Control (Kiểm định chất lượng)",
        "words": [
            ("brand", "n/v", "thương hiệu / xây dựng thương hiệu", "trademark, label / market", "The company built a globally recognized luxury brand."),
            ("conform", "v", "tuân theo chuẩn mực", "comply, match, adhere, adapt", "All exported goods must conform to European safety standards."),
            ("defect", "n", "khiếm khuyết, lỗi sản phẩm", "flaw, fault, imperfection, blemish", "Quality inspectors check each smartphone for screen defects."),
            ("enhance", "v", "nâng cao, cải thiện", "improve, boost, enrich, heighten", "Upgraded firmware enhanced battery life by 20 percent."),
            ("garment", "n", "hàng may mặc, quần áo", "clothing, apparel, attire", "Textile inspectors examine each garment for stitching flaws."),
            ("inspect", "v", "kiểm tra, thanh tra", "examine, audit, scrutinize, check", "Safety technicians inspect hydraulic brakes before every takeoff."),
            ("perceive", "v", "nhận thức, đánh giá", "regard, view, discern, notice", "Consumers perceive domestic brands as offering greater durability."),
            ("repel", "v", "chống lại, đẩy lùi (nước/bụi)", "resist, ward off, drive away", "The waterproof exterior fabric effectively repels rain."),
            ("take back", "v phrase", "nhận lại, thu hồi", "accept return, reclaim, withdraw", "The retailer took back the defective toaster and issued a full refund."),
            ("throw out", "v phrase", "vứt bỏ, loại bỏ", "discard, dump, dispose of", "Damaged packaging should be thrown out immediately."),
            ("uniformly", "adv", "đồng đều, đồng nhất", "consistently, evenly, identically", "The paint coating must be sprayed uniformly across the car panel."),
            ("wrinkle", "n/v", "nếp nhăn / làm nhăn", "crease, fold, pucker", "The treated wool blend is resistant to fabric wrinkles.")
        ]
    },
    {
        "category": "Management Issues",
        "lesson_id": 29,
        "lesson_name": "Product Development (Phát triển sản phẩm)",
        "words": [
            ("anxious", "adj", "lo lắng, sốt ruột mong chờ", "worried, nervous, eager", "Engineers were anxious about the results of the crash test."),
            ("ascertain", "v", "xác minh chắc chắn, làm sáng tỏ", "determine, find out, discover", "Further laboratory testing is needed to ascertain the cause of failure."),
            ("assume", "v", "giả định, đảm đương", "presume, suppose / take on, shoulder", "Never assume user requirements without conducting field research."),
            ("decade", "n", "thập kỷ (10 năm)", "ten-year period", "Our firm has led battery innovation for over a decade."),
            ("examine", "v", "kiểm tra, nghiên cứu kỹ", "inspect, scrutinize, analyze", "The research lab examined several composite materials for durability."),
            ("experiment", "v/n", "thử nghiệm / cuộc thí nghiệm", "test, try out / trial, investigation", "Developers experimented with different touch-screen layouts."),
            ("logical", "adj", "hợp lý, logic", "rational, sensible, coherent", "Automating data collection is the logical next step in optimization."),
            ("research", "n/v", "nghiên cứu", "study, inquiry / explore, investigate", "Substantial budget is allocated to pharmaceutical R&D research."),
            ("responsibility", "n", "trách nhiệm, nhiệm vụ", "duty, accountability, obligation", "Leading the design overhaul is the lead engineer's responsibility."),
            ("solve", "v", "giải quyết (vấn đề)", "resolve, fix, unravel", "Innovative design helped solve thermal overheating in the laptop."),
            ("supervisor", "n", "người giám sát, quản lý", "manager, overseer, team lead", "Report any machinery irregularities to your shop supervisor."),
            ("systematically", "adv", "một cách có hệ thống", "methodically, orderly, systematically", "Technicians systematically tested each circuit board component.")
        ]
    },
    {
        "category": "Management Issues",
        "lesson_id": 30,
        "lesson_name": "Renting and Leasing (Thuê & Cho thuê mặt bằng)",
        "words": [
            ("apprehensive", "adj", "e ngại, lo âu", "anxious, uneasy, worried", "Tenants were apprehensive about proposed utility rate hikes."),
            ("circumstance", "n", "hoàn cảnh, tình huống", "situation, condition, context", "Under no circumstances should building security doors be left propped open."),
            ("condition", "n", "điều kiện, tình trạng", "state, terms, prerequisite", "The office premises must be returned in pristine condition."),
            ("due to", "prep", "do, vì, nhờ có", "because of, owing to, on account of", "The lease renegotiation stalled due to disagreements over rent."),
            ("fluctuate", "v", "dao động, biến động", "waver, vary, oscillate, shift", "Commercial rental rates fluctuate according to regional economic cycles."),
            ("get out of", "v phrase", "thoát khỏi (hợp đồng/nghĩa vụ)", "escape, break, exit, withdraw from", "The tenant hired a lawyer to get out of the restrictive lease."),
            ("indicator", "n", "chỉ số, dấu hiệu", "sign, measure, metric, index", "Low vacancy rates are a key indicator of commercial real estate health."),
            ("lease", "n/v", "hợp đồng thuê / cho thuê", "rental agreement / rent, charter", "The company signed a five-year lease on the downtown skyscraper."),
            ("lock into", "v phrase", "ràng buộc chặt chẽ vào", "commit to, bind, secure", "A multi-year contract locks the tenant into a fixed monthly rate."),
            ("occupy", "v", "chiếm hữu, sử dụng", "inhabit, take up, reside in", "The accounting firm occupies the top three floors of the building."),
            ("subject to", "adj phrase", "tùy thuộc vào, có thể bị", "conditional on, dependent on, prone to", "Rental quotes are subject to change without prior written notice."),
            ("tenant", "n", "người thuê nhà/văn phòng", "renter, lessee, occupant", "Landlords must give tenants 24 hours notice before entering units.")
        ]
    },

    # =========================================================================
    # UNIT 7: RESTAURANTS AND EVENTS (Bài 31 - 35)
    # =========================================================================
    {
        "category": "Restaurants & Events",
        "lesson_id": 31,
        "lesson_name": "Selecting a Restaurant (Chọn nhà hàng)",
        "words": [
            ("appeal", "v/n", "lôi cuốn, hấp dẫn / sự lôi cuốn", "attract, interest / allure, charm", "The bistro's outdoor patio appeals to lunch crowds."),
            ("arrive", "v", "đến nơi", "reach, show up, turn up", "Guests are expected to arrive at the banquet hall by 7:00 P.M."),
            ("compromise", "n/v", "sự thỏa hiệp / thỏa hiệp", "concession, middle ground / settle", "Choosing a fusion menu was a compromise between team members."),
            ("daring", "adj", "táo bạo, mạo hiểm", "bold, adventurous, audacious", "The chef is known for his daring combinations of sweet and savory."),
            ("familiar", "adj", "quen thuộc", "known, recognizable, customary", "Corporate travelers prefer staying near familiar restaurant chains."),
            ("guide", "n/v", "sách hướng dẫn / chỉ dẫn", "handbook, directory / direct, lead", "Check the local dining guide for top-rated seafood restaurants."),
            ("majority", "n", "đa số, phần lớn", "bulk, greater part, preponderance", "The majority of guests preferred vegetarian meal options."),
            ("mix", "v/n", "kết hợp, pha trộn / sự pha trộn", "blend, combine / mixture, assortment", "The eatery offers a pleasant mix of traditional and modern cuisine."),
            ("rely", "v", "dựa vào, tin cậy vào (rely on)", "depend on, count on, bank on", "Caterers rely on fresh morning market deliveries."),
            ("secure", "v/adj", "giữ được, bảo đảm / an toàn", "obtain, guarantee / safe, stable", "Make sure to secure a table reservation two weeks in advance."),
            ("subjective", "adj", "chủ quan", "personal, individual, biased", "Food ratings can often be subjective rather than objective."),
            ("suggestion", "n", "gợi ý, đề xuất", "recommendation, proposal, tip", "The server provided excellent suggestions for wine pairings.")
        ]
    },
    {
        "category": "Restaurants & Events",
        "lesson_id": 32,
        "lesson_name": "Eating Out (Ăn ngoài công sở)",
        "words": [
            ("basic", "adj", "căn bản, cơ bản", "fundamental, essential, rudimentary", "Salt and pepper are basic seasonings used in every kitchen."),
            ("complete", "adj/v", "hoàn chỉnh, trọn vẹn / hoàn thành", "whole, full / finish, conclude", "The three-course dinner comes complete with complimentary dessert."),
            ("excite", "v", "kích thích, làm hào hứng", "thrill, stimulate, animate", "The seasonal tasting menu excited local culinary critics."),
            ("flavor", "n/v", "hương vị / nêm nếm gia vị", "taste, savor, aroma / season", "Slow cooking enhances the natural flavor of the beef stew."),
            ("forget", "v", "quên", "fail to remember, overlook, neglect", "Do not forget to inform the server about food allergies."),
            ("ingredient", "n", "nguyên liệu, thành phần", "component, element, constituent", "Our pastry chefs use only certified organic ingredients."),
            ("judge", "v/n", "đánh giá, phán xét / thẩm phán", "rate, evaluate, appraise / arbiter", "Do not judge a restaurant solely by its casual interior decor."),
            ("patron", "n", "khách quen, khách hàng thân thiết", "customer, client, regular visitor", "The cafe rewards loyal patrons with free beverage upgrades."),
            ("predict", "v", "dự đoán, tiên lượng", "forecast, anticipate, foresee", "Hospitality analysts predict strong holiday restaurant bookings."),
            ("random", "adj", "ngẫu nhiên", "arbitrary, chance, accidental", "Inspectors conduct random hygiene checks at regional diners."),
            ("remind", "v", "nhắc nhở", "prompt, jog memory, alert", "The concierge called to remind the executive of his 8:00 P.M. booking."),
            ("spicy", "adj", "cay, nhiều gia vị", "hot, peppery, piquant, seasoned", "Dishes marked with a chili icon are exceptionally spicy.")
        ]
    },
    {
        "category": "Restaurants & Events",
        "lesson_id": 33,
        "lesson_name": "Ordering Lunch (Đặt bữa trưa công sở)",
        "words": [
            ("burden", "n/v", "gánh nặng / đè nặng", "load, strain, encumbrance / weigh down", "Ordering catering for 300 staff is a heavy logistical burden."),
            ("commonly", "adv", "thường, phổ biến", "frequently, typically, universally", "Sandwiches and wraps are commonly served at corporate lunches."),
            ("delivery", "n", "giao hàng, sự vận chuyển", "conveyance, carriage, dispatch", "Order lunch before 11:00 A.M. to guarantee timely delivery."),
            ("elegance", "n", "sự thanh lịch, tao nhã", "grace, refinement, sophistication", "The banquet hall impressed guests with its architectural elegance."),
            ("fall to", "v phrase", "rơi vào tay (trách nhiệm)", "become duty of, devolve upon", "Organizing the retirement luncheon fell to the junior coordinator."),
            ("impress", "v", "gây ấn tượng tốt", "make an impact on, dazzle, awe", "The presentation and quality of the gourmet catering impressed the board."),
            ("individual", "adj/n", "cá nhân, riêng biệt / người", "separate, distinct, personal / person", "Each attendee received an individual boxed gourmet lunch."),
            ("narrow", "v/adj", "thu hẹp / chật hẹp", "constrict, limit / tight, slender", "We narrowed down the catering choices to three top culinary vendors."),
            ("pick up", "v phrase", "lấy hàng, đón", "collect, fetch, gather", "Please pick up the catering platters from the bakery at noon."),
            ("settle", "v", "thanh toán, ổn định", "pay, resolve, establish", "The account manager settled the dining bill using the corporate card."),
            ("coordinate", "v", "điều phối, sắp xếp", "organize, align, synchronize", "The administrative assistant coordinated catering for the board seminar."),
            ("appetizing", "adj", "hấp dẫn, ngon miệng", "mouthwatering, savory, delectable", "The buffet display featured an array of appetizing hot appetizers.")
        ]
    },
    {
        "category": "Restaurants & Events",
        "lesson_id": 34,
        "lesson_name": "Cooking as a Craft (Nghệ thuật ẩm thực)",
        "words": [
            ("accustom to", "v phrase", "làm cho quen với", "familiarize with, habituate to", "Chefs must accustom themselves to working in high-heat kitchens."),
            ("apprentice", "n/v", "người học việc / thực tập", "trainee, intern, pupil", "The culinary academy apprentice trained under three Michelin chefs."),
            ("culinary", "adj", "thuộc về ẩm thực/nấu nướng", "gastronomic, cooking, kitchen", "France is globally celebrated for its rich culinary heritage."),
            ("demanding", "adj", "đòi hỏi khắt khe, áp lực", "exacting, tough, strenuous", "Running an executive kitchen during dinner rush is highly demanding."),
            ("draw", "v", "thu hút, lôi kéo", "attract, entice, pull in", "The food festival draws thousands of tourists each autumn."),
            ("incorporate", "v", "kết hợp, sáp nhập", "integrate, include, assimilate", "The chef incorporated organic micro-greens into every entree."),
            ("influx", "n", "dòng người/vật tràn vào", "inrush, flood, stream, inflow", "Summer holidays bring a huge influx of tourists to coastal bistros."),
            ("method", "n", "phương pháp, kỹ thuật", "technique, procedure, process", "Braising is a traditional cooking method for tenderizing meat."),
            ("outlet", "n", "chi nhánh, cửa hiệu / lối thoát", "branch, shop, market / exit", "The bakery chain opened five new retail outlets this quarter."),
            ("profession", "n", "nghề nghiệp, chuyên môn", "career, occupation, calling, trade", "Professional catering is a rewarding but taxing profession."),
            ("relinquish", "v", "từ bỏ, nhượng lại", "surrender, give up, hand over", "The veteran head chef relinquished management of the kitchen."),
            ("theme", "n", "chủ đề", "topic, subject, motif", "The corporate gala featured a vintage Mediterranean dining theme.")
        ]
    },
    {
        "category": "Restaurants & Events",
        "lesson_id": 35,
        "lesson_name": "Events (Sự kiện & Tiệc chiêu đãi)",
        "words": [
            ("assist", "v", "hỗ trợ, giúp đỡ", "help, aid, support", "Volunteers assisted attendees with directional navigation."),
            ("coordinate", "v", "điều phối, sắp xếp", "harmonize, organize, orchestrate", "Event planners coordinate logistics between hotels and shuttles."),
            ("dimension", "n", "kích thước, quy mô", "size, proportion, measurement", "Measure the booth dimensions before designing backdrop banners."),
            ("exact", "adj", "chính xác", "precise, accurate, correct", "Please state the exact number of attendees for banquet seating."),
            ("general", "adj", "chung, tổng quát", "broad, overall, non-specific", "The general admission ticket grants entry to all exhibition halls."),
            ("ideal", "adj/n", "lý tưởng / chuẩn mực lý tưởng", "perfect, optimal / paragon", "The beachfront resort was an ideal venue for the team retreat."),
            ("lead time", "n phrase", "thời gian chuẩn bị, tiến độ đặt trước", "preparation period, planning lag", "Custom convention merchandise requires a four-week lead time."),
            ("plan", "v/n", "lên kế hoạch / kế hoạch", "scheme, program, map out", "The committee met to plan the schedule for the product unveil."),
            ("proximity", "n", "sự gần gũi, cự ly gần", "nearness, closeness, vicinity", "Hotel proximity to the airport was a decisive selection factor."),
            ("regulate", "v", "điều tiết, quy định", "control, govern, modulate", "Fire safety bylaws regulate the maximum occupancy of conference rooms."),
            ("site", "n", "địa điểm, vị trí", "location, venue, spot, area", "Inspectors visited the construction site to ensure code compliance."),
            ("stage", "v/n", "tổ chức, dàn dựng / sân khấu", "mount, organize, hold / platform", "The association will stage its biennial technology expo in Berlin.")
        ]
    },

    # =========================================================================
    # UNIT 8: TRAVEL (Bài 36 - 40)
    # =========================================================================
    {
        "category": "Travel",
        "lesson_id": 36,
        "lesson_name": "General Travel (Du lịch & Công tác tổng quan)",
        "words": [
            ("agent", "n", "đại lý, nhân viên ủy quyền", "representative, broker, operative", "Consult your travel agent for discount group airfares."),
            ("announcement", "n", "thông báo", "notice, declaration, broadcast", "Passengers listened carefully to the gate change announcement."),
            ("beverage", "n", "đồ uống, thức uống", "drink, refreshment, liquid", "Complimentary hot beverages are offered on all long-haul flights."),
            ("blanket", "n/v", "chăn đắp / bao phủ", "cover, quilt / cover entirely", "Flight attendants distributed blankets and pillows on the red-eye flight."),
            ("board", "v/n", "lên tàu/xe/máy bay / ban giám đốc", "embark, get on / council, committee", "Passengers with small children may board the aircraft first."),
            ("claim", "v/n", "nhận lại, yêu cầu / sự đòi bồi thường", "retrieve, demand / assertion", "Proceed directly to carousel four to claim checked luggage."),
            ("delay", "v/n", "trì hoãn, chậm trễ / sự chậm trễ", "postpone, stall, defer / hold-up", "Adverse winter weather caused an unexpected three-hour flight delay."),
            ("depart", "v", "khởi hành, rời đi", "leave, take off, set out", "The high-speed express train departs from track nine promptly."),
            ("embarkation", "n", "sự lên tàu/thuyền/máy bay", "boarding, departure", "Have your passport and boarding pass ready at embarkation."),
            ("itinerary", "n", "lịch trình chuyến đi", "travel schedule, route, route plan", "The administrative assistant prepared a detailed five-day itinerary."),
            ("luggage", "n", "hành lý", "baggage, suitcases, bags", "Airlines impose weight restrictions on carry-on luggage."),
            ("prohibit", "v", "cấm, ngăn cấm", "forbid, ban, disallow, veto", "Federal aviation laws prohibit smoking inside commercial cabins.")
        ]
    },
    {
        "category": "Travel",
        "lesson_id": 37,
        "lesson_name": "Air Travel (Vận tải hàng không)",
        "words": [
            ("airline", "n", "hãng hàng không", "carrier, aviation company", "The airline launched new non-stop routes to Southeast Asia."),
            ("cargo", "n", "hàng hóa chuyên chở", "freight, shipment, payload, goods", "Cargo planes transported medical relief supplies overnight."),
            ("clearance", "n", "sự thông quan, cấp phép cất cánh", "authorization, permission, customs check", "The aircraft received air traffic clearance for takeoff on runway two."),
            ("crew", "n", "phi hành đoàn, đội ngũ", "staff, team, personnel", "Flight cabin crew demonstrated safety oxygen mask protocols."),
            ("embark", "v", "lên tàu/máy bay", "board, go aboard", "Travelers embarked on the charter flight after security checks."),
            ("flight", "n", "chuyến bay", "aviation trip, air journey", "Her direct flight arrived in London twenty minutes ahead of time."),
            ("onboard", "adj/adv", "trên máy bay/tàu", "aboard, on the craft", "Free Wi-Fi connectivity is available onboard all international flights."),
            ("passenger", "n", "hành khách", "commuter, traveler, voyager", "All passengers must remain seated with seatbelts fastened."),
            ("charter", "v/n", "thuê bao trọn gói / chuyến bay bao chuyến", "hire, lease, rent / leased craft", "The corporation chartered a private jet for the leadership summit."),
            ("delayed", "adj", "bị trì hoãn, trễ", "late, held up, stalled", "Delayed passengers were issued meal and hotel accommodation vouchers."),
            ("economy", "n/adj", "hạng phổ thông / tiết kiệm", "coach class, standard seating / budget", "Many business travelers book economy tickets to cut overhead costs."),
            ("valid", "adj", "hợp lệ, còn hiệu lực", "legitimate, authorized, unexpired", "International passengers must hold a passport valid for at least six months.")
        ]
    },
    {
        "category": "Travel",
        "lesson_id": 38,
        "lesson_name": "Trains (Đường sắt & Tàu hỏa)",
        "words": [
            ("accelerate", "v", "tăng tốc, thúc đẩy", "speed up, quicken, hasten", "The bullet train accelerates smoothly to 300 kilometers per hour."),
            ("conductor", "n", "người soát vé, trưởng tàu", "ticket collector, train manager", "The conductor walked down the train car checking rail passes."),
            ("departure", "n", "sự khởi hành", "leaving, takeoff, exit", "Check the overhead display board for updated departure times."),
            ("duration", "n", "khoảng thời gian kéo dài", "length, span, period", "The overall duration of the rail journey is approximately two hours."),
            ("exotic", "adj", "kỳ lạ, độc đáo, ngoại lai", "foreign, unusual, striking", "Scenic train journeys traverse exotic mountain landscapes."),
            ("freight", "n/v", "hàng hóa chuyên chở / vận chuyển hàng", "cargo, haulage / transport", "Railways carry vast amounts of industrial container freight."),
            ("pass", "n/v", "thẻ thông hành / đi qua", "permit, ticket / go by, traverse", "The unlimited seven-day regional rail pass saves visitors money."),
            ("picturesque", "adj", "đẹp như tranh vẽ", "scenic, charming, beautiful", "Passengers enjoyed picturesque vistas along the coastal railway line."),
            ("platform", "n", "sân ga tàu", "track area, concourse, quay", "The express train to Manchester is arriving at platform three."),
            ("reliable", "adj", "đáng tin cậy", "dependable, trustworthy, solid", "Electric commuter trains provide a clean and reliable service."),
            ("ride", "v/n", "đi xe/tàu / chuyến đi", "travel, journey / trip", "The commuter ride into the downtown financial center takes 25 minutes."),
            ("transfer", "v/n", "chuyển tuyến, sang tàu / sự đổi tàu", "switch, shift, relocate / transit", "Passengers traveling to the airport must transfer at Central Station.")
        ]
    },
    {
        "category": "Travel",
        "lesson_id": 39,
        "lesson_name": "Hotels (Khách sạn & Lưu trú)",
        "words": [
            ("advance", "n/adj/v", "sự đặt trước / trước / tiến bộ", "prior / in advance / forward", "Book your hotel accommodation months in advance during peak season."),
            ("chain", "n", "chuỗi (khách sạn/nhà hàng)", "group, syndicate, franchise", "The international hotel chain opened three new boutique resorts."),
            ("check in", "v phrase", "làm thủ tục nhận phòng", "register, sign in", "Guests may check in at the reception desk starting at 3:00 P.M."),
            ("confirm", "v", "xác nhận", "verify, validate, corroborate", "The receptionist called to confirm our hotel reservation dates."),
            ("expect", "v", "mong chờ, dự kiến", "anticipate, foresee, await", "The hotel expects full occupancy throughout the convention weekend."),
            ("housekeeper", "n", "nhân viên dọn phòng", "maid, room cleaner", "The executive requested extra fresh towels from the floor housekeeper."),
            ("notify", "v", "thông báo", "inform, alert, advise", "Please notify hotel staff immediately if your key card fails."),
            ("preclude", "v", "ngăn chặn, loại trừ", "prevent, rule out, exclude", "A major plumbing leak precluded guests from using the swimming pool."),
            ("quote", "v/n", "báo giá / bản báo giá", "price, estimate / quotation", "The front desk agent quoted a discounted corporate room rate."),
            ("rate", "n", "mức giá, thuế suất", "price, tariff, cost, charge", "The hotel offers discounted weekend room rates for large tour groups."),
            ("reserve", "v", "đặt trước", "book, secure, hold", "We reserved a non-smoking suite with a panoramic harbor view."),
            ("service", "n", "dịch vụ", "assistance, amenities, care", "Prompt room service is available 24 hours a day for all guests.")
        ]
    },
    {
        "category": "Travel",
        "lesson_id": 40,
        "lesson_name": "Car Rentals (Thuê xe tự lái)",
        "words": [
            ("busy", "adj", "bận rộn, nhộn nhịp", "occupied, hectic, crowded", "Car rental kiosks at the terminal were extremely busy on Friday."),
            ("coincide", "v", "trùng hợp, diễn ra đồng thời", "concur, overlap, correspond", "Our business trip coincided with a major automotive convention."),
            ("confuse", "v", "làm nhầm lẫn, bối rối", "mix up, bewilder, baffle", "Poor airport signage can confuse arriving foreign drivers."),
            ("contact", "v/n", "liên hệ / người liên hệ", "reach, get in touch with / connection", "Contact the emergency roadside hotline if the rental car breaks down."),
            ("disappoint", "v", "làm thất vọng", "let down, dishearten", "The lack of available GPS units disappointed business renters."),
            ("intend", "v", "dự định, có ý định", "plan, aim, purpose", "The sales representative intends to return the sedan by 6:00 P.M."),
            ("license", "n", "giấy phép, bằng lái", "permit, authorization, certificate", "You must present a valid driver's license to pick up the vehicle."),
            ("nervous", "adj", "lo lắng, bồn chồn", "apprehensive, anxious, tense", "Navigating an unfamiliar foreign city makes some drivers nervous."),
            ("optional", "adj", "tùy chọn, không bắt buộc", "voluntary, discretionary, elective", "Comprehensive collision damage insurance is an optional upgrade."),
            ("tempt", "v", "cám dỗ, lôi cuốn", "entice, lure, attract", "The luxury sports car upgrade tempted many vacationing travelers."),
            ("thrill", "n/v", "sự phấn khích / làm thích thú", "excitement, sensation / exhilarate", "Clients were thrilled with the dealership's prompt vehicle exchange."),
            ("tier", "n", "hạng, bậc, cấp độ", "level, rank, grade, layer", "Rental vehicle prices vary significantly depending on vehicle tier.")
        ]
    },

    # =========================================================================
    # UNIT 9: ENTERTAINMENT (Bài 41 - 45)
    # =========================================================================
    {
        "category": "Entertainment",
        "lesson_id": 41,
        "lesson_name": "Movies (Điện ảnh & Chiếu phim)",
        "words": [
            ("attain", "v", "đạt được", "achieve, reach, accomplish", "The independent documentary attained widespread international acclaim."),
            ("combine", "v", "kết hợp", "merge, blend, unite", "The film combines historical drama with cutting-edge CGI visual effects."),
            ("description", "n", "sự mô tả, miêu tả", "depiction, portrayal, account", "The trailer gives a thrilling description of the upcoming sci-fi release."),
            ("disperse", "v", "giải tán, tản ra", "scatter, distribute, dissolve", "Moviegoers dispersed quietly after the midnight screening ended."),
            ("entertainment", "n", "sự giải trí, ngành giải trí", "amusement, recreation, leisure", "The digital streaming sector revolutionized global entertainment."),
            ("influence", "v/n", "ảnh hưởng, tác động", "affect, shape / impact, leverage", "Foreign art cinema strongly influenced the director's unique aesthetic."),
            ("range", "n/v", "phạm vi, dải / trải dài", "scope, spectrum / vary, extend", "The theater screens a wide range of family-friendly animated films."),
            ("release", "v/n", "phát hành, ra mắt / sự công chiếu", "launch, premiere / publication", "The movie studio scheduled the sequel's release for Thanksgiving weekend."),
            ("represent", "v", "đại diện, tượng trưng", "stand for, symbolize, embody", "A talent agency was hired to represent the lead actors globally."),
            ("separate", "adj/v", "riêng biệt / chia tách", "distinct, individual / divide", "VIP ticket holders enter the auditorium through a separate foyer."),
            ("successive", "adj", "liên tiếp, kế tiếp nhau", "consecutive, sequential, continuous", "The summer blockbuster topped box office rankings for three successive weeks."),
            ("visual", "adj/n", "thị giác, trực quan / hình ảnh", "optical, graphic / visual aid", "The visual effects team was recognized with an industry academy award.")
        ]
    },
    {
        "category": "Entertainment",
        "lesson_id": 42,
        "lesson_name": "Theater (Sân khấu kịch nghệ)",
        "words": [
            ("action", "n", "hành động, diễn biến kịch tính", "movement, deed, drama", "The rapid dramatic action held the theater audience spellbound."),
            ("approach", "v/n", "tiếp cận / cách tiếp cận", "reach, near / method, technique", "The theater director took an innovative approach to staging Shakespeare."),
            ("audience", "n", "khán giả", "spectators, viewers, crowd", "The enthusiastic audience gave the Broadway cast a standing ovation."),
            ("creative", "adj", "sáng tạo", "inventive, original, imaginative", "The playwright received high praise for her creative scriptwriting."),
            ("dialogue", "n", "lời thoại, cuộc đối thoại", "conversation, lines, script talk", "Actors spent weeks perfecting the dialect in their stage dialogue."),
            ("element", "n", "yếu tố, thành phần", "component, factor, facet", "Sound design was a crucial element in creating dramatic suspense."),
            ("experience", "n/v", "trải nghiệm, kinh nghiệm / nếm trải", "adventure, knowledge / encounter", "Attending an outdoor Shakespeare festival is an unforgettable experience."),
            ("occur", "v", "xảy ra, diễn ra", "happen, take place, transpire", "Technical microphone glitches occurred during the first act opening."),
            ("perform", "v", "biểu diễn, trình diễn", "act, stage, execute", "The philharmonic orchestra will perform live at the grand hall."),
            ("rehearse", "v", "diễn tập, luyện tập", "practice, run through, prep", "The theater ensemble rehearsed daily leading up to opening night."),
            ("review", "n/v", "bài đánh giá, phê bình / xem xét", "critique, evaluation / assess", "The drama received glowing reviews in several weekend newspapers."),
            ("sold out", "adj phrase", "hết vé, cháy vé", "all tickets sold, packed", "All Saturday evening Broadway performances are completely sold out.")
        ]
    },
    {
        "category": "Entertainment",
        "lesson_id": 43,
        "lesson_name": "Music (Âm nhạc & Hòa nhạc)",
        "words": [
            ("available", "adj", "có sẵn, còn chỗ", "accessible, obtainable, on hand", "Concert tickets are available online through verified digital box offices."),
            ("broaden", "v", "mở rộng", "widen, expand, diversify", "Streaming algorithms help listeners broaden their musical tastes."),
            ("category", "n", "thể loại, nhóm, hạng mục", "classification, genre, group", "Jazz and classical music belong to distinct award categories."),
            ("disparate", "adj", "khác biệt, tạp nham", "diverse, distinct, contrasting", "The collaborative album harmoniously blends disparate world rhythms."),
            ("divide", "v", "chia cắt, phân chia", "split, separate, portion", "Royalties were divided equally among band members and songwriters."),
            ("favor", "v/n", "ủng hộ, ưa chuộng / ân huệ", "prefer, lean toward / kindness, goodwill", "Younger demographics favor music streaming over vinyl records."),
            ("instinct", "n", "bản năng, năng khiếu tự nhiên", "intuition, flair, inclination", "The conductor relied on his musical instincts to set the tempo."),
            ("prefer", "v", "thích hơn", "favor, choose rather than", "Many music purists prefer analog acoustic recordings."),
            ("reason", "n/v", "lý do, nguyên nhân / lập luận", "cause, rationale / deduce", "The concert was postponed for safety reasons due to lightning."),
            ("relaxation", "n", "sự thư giãn, nghỉ ngơi", "leisure, repose, unwinding", "Listening to mellow classical guitar promotes physical relaxation."),
            ("taste", "n/v", "gu thưởng thức, khiếu thẩm mỹ / nếm", "preference, appreciation / sample", "Her eclectic musical taste spans indie rock and Renaissance baroque."),
            ("urge", "v/n", "thúc giục, kêu gọi / thôi thúc", "encourage, implore / impulse", "Organizers urge concertgoers to utilize public light rail transit.")
        ]
    },
    {
        "category": "Entertainment",
        "lesson_id": 44,
        "lesson_name": "Museums (Bảo tàng & Triển lãm)",
        "words": [
            ("acquire", "v", "mua lại, có được", "obtain, purchase, secure", "The national museum acquired a rare seventeenth-century portrait."),
            ("admire", "v", "chiêm ngưỡng, thán phục", "appreciate, marvel at, respect", "Art tourists gathered in the gallery to admire the Impressionist paintings."),
            ("collection", "n", "bộ sưu tập", "exhibit, assemblage, gathering", "The museum houses a priceless private collection of Roman artifacts."),
            ("criticism", "n", "lời phê bình, nhận xét", "critique, commentary, review", "The curator addressed criticism regarding exhibition admission price hikes."),
            ("express", "v", "bày tỏ, thể hiện", "convey, articulate, exhibit", "The sculptor uses recycled scrap bronze to express environmental themes."),
            ("fashion", "n/v", "thời trang, phong cách / tạo tác", "trend, vogue / craft, shape", "The retrospective explores how fashion photography evolved through the decades."),
            ("leisure", "n", "thời gian rảnh rỗi", "spare time, recreation, downtime", "Visiting regional art galleries is a relaxing leisure activity."),
            ("respond", "v", "phản hồi, hưởng ứng", "reply, answer, react", "Over 5,000 visitors responded positively to the interactive installation."),
            ("schedule", "v/n", "lên lịch / thời gian biểu", "arrange, slate / timetable", "Guided docent tours are scheduled daily at 10:00 A.M. and 2:00 P.M."),
            ("significant", "adj", "quan trọng, có ý nghĩa lớn", "meaningful, notable, momentous", "The archaeological discovery represents a significant historical find."),
            ("specialize", "v", "chuyên về", "focus on, major in", "The museum specializes in contemporary East Asian abstract sculptures."),
            ("spectrum", "n", "dải, quang phổ, phạm vi rộng", "range, span, continuum", "The exhibition covers a broad spectrum of twentieth-century art movements.")
        ]
    },
    {
        "category": "Entertainment",
        "lesson_id": 45,
        "lesson_name": "Media (Truyền thông & Báo chí)",
        "words": [
            ("assignment", "n", "nhiệm vụ, bài phân công", "task, job, project, mission", "The photojournalist accepted a dangerous overseas field assignment."),
            ("choose", "v", "chọn lựa", "select, pick, opt for", "Subscribers can choose between digital and printed delivery formats."),
            ("constantly", "adv", "liên tục, không dứt", "incessantly, perpetually, continuously", "Digital newsfeeds update constantly to provide breaking bulletins."),
            ("constitute", "v", "cấu thành, tạo nên", "comprise, form, represent", "Investigative reporting constitutes the foundation of credible journalism."),
            ("decision", "n", "quyết định", "judgment, verdict, resolution", "The chief editor's decision to retract the article was widely praised."),
            ("disseminate", "v", "lan tỏa, truyền bá thông tin", "distribute, circulate, publicize", "Social platforms disseminate breaking press releases instantaneously."),
            ("impact", "n/v", "tác động, ảnh hưởng lớn", "effect, influence / hit, strike", "Television debates had a notable impact on voter perception."),
            ("investigate", "v", "điều tra, nghiên cứu kỹ", "inquire into, probe, examine", "Reporters spent six months investigating corporate tax sheltering."),
            ("link", "n/v", "mối liên kết / gắn kết", "connection, relation / associate", "Studies demonstrated a direct link between advertising and digital clicks."),
            ("subscribe", "v", "đăng ký dài hạn (báo/kênh)", "enroll, sign up, pledge", "Thousands of users subscribe to the financial newspaper's online edition."),
            ("thorough", "adj", "kỹ lưỡng, thấu đáo", "exhaustive, detailed, comprehensive", "The journalist conducted a thorough investigation into the accounting leak."),
            ("uninformative", "adj", "thiếu thông tin, nghèo nàn", "unenlightening, vague, unhelpful", "Critics dismissed the official press release as sterile and uninformative.")
        ]
    },

    # =========================================================================
    # UNIT 10: HEALTH (Bài 46 - 50)
    # =========================================================================
    {
        "category": "Health",
        "lesson_id": 46,
        "lesson_name": "Doctor's Office (Phòng khám bác sĩ)",
        "words": [
            ("annual", "adj", "hàng năm, thường niên", "yearly, anniversary", "Employees are entitled to a paid annual medical physical checkup."),
            ("appointment", "n", "cuộc hẹn khám", "booking, consultation, session", "Call the clinic early to reschedule your medical appointment."),
            ("assess", "v", "đánh giá tình trạng", "evaluate, judge, appraise", "The physician assessed the patient's symptoms before prescribing therapy."),
            ("diagnose", "v", "chẩn đoán bệnh", "identify, detect, determine", "Early screening allows doctors to diagnose health conditions promptly."),
            ("effective", "adj", "hiệu quả", "efficacious, potent, productive", "The prescribed treatment regimen proved highly effective."),
            ("instrument", "n", "dụng cụ, thiết bị y tế", "device, tool, apparatus", "Surgical instruments must undergo rigorous autoclave sterilization."),
            ("manage", "v", "quản lý, kiểm soát (bệnh/triệu chứng)", "control, handle, oversee", "Regular cardio exercise helps patients manage stress and blood pressure."),
            ("prevent", "v", "ngăn ngừa, phòng chống", "avert, thwart, stop", "Proper workplace ergonomics helps prevent repetitive strain injuries."),
            ("recommendation", "n", "khuyến nghị, lời khuyên", "advice, counsel, suggestion", "The physician made several dietary recommendations to reduce cholesterol."),
            ("record", "n/v", "hồ sơ bệnh án / ghi lại", "medical history, file / document", "Patients can access electronic health records via a secure medical portal."),
            ("refer", "v", "giới thiệu chuyển viện/chuyên khoa", "direct, send, recommend", "The family practitioner referred the patient to a cardiologist."),
            ("serious", "adj", "nghiêm trọng, trầm trọng", "severe, grave, critical", "Chest discomfort should always be treated as a serious medical condition.")
        ]
    },
    {
        "category": "Health",
        "lesson_id": 47,
        "lesson_name": "Dentist's Office (Nha khoa)",
        "words": [
            ("astonish", "v", "làm ngạc nhiên, kinh ngạc", "amaze, surprise, astound", "The painless dental laser treatment astonished the nervous patient."),
            ("calm", "adj/v", "bình tĩnh / làm dịu", "serene, tranquil / soothe, pacify", "The dentist spoke gently to keep young children calm during cleaning."),
            ("catch up", "v phrase", "bắt kịp, theo kịp", "reach, overtake", "Regular bi-annual checkups help you catch up on neglected oral hygiene."),
            ("distract", "v", "làm xao nhãng, phân tâm", "divert, sidetrack", "Overhead monitors screen peaceful nature videos to distract dental patients."),
            ("encircle", "v", "vây quanh, bao quanh", "surround, enclose, ring", "A soft rubber protective dam encircled the molar during root treatment."),
            ("errant", "adj", "lệch hướng, sai lệch", "straying, aberrant, deviant", "The dental hygienist used suction to trap errant water droplets."),
            ("floss", "v/n", "dùng chỉ nha khoa / chỉ nha khoa", "clean with thread / dental string", "Dentists strongly advise patients to floss daily between meals."),
            ("habit", "n", "thói quen", "custom, routine, practice", "Grinding teeth under stress is a harmful nighttime habit."),
            ("maintain", "v", "duy trì, giữ gìn", "preserve, upkeep, sustain", "Brushing twice daily helps maintain healthy gums and enamel."),
            ("dental", "adj", "thuộc về răng miệng, nha khoa", "oral, orthodontic", "The corporate benefits package includes comprehensive dental coverage."),
            ("procedure", "n", "thủ thuật y tế, quy trình", "operation, medical process, method", "Wisdom tooth extraction is a routine outpatient procedure."),
            ("shine", "v/n", "sáng bóng / độ bóng", "gleam, sparkle, polish", "Ultrasonic polishing restored a bright shine to her teeth.")
        ]
    },
    {
        "category": "Health",
        "lesson_id": 48,
        "lesson_name": "Health Insurance (Bảo hiểm y tế)",
        "words": [
            ("allow", "v", "cho phép, chấp thuận", "permit, grant, authorize", "The health insurance policy allows for two preventive checkups per year."),
            ("alternative", "n/adj", "sự lựa chọn thay thế / thay thế", "option, substitute / alternate", "Generic prescription drugs offer an affordable alternative to brand names."),
            ("aspect", "n", "khía cạnh, phương diện", "facet, element, feature", "Copayments are one aspect of healthcare coverage to consider carefully."),
            ("concern", "n/v", "mối lo ngại / bận tâm", "worry, issue / bother, affect", "Rising monthly insurance premiums are a major concern for small businesses."),
            ("emphasize", "v", "nhấn mạnh", "stress, highlight, underline", "Human resources emphasized the deadline for open health enrollment."),
            ("incur", "v", "gánh chịu, phát sinh (chi phí/nợ)", "sustain, bring upon oneself, suffer", "Patients incur out-of-pocket costs when visiting out-of-network clinics."),
            ("personnel", "n", "nhân sự, đội ngũ nhân viên", "staff, employees, workforce", "Corporate wellness perks help retain talented engineering personnel."),
            ("policy", "n", "chính sách, hợp đồng bảo hiểm", "contract, plan, guidelines", "Carefully read the insurance policy exclusions before traveling abroad."),
            ("portion", "n", "phần, tỷ lệ chi trả", "share, part, segment", "The insurance provider covers a substantial portion of prescription expenses."),
            ("regardless", "adv", "bất chấp, không màng đến", "in spite of, despite, heedless", "Emergency trauma rooms treat all urgent cases regardless of insurance status."),
            ("salary", "n", "tiền lương tháng/năm", "earnings, remuneration, pay", "Medical insurance deductions are automatically withheld from your salary."),
            ("suit", "v/n", "phù hợp / bộ âu phục", "fit, match, accommodate / costume", "Select an insurance plan that best suits your family's healthcare needs.")
        ]
    },
    {
        "category": "Health",
        "lesson_id": 49,
        "lesson_name": "Hospitals (Bệnh viện & Cấp cứu)",
        "words": [
            ("admit", "v", "nhập viện, tiếp nhận", "check in, accept, allow entry", "The ER physician decided to admit the patient for overnight observation."),
            ("authorize", "v", "cho phép, ủy quyền", "approve, sanction, permit", "Only licensed medical directors can authorize surgical discharges."),
            ("designate", "v", "chỉ định, định rõ", "appoint, assign, specify", "Specific hospital wings are designated exclusively for pediatric intensive care."),
            ("escort", "v/n", "hộ tống, dẫn đường / người hộ tống", "accompany, guide, usher / guard", "Volunteers escort family members to the surgical waiting lounge."),
            ("identify", "v", "nhận diện, xác định", "recognize, pinpoint, diagnose", "Patients wear barcode wristbands to identify their medications accurately."),
            ("mission", "n", "sứ mệnh", "purpose, objective, goal", "The hospital's charitable mission is providing care to underserved communities."),
            ("permit", "v/n", "cho phép / giấy phép", "allow, grant / license, pass", "Hospital rules do not permit visiting hours after 8:00 P.M."),
            ("pertinent", "adj", "thích hợp, có liên quan trực tiếp", "relevant, applicable, germane", "The triage nurse documented all pertinent symptoms into the digital chart."),
            ("procedure", "n", "thủ thuật y tế, phẫu thuật", "operation, medical intervention", "The laparoscopic procedure required only three small incisions."),
            ("result", "n/v", "kết quả xét nghiệm / dẫn đến", "outcome, lab findings / ensue", "Blood test results were transmitted directly to the attending physician."),
            ("statement", "n", "bản sao kê, hóa đơn viện phí", "bill, invoice, declaration", "Patients receive a detailed itemized statement after hospital discharge."),
            ("usually", "adv", "thường, thông thường", "normally, generally, customarily", "Post-operative recovery usually takes between four and six weeks.")
        ]
    },
    {
        "category": "Health",
        "lesson_id": 50,
        "lesson_name": "Pharmacy (Hiệu thuốc & Dược phẩm)",
        "words": [
            ("consult", "v", "tham vấn, hỏi ý kiến", "seek advice, confer with", "Always consult a licensed pharmacist before combining herbal remedies."),
            ("control", "v/n", "kiểm soát / sự kiểm soát", "manage, regulate / restraint", "Insulin injections help patients control blood glucose levels."),
            ("convenient", "adj", "thuận tiện, tiện lợi", "accessible, handy, practical", "Drive-through pharmacies offer convenient prescription pickup."),
            ("detect", "v", "phát hiện, nhận ra", "discover, identify, spot", "Diagnostic test strips can detect bacterial infections in minutes."),
            ("factor", "n", "yếu tố, nhân tố", "element, component, consideration", "Patient age and body weight are key factors in determining medication dosage."),
            ("interaction", "n", "tương tác thuốc", "interplay, reciprocal effect", "Check medicine warning labels for potential adverse drug interactions."),
            ("limit", "v/n", "giới hạn / hạn mức", "restrict, cap / boundary, ceiling", "Federal law limits the purchase quantity of certain decongestant pills."),
            ("monitor", "v/n", "theo dõi, giám sát / màn hình theo dõi", "track, supervise, observe / screen", "Pharmacists monitor patient refill histories to ensure safe adherence."),
            ("potential", "adj/n", "tiềm tàng, tiềm năng / khả năng", "possible, latent / capability", "Patients were cautioned about potential mild side effects like drowsiness."),
            ("sample", "n/v", "mẫu thử / dùng thử", "specimen, trial piece / test", "The pharmaceutical sales rep provided free physician samples of the inhaler."),
            ("sense", "n/v", "cảm nhận, ý thức / cảm thấy", "feeling, awareness / perceive", "Elderly patients who sense dizziness should discontinue the tablet immediately."),
            ("volunteer", "v/n", "tình nguyện / tình nguyện viên", "offer freely / pro bono worker", "Over 2,000 healthy volunteers participated in the phase-three vaccine trial.")
        ]
    }
]

def build_dataset():
    all_words = []
    word_id = 1

    for lesson in LESSONS_DATA:
        cat = lesson["category"]
        lid = lesson["lesson_id"]
        lname = lesson["lesson_name"]
        words = lesson["words"]
        for item in words:
            w, pos, mean, syn, ex = item
            all_words.append({
                "id": word_id,
                "word": w,
                "pos": pos,
                "meaning": mean,
                "lesson_id": lid,
                "lesson_name": lname,
                "category": cat,
                "synonyms": syn,
                "example": ex,
                "encounters": 0,  # Số lần xuất hiện trong đề/bài kiểm tra
                "level": 1,  # Mặc định tất cả bắt đầu ở Level 1
                "status": "untested"
            })
            word_id += 1

    return all_words


def generate_markdown(all_words):
    lines = []
    lines.append("# 📚 KHO 600 TỪ VỰNG CỐT LÕI TOEIC (600 ESSENTIAL WORDS FOR THE TOEIC)")
    lines.append("")
    lines.append("> **Chuẩn Barron's & ETS/IIG:** 50 bài x 12 từ = **600 từ vựng cốt lõi** phân bổ đều trong 10 chủ điểm công sở.")
    lines.append("> **Hệ thống cấp độ Mastery:** Mặc định toàn bộ 600 từ được khởi tạo ở **Level 1**.")
    lines.append("> **Số lần gặp (Encounters):** Đếm số lần từ vựng xuất hiện trong các bài test/drill thực tế.")
    lines.append("> Mỗi khi từ vựng được đưa vào bài tập và bạn trả lời đúng $\\rightarrow$ Thăng hạng lên **Level 2** và **Level 3**.")
    lines.append("")

    # Nhóm theo category
    categories = {}
    for w in all_words:
        cat = w["category"]
        if cat not in categories:
            categories[cat] = {}
        lid = w["lesson_id"]
        if lid not in categories[cat]:
            categories[cat][lid] = {
                "lesson_name": w["lesson_name"],
                "words": []
            }
        categories[cat][lid]["words"].append(w)

    for cat_name, lessons in categories.items():
        lines.append(f"## 🏢 CHỦ ĐIỂM: {cat_name.upper()}")
        lines.append("")
        for lid, ldata in sorted(lessons.items()):
            lines.append(f"### Lesson {lid:02d}: {ldata['lesson_name']}")
            lines.append("")
            lines.append("| ID | Từ vựng | Loại | Nghĩa tiếng Việt | Từ đồng nghĩa & Liên kết cây | Ngữ cảnh / Câu ví dụ thực tế | Số lần gặp | Mức độ |")
            lines.append("| :---: | :--- | :---: | :--- | :--- | :--- | :---: | :---: |")
            for w in ldata["words"]:
                lines.append(f"| {w['id']} | **{w['word']}** | {w['pos']} | {w['meaning']} | *{w['synonyms']}* | {w['example']} | {w.get('encounters', 0)} lần | Level {w['level']} |")
            lines.append("")

    return "\n".join(lines)


def main():
    words = build_dataset()
    print(f"Tổng số từ vựng tạo được: {len(words)} từ.")

    # 1. Ghi file JSON
    json_path = VOCAB_DIR / "toeic_600_words.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"[✓] Đã xuất thành công JSON: {json_path}")

    # 2. Ghi file Markdown
    md_content = generate_markdown(words)
    md_path = VOCAB_DIR / "toeic_600_words.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[✓] Đã xuất thành công Markdown catalog: {md_path}")


if __name__ == "__main__":
    main()
