while True:
    age_input = int(input("Please enter your age: "))
    print(f"Your age is: {age_input}")

    if 0 < age_input < 120:
        print("User age is valid")
        break
    
    else:
        print("User age has to be between 0 and 120. Please try again")
