# File nay duoc GitHub Actions goi moi lan chay
# Khong can schedule loop, chay 1 lan roi thoat

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from content_themes import THEMES
from claude_content import create_facebook_post, create_tiktok_script, create_youtube_script
from gemini_image import generate_product_image
from facebook_post import post_to_facebook
from telegram_notify import send_script, send_alert

def main():
    # Xac dinh buoi sang hay toi theo gio UTC
    hour_utc = datetime.utcnow().hour
    session_name = "BUOI SANG 7:00" if hour_utc < 6 else "BUOI TOI 19:00"

    print(f"🚀 BAT DAU - {session_name}")
    print(f"⏰ {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    send_alert(f"Bot bat dau chay - {session_name}")

    day = datetime.now().weekday()
    theme = THEMES[day]

    # 1. Tao content Facebook
    print("\n📝 Tao bai Facebook...")
    fb_content = create_facebook_post(theme["facebook"])

    # 2. Tao anh
    print("🎨 Tao anh Gemini...")
    image_path = generate_product_image(theme["facebook"])

    # 3. Dang Facebook
    print("📤 Dang len Facebook...")
    success = post_to_facebook(fb_content, image_path)

    # 4. Xoa anh tam
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    # 5. Script TikTok
    print("🎵 Tao script TikTok...")
    tiktok_script = create_tiktok_script(theme["tiktok"])
    send_script("TikTok", tiktok_script, session_name)

    # 6. Script YouTube
    print("▶️  Tao script YouTube...")
    youtube_script = create_youtube_script(theme["youtube"])
    send_script("YouTube", youtube_script, session_name)

    status = "✅ HOAN THANH" if success else "⚠️ XONG - Co loi Facebook"
    print(f"\n{status} - {session_name}")
    send_alert(f"{status} - {session_name}")

if __name__ == "__main__":
    main()
