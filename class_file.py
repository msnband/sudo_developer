# The module is contains the class for user and admin for both client and server to manage the files

""" importing required libraries for the module """
import shutil
import os
import time
import pickle

class User:

    def __init__(self, user_name, password, privileges):
        """ Defining variables in user class"""
        self.user_name = user_name
        self.password = password
        self.privilege = privileges
        self.currentPath = ""
        self.index = 0
        self.file_name = ""

    
    def __repr__(self):
        return self.user_name



    def read_noninput(self):
        temporary = self.file_name
        self.file_name = ""
        self.index = 0
        message = "file has been closed"
        return temporary + message



    def readfile(self, file_name):
        """ Change to current user directory """
        os.chdir(self.currentPath)

        """ opening the file for reading """

        try:

            if self.file_name == file_name:
                file_to_read = open(self.file_name, 'r')
                outcome = file_to_read.read(self.index + 100)
                outcome = outcome[self.index: ]
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
            
            return "File content are: \n\n" + outcome + "\n\n"


    def write_nontext(self, file_name):

        # Change to current directoty
        os.chdir(self.currentPath)
        # Open the file to remove its contents
        file_erase = open(file_name, 'w')
        file_erase.close()
        print(f"Folder {file_name} is removed.")
        return "Folder" + file_name + "is removed"

    def write_file(self, file_name, text):

        # Change to current directoty
        os.chdir(self.currentPath)
        inputData = ' '.join(text)

        try: 
            """ Add to the file if exist """
            if os.path.isfile(file_name):
                file_to_add = open(file_name, 'a')
                file_to_add.write(inputData + "\n")
                file_to_add.close()
                return " File " + file_name + " is updated. "

            else:
                file_to_write = open(file_name, 'w')
                fil_to_write.write(inputData + "\n")
                file_to_write.close()
                return " File " + file_name + "is created now. "

        except FileNotFoundError:
            print("* File does not found! *")
            return "* File does not found! *"

    def create_directory(self, folder_name):

        try:
            os.chdir(self.currentPath)
            os.mkdir(folder_name)
            print(f"Directory {folder_name} is created.")

        except FileExistsError:
            print(f"* {folder_name} is already created! *")
        return folder_name + " is already created!"

    
    def change_directory(sef, directory_name):

        print("You are located in  ", os.getcwd())

        try:
            if directory_name == '..':

                # Controling user from leaving the home folder
                if self.privilege == "user" and os.path.basename(self.currentPath) == self.user_name:
                    print("User not permitted to leave the home folder! ")
                    return "User not permitted to leave the home folder! "
                
                # Controling admin from leaving the home folder
                if self.privilege == "admin" and os.path.basename(self.currentPath) == 'root':
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

        # Handling filenotfound error
        except FileNotFoundError:
            print('* Folder is not available! *')
            return "* Folder is not available! *" 

    def list_file(self):

        os.chdir(self.currentPath)
        file_list = os.listdir(os.getcwd())

        if file_list:
            for File in file_list:
                fName = os.path.basename(os.getcwd()) + File)
                


