"""EX02 - One Shot Wordle."""
__author__ = "730466273"

Green: str = "\U0001F7E9"
White: str = "\U00002B1C"
Yellow: str = "\U0001F7E8"
guess = str("")
secret = "python"
i = 0

word = (input("What is your 6-letter guess? "))
while len(word) !=6:
    word = input("That was not 6 letters! Try again: ")

while i < len(secret):
    if word[i] == secret[i]:
        guess = guess + Green 
    else:
        j: int = 0
        yellow: bool = False
        while j < len(secret) and yellow == False:
            if word[i] == secret[j]:
                yellow = True
            else:
                j = j + 1
        if yellow:
            guess = guess + Yellow
        else:
            guess = guess + White
    i = i + 1
print(guess)

if word == secret:
    print("Woo? You got it!")
else:
    print("Not quite. Play again soon!")