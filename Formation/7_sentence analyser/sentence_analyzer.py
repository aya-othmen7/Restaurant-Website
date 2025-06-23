def analyze_sentence(sentence):
    # Initialize counters
    char_count = 0
    word_count = 0
    vowel_count = 0
    
    # Define vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Flag to track if we're in a word
    in_word = False
    
    # Read sentence character by character
    for char in sentence:
        # Increment character counter
        char_count += 1
        
        # Count vowels
        if char in vowels:
            vowel_count += 1
            
        # Count words
        if char == ' ':
            in_word = False
        elif char != '.' and not in_word:
            word_count += 1
            in_word = True
            
    return char_count, word_count, vowel_count

# Example usage
sentence = input("Enter a sentence ending with a period: ")
chars, words, vowels = analyze_sentence(sentence)
print(f"Length of sentence: {chars} characters")
print(f"Number of words: {words}")
print(f"Number of vowels: {vowels}")