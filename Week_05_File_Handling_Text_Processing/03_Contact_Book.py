"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
print("1. Add a contact")
print("2. Search for a contact ")
print("3. Show all contacts")
option = int(input("Enter the number of the option you want to chose: "))
if option == 1:
    with open("contact_book.txt","a") as file:
        contact_name = input("Enter the contacts name: ")
        contact_number = input("Enter contacts number: ")
        file.write(contact_name + "," + contact_number)
elif option == 2:
    with open("contact_book.txt","r") as file:
        names = input("Enter name: ")
        for i in file:
            name, number = i.split(",")
            number = number.strip()
            name = name.strip()
            if name == names:
                print(name, number)
elif option == 3:
    with open("contact_book.txt","r") as file:
        for i in file:
            print(i)
    
        

    pass


if __name__ == "__main__":
    main()
