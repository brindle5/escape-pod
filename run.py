import random

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
       
random_index = random.randint(0, 3)
random_question = QUESTIONS[random_index]     
my_question = random_question['question']    
correct_answer = random_question['answer']      
my_answer = input(my_question)


def validate_answer(my_answer, correct_answer, my_question):
    """
    Compare the player's answer with the correct answer from the dictionary
    Provide feedback from the terminal
    """
    if my_answer == correct_answer:
        print('Correct')
        # get_next_question(my_question)    
        
    else:
        print('That is not correct.')



        # attempt = 2
        # attempts_countdown(attempt)
             

# def attempts_countdown(attempt):
#     if attempt > 0:
#         print(f'You have {attempt} chances remaining.')
#         attempt -= 1
#         validate_answer(my_answer, correct_answer, my_question)        
#     else:        
#         print('This pod will collapse')
  

    
    

       
#         
#         
#         
       


# current_question = 0

# my_question = current_question
# def get_next_question(current_question):  

#     print(current_question)

    # """
    # Ask questions up to 10
    # """
    # global current_question
    # my_question = current_question

    # while True:    
    #     if current_question <= 10:            
    #         current_question +=1
    #         get_question()
    #     else:
    #         print('Finished')


validate_answer(my_answer, correct_answer, my_question)

   











