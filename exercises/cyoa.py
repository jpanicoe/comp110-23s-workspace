"""Choose Your Own Adventure."""
___author___ = "730466273"


from random import randint


points: int = 0
player: str = ()


def greet() -> None: 
    """Greet Procedure and Welcome Message."""
    player = input("Greetings! Welcome to my game where you will be competing for the high score in two games. The first is a coinflip where you will pick heads or tails and the second is choosing a random number 1-10. Please enter your name: ")
    print(f"Greeting {player}. I'm excited to play with you!")


def main() -> None:
    """Main Function."""
    global player
    global points
    points = 0 
    greet()
    proceed: int = input("Please enter 1 to play coin toss, 2 to play guess the number, or 3 to exit. ")
    if proceed == 1:
        coinflip()
    elif proceed == 2: 
        numberpick()
    elif proceed == 3:
        end()


def coinflip(points: int) -> int:
    """Coin Flip Game."""
    j: int = 0
    while j < 3: 
        toss: int = randint(1, 2)
        guess: int = int(input("Type 1 for heads/Type 2 for tails: "))
        if toss == guess:
            points = points + 1
            print ("Correct!")
        else: 
            print ("Wrong!")
        j = j + 1
        print(f"Good job {player}, your score is {points}.")
        return points
    

def numberpick(points: int) -> int:
    """Number Pick Game"""
    j: int = 0
    number = randint(1, 10)
    guess: int = int(input("Type a random number between 1 and 10: "))
    if guess == number:
        points = points + 1
        print("Correct!")
    else:
        print("Incorrect!")
    j = j + 1
    print(f"Good job {player}, your score is {points}.")
    return points



def end() -> None:
    """Game Over."""
    print(f"Finished with {points} points! Can't wait to play again!")


if __name__ == "__main__":
    main()