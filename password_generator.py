import random,string

def password_generator(length):
    letters = string.ascii_letters
    digits = string.digits
    Symbols = string.punctuation
    
    all_chars = letters + digits + Symbols
    
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

def main():
    try:
        length = int(input("enter length of password: "))
        if length < 4:
            print("The password is too weak")
        else:
            print(f"The password is {password_generator(length)}")
            
    except ValueError:
        print("There is something error in generating Password")
        
if __name__ == "__main__":
    main()
