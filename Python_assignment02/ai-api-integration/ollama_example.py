import ollama

def fetch_ollama_completion(prompt_text):
    try:
        # 1. Get the list of installed models using the updated 2026 structure
        response = ollama.list()
        
        # In the 2026 SDK, 'models' is a list of objects. 
        # We access the model name using the .model attribute (or .name)
        model_names = [m.model for m in response.models]
        
        if not model_names:
            return "Error: No models found. Run 'ollama pull llama3.2' in your terminal."

        # 2. Strategy: Use what's available, preferring Llama 3 series
        selected_model = model_names[0] # Default to the first one found
        for m in ["llama3.3", "llama3.2", "llama3.1", "llama3"]:
            # Check if any part of the model name matches our target
            matching = [name for name in model_names if m in name]
            if matching:
                selected_model = matching[0]
                break
        
        print(f"Using local model: {selected_model}...")

        # 3. Use the simplified 2026 chat interface
        response = ollama.chat(
            model=selected_model,
            messages=[{'role': 'user', 'content': prompt_text}],
        )
        
        # Access content via attribute for maximum 2026 compatibility
        return response.message.content

    except Exception as e:
        return f"Local Ollama Error: {str(e)}"

if __name__ == "__main__":
    print("--- Ollama 2026 Corrected Client ---")
    user_query = input("Ask your local model: ")
    
    print("Processing...")
    result = fetch_ollama_completion(user_query)
    
    print("\n[Ollama Response]:")
    print("-" * 30)
    print(result)