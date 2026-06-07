import requests
import os

def post_to_facebook(message: str, image_path: str = None) -> bool:
    FB_PAGE_ID = os.getenv("FB_PAGE_ID")
    FB_TOKEN = os.getenv("FB_ACCESS_TOKEN")

    try:
        if image_path and os.path.exists(image_path):
            url = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/photos"
            with open(image_path, 'rb') as img:
                response = requests.post(url, data={
                    "message": message,
                    "access_token": FB_TOKEN
                }, files={"source": img})
        else:
            url = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/feed"
            response = requests.post(url, data={
                "message": message,
                "access_token": FB_TOKEN
            })

        result = response.json()
        if "id" in result:
            print(f"✅ Facebook: Dang thanh cong! Post ID: {result['id']}")
            return True
        else:
            print(f"❌ Facebook loi: {result}")
            return False

    except Exception as e:
        print(f"❌ Facebook exception: {e}")
        return False
