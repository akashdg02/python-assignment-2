def q3_string_manipulator():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    
    # Calculate string metrics [cite: 63, 64, 65]
    print(f"Original: {sentence}")
    print(f"Characters (with spaces): {len(sentence)}")
    print(f"Characters (without spaces): {len(sentence.replace(' ', ''))}")
    print(f"Words: {len(words)}")
    
    # Case transformations [cite: 66, 67, 68]
    print(f"UPPERCASE: {sentence.upper()}")
    print(f"lowercase: {sentence.lower()}")
    print(f"Title Case: {sentence.title()}")
    
    # Extract first and last words if they exist [cite: 69, 70]
    if words:
        print(f"First word: {words[0]}")
        print(f"Last word: {words[-1]}")
    
    # Reverse string [cite: 71]
    print(f"Reversed: {sentence[::-1]}")