def count_vowel_and_consonants(text):
    text = text.lower().replace(" ", "")
    
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    # Loop through each character in the text
    for char in text:
        if char.isalpha(): # Check if it's a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
                
input_text = input("Enter text: ")
vowels, consonants = count_vowel_and_consonants(input_text)
print(f"vowels: {vowels}")
print(f"consonants: {consonants}")
        
