"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   list=[]
   stop = False
    while stop == False:
      number = input("enter stop if you are done:")
      if number.lower() != "stop":
        number = int(number)
        list.append(number)
      else:
        stop = True
   sum = sum(list)
   length = len(list)
   total = sum/length
   print(total)

    pass



if __name__ == "__main__":
    main()
