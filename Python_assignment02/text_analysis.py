def q19_text_analysis():
    """
    Q19: Comprehensive Text Analysis.
    Performs word counts, character checks, and frequency mapping.
    """
    text = input("Enter a sentence or paragraph: ")
    
    # 1. Basic Counts
    words = text.split()
    num_words = len(words)
    
    # 2. Vowel and Consonant Analysis
    vowels_set = "aeiouAEIOU"
    num_vowels = sum(1 for char in text if char in vowels_set)
    num_consonants = sum(1 for char in text if char.isalpha() and char not in vowels_set)
    
    # 3. Transformations
    reversed_text = text[::-1]
    # Check palindrome (ignore spaces and case)
    clean_text = "".join(text.split()).lower()
    is_palindrome = clean_text == clean_text[::-1]
    
    # 4. Content Manipulation
    no_vowels = "".join([c for c in text if c not in vowels_set])
    
    # 5. Frequency and Length
    # Use a dictionary to count unique word occurrences [cite: 200]
    word_freq = {}
    for word in words:
        clean_word = word.lower().strip(".,!?;:")
        word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
        
    longest = max(words, key=len) if words else "None"

    # Display Results [cite: 200, 201]
    print("\n" + "="*25)
    print("   TEXT ANALYSIS RESULT")
    print("="*25)
    print(f"Total Words      : {num_words}")
    print(f"Vowels Count     : {num_vowels}")
    print(f"Consonants Count : {num_consonants}")
    print(f"Reversed Text    : {reversed_text}")
    print(f"Is Palindrome    : {'Yes' if is_palindrome else 'No'}")
    print(f"Text No Vowels   : {no_vowels}")
    print(f"Longest Word     : {longest} ({len(longest)} letters)")
    print(f"Word Frequency   : {word_freq}")