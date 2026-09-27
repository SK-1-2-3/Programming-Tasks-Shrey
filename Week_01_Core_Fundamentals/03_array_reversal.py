"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   list=[]
for i in range (6):
 num = int(input())
 list.append(num)
for i in range (5,-1,-1):
 print(f"the numbers you enetered revserse is: {list[i]}")




if __name__ == "__main__":
    main()
