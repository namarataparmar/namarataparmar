def get_integer_input():
    while True:
        user_input = input("Please enter an integer: ")
        try:
            number = int(user_input)
            print(f"You entered the integer: {number}")
            break
        except ValueError:
            print("Error: That's not a valid integer. Please try again.")

get_integer_input()
