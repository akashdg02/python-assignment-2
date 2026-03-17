import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_output(prompt_text):
    # The 2026 SDK automatically uses the latest stable API version
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    try:
        # Use 'gemini-2.5-flash' (Standard) or 'gemini-3.1-flash-lite-preview' (Fastest)
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt_text,
            config={
                "temperature": 0.7,
                "max_output_tokens": 500,
            }
        )
        return response.text if response.text else "No content returned."

    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            return "Quota Full: Please wait 60s or link a billing account."
        if "404" in error_msg:
            return "Model Error: The selected model is deprecated. Please use 'gemini-2.5-flash'."
        return f"Gemini Error: {error_msg}"

if __name__ == "__main__":
    u_prompt = input("Enter prompt: ")
    print("\nResult:\n" + "="*40)
    print(get_gemini_output(u_prompt))