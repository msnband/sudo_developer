#The module contains the class for user and admin for both client and server to manage the files

""" importing required libraries for the module """
import shutil
import os
import time
import pickle
class User:
    """ class for privilege user """
    def __init__(self, user_name, password, privileges):
        """ Initializing variables in user class"""
        self.user_name = user_name
        self.password = password
        self.privilege = privileges
        self.currentPath = ""
        self.index = 0
        self.file_name = ""

    def __repr__(self):
        return self.user_name

    def read_noninput(self):
        """ This function is designed to close
        the file that user logged previousely """
        temporary = self.file_name
        self.file_name = ""
        self.index = 0
        return temporary + "file has been closed"

    def read_file(self, file_name):
        """ If user insert read file command without name of the file
        It should close the file."""
        #Change to current user directory
        os.chdir(self.currentPath)
        """ If the user insert command 'read_file', this
        command will implement the required service for user """
        # opening the file for reading.
        try:
            if self.file_name == file_name:
                file_to_read = open(self.file_name, 'r')
                # Reading the first 100 charachters from the opened file
                outcome = file_to_read.read(self.index + 100)
                outcome = outcome[self.index:]
                if len(outcome) < 100:
                    self.index = -100
                file_to_read.close()
                self.index = self.index + 100
            else:
                self.file_name = file_name
                file_to_read = open(self.file_name, 'r')
                outcome = file_to_read.read(100)
                file_to_read.close()
                self.index = 100
            return "File content are: \n\n" +outcome+ "\n\n"
        except OSError:
            print("* Request not accepted *")
            return "* Request not accepted *"

    def write_nontext(self, file_name):
        """If user insert write file command without name of the file It should close the file.
        file_name = str """
        # Change to current directoty
        os.chdir(self.currentPath)
        # Open the file to remove its contents
        file_erase = open(file_name, 'w')
        file_erase.close()
        outcome = "Folder " + file_name + " is removed"
        print(outcome)
        return outcome

    def write_file(self, file_name, text):
        """ If the user insert command 'write_file',
        this command will implement the required service for user."""
        # Change to current directoty
        os.chdir(self.currentPath)
        inputData = ' '.join(text)
        try:
            """ Add to the file if exist """
            if os.path.isfile(file_name):
                # open file to write on it.
                file_to_add = open(file_name, 'a')
                file_to_add.write(inputData + "\n")
                file_to_add.close()
                outcome = " File " + file_name + " is updated. "
                return outcome
            file_to_write = open(file_name, 'w')
            file_to_write.write(inputData + "\n")
            file_to_write.close()
            outcome = " File " + file_name + " is created now. "
            return outcome
        # Error handling in case required file is not exist!
        except FileNotFoundError:
            print("* File does not found! *")
            return "* File does not found! *"

    def create_directory(self, folder_name):
        """This function is designed to create folder in the current path.
        when creating the folder, change current path to created folder."""
        try:
            os.chdir(self.currentPath)
            os.mkdir(folder_name)
            print(f"Directory {folder_name} is created.")
        # Error handling in case the given name is already exist!
        except FileExistsError:
            outcome = folder_name + "* is created! *"
            print(outcome)
        return folder_name + "* is created! *"

    def change_directory(self, directory_name):
        """This function is designed to be able to move along the directories and folders
        to see the contents... """
        
        print("You are located in ", os.getcwd())
        try:
            if directory_name == '..':
                # Controling user from leaving the home folder
                if self.privilege == "user" and os.path.basename(\
                    self.currentPath) == self.user_name:
                    outcome = "User not permitted to leave the home folder!"
                    print(outcome)
                    return outcome
                # Controling admin from leaving the home folder
                if self.privilege == "admin" and os.path.basename(\
                    self.currentPath) == 'root':
                    print("Admin is not permitted to leave from root")
                    return "Admin is not permitted to leave from root"
                os.chdir(self.currentPath)
                os.chdir('..')
                self.currentPath = os.getcwd()
                print(f"You leaved the folder  {self.currentPath}.")
            else:
                os.chdir(self.currentPath)
                os.chdir(directory_name)
                self.currentPath = os.getcwd()
                print(f"You changed to  {self.currentPath}")
            return "You are located in " + self.currentPath
        # Handling filenotfound error in case folder is not created yet.
        except FileNotFoundError:
            print('* Folder is not available! *')
            return "* Folder is not available! *"
    
    def list_file(self):
        """ This function is designed to list all available files and folders
        in the current work directory. It also shows the time, date and size of
        file created."""
        os.chdir(self.currentPath)
        file_list = os.listdir(os.getcwd())
        string_return = ""
        if file_list:
            for File in file_list:
                # Showing and returning file name
                fName = os.path.basename(os.getcwd() + '\\' + File)
                string_return += fName + "\t"
                # Showing and returning file size
                file_size = os.path.getsize(os.getcwd() + '\\' + File)
                string_return += str(file_size) + "\t"
                # Showing file returning created time
                file_time = time.ctime(os.path.getctime(os.getcwd() + '\\' + File))
                string_return += file_time + "\n"
        else:
            string_return = '* Folder is empty *' 
        print(string_return)
        return string_return
class Admin(User):
    """ This class is designed to get permission to Admin to delet any user. 
    This class also inherited from class user."""  

    def delete(self, user_name, password, rootPath):
        """ This function is designed to delete registered 
        username and password. Only user with Admin privileges 
        is permitted to delete user from system. """

        # Change to root folder
        os.chdir(rootPath)  
        try:
            with open('reg.pickle', 'rb') as user_list_file:
                user_list = pickle.load(user_list_file)
        # Handling error in case user is not registered yet. 
        except FileNotFoundError:
            return "* User is not registered yet or file is not founded! *"
        if self.privilege == "admin":
            if self.password == password:
                if user_name in [User.user_name for User in user_list]:
                    # Delete user's directory
                    try:
                        shutil.rmtree(os.path.join('Users', user_name))
                    except FileNotFoundError:
                        shutil.rmtree(os.path.join('Admins', user_name))
                    # Delete user from pickle file
                    userlist_new = []
                    for user in user_list:
                        if user.user_name != user_name:
                            userlist_new.append(user)
                    user_list_file = open('reg.pickle', 'wb')
                    pickle.dump(userlist_new, user_list_file)
                    print(f'{user_name} is removed.')
                    outcome = user_name + "is removed."
                    return outcome
                # If user is not exist, return proper error.
                print(f"{user_name} not availabe.")
                outcome = user_name + "not availabe."
                return outcome
            # If Admin password is not correct, return proper error.
            print(f'Admin password is incorrect {self.user_name}')
            outcome = f'Admin password is incorrect {self.user_name}'
            return outcome
        # If user is not admin, does not have accesibility to this function.
        print("Your privilege must be Admin")
        return "Your privilege must be Admin"






    
                


