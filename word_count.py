input_string = input("enter a string: ")

# lower-which considers insensitive-cases like spaces,capital letters,small letters
input_string = input_string.lower()

# split()-It Converts string into words
words = input_string.split()

# Creating a empty dictionary to store word counts
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    
print("\n word occurrences: ")
for word, count in word_count.items():
    print(f"{word}: {count}")

