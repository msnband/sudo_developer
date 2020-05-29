import asyncio
import random
import os
import shutil

class User:
    def __init__(self, name, password, privilages):
        self.name = name
        self.__password = password
        self.privilages = privilages
        
    
    def change_folder (self,name):
        pass

    # def list():
    #     pass


    def read_file(self, name):
        pass


    def write_file(self, name, input):
        pass


    def create_folder(self, name):
        pass


    def register(self, username, password, privileges):

        self.user_name = username
        self.user_password = password
        self.privilages = privileges

        if message == "register":
    
                exist_check = False
                user_list = []
                writer.write("\n\rPlease insert your Username >> \n\r".encode(encoding="UTF-8"))
                data = await reader.readline()
                user_name = data.decode().strip()
                if exist_check == False:
                    for items in user_list:
                        if items == user_name:
                            writer.write("\n\rThis username is already created. Please try another username. ".encode(encoding="UTF-8"))
                            exist_check = True

                    if exist_check == False:        
                        user_list.append(user_name)
                        writer.write("\n\rPlease insert your Password: \n\r".encode(encoding="UTF-8"))
                        data = await reader.readline()
                        user_password = data.decode().strip()

                        writer.write("\n\rPlease insert your Privilages << 'user' or 'admin >>': \n\r".encode(encoding="UTF-8"))
                        data = await reader.readline()
                        user_privilages = data.decode().strip()

                        if user_privilages == 'admin':

                            if not os.path.exists('M:\python_bth\my_assignment_3\Root\Admin\Top_secret_data'):
                                os.makedirs("M:\python_bth\my_assignment_3\Root\Admin\Top_secret_data")
                            os.chdir('M:\python_bth\my_assignment_3\Root\Admin\Top_secret_data')
                            # else:
                                # writer.write("The directory with this name is already created!".encode(encoding="UTF-8"))
                            if os.path.exists(user_name + ".txt"):
                                writer.write("\n>> This username is already exist!".encode(encoding="UTF-8"))

                            else:
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write("User name >> " + user_name)
                                user_folder.write("\nPassword >> " + user_password )
                                writer.write("\nYour username and password have created successfully...".encode(encoding="UTF-8"))
                                writer.write("\n\rWaiting to connect to server.....".encode(encoding="UTF-8"))
                            user_folder.close()

                            if user_privilages != 'admin':
                                writer.write("\n\rYour privilage must be 'user' or 'admin'!\n\r".encode(encoding="UTF-8"))
                                Flag == True

                        if user_privilages == 'user':

                            if not os.path.exists('M:\python_bth\my_assignment_3\Root\My_Pictures'):
                                os.makedirs("M:\python_bth\my_assignment_3\Root\My_Pictures")
                            os.chdir('M:\python_bth\my_assignment_3\Root\Admin\Top_secret_data')
                            # else:
                                # writer.write("The directory with this name is already created!".encode(encoding="UTF-8"))
                            if os.path.exists(user_name + ".txt"):
                                writer.write("\n>> This username is already exist!".encode(encoding="UTF-8"))
                            
                            else:
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write("User name >> " + user_name)
                                user_folder.write("\nPassword >> " + user_password )
                                writer.write("\n\rYour username and password have created successfully...".encode(encoding="UTF-8"))
                                writer.write("\n\rWaiting to connect to server.....".encode(encoding="UTF-8"))
                            user_folder.close()

                            if user_privilages != 'user':
                                writer.write("\n\rYour privilage must be 'user' or 'admin'!\n\r".encode(encoding="UTF-8"))
                                Flag == True         



    def login(self, username, password):
        pass

