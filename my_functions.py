import password_encryption as pe
import numpy as np
from os import path as pt
# import new_classes as nc
import pickle
import os
import sys
import My_class as mc


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


# **********************************************
# ******** check_answer

def check_yes_no(answer, body):
    acceptable_answers = ['yes', 'no']
    while answer.lower() not in acceptable_answers:
        print('Please answer with yes or no')
        answer = input(body)
    return answer


# **********************************************
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
    new_user = mc.User(user)
    file_name = user + '.obj'
    user_file = open(file_name, 'wb')
    pickle.dump(new_user, user_file)
    user_file.close()

    # **************

    print(f'You are singed up with username : {user}')
    print('You can log in now')
    print('\n')
    log_in()

    return new_user

# **********************************************
# ************* Log in Method ****************


def log_in():

    user = input('Username : ')

    # ***** checking to see if the username is right
    usernames = [line.rstrip('\n') for line in open('already_used_usernames.txt')]
    count = 1
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
    count = 1
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

# # **********************************************
# # set key_value
#
#
# def set_key_value(obj):
#
#     key = input('What is your key? : ')
#     value = input('please set your value : ')
#     setattr(obj, key, value)
#
# # **********************************************
# # ******** see all attributes
#
#
# def see_attributes(obj):
#
#     all_attributes = obj.__dict__.keys()
#     # print(all_attributes)
#     # for att in all_attributes:
#     #     print(att)
#
#     return all_attributes
#
# # **********************************************
# # ******** get value of  a key
#
#
# def get_key(obj):
#     key = input('What is the KEY you want to get value of ?  : ')
#     all_keys = see_attributes(obj)
#
#     if key in all_keys:
#
#         value = getattr(obj, key)
#         print(f'The value of {key} is :  {value}')
#         return
#
#     else:
#         print('This key does not exist')
#
#         ans = input('Do you want to get another key? : ')
#
#         ans = check_yes_no(ans, 'Do you want to get another attribute? : ')
#
#         if ans.lower() == 'yes':
#
#             # new_att = input('What key you want to get? : ')
#             get_key(obj)
#
#         else:
#
#             print('No value')
#             return
# # **********************************************
# # ******** delete a key value
#
#
# def delete_key_value(obj):
#
#     att = input('Which key you want to delete? : ')
#
#     if att == 'name':
#         print('You can NOT delete name attribute. ')
#         print(' If you delete name attribute, your account and all your data will be deleted. ')
#
#         answer = input('Do you want to continue with deleting? : ')
#
#         answer = check_yes_no(answer, "Do you want to continue with deleting? : ")
#
#         if answer.lower() == 'no':
#
#             del_att = input('Do you want to delete another attribute? : ')
#             del_att = check_yes_no(del_att, 'Do you want to delete another attribute? : ')
#
#             if del_att.lower() == 'no':
#                 print('No attribute got deleted')
#                 return
#             else:
#                 # new_att = input('What attribute you want to delete: ')
#                 delete_key_value(obj)
#
#         else:
#
#             delete_account(obj)
#             print('You deleted your whole account.')
#             print('Have a Good day.')
#             return
#
#     else:
#
#         all_keys = see_attributes(obj)
#
#         if att in all_keys:
#
#             print(f'You deleted key {att} with value of {getattr(obj, att)}')
#             obj.__delattr__(att)
#
#             return
#
#         else:
#             print('This key does not exist')
#
#             ans = input('Do you want to delete another attribute? : ')
#
#             ans = check_yes_no(ans, 'Do you want to delete another attribute? : ')
#
#             if ans.lower() == 'yes':
#
#                 # new_att = input('What attribute you want to delete: ')
#                 delete_key_value(obj)
#
#             else:
#
#                 print('No attribute got deleted')
#                 return
# # **********************************************
# # ******** getting help
#
#
# def my_help():
#     # print('1. ask for help by typing help')
#     print('************** HELP **************')
#     # print('Type in the number of the command you want to do ')
#     print('see all keys : see a summary of what you have in your profile')  # get all the attributes
#     print('get key : Get value for a specific key')
#     print('set key value : add a key-value')
#     print('remove key : remove a key-value')
#     print('save : save all the changes you have made so far ')
#     print('delete account : deleting your account and all its data')
#     print('logout : You will logout from your account ')
#
# # **********************************************
# # ******** save everything
#
#
# def save_object(obj):
#     file_name = obj.name + '.obj'
#     user_file = open(file_name, 'wb')
#     pickle.dump(obj, user_file)
#     user_file.close()
#     # save = 1
#     print('You successfully saved all your data.')
#     return
#
#
# # **********************************************
# # ******** logout
#
# def log_out(obj, save):
#
#     if save == 0:
#         print('!!! You have not saved the changes you made !!!')
#         answer = input('Do you want to continue without saving? : ')
#         answer = check_yes_no(answer, 'Do you want to continue without saving? : ')
#
#         if answer.lower() == 'yes':
#
#             print('!!! Nothing was saved !!!')
#             print('You logged out of your account successfully. ')
#             print('Have a good day')
#
#         else:
#
#             save_object(obj)
#             print('Now you can safely log out')
#             # print('All your data successfully saved.')
#
#     else:
#         print('You have already saved all your data')
#         print('Now you can safely log out')
#
#     print('Have a good day')
#     return
#
# # **********************************************
# # ******** deleting the account


