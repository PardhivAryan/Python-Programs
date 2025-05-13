import random

def random_number_generator():
    secret_number = random.randint(1,100)
    attempts = 0
    while True:
        try:
            guess = int(input("enter number: "))
            attempts += 1
            
            if guess < secret_number:
                print("the number is greater")
            elif guess > secret_number:
                print("the number is lower")
            else:
                print(f"congratulations! yes it is absolute correct you guessed in {attempts} attempts")
                break
        except ValueError:
            print("please enter a valid number")
            
if __name__ == "__main__":
    random_number_generator()
    