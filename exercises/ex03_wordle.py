"""EX03 - Structured Wordle."""
__author__ = "730466273"

def contains_char(word: str, letter: str) -> bool:
    """Find letter in the word."""
    assert len(letter) == 1
    k: int = 0
    while k < len(word):
        if word[k] == letter:
            return True
        else:
            k = k + 1
    return False    
def emojified(guess: str, secret: str) -> str:
    """Emojified."""
    assert len(guess) == len(secret)
    Green: str = "\U0001F7E9"
    White: str = "\U00002B1C"
    Yellow: str = "\U0001F7E8"
    emoji: str = ""
    j: int = 0
    while j < len(guess):
        if guess[j] == secret[j]:
            emoji += Green
        else: 
            if contains_char(secret, guess[j]) is True:
                emoji += Yellow
            else:
                emoji += White
        j = j + 1
    return emoji
def input_guess(guess_length: int) -> str:
    """Expected length"""
    guess: str = input(f"Enter a {guess_length} character word: ")
    while len(guess) != guess_length:
        guess = input(f"That wasn't {guess_length} chars! Try again: ")
    if len(guess) == guess_length:
        guess = guess
    return guess
def main() -> None:
    """The entrypoint of the program and main game loop"""
    secret: str = "codes"
    turn: int = 1
    win: bool = False
    while turn <= 6 and win is False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            win = True
        else:
            turn += 1
    if win is False:
        print("X/6 - Sorry, try again tomorrow!")
    if win is True:
        print(f"You won in {turn}/6 turns!")

if __name__ == "__main__":
    main()
