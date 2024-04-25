def longest_word_and_length(words):
    if not words:
        return None, 0
    
    longest_word = ''
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    
    return longest_word, max_length

words = ['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']
longest, length = longest_word_and_length(words)
print(f"Longest word: {longest}, Length: {length}")
