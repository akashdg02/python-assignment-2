import os
import sys
from dotenv import load_dotenv

# --- CORRECTED IMPORTS ---
from groq_example import query_groq_llama
from ollama_example import fetch_ollama_completion
from huggingface_example import query_huggingface  # Changed from query_huggingface_model
from gemini_example import get_gemini_output
from cohere_example import query_cohere_api
# -------------------------

load_dotenv()

def run_multi_tool():
    """
    Main controller to select AI providers and route prompts.
    """
    providers = {
        "1": ("Groq", query_groq_llama),
        "2": ("Ollama", fetch_ollama_completion),
        "3": ("Hugging Face", query_huggingface), # Update the reference here too
        "4": ("Google Gemini", get_gemini_output),
        "5": ("Cohere", query_cohere_api)
    }

    print("\n--- 🚀 Multi-API Query Tool ---")
    for key, (name, _) in providers.items():
        print(f"{key}. {name}")
    
    choice = input("\nSelect a provider (1-5) or 'q' to quit: ")
    
    if choice.lower() == 'q':
        sys.exit()

    if choice in providers:
        name, func = providers[choice]
        prompt = input(f"[{name}] Enter your prompt: ")
        
        print(f"\nContacting {name}...")
        try:
            response = func(prompt)
            print("-" * 30)
            print(f"RESPONSE:\n{response}")
            print("-" * 30)
        except Exception as e:
            print(f"Critical error routing to {name}: {e}")
    else:
        print("Invalid selection. Please try again.")

if __name__ == "__main__":
    while True:
        run_multi_tool()
        if input("\nRun another query? (y/n): ").lower() != 'y':
            break