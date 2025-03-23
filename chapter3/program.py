from collatz import collatz

user_number = input("Enter a number: ")

while user_number != 1:
    try:
        user_number = int(user_number)
        user_number = collatz(user_number)
        print(user_number)
    except:
        print("Please enter a digit, not letters")
        user_number = input("Enter a number: ")
        
