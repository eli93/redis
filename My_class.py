import pickle
import my_functions as fc
import numpy as np
import os
# **********************************************************************************************************************
# **********************************************************************************************************************


class User:

    def __init__(self, username):
        self.name = username

    # **********************************************
    # ******** set key_value

    def set_key_value(self):
        key = input('What is your key? : ')
        value = input('please set your value : ')
        setattr(self, key, value)

    # **********************************************
    # ******** see all attributes

    def see_attributes(self):
        all_attributes = self.__dict__.keys()
        # print(all_attributes)
        # for att in all_attributes:
        #     print(att)

        return all_attributes

    # **********************************************
    # ******** get value of  a key

    def get_key(self):
        key = input('What is the KEY you want to get value of ?  :')
        all_keys = self.see_attributes()

        if key in all_keys:

            value = getattr(self, key)
            print(f'The value of {key} is :  {value}')
            return

        else:
            print('This key does not exist')

            ans = input('Do you want to get another key? : ')

            ans = fc.check_yes_no(ans, 'Do you want to get another attribute? : ')

            if ans.lower() == 'yes':

                # new_att = input('What key you want to get? : ')
                self.get_key()

            else:

                print('No value')
                return

    # **********************************************
    # ******** delete a key value

    def delete_key_value(self):

        att = input('Which key you want to delete? :')

        if att == 'name':
            print('You can NOT delete name attribute. ')
            print(' If you delete name attribute, your account and all your data will be deleted. ')

            answer = input('Do you want to continue with deleting? : ')

            answer = fc.check_yes_no(answer, "Do you want to continue with deleting? : ")

            if answer.lower() == 'no':

                del_att = input('Do you want to delete another attribute? : ')
                del_att = fc.check_yes_no(del_att, 'Do you want to delete another attribute? : ')

                if del_att.lower() == 'no':
                    print('No attribute got deleted')
                    return
                else:
                    # new_att = input('What attribute you want to delete: ')
                    self.delete_key_value()

            else:

                self.delete_account()
                # del self
                print('There is nothing more you can do')
                print('\n')
                return att

        else:

            all_keys = self.see_attributes()

            if att in all_keys:
                value = getattr(self, att)
                print(f'You deleted key {att} with value of {value}')
                self.__delattr__(att)

                return

            else:
                print('This key does not exist')

                ans = input('Do you want to delete another attribute? : ')

                ans = fc.check_yes_no(ans, 'Do you want to delete another attribute? : ')

                if ans.lower() == 'yes':

                    # new_att = input('What attribute you want to delete: ')
                    self.delete_key_value()

                else:

                    print('No attribute got deleted')
                    return

    # **********************************************
    # ******** getting help

    def my_help(self):
        # print('1. ask for help by typing help')
        print('************** HELP **************')
        # print('Type in the number of the command you want to do ')
        print('see all keys : see a summary of what you have in your profile')  # get all the attributes
        print('get key : Get value for a specific key')
        print('set key value : add a key-value')
        print('remove key : remove a key-value')
        print('save : save all the changes you have made so far ')
        print('delete account : deleting your account and all its data')
        print('logout : You will logout from your account ')
        return

    # **********************************************
    # ******** save everything

    def save_object(self):
        file_name = self.name + '.obj'
        user_file = open(file_name, 'wb')
        pickle.dump(self, user_file)
        user_file.close()
        # save = 1
        print('You successfully saved all your data.')
        return

    # **********************************************
    # ******** logout

    def log_out(self, save):

        if save == 0:
            print('!!! You have not saved the changes you made !!!')
            answer = input('Do you want to continue without saving? : ')
            answer = fc.check_yes_no(answer, 'Do you want to continue without saving? : ')

            if answer.lower() == 'yes':

                print('!!! Nothing was saved !!!')
                print('You logged out of your account with out saving your data. ')

            else:

                self.save_object()
                # print('All your data successfully saved.')
                print('Now you can safely log out')

        else:
            print('You have already saved all your data')
            print('Now you can safely log out')

        print('Have a good day')
        return

    # **********************************************
    # ******** deleting the account

    def delete_account(self):

        # usernames = [line.rstrip('\n') for line in open('already_used_usernames.txt')]
        password_list = [line.rstrip('\n') for line in open('passwords.txt')]

        maybe_users = []
        for elm in password_list:
            if elm.__contains__(self.name):
                maybe_users = np.append(maybe_users, elm)

        for elem in maybe_users:
            my_delimiter = elem.index(',')
            this_user = elem[0:my_delimiter]

            if this_user == self.name:
                hash_pass = elem[my_delimiter + 1:len(elem)]
                break

        # deleting user name
        with open("already_used_usernames.txt", "r") as f:
            lines = f.readlines()
        with open("already_used_usernames.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != this_user:
                    f.write(line)

        # deleting user name and password
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
        with open("passwords.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != this_user + ',' + hash_pass:
                    f.write(line)

        # deleting users file
        file_name = self.name + '.obj'
        os.remove(file_name)

        # delete object outside class
        print('There is nothing more you can do')
        print('\n')
        print('*************** End Of Program ***************')
