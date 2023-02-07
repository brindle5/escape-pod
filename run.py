import random
import time

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
        "question" : "what has a head and tail but no body? \n",
        "answer" : "A coin"
    },
    {
        "question" : "what fills a room but takes up no space? \n",
        "answer" : "Light"
    },
    {
        "question" : "How much is a baker's dozen? \n",
        "answer" : "13"
    },
    {
        "question" : "How many wives did King Henry VIII have beheaded? \n",
        "answer" : "2"
    },
    {
        "question" : "Which of Shakespeare's plays is known as the Scottish play? \n",
        "answer" : "Macbeth"
    },
    {
        "question" : "Whoever makes it, has no need of it. Whoever buys it, has no use for it. Whoever uses it, can neither feel nor see it. What is it? \n",
         "answer" : "A coffin"
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
    return False
    
def main():

    game_active = True
    # chances = 0
   
    while game_active:        

        # question_active = True        

        # while question_active:  

        random.shuffle(QUESTIONS) 

        for i in range(0, 9):                       
            question = QUESTIONS[i]['question'] 
            correct_answer = QUESTIONS[i]['answer']                     
            my_answer = input(question)             
            validate_answer(question, my_answer, correct_answer, attempt)
            # if True:
            #     continue
            # else:
            #     break                    
           
        else:
            print('You have proven your humanity.')
            print('You may now access the escape pod.')
            game_active = False        
            
main()

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