# def delete_account(obj):
#
#     # usernames = [line.rstrip('\n') for line in open('already_used_usernames.txt')]
#     password_list = [line.rstrip('\n') for line in open('passwords.txt')]
#
#     maybe_users = []
#     for elm in password_list:
#         if elm.__contains__(obj.name):
#             maybe_users = np.append(maybe_users, elm)
#
#     for elem in maybe_users:
#         my_delimiter = elem.index(',')
#         this_user = elem[0:my_delimiter]
#
#         if this_user == obj.name:
#             hash_pass = elem[my_delimiter + 1:len(elem)]
#             break
#
#     # deleting user name
#     with open("already_used_usernames.txt", "r") as f:
#         lines = f.readlines()
#     with open("already_used_usernames.txt", "w") as f:
#         for line in lines:
#             if line.strip("\n") != this_user:
#                 f.write(line)
#
#     # deleting user name and password
#     with open("passwords.txt", "r") as f:
#         lines = f.readlines()
#     with open("passwords.txt", "w") as f:
#         for line in lines:
#             if line.strip("\n") != this_user + ',' + hash_pass:
#                 f.write(line)
#
#     # deleting users file
#     file_name = obj.name + '.obj'
#     os.remove(file_name)
#
#     # delete object outside class
#     del obj
#     print('There is nothing more you can do')
#     print('\n')
#     print('*************** End Of Program ***************')
#     sys.exit()
# **********************************************
# **********************************************
# ******** redis program


def redis_program(obj):

    save = 0
    flag = 0
    answer_1 = input('What do you want to do? ')
    acceptable_answers = ['help', 'set key value', 'get key', 'remove key',
                          'save', 'logout', 'see all keys', 'delete account']

    while answer_1 not in acceptable_answers:
        print('requested command does not exist.')
        print('If you know the write command go ahead, or ask for help by typing help')
        answer_1 = input('What do you want to do? ')

    if answer_1 == 'help':
        obj.my_help()
        # my_help()

    elif answer_1 == 'set key value':
        obj.set_key_value()
        # set_key_value(obj)

    elif answer_1 == 'get key':
        obj.get_key()
        # get_key(obj)

    elif answer_1 == 'remove key':
        key = obj.delete_key_value()
        if key == 'name':
            del obj
            sys.exit()
        # delete_key_value(obj)

    elif answer_1 == 'see all keys':
        all_att = obj.see_attributes()
        # all_att = see_attributes(obj)
        for att in all_att:
            print(att)

    elif answer_1 == 'delete account':
        obj.delete_account()
        del obj
        sys.exit()
        # delete_account(obj)

    elif answer_1 == 'save':
        obj.save_object()
        # save_object(obj)
        save = 1

    elif answer_1 == 'logout':
        obj.log_out(save)
        # log_out(obj, save)
        flag = 1

    return answer_1, flag
