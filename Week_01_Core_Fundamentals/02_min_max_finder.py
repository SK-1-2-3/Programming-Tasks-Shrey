"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
import random
numbers = random.randint(1, 50)
list = random.sample(range(1, 100), numbers)
min = list[0]
max = list[0]
for i in list:
    if min > i:
        min = i
    elif max < i:
        max = i
print("the lowest number is:", min)
print("the highest number is:", max)

    pass


if __name__ == "__main__":
    main()
