
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

        self.assertEqual(login_outcome, expected_login_outcome)
        self.assertEqual(outcome, expected_outcome)

    def change_directory_test(self):

        usr = class_file.User('name', 'password', 'user')
        usr.currentPath = os.path.join(main_path, 'root', 'Users')
        expected_outcome = "You are located in " + usr.currentPath + "\\Users"
        outcome = usr.change_directory("Users")
        os.chdir(main_path)
        self.assertEqual(outcome, expected_outcome)

    def write_file_test(self):

        usr = class_file.User("name", 'password', 'user')
        usr.currentPath = os.path.join(main_path, 'root', "Users")
        expected_outcome = ["File text.txt is created", "File text.txt is updated"]
        outcome = []
        input_check = ['text.txt', 'text.txt']

        outcome.append(usr.write_file(input_check[0], 'testing'))
        outcome.append(usr.write_file(input_check[1], 'testing'))

        self.assertEqual(outcome, expected_outcome)
        os.remove('text.txt')
        os.chdir(main_path)
    
    def create_directory_test(self):

        usr = class_file.User('name', "password", 'user')
        usr.currentPath = os.path.join(main_path, 'root', 'Users')
        expected_outcome = ["Folder create TESTING", "Folder already exists TESTING"]
        outcome = []
        input_check = ["TESTING", "TESTING"]

        outcome.append(usr.create_directory(input_check[0]))
        outcome.append(usr.create_directory(input_check[1]))

        self.assertEqual(outcome, expected_outcome)
        os.rmdir("TESTING")
        os.chdir(main_path)

    def list_file_test(self):

        usr = class_file.User("name", "password", "user")
        usr.currentPath = os.path.join(main_path, 'root', 'Users')
        usr.create_directory("file_test")
        usr.currentPath = os.path.join(usr.currentPath, "file_test")
        expected_outcome = '* Folder is empty *'
        outcome = usr.list_file()
        self.assertEqual(outcome, expected_outcome)
        os.chdir(main_path)

    def read_noninput_test(self):

        usr = class_file.User("name", 'password', 'user')
        usr.currentPath = os.path.join(main_path, 'root', 'Users')
        usr.file_name = 'random_file.extension'
        expected_outcome = "random_file.extension is closed"
        outcome = usr.read_noninput()
        self.assertEqual(outcome, expected_outcome)
        os.chdir(main_path)

    def write_nontext_test(self):
        
        usr = class_file.User("name", "password", "user")
        usr.currentPath = os.path.join(main_path, 'root', 'Users')
        expected_outcome_folder = ["Folder created TEST_ALL"]
        expected_outcome_write = ["File TESTALL.txt is created"]

        for expected_folder, expected_write, in zip(expected_outcome_folder, expected_outcome_write):
            self.assertEqual(usr.create_directory("TEST_ALL"), expected_folder)
            self.assertEqual(usr.write_file("TESTALL.txt", '*** This is test ***'), expected_write)

        os.rmdir('TEST_ALL')
        os.remove('TESTALL.txt')
        os.chdir(main_path)
















        

if __name__ == "__main__":
    unittest.main()


    