"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   shopping_list = []
   finished = False
   while finished == False:
        item = input("Enter what item you want to add to the list, enter 'done' when you are finished : ")
        if item.lower() != "done":
            shopping_list.append(item)
        else:
            finished = True

    print("This is your shopping list:")
    print(shopping_list)

    change = input("Do you want to change anything? yes or no :")
    if change.lower() == "yes":
        num = int(input("What item number do you want to change? "))
        item_change = input("What do you want to change it to? ")
        shopping_list[num - 1] = item_change
        print("This is your new list:")
        print(shopping_list)
    else:
        print("Ok")


    pass


if __name__ == "__main__":
    main()
