
import os
import server1
import class_file
import pickle
import unittest

main_path = os.getcwd()
server1.my_server()

class TCPconnectionCheck(unittest.TestCase):

    def repr_test(self):
        usr = class_file.User('name', 'password', 'user')
        expected_outcome = 'name'
        outcome = str(usr)

        self.assertEqual(outcome, expected_outcome)

    def login_register_test(self):

        os.chdir(main_path)
        serv = server1.my_server()
        expected_outcome = ["Congratulations. New user is registered succesfully...", "Username you enterd is not valid or already exists"]
        outcome = []

        outcome.append(serv.register('temp', 'pwd', 'user')[:27])
        outcome.append(serv.register('temp', 'pwd', 'user')[:27])

        expected_login_outcome = "temp: You logged in successfully."
        login_outcome = (serv.login('temp', 'pwd', 'tcp port')[:22])

        with open ('reg.pickle', 'rb') as listFile:
            user_list = pickle.load(listFile)

        try:
            os.removedirs(os.path.join('Users', 'temp'))
        except FileNotFoundError:
            os.removedirs(os.path.join("Admins", "temp"))

        new_user = []
        for user in user_list:
            if user.username != 'temp':
                new_user.append(user)
            
        listFile = open('reg.pickle', 'wb')
        pickle.dump(new_user, listFile)
        listFile.close()