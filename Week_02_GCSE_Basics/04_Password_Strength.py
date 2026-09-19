"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
password = input("enter password :")
lengths = len(password)
has_num = False
has_capital_lower = False
special = False
length = False
has_capital = False
has_lower = False
for character in password:
        if character.isdigit():
            has_num = True
        elif character.isupper():
            has_capital = True
        elif character.islower():
            has_lower = True
        elif not character.isalnum():
            special = True
if lengths >= 8:
    length = True
if has_capital == True and has_lower == True:
    has_capital_lower = True

total = sum([has_num, has_capital_lower, special, length])
if total == 0:
    print("You have weak password")
elif total == 1:
    print("You have a weak password!")
elif total == 2:
    print("You have a medium password!")
elif total == 3:
    print("You have a medium password!")
elif total == 4:
    print("You have a strong password!")


    pass


if __name__ == "__main__":
    main()
