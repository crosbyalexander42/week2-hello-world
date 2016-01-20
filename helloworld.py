# Alexander Ryan Crosby
#This is the intro for my Robo Butler language request
print('Good day to you master!')
print('what language would you like to converse in today?')
print('1. Spanish')
print('2. French')
print('3. German')
language=input() # Making input language isn't really necessary but I wanted to
                 # simplify it for myself

if language == 'spanish':
    print('Hola!')
elif language == 'french':
    print('Bonjour!')
elif language == 'german':
    print('Hallo!')
elif language != 'spanish' or 'french' or 'german': # This is just so that it
    print('That is not a correct input...')         # just doesn't close out
    print('Are you quite alright master?')          # when there is an incorrect
                                                    # input. Not needed though

import sys  # Just so that the prgram doesn't immediately close when it finishes
input()     # executing. Want to at least see the response based on my input
sys.exit
