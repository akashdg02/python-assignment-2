import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

def query_huggingface(prompt_text):
    api_key = os.getenv("HF_TOKEN")
    if not api_key:
        return "Error: HF_TOKEN not found in your .env file."

    # 1. Initialize with the modern 2026 Client
    # We use Llama-3.1-8B-Instruct as it is the most stable free chat model
    client = InferenceClient(api_key=api_key)

    try:
        # 2. Use the OpenAI-compatible completions interface
        # No 'provider' argument inside this call; the router handles it
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[{"role": "user", "content": prompt_text}],
            max_tokens=500,
            temperature=0.7
        )
        
        return completion.choices[0].message.content

    except Exception as e:
        # 3. Automatic Fallback to legacy text-generation if Chat is busy
        try:
            print(f"Chat error ({str(e)[:50]}...), trying legacy text-gen...")
            output = client.text_generation(
                prompt=f"Q: {prompt_text}\nA:",
                model="mistralai/Mistral-7B-Instruct-v0.3",
                max_new_tokens=100
            )
            return output
        except Exception as e2:
            return f"Final HF Error: {str(e2)}"

if __name__ == "__main__":
    print("--- Hugging Face 2026 Final Stability Test ---")
    user_prompt = input("Enter prompt: ")
    
    result = query_huggingface(user_prompt)
    print("\nResult:\n" + "="*40)
    print(result)