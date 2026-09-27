"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    def times_table(num):
        for i in range(1, 13):
            answer = num * i
            print(f"{num} X {i} = {answer}")

    multiply = int(input("Enter what times tables you want : "))
    times_table(multiply)

    pass


if __name__ == "__main__":
    main()
