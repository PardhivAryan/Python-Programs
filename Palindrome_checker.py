def palindrome(text):
    text = text.lower().replace(" ","")
    return text == text[::-1]
input_text=input("enter any text: ")
if palindrome(input_text):
    print(f"'{input_text}' is a palindrome")
else:
    print(f"'{input_text}' is not palindrome")