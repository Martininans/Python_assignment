user_input = input("Enter character: ")
vowels = 0
consonants = 0
for char in user_input:
    if char.isalpha():
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print("Number of vowels:",vowels)
print("Number of consonants:", consonants)
