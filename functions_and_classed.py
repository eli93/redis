import password_encryption as pe
import numpy as np
from os import path as pt
# import new_classes as nc
import pickle


# **********************************************************************************************************************
# **********************************************************************************************************************


def check_password(user, entered_password):
    password_list = [line.rstrip('\n') for line in open('passwords.txt')]
    # print(ch)
    maybe_users = []
    for elm in password_list:
        if elm.__contains__(user):
            maybe_users = np.append(maybe_users, elm)

    # print(des)

    check = False
    for elem in maybe_users:
        my_delimiter = elem.index(',')
        this_user = elem[0:my_delimiter]

        if this_user == user:
            hashed_password = elem[my_delimiter + 1:len(elem)]
            # print(this_user)
            # print(password)

            check = pe.check_encrypted_password(entered_password, hashed_password)

    return check

# ************* Sign up Method ****************


def sign_up():

    user = input('Pick you Username : ')

    while user.__contains__(','):
        print('username can not contain --> , <-- ')
        user = input('Pick you Username : ')

    if pt.exists('already_used_usernames.txt'):

        already_used_usernames = [line.rstrip('\n') for line in open('already_used_usernames.txt')]

        while user in already_used_usernames:
            print('This user name is taken, please choose another user name')
            user = input('Pick you Username :')

    # get password

    password_1 = input('Pick your Password : ')
    while password_1.__contains__(','):
        print('password can not contain --> , <-- ')
        password_1 = input('Pick your Password : ')

    while password_1.__len__() < 8:
        print('Your password should at least have 8 characters')
        password_1 = input('Pick your Password : ')

    password_2 = input('verify password : ')

    while password_1 != password_2:
        print('passwords do not match, please try again')
        password_1 = input('Pick your Password : ')
        password_2 = input('verify password : ')

    # adding username
    file_name = open('already_used_usernames.txt', 'a+')
    file_name.write(user + '\n')
    file_name.close()

    # adding username and encrypted password
    password_file = open('passwords.txt', 'a+')
    password_file.write(user)
    password_file.write(',')
    pe.encrypt_password(password_2, password_file)
    password_file.close()

    # *** Creating the users object
    new_user = nc.User(user)
    file_name = user + '.obj'
    user_file = open(file_name, 'wb')
    pickle.dump(new_user, user_file)
    user_file.close()

    # **************

    print(f'You are singed up with username : {user}')
    print('You can log in now')
    log_in()

    return new_user

# ************* Log in Method ****************


def log_in():

    user = input('Username : ')

    # ***** checking to see if the username is right
    usernames = [line.rstrip('\n') for line in open('already_used_usernames.txt')]
    count = 0
    while user not in usernames:
        print('Your user name is incorrect, try again')
        user = input('Username : ')
        count += 1

        if count == 3:
            print('It seems you dont remember your username')
            temp = input('do you want sign up again? : ')

            acceptable_answers = ['yes', 'no']
            while temp.lower() not in acceptable_answers:
                print('Please answer with yes or no')
                temp = input('do you want sign up again? : ')

            if temp.lower() == 'yes':
                print('You can sign up now')
                sign_up()
                return
            else:
                count = 0
                print('you can try 3 more times')

    # ***** checking to see if the password is right

    entered_password = input('Password : ')

    checked_pass = check_password(user, entered_password)
    # print(checked_pass)
    count = 0
    while checked_pass is False:
        print('Your password in not correct, Try again')
        entered_password = input('Password : ')
        checked_pass = check_password(user, entered_password)
        count += 1
        if count == 3 and checked_pass is False:
            print('you dont remember your password.')

            # print('you have tried so many times your account will be deleted')
            # delete account

            temp = input('do you want sign up again? : ')

            acceptable_answers = ['yes', 'no']
            while temp.lower() not in acceptable_answers:
                print('Please answer with yes or no')
                temp = input('do you want sign up again? : ')

            if temp.lower() == 'yes':
                print('You can sign up now')
                sign_up()
                return
            else:
                count = 0
                print('you can try 3 more times')

    if checked_pass:

        print('You are logged into your profile')

        file_name = user + '.obj'
        user_file = open(file_name, 'rb')
        user_obj = pickle.load(user_file)
        user_file.close()

        return user_obj
