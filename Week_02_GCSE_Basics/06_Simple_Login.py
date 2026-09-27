"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    username = "Shrey"
    password = "computerscience"
    attempts = 3
    while attempts != 0:
        username1 = input("Enter your username: ")
        password1 = input("Enter your password: ")

        if username1 != username or password1 != password:
                attempts = attempts - 1
                print(f"Access Denied, {attempts} atempts remaining!")
        else:
                print("Welcome")
                break

    if attempts == 0:
        print("You have no more attempts!")



    pass


if __name__ == "__main__":
    main()
