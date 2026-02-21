def q19_text_analysis():
    text = input("Enter text: ")
    words = text.split()
    # Word freq dictionary [cite: 200]
    freq = {w: words.count(w) for w in set(words)}
    print(f"Words: {len(words)} | Longest Word: {max(words, key=len)}")
    print(f"Word Frequency: {freq}")