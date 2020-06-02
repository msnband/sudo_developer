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




    def readfile(self, file_name):
        os.chdir(self.currentPath)