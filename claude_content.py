import anthropic
import os
from datetime import datetime

client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

BRAND_INFO = """
Thuong hieu: Tu Bep Phuong Nam
San pham chinh: Tu bep canh kinh cao cap (80% nhom, 20% inox)
Thi truong: TP.HCM va cac tinh lan can
Co showroom truc tiep de khach hang trai nghiem
Email: sieuthibepphuongnam@gmail.com
Diem manh: Bao hanh dai han, thi cong chuyen nghiep, gia canh tranh
"""

def create_facebook_post(theme: str) -> str:
    try:
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=800,
            messages=[{
                "role": "user",
                "content": f"""Viet 1 bai dang Facebook cho thuong hieu tu bep sau:

{BRAND_INFO}

Chu de hom nay: {theme}

Yeu cau:
- Dai 150-200 chu
- Tone: gan gui, chuyen nghiep, than thien
- Co emoji phu hop (khong qua 5 emoji)
- Cuoi bai co CTA ro rang (keu goi nhan tin / goi dien / den showroom)
- Co 5-7 hashtag lien quan den tu bep, noi that, TP.HCM
- Viet bang tieng Viet co dau day du"""
            }]
        )
        return message.content[0].text
    except Exception as e:
        return f"Loi tao content Facebook: {e}"

def create_tiktok_script(theme: str) -> str:
    try:
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=700,
            messages=[{
                "role": "user",
                "content": f"""Viet script video TikTok 60 giay cho thuong hieu tu bep:

{BRAND_INFO}

Chu de: {theme}

Format bat buoc:
[0-5s] HOOK - Cau mo dau gay chu y, bat nguoi xem dung lai
[5-15s] Van de - Neu van de khach hang thuong gap
[15-45s] Giai phap - Noi dung chinh, gia tri cung cap
[45-55s] Showcase - Gioi thieu san pham/cong trinh
[55-60s] CTA - Keu goi hanh dong + thong tin lien he

---
CAPTION TIKTOK: (viet rieng phan nay)
- 2-3 cau hap dan
- 5 hashtag

Viet bang tieng Viet co dau"""
            }]
        )
        return message.content[0].text
    except Exception as e:
        return f"Loi tao script TikTok: {e}"

def create_youtube_script(theme: str) -> str:
    try:
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1200,
            messages=[{
                "role": "user",
                "content": f"""Viet script video YouTube 3-5 phut cho thuong hieu tu bep:

{BRAND_INFO}

Chu de: {theme}

Format bat buoc:
TIEU DE VIDEO: (SEO-friendly, co tu khoa)
MO TA VIDEO: (150 chu + hashtag cho YouTube SEO)

SCRIPT DAY DU:
[Intro - 30 giay]: Chao hoi + gioi thieu noi dung
[Phan 1 - 1 phut]: Noi dung chinh thu nhat
[Phan 2 - 1-2 phut]: Noi dung chinh thu hai
[Phan 3 - 1 phut]: Vi du thuc te / cong trinh
[Outro - 30 giay]: Tom tat + keu goi subscribe + lien he

Viet bang tieng Viet co dau"""
            }]
        )
        return message.content[0].text
    except Exception as e:
        return f"Loi tao script YouTube: {e}"
