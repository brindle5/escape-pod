import os
import random
import time

import os


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


QUESTIONS = [
    {
        "question": "What is the third planet from the Sun? \n",
        "answer": "Earth"
    },
    {
        "question": "What has hands but cannot clap? \n",
        "answer": "A clock"
    },
    {
        "question": "Where is the Sea of Tranquility? \n",
        "answer": "The Moon"
    },
    {
        "question": "What has a neck but no head? \n",
        "answer": "A bottle"
    },
    {
        "question": "what has a head and tail but no body? \n",
        "answer": "A coin"
    },
    {
        "question": "what fills a room but takes up no space? \n",
        "answer": "Light"
    },
    {
        "question": "How much is a baker's dozen? \n",
        "answer": "13"
    },
    {
        "question": "How many wives did King Henry VIII have beheaded? \n",
        "answer": "2"
    },
    {
        "question": "Which of Shakespeare's plays is known as the Scottish play? \n",  # noqa
        "answer": "Macbeth"
    },
    {
        "question": "Whoever makes it, has no need of it. Whoever buys it, has no use for it. Whoever uses it, can neither feel nor see it. What is it? \n",  # noqa
        "answer": "A coffin"
    },
    {
        "question": "11 \n",
        "answer": "11"
    },
     {
        "question": "12? \n",
        "answer": "12"
    },
    {
        "question": "13 \n",
        "answer": "13"
    },
    {
        "question": "14 \n",
        "answer": "14"
    },
    {
        "question": "15 \n",
        "answer": "15"
    },
]

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
print('To enter this escape pod, you must answer ten questions.')
print()
print('The pod will explode if you enter two incorrect answers.')
print()
print('Good luck')
print()

attempt = 2


def validate_answer(question, my_answer, correct_answer, attempt):
    """
    Compare the player's answer with the correct answer from the dictionary
    Provide feedback from the terminal
    """
    clear()
    if my_answer == correct_answer:
        print('Correct')
        return True
    else:
        print('That is not correct.')
        attempt -= 1
        if attempt > 0:
            print(f'You have {attempt} chance remaining.')
            my_answer = input(question)
            validate_answer(question, my_answer, correct_answer, attempt)
        else:
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
    Sends the user's answere to the validate function.
    Keeps the player in a loop until they have answered 10 correct questions.
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
            my_answer = input(f"Question #{i+1}: {question}")
            is_correct = validate_answer(
                question, my_answer, correct_answer, attempt)
            if is_correct:
                continue
            else:
                game_active = False
                break
        else:
            clear()
            print('You have proven your humanity.')
            print('You may now access the escape pod.')
            game_active = False

    play_again = input("Would you like to play again? [yes/no]\n").lower()
    if play_again == "no":
        print("\nThanks for playing")
    elif play_again == "yes":
        main()


main()
