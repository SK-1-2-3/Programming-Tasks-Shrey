"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    sentence = input("enter a sentence:")
words = []
word = ""
for character in sentence:
    if character == " ":
        words.append(word)
        word = ""
    else:
        word = word + character

words.append(word)
length = len(words)
print(f"there are {length} words in this sentence")
print(f"the words were: {words}")

    pass


if __name__ == "__main__":
    main()
