import requests
import os

def send_script(platform: str, content: str, session_time: str):
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    icon = "🎵" if platform == "TikTok" else "▶️"
    message = f"""{icon} *SCRIPT {platform.upper()}* - {session_time}
━━━━━━━━━━━━━━━━━━━━

{content}

━━━━━━━━━━━━━━━━━━━━
🏠 _Tu Bep Phuong Nam Content Bot_"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        })
        if resp.ok:
            print(f"✅ Telegram: Gui script {platform} thanh cong!")
        else:
            print(f"❌ Telegram loi: {resp.text}")
    except Exception as e:
        print(f"❌ Telegram exception: {e}")

def send_alert(message: str):
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": f"🤖 {message}"
        })
    except:
        pass
