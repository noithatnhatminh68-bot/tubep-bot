import schedule
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from content_themes import THEMES
from claude_content import create_facebook_post, create_tiktok_script, create_youtube_script
from gemini_image import generate_product_image
from facebook_post import post_to_facebook
from telegram_notify import send_script, send_alert

def run_content_session(session_name: str):
    print(f"\n{'='*50}")
    print(f"🚀 BAT DAU TAO CONTENT - {session_name}")
    print(f"⏰ {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"{'='*50}")

    send_alert(f"Bat dau tao content - {session_name}")

    day = datetime.now().weekday()
    theme = THEMES[day]

    # 1. Tao content Facebook
    print("\n📝 Dang tao bai Facebook...")
    fb_content = create_facebook_post(theme["facebook"])

    # 2. Tao anh Gemini
    print("🎨 Dang tao anh bang Gemini...")
    image_path = generate_product_image(theme["facebook"])

    # 3. Dang Facebook
    print("📤 Dang dang len Facebook...")
    success = post_to_facebook(fb_content, image_path)

    # 4. Xoa anh tam
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    # 5. Tao + gui script TikTok
    print("🎵 Dang tao script TikTok...")
    tiktok_script = create_tiktok_script(theme["tiktok"])
    send_script("TikTok", tiktok_script, session_name)

    # 6. Tao + gui script YouTube
    print("▶️  Dang tao script YouTube...")
    youtube_script = create_youtube_script(theme["youtube"])
    send_script("YouTube", youtube_script, session_name)

    status = "✅ THANH CONG" if success else "⚠️ CO LOI FACEBOOK"
    print(f"\n{status} - {session_name}")
    send_alert(f"{status} - {session_name}")

def morning_session():
    run_content_session("BUOI SANG 7:00")

def evening_session():
    run_content_session("BUOI TOI 19:00")

# Lich chay
schedule.every().day.at("07:00").do(morning_session)
schedule.every().day.at("19:00").do(evening_session)

print("🤖 Tu Bep Phuong Nam Content Bot")
print("📅 Lich: 7:00 sang va 19:00 toi moi ngay")
print("⏳ Dang cho lich chay...\n")

send_alert("Bot khoi dong thanh cong! Lich: 7:00 sang + 19:00 toi")

# Test chay ngay khi khoi dong (comment dong duoi neu khong muon test)
# run_content_session("KHOI DONG - TEST")

while True:
    schedule.run_pending()
    time.sleep(60)
