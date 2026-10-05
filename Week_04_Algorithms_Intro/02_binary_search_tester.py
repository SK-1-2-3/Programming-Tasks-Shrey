"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
numbers = [2, 5, 8, 12, 16, 21, 27, 35, 42, 56, 67, 69, 74, 87, 90, 98]
search = int(input("What number do you want to search for? "))
while len(numbers) > 0:
    middle = len(numbers) // 2
    middle_item = numbers[middle]
    if search == middle_item:
        print("Your number was found in the list")
        break
    elif search > middle_item:
        numbers= numbers[middle+1:len(numbers)]
    elif search < middle_item:
        numbers= numbers[0:middle]

if len(numbers) == 0:
    print("Your number is not in the list")



    pass


if __name__ == "__main__":
    main()
