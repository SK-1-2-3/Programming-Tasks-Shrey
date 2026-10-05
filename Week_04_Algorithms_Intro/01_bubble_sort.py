"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
  import random
amount = int(input("How many number should we sort: "))
list = []
swaps = 0
for i in range(0,amount):
    number = random.randint(1,100)
    list.append(number)
print("list before: ", list)
for i in range(len(list)):
    for x in range(0,len(list)-1):
        if list[x] > list[x+1]:
            list[x], list[x+1] = list[x+1], list[x]
            swaps += 1
print("list after: ", list)

print(f"There were {swaps} swaps")

    pass


if __name__ == "__main__":
    main()
