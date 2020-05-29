import asyncio
import random
import os
import os.path, time
import time
import datetime
import shutil


class User:
    def __init__(self, name, password, privilages, message):
        name = name
        password = password
        privilages = privilages
        message = message

    
    async def send_back(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):

        writer.write("Waiting to connect to server...".encode())
        await writer.drain()
        await asyncio.sleep(random.randint(0, 2))
        message = 'connected to server !!'
        print(message)
        writer.write(f"\n\r{message}".encode())
        writer.write("\n\n\r ------------------------ WELLCOME TO PYTHON SERVER ------------------------\
        \n\n\rYou are connected to SERVER...\
        \n\n\r>>To see the available commands and options, press 'commands >> ".encode())
        await writer.drain()

        Flag = True
        while Flag == True:
            
            await writer.drain()        
            data = await reader.readline()
            message = data.decode().strip()
            print(message)

        else:
            await asyncio.sleep(random.randint(0, 3))
            writer.write('\n\rWrite your commands: '.encode())
            await writer.drain()  
    # writer.close()


    def show_commands():

        if message == 'commands':
            writer.write(
            "\n\r>> Command 'change_folder' to move the current working directory.[change_folder <name>]\
                \n\n\r>> command 'list' to print all files and folders in the current working directory.[list]\
                \n\n\r>> Command 'read_file' to read data from the file <name> in the current working directory.[read_file <name>]\
                \n\n\r>> Command 'write_file' to write the data in <input> to the end of the file <name> in the current working directory.[write_file <name> <input>]\
                \n\n\r>> Command 'create_folder' to create a new folder with the specified <name> in the current working directory.[create_folder <name>]\
                \n\n\r>> command 'register' to register a new user and password with optional privilage.[register <username> <password> <privileges>]\
                \n\n\r>> Command 'login' to log in server.[login <username> <password>]\
                \n\n\r>> Command 'delete' to delete the user conforming with <username> from the server.[delete <username> <password>]\
                \n\n\r>> Command 'quit' to leave your directory and close the page.[quit]\
                \n\n\r>> Command 'exit' to close the page.[exit]".encode())
            # await writer.drain()
        
        else:
            asyncio.sleep(random.randint(0, 3))
            writer.write('\n\rWrite your commands: '.encode())
            writer.drain()  
    


    def register(self, username, password, privileges):

        if message == "register":
                # user_folder = []
                exist_check = False
                user_list = []
                writer.write("\n\rPlease insert your Username >> ".encode())
                data = reader.readline()
                user_name = data.decode().strip()
                if len (user_name) < 6:
                    writer.write("Your username can not be blank or less than 5 charachters!".encode())
                    return False
                if exist_check == False:
                    for items in user_list:
                        if items == user_name:
                            writer.write("\n\rThis username is already created. Please try another username. ".encode())
                            exist_check = True

                    if exist_check == False:        
                        user_list.append(user_name)
                        writer.write("\n\rPlease insert your Password: ".encode())
                        data = reader.readline()
                        user_password = data.decode().strip()
                        if len (user_password) < 6:
                            writer.write("Your password can not be empty or less than 6 charachters!".encode())
                            return False

                        writer.write("\n\rPlease insert your Privilages << 'user' or 'admin' >> ".encode())
                        data = reader.readline()
                        privilages = data.decode().strip()

                        if privilages == 'user':

                            if not os.path.exists('my_assignment_3\Root\Admin\Top_secret_data'):
                                os.makedirs("my_assignment_3\Root\Admin\Top_secret_data")
                                os.makedirs("my_assignment_3\Root\Admin\Current_Users")
                                os.makedirs("my_assignment_3\Root\Admin\Logged_History")
                                os.makedirs("my_assignment_3\Root\Admin\privilages_status")
                                os.chdir("my_assignment_3\Root\Admin\privilages_status")
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write(f"{privilages}")
                            os.chdir('my_assignment_3\Root\Admin\Top_secret_data')
                            if os.path.exists(user_name + ".txt"):
                                writer.write("\n\r>> This username is already exist!".encode())

                            else:
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write(f"{user_password}")
                                writer.write("\nYour username and password have created in server successfully...".encode())
                                writer.write("\n\rWaiting to connect to server.....".encode())
                                user_folder.close()
                               
                            if not os.path.exists(f'my_assignment_3\{user_name}_Folder'):
                                os.makedirs(f"my_assignment_3\{user_name}_Folder")
                            os.chdir(f'my_assignment_3\{user_name}_Folder')

                            if os.path.exists(user_name + ".txt"):
                                writer.write("\n\r}>> This username is already exist!".encode())
                                # Flag = True

                            else:
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write(f"Username >> {user_name}")
                                user_folder.write(f"\n\nPassword >> {user_password}\n\n\rAccessibility >> {privilages}" )
                                writer.write("\n\rYour username and password have created in your profile successfully...".encode())
                                writer.write("\n\rWaiting to connect to server.....".encode())
                                user_list.clear()
                                user_folder.close()   
                                user_list.clear() 

                        
                        if privilages == 'admin':

                            if not os.path.exists('my_assignment_3\Root\Admin\Admin_secret_data'):
                                os.makedirs("my_assignment_3\Root\Admin\Admin_secret_data")
                                os.makedirs("my_assignment_3\Root\Admin\Current_Users")
                                os.makedirs("my_assignment_3\Root\Admin\Logged_History")
                                os.makedirs("my_assignment_3\Root\Admin\Top_secret_data")
                                os.makedirs("my_assignment_3\Root\Admin\privilages_status")
                                os.chdir("my_assignment_3\Root\Admin\privilages_status")
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write(f"{privilages}")
                            os.chdir('my_assignment_3\Root\Admin\Top_secret_data')
                            if os.path.exists(user_name + ".txt"):
                                writer.write("\n\r>> This username is already exist!".encode())

                            else:
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write(f"{user_password}")
                                writer.write("\nYour username and password have created in server successfully...".encode())
                                writer.write("\n\rWaiting to connect to server.....".encode())
                            user_folder.close()

                            if not os.path.exists(f'my_assignment_3\Root\Admin\Admin_secret_data\{user_name}_Admin'):
                                os.makedirs(f'my_assignment_3\Root\Admin\Admin_secret_data\{user_name}_Admin')
                                os.chdir(f'my_assignment_3\Root\Admin\Admin_secret_data\{user_name}_Admin')
                            if not os.path.exists(f'my_assignment_3\{user_name}_Folder'):
                                os.makedirs(f"my_assignment_3\{user_name}_Folder")

                            if os.path.exists(user_name + ".txt"):
                                writer.write("\n>> This username is already exist!".encode())

                            else:
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write(f"Username >> {user_name}")
                                user_folder.write(f"\n\nPassword >> {user_password}\n\n\rAccessibility >> {privilages}" )
                                writer.write("\n\rYour username and password have created in your profile successfully...".encode())
                                writer.write("\n\rWaiting to connect to server.....".encode())
                                user_list.clear()
                            user_folder.close()   
                            user_list.clear() 

                        if privilages != 'admin' and privilages != 'user':
                            writer.write("\n\rYour privilage must be 'user' or 'admin'!\n\r".encode())
                            Flag == True
        
        else:
            asyncio.sleep(random.randint(0, 3))
            writer.write('\n\rWrite your commands: '.encode())
            writer.drain()
                

    def login(self, username, password):

        if message == "login":
            status = False
            user_list = []
            writer.write("\n\nUse your username and password to access your data...".encode())
            os.chdir('my_assignment_3\Root\Admin\Top_secret_data')
            writer.write("\n\rUsername >>".encode())
            data = reader.readline()
            user_name = data.decode().strip()
            user_list.append(user_name)
            writer.write("\nPassword >>".encode())
            data = reader.readline()
            user_password = data.decode().strip()
            if not os.path.exists(user_name +".txt"):
                writer.write("...ERROR...<<<Your username is not created in the server yet>>>\n\n".encode())
            
            else:
                """ Username and Password Authentication check..."""
                file = open(user_name+".txt")
                f = file.readlines()
                if f[0] == user_password:
                    status = True
                    os.chdir("my_assignment_3\Root\Admin\Current_Users")
                    if os.path.exists(f"my_assignment_3\Root\Admin\Current_Users\{user_name}"):
                        writer.write("\n\r...ERROR...<<You are already logged in>>".encode())
                    if not os.path.exists(f"my_assignment_3\Root\Admin\Current_Users\{user_name}"):
                        os.makedirs(f"my_assignment_3\Root\Admin\Current_Users\{user_name}")
                        writer.write("\n\rAuthentication Pass... <You logged in>...\n".encode())
                        currentTime = datetime.datetime.now() 
                        print(f"{user_name} is signed in at: ", currentTime)
                        writer.write(f"\n\rYou logged in at: {currentTime}".encode())  
                        writer.write(f"\n\n\rYou are now in {user_name}_Folder >>".encode())

                    if os.path.exists(f"my_assignment_3\{user_name}_Folder"):
                        os.chdir(f"my_assignment_3\{user_name}_Folder")
                    if not os.path.exists(f"my_assignment_3\{user_name}_Folder"):
                        os.chdir(f"my_assignment_3\Root\Admin\Admin_secret_data\{user_name}_Admin")

                else:
                    writer.write("You still connected to server...But Authentication FAILED..<Your Username or Password is NOT valid>>>".encode())
                # file.close()
        
        else:
            asyncio.sleep(random.randint(0, 3))
            writer.write('\n\rWrite your commands: '.encode())
            writer.drain()

    def create_folder(self, name):

        if message == "create_folder":
            writer.write("\nEnter a name to create the folder: ".encode())
            data = reader.readline()
            folder_name = data.decode().strip()
            if os.path.exists(f"my_assignment_3\{user_name}_Folder\{folder_name}"):
                writer.write("This folder is already created. Try another name...".encode())

            if not os.path.exists(f"my_assignment_3\{user_name}_Folder\{folder_name}"):
                os.makedirs(f"my_assignment_3\{user_name}_Folder\{folder_name}")
                now = datetime.datetime.now()
                writer.write(f"\n\r{folder_name} has created successfully in your folder at {now} ".encode())
                print(f"A file has created in {user_name} directory at {now}... ")

        else:
            asyncio.sleep(random.randint(0, 3))
            writer.write('\n\rWrite your commands: '.encode())
            writer.drain()

    def change_folder (self,name):
        pass

    def List():

        if message == 'list':
            os.chdir(f"my_assignment_3\{user_name}_Folder")
            CreationTime = time.ctime(os.path.getctime(f"my_assignment_3\{user_name}_Folder"))
            FileSize = os.path.getsize(f"my_assignment_3\{user_name}_Folder")
            for items in os.listdir("."):
                writer.write(f'\n\r{items}   created at      {CreationTime}   size   {FileSize}KB\n'.encode())
            
            if not os.path.exists(f"my_assignment_3\{user_name}_Folder"):
                writer.write("You need to login first to access to your data...".encode())

        else:
            asyncio.sleep(random.randint(0, 3))
            writer.write('\n\rWrite your commands: '.encode())
            writer.drain()

    def read_file(self, name):
        
        if message == 'read_file':
            writer.write("\nWrite name of the file you want to see its contents: ".encode())
            data = reader.readline()
            file_name = data.decode().strip()

            if os.path.exists(file_name+".txt"):
                file = open(file_name+".txt")
                f = file.readline(100)
                writer.write(f"\n\n{f}".encode())

            if not os.path.exists(file_name+".txt"):
                writer.write("....ERROR...This file is not exist or you did not logged in!".encode())

        else:
            asyncio.sleep(random.randint(0, 3))
            writer.write('\n\rWrite your commands: '.encode())
            writer.drain()

    def write_file(self, name, input):
        pass

    def quit():

        if message == 'quit':
            os.chdir("my_assignment_3\Root\Admin\Current_Users")

            try:
                shutil.move(f"my_assignment_3\Root\Admin\Current_Users\{user_name}", "my_assignment_3\Root\Admin\Logged_History")
            except shutil.Error:
                os.rmdir(f"{user_name}")
                writer.write(f"\n\r{user_name} wants to close the connection.\n\r".encode())
                writer.write("\n\rWaiting to disconnect from server...\n\n".encode())
                asyncio.sleep(random.randint(0, 4))
                print("Connection lost...")
                writer.write("\n\rThe Window will close soon...".encode())
                writer.write(f"\n\r< {user_name} > is successfully logged out...".encode())
                asyncio.sleep(random.randint(0, 4))
                print(f"{user_name} is logged out...")
        # break
        try:
            message == 'quit'    

        except OSError:
            writer.write(f"\n\r{user_name} wants to close the connection.\n\r".encode())
            writer.write("\n\rWaiting to disconnect from server...\n\n".encode())
            asyncio.sleep(random.randint(0, 4))
            print("Connection lost...")
            writer.write("\n\rThe Window will close soon...".encode())
            writer.write(f"\n\r< {user_name} > is successfully logged out...".encode())
            asyncio.sleep(random.randint(0, 4))
            print(f"{user_name} is logged out...")
        # break

    
#     else:
#         await asyncio.sleep(random.randint(0, 3))
#         writer.write('\n\rWrite your commands: '.encode())
#         await writer.drain()  
# writer.close()


async def main():
    server = await asyncio.start_server(send_back, '127.0.0.3', 8080)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}'.encode())
    async with server:
        await server.serve_forever()

    

asyncio.run(main())
asyncio(send_back())
show_commands()
register()
login()
create_folder()
List()
read_file()
quit()

