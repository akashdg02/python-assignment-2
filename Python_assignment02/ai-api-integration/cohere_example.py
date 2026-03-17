import os
import cohere
from dotenv import load_dotenv

load_dotenv()

# Use the V2 Client (Standard for 2026)
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

def query_cohere_api(prompt: str) -> str:
    """
    Fixed for 2026 model deprecations.
    Uses 'command-a-03-2025' for high-performance agentic tasks.
    """
    if not COHERE_API_KEY:
        return "Error: COHERE_API_KEY is missing from your .env file."

    # Initializing V2 Client
    co = cohere.ClientV2(api_key=COHERE_API_KEY)

    try:
        # 404 FIX: Use the latest active model ID
        response = co.chat(
            model="command-a-03-2025", 
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        
        # Access the text safely in the V2 response object
        return response.message.content[0].text.strip()

    except cohere.errors.BadRequestError as e:
        return f"Model Error (404/400): {e.message}. Try using 'command-r-08-2024'."
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

if __name__ == "__main__":
    print("--- Testing Cohere 2026 ---")
    answer = query_cohere_api("Explain why Python is considered slow in one sentence.")
    print(f"Output: {answer}")