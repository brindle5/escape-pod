import os
import random
import time
from questions import QUESTIONS


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


print('Welcome to the USS Odyssey')
print()
print('To gain access to the escape pod, you must unlock it.')
print()

playing = input('Press enter to continue. \n')

while True:
    player = input('Please enter your name: \n')

    if not player.isalpha():
        print('That is an invalid response')
        print('Only letters are accepted')
    else:
        break

print(f'Hi {player} and welcome to the escape pod!')
print()
print('To access the escape pod, you must answer ten questions.')
print()
print('The ship will explode if you enter two incorrect answers.')
print()
print('Good luck')
print()


def validate_answer(question, correct_answer):
    """
    Compare the player's answer with the correct answer from the dictionary
    Provide feedback from the terminal
    """
    attempt = 2
    while attempt > 0:
        user_answer = input(question)
        if user_answer.lower() == correct_answer.lower():
            clear()
            print('Correct\n')
            break
        else:
            clear()
            attempt -= 1
            print('That is not correct.')
            print(f'You have {attempt} chance remaining.\n')

    if attempt > 0:
        return True
    else:
        game_active = False
        print('Detonation sequence triggered...')
        explode()


def explode():
    """
    The second incorrect answer will trigger a
    detonation sequence which ends the game.
    """
    print("The pod will explode in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GAME OVER")
    return False


def main():
    """
    Shuffles the dictionary of questions and asks for user input.
    Sends the user's answer to the validate answer function.
    Keeps the player in a loop until they have answered 10 questions correctly.
    Asks if they want to play again at the game's conclusion.
    """
    clear()
    game_active = True
    while game_active:

        random.shuffle(QUESTIONS)
        questions = QUESTIONS[:10]

        for i in range(0, 10):
            question = questions[i]['question']
            correct_answer = questions[i]['answer']
            is_correct = validate_answer(
                f"Question #{i+1}: {question}", correct_answer)
            if is_correct:
                continue
            else:
                game_active = False
                break
        else:
            clear()
            print('You have proven your humanity.')
            print('You may now access the escape pod.\n')
            game_active = False

    while True:
        play_again = input("Would you like to play again? [yes/no]\n").lower()
        if play_again == "no":
            clear()
            print("\nThanks for playing")
            break
        elif play_again == "yes":
            main()
        else:
            clear()
            print("Please select either 'yes' or 'no'.")


main()
