print('Hello and welcome to the Terminal')

playing = input('To gain access to the escape pod, you must unlock it. Do you wish to continue? ')

if playing.lower() != 'yes':
    print('This pod will collapse in 5, 4, 3, 2 ,1')
    quit()

else:
    player = input('Please enter your name: ')

print(f'Hi {player} and welcome to the escape pod!')
print('To enter this escape pod, you have three attempts.')
print('After the third unsuccessful attempt, the pod will be collapsed.')

answer = input('What is the third planet from the sun? ')

if answer == 'earth':
    print('That is correct')
else:
    print('That is not correct')
    print(f'You have only two attempts remaining, {player}')

print('Time for a riddle.')
print(f'Do you like riddles, {player}?')
print('I hope so.')

answer = input('What has hands but cannot clap? ').lower()

if answer.lower != 'a clock':
    print('That is correct')
else:
    print('Sorry, that is not right.')

