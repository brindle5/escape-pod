import random
import time

QUESTIONS = [
    {
        "question": "What is the third planet from the sun? ",
        "answer": "Earth"
    },
    {
        "question": "What has hands but cannot clap? ",
        "answer": "A clock"
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
    },
    {
        "question" : "what has a head and tail but no body? ",
        "answer" : "A coin"
    },
    {
        "question" : "what fills a room but takes up no space? ",
        "answer" : "Light"
    },
    {
        "question" : "How much is a baker's dozen? ",
        "answer" : "13"
    },
    {
        "question" : "How many wives did King Henry VIII have beheaded? ",
        "answer" : "2"
    },
    {
        "question" : "Which of Shakespeare's plays is known as the Scottish play? ",
        "answer" : "Macbeth"
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

attempt = 2

def validate_answer(question, my_answer, correct_answer, attempt):
    """
    Compare the player's answer with the correct answer from the dictionary
    Provide feedback from the terminal
    """
    
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
    print("The pod will explode in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1..." )
    time.sleep(1)
    print("GAME OVER")    

    # return False

def main():    

    game_active = True
    chances = 0
   
    while game_active:        

        question_active = True        

        while question_active:  

            random.shuffle(QUESTIONS) 
            for i in range(0, 12): 
                question = QUESTIONS[i]['question'] 
                correct_answer = QUESTIONS[i]['answer']                     
                my_answer = input(question)
                validate_answer(question, my_answer, correct_answer, attempt)
                
                question_active = False
                

                
                # if chances == 0:
                #     validate_answer(question, my_answer, attempt)
                #     """
                #     Only generates a new question if the user has moved to the next -
                #     avoids generating new question when they get the answer wrong
                #     """
                #     answer = validate_answer(question, my_answer, correct_answer, attempt)
            
                #     if chances <= 2:
                #         if answer is False:
                        # chances += 1                        

                # else:
            #     chances = 0  # Resets the attempts for the next question
            #     question_active == False
                    # else:
        #     # Run out of attempts - show messaging for that
        #           question_active = False  # Loop will then break and the program will stop
        #       if len(QUESTIONS) >= 10:
        #     # User has answered all questions correctly - show messaging for that
        #     game_active= False

main()