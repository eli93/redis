# implementing redis data set

import my_functions as fc

# **********************************************************************************************************************
# **********************************************************************************************************************

# ********* sign up or log in

answer = input("Do you already have an account?  : ")
acceptable_answers = ['yes', 'no']

while answer.lower() not in acceptable_answers:
    print('Please answer with yes or no')
    answer = input("Do you already have an account?  : ")

if answer.lower() == 'yes':

    print('Please log in with your username and password')
    user_obj = fc.log_in()

else:
    print('You have to sign up first')
    user_obj = fc.sign_up()

# ****** redis program starts

print('**********************************************************')
print('\n')
print('At this point you can choose what you want to do')
print('if you do not know the right way to do what you want, ask for help by typing help. ')


command, flag = fc.redis_program(user_obj)
# flag = 0
while command != 'logout' and flag == 0:
    if flag == 1:
        break
    command, flag = fc.redis_program(user_obj)

print('***************************** END ******************************')


# **********************************************************************************************************************
# **********************************************************************************************************************


