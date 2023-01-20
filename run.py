import random
import time

QUESTIONS = [
    {
        "question": "What is the third planet from the sun? ",
        "answer": "Earth"},
    {
        "question": "What has hands but cannot clap? ",
        "answer": "Clock"
    },
    {
        "question": "What is 2 + 2? ",
        "answer": "4"
    },
    {
        "question": "what is 4 + 7? ",
        "answer": "11"
    },
    {
        "question": "who was the first man on the moon? ",
        "answer": "Neil Armstrong"
    },
    {
        "question": "who was the first president of the USA? ",
        "answer": "George Washington"
    }
]

# print('Hello and welcome to the Terminal')
# print('To gain access to the escape pod, you must unlock it.')

# playing = input('Press enter to continue. \n')

# while True:
#     player = input('Please enter your name: \n')

#     if not player.isalpha():
#         print('That is an invalid response') 
#         print('Only letters are accepted')
#     else: 
#         break

# print(f'Hi {player} and welcome to the escape pod!')
# print('To enter this escape pod, you have three attempts.')
# print('After the third unsuccessful attempt, the pod will collapse.')

def question_picker(QUESTIONS): 
    global number
    number = random.randint(0, 5)   
    global used_numbers 
    used_numbers = []        
    while True:                             
        if number not in used_numbers:
            used_numbers.append(number)            
            return QUESTIONS[number]            
            ask_question(number)                       
            if len(used_numbers) >= 6:
                break 

def ask_question(number):       
    random_question = QUESTIONS[number]
    global my_question
    my_question = random_question['question']
    global correct_answer     
    correct_answer = random_question['answer']
    global my_answer    
    my_answer = input(my_question)
   
attempt = 2

def validate_answer(my_answer, correct_answer, my_question, attempt):
    """
    Compare the player's answer with the correct answer from the dictionary
    Provide feedback from the terminal
    """
    if my_answer == correct_answer:
        print('Correct')              
        question_picker(QUESTIONS) 
          
    else:
        print('That is not correct.')
        attempt -= 1
        if attempt > 0:
            print(f'You have {attempt} chance remaining.')          
            my_answer = input(my_question)            
            validate_answer(my_answer, correct_answer, my_question, attempt)         
        else:        
            print('Detonation sequence triggered...')
            explode()  


# def explode():
#     print("The pod will explode in 3...")
#     time.sleep(1)
#     print("2...")
#     time.sleep(1)
#     print("1..." )
#     time.sleep(1)
#     print("KABOOM")

question_picker(QUESTIONS)
ask_question(number)
validate_answer(my_answer, correct_answer, my_question, attempt)


# if __name__ == "__main__":
#     game_over = False
#     attempts = 0
#     while game_over == False:
#         if attempts == 0:
#             # Only generates a new question if the user has moved to the next - avoids generating new question when they get the answer wrong
#             random_question = question_picker(QUESTIONS)
#         answer = validate_answer(random_question)
#         if attempts <= 2:
#             if answer is False:
#                 attempts += 1
#             else:
#                 attempts = 0  # Resets the attempts for the next question
#         else:
#             # Run out of attempts - show messaging for that
#             game_over = True  # Loop will then break and the program will stop
#         if len(QUESTIONS) >= 6:
#             # User has answered all questions correctly - show messaging for that
#             game_over = True





