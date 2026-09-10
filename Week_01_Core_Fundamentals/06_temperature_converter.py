"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    celsius = input("enter temperature you want to convert, type stop when finished:")
    while celsius != "stop":
      if celsius.isdigit():
       celsius = int(celsius)
       fahrenheit = (celsius * 1.8) + 32
       print("your temperature in fahrenheit is", fahrenheit)
      else:
       print("error enter a number")

      celsius = input("enter temperature you want to convert, type stop when finished:")

    print("Bye")



    pass


if __name__ == "__main__":
    main()
