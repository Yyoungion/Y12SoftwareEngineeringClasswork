while True:
    username = input("Enter your username: ")

    if '<script>' in username:
        print("Username cannot contain <script>. Please try again")

    elif username.isalnum() == False:
        print("Username cannot contain special characters. Please try again.")
 
    elif 3 > len(username) or 15 < len(username):
        print("Username has to be between 3 and 15 characters. Please try again")

    else:
        print("Username is valid")
        break