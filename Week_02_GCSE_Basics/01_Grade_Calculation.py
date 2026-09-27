"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   def get_grade(score):
    if score >= 80 and score <= 100:
        print("You got a grade A")
    elif score >= 60 and score <= 79:
        print("You got a grade B")
    elif score >= 40 and score <= 59:
        print("You got a grade C")
    elif score >= 0 and score <= 39:
        print("You got a grade D")
    else:
        print("Enter a vaild percentage")

grade = int(input("Enter the percentage you got :"))
get_grade(grade)

    pass


if __name__ == "__main__":
    main()
