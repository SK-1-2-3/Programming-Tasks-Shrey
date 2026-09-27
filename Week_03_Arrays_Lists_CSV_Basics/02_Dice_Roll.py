"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    import random
amount = int(input("How many times do you want to roll the dice? "))
counts = 0
total = []
count = [0 , 0 , 0 , 0 , 0 , 0]
while counts != amount:
    dice = random.randint(1,6)
    print(dice)
    total.append(dice)
    counts = counts + 1
    count[dice - 1] = count[dice - 1] + 1
print("Enter 1 if you want to see: Totals for each number")
print("Enter 2 if you want to see: Average dice roll")
what_see = int(input("What number? "))
sum = sum(total)
if what_see == 1:
    for i in range(6):
        print(f"You have rolled {i + 1}: {count[i]} times")
elif what_see == 2:
    average = sum/amount
    print("The average number is:", average)


    pass


if __name__ == "__main__":
    main()
