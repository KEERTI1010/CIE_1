Name = input("Enter your name: ")
print(f"Welcome, {Name}! Please log in to continue.")

login = input("Enter your username: ")
password = input("Enter your password: ")

if login == "student" and password == "password123":
    print("Login successful! You can now access your student portal.")
else:
    print("Login failed! Please check your username and password and try again.")

