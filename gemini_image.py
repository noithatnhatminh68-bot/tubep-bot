import google.generativeai as genai
import os
import requests
from pathlib import Path

def generate_product_image(theme: str) -> str:
    """Tao anh tu bep bang Gemini Imagen"""
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.ImageGenerationModel("imagen-3.0-generate-002")

        prompt = f"""
        Professional interior photography of a modern Vietnamese kitchen cabinet,
        premium aluminum and stainless steel with glass doors,
        elegant high-end showroom display, bright natural lighting,
        clean minimalist background, photorealistic quality,
        theme concept: {theme}
        """

        result = model.generate_images(
            prompt=prompt,
            number_of_images=1,
            aspect_ratio="4:5"
        )

        image_path = f"temp_image.jpg"
        result.images[0].save(image_path)
        print(f"✅ Gemini: Tao anh thanh cong!")
        return image_path

    except Exception as e:
        print(f"⚠️ Gemini anh loi: {e} - Se dang khong co anh")
        return None
