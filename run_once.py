# GitHub Actions: Tao content + Gui Telegram
# Make.com se lo viec dang Facebook

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from content_themes import THEMES
from claude_content import create_facebook_post, create_tiktok_script, create_youtube_script
from telegram_notify import send_script, send_alert

def main():
    hour_utc = datetime.utcnow().hour
    session_name = "BUOI SANG 7:00" if hour_utc < 12 else "BUOI TOI 19:00"

    print(f"🚀 BAT DAU - {session_name}")
    send_alert(f"Bot bat dau - {session_name}")

    day = datetime.now().weekday()
    theme = THEMES[day]

    # 1. Tao content Facebook → gui Telegram de tham khao
    print("📝 Tao content Facebook...")
    fb_content = create_facebook_post(theme["facebook"])
    send_script("Facebook", fb_content, session_name)

    # 2. Script TikTok → gui Telegram
    print("🎵 Tao script TikTok...")
    tiktok_script = create_tiktok_script(theme["tiktok"])
    send_script("TikTok", tiktok_script, session_name)

    # 3. Script YouTube → gui Telegram
    print("▶️  Tao script YouTube...")
    youtube_script = create_youtube_script(theme["youtube"])
    send_script("YouTube", youtube_script, session_name)

    print(f"✅ HOAN THANH - {session_name}")
    send_alert(f"✅ Xong! Kiem tra Telegram nhan script.")

if __name__ == "__main__":
    main()
