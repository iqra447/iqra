username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") ==  -1:
    print("Your username can't contain spaces")
elif not username.isalpha(): 
    print("Your username cannot contain any digits")
else:
    print(f"Welcome {username}")
