import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from your .env file
load_dotenv()

def query_groq_llama(user_input):
    # Get key from environment
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Error: GROQ_API_KEY is missing from your .env file."

    # Initialize the Groq client
    client = Groq(api_key=api_key)

    try:
        # UPDATED: Use llama-3.3-70b-versatile (Active 2026 model)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        # Safe extraction of the response text
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Groq API Error: {str(e)}"

if __name__ == "__main__":
    print("--- Groq Llama 3.3 Test ---")
    prompt = input("Enter your prompt for Groq: ")
    
    result = query_groq_llama(prompt)
    print("\nResult:\n" + "="*40)
    print(result)