"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   rows, cols = 3, 3
array = [[0 for i in range(cols)] for i in range(rows)]
for i in array:
          print(i)
print("1. Append a new row, adding an item")
print("2. Read all current values")
print("3. Delete a chosen item")
answer = int(input("Enter choice from 1 to 3"))
if answer == 1:
          new_row = []
          adding = input("what do you want to add? ")
          new_row.append(adding)
          array.append(new_row)
          for i in array:
              print(i)
elif answer == 2:
    for i in array:
        print(i)

elif answer == 3:
    row = int(input("what row is the item you want to delete?"))
    column = int(input("what column is the item you want to delete?"))
    array[row][column] = 0
    for i in array:
        print(i)





    pass


if __name__ == "__main__":
    main()
