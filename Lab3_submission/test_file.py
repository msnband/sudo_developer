""" 
    This module contains the test required for Lab3
    The following libraries are imported to use in this module.
"""
import os
import pickle
import unittest
import server

import class_file

MAIN_PATH = os.getcwd()
server.MyServer()
class TCPconnectionCheck(unittest.TestCase):
    """ This class designed to handle all test functions """
    def test_repr(self):
        """ Test function to print the username """
        usr = class_file.User('name', 'password', 'user')
        expected_outcome = 'name'
        outcome = str(usr)
        self.assertEqual(outcome, expected_outcome)

    def test_login_register(self):
        """ Test for registering and logging on the user 
                for doing this function, root and users folder should be already created
        """
        # switch to current working directory
        os.chdir(MAIN_PATH)
        serv = server.MyServer()
        expected_outcome = ["Congratulations. New user is registered succesfully", "Username you enterd is not valid or already exists"]
        outcome = []
        outcome.append(serv.register('temp', 'pwd', 'user')[:70])
        outcome.append(serv.register('temp', 'pwd', 'user')[:70])
        expected_login_outcome = "Successfully logged in"
        login_outcome = (serv.login('temp', 'pwd', 'tcp port')[:22])

        # delete user before start next test
        with open('reg.pickle', 'rb') as listfile:
            user_list = pickle.load(listfile)
        try:
            os.removedirs(os.path.join('Users', 'temp'))
        except FileNotFoundError:
            os.removedirs(os.path.join("Admins", "temp"))

        new_user = []
        for user in user_list:
            if user.user_name != 'temp':
                new_user.append(user)      
        listfile = open('reg.pickle', 'wb')
        pickle.dump(new_user, listfile)
        listfile.close()

        self.assertEqual(login_outcome, expected_login_outcome)
        self.assertEqual(outcome, expected_outcome)

    def test_change_directory(self):
        """ Check for changing root and user directory.
        for doing this function, root and users folder should be already created
        """
        usr = class_file.User("name", "password", "user")
        usr.currentPath = os.path.join(MAIN_PATH, 'root')
        expected_outcome = "You are located in "\
             + usr.currentPath+"\\Users"
        outcome = usr.change_directory("Users")
        os.chdir(MAIN_PATH)
        self.assertEqual(outcome, expected_outcome)   

    def test_write_file(self):
        """ Check to write text in root and user directory
        for doing this function, root and users folder should be already created.
        """
        usr = class_file.User("name", "password", "user")
        usr.currentPath = os.path.join(MAIN_PATH, "root", "Users")
        expected_outcome = ["File text.txt is updated.", \
             "File text.txt is updated."]
        outcome = []
        input_check = ['text.txt', 'text.txt']
        outcome.append(usr.write_file(input_check[0], 'testing'))
        outcome.append(usr.write_file(input_check[1], 'testing'))

        self.assertEqual(outcome, expected_outcome)
        # delete created test file after test is completed and
        # change to main directory
        os.remove('text.txt')
        os.chdir(MAIN_PATH)
    
    def test_create_directory(self):
        """ Check tp create root and user directory
        for doing this function, root and users folder should be already created.
        """
        usr = class_file.User('name', "password", 'user')
        usr.currentPath = os.path.join(MAIN_PATH, "root", "Users")
        expected_outcome = ["Folder testing created", \
            "Folder testing created"]
        outcome = []
        input_check = ["testing", "testing"]
        outcome.append(usr.create_directory(input_check[0]))
        outcome.append(usr.create_directory(input_check[1]))
        self.assertEqual(outcome, expected_outcome)
        # delete created test file after test is completed and
        # change to main directory
        os.rmdir("testing")
        os.chdir(MAIN_PATH)

    def test_list_file(self):
        """ Check to list contents of root and user directory
        for doing this function, root and users folder should be already created.
        """
        usr = class_file.User("name", "password", "user")
        usr.currentPath = os.path.join(MAIN_PATH, 'root', 'Users')
        usr.create_directory("file_test")
        usr.currentPath = os.path.join(usr.currentPath, "file_test")
        expected_outcome = '* Folder is empty *'
        outcome = usr.list_file()
        self.assertEqual(outcome, expected_outcome)
        os.chdir(MAIN_PATH)

    def test_read_noninput(self):
        """ Check the readfile wether the user passed
            without any name for the file root and Users directory.
        """
        usr = class_file.User("name", 'password', 'user')
        usr.currentPath = os.path.join(MAIN_PATH, "root", "Users")
        usr.file_name = "random_file.extension "
        expected_outcome = "random_file.extension file has been closed"
        outcome = usr.read_noninput()
        self.assertEqual(outcome, expected_outcome)
        os.chdir(MAIN_PATH)

    def test_write_noninput(self):

        usr = class_file.User("name", "password", "user")
        usr.currentPath = os.path.join(MAIN_PATH, "root", "Users")
        expected_outcome = "Folder text1.txt is removed"
        outcome = usr.write_nontext('text1.txt')
        self.assertEqual(outcome, expected_outcome)
        os.chdir(MAIN_PATH)

    def test_create_write(self):
        
        usr = class_file.User("name", "password", "user")
        usr.currentPath = os.path.join(MAIN_PATH, "root", "Users")
        expected_outcome_folder = ["Folder TEST_ALL created"]
        expected_outcome_write = ["File TESTALL.txt is updated."]
        for expected_folder, expected_write, in zip(\
            expected_outcome_folder, expected_outcome_write):
            self.assertEqual(usr.create_directory("TEST_ALL"), expected_folder)
            self.assertEqual(usr.write_file("TESTALL.txt", \
                '*** This is test ***'), expected_write)
        
        # delete created test file after test is completed and
        # change to main directory
        os.rmdir('TEST_ALL')
        os.remove('TESTALL.txt')
        os.chdir(MAIN_PATH)

    def test_read_write(self):
        """ Check for read and write function.
        for doing this function, root and users folder should be already created
        """
        usr = class_file.User("name", "password", "user")
        usr.currentPath = os.path.join(MAIN_PATH, "root", "Users")
        expected_write_c = "File textread.txt is updated."
        expected_read_c = "File content are: \n\n"+"HelloWorld\n\n"
        self.assertEqual(usr.write_file('textread.txt',\
             ['HelloWorld']), expected_write_c)
        self.assertEqual((usr.read_file('textread.txt')), expected_read_c)
        os.remove('textread.txt')
        os.chdir(MAIN_PATH)

    def test_readfile_empty(self):
        """ check for read function to read empty file
        for doing this function, root and users folder 
        should be already created
        """
        usr = class_file.User("name", 'password', 'user')
        usr.currentPath = os.path.join(MAIN_PATH, 'root', "Users")
        expected_outcome = "* Request not accepted *"
        outcome = usr.read_file('empty.txt')
        os.chdir(MAIN_PATH)
        self.assertEqual(outcome, expected_outcome)

    def test_previous_directory(self):
        """ Test to change directory to return to previous directory and folder.
        for doing this function, root and users folder should be already created.
        """
        usr = class_file.User('name', 'password', 'user')
        usr.currentPath = os.path.join(MAIN_PATH, \
            'root', 'Users', 'name')
        expected_outcome = "User not permitted to leave the home folder!"  
        outcome = usr.change_directory("..")
        os.chdir(MAIN_PATH)
        self.assertEqual(outcome, expected_outcome)

if __name__ == "__main__":
    unittest.main()


    