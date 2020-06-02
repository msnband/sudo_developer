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
        self.privileges = privileges
        self.currentPath = ""
        self.index = 0
        self.file_name = ""

    



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


