import asyncio
import random
import os
import shutil

# class color:
#     RED = '\033[91m'
#     BOLD = '\033[1m'
#     GREEN = '\033[92m'

# message != 'quit' and
async def send_back(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    
    # 'peername' is remote address connected to
    addr = writer.get_extra_info('peername')
    writer.write("Waiting to connect to server...".encode(encoding="UTF-8"))
    await asyncio.sleep(random.randint(0, 10))
    message = f'{addr!r} is connected to server !!!!' # !r calls the __repr__ method
    writer.write(f"\n\r{message}".encode(encoding="UTF-8"))
    writer.write("\n\n\r ************************** WELLCOME TO PYTHON SERVER **************************".encode(encoding="UTF-8"))

    Flag = True
    while Flag == True:
        writer.write("\n\n\rYou are connected to SERVER...".encode(encoding="UTF-8"))
        writer.write("\n\n\r>>To see the available commands and options, press 'commands>> '".encode(encoding="UTF-8"))
        data = await reader.readline()
        message = data.decode().strip()

        if message == 'commands':
            writer.write("\n\n\r>> Command 'change_folder' to move the current working directory.[change_folder <name>]".encode(encoding="UTF-8"))
            writer.write("\n\n\r>> command 'list' to print all files and folders in the current working directory.[list]".encode(encoding="UTF-8"))
            writer.write("\n\n\r>> Command 'read_file' to read data from the file <name> in the current working directory.[read_file <name>]".encode(encoding="UTF-8"))
            writer.write("\n\n\r>> Command 'write_file' to write the data in <input> to the end of the file <name> in the current working directory.[write_file <name> <input>]".encode(encoding="UTF-8"))
            writer.write("\n\n\r>> Command 'create_folder' to create a new folder with the specified <name> in the current working directory.[create_folder <name>]".encode(encoding="UTF-8"))
            writer.write("\n\n\r>> command 'register' to register a new user and password with optional privilage.[register <username> <password> <privileges>]".encode(encoding="UTF-8"))
            writer.write("\n\n\r>> Command 'login' to log in server.[login <username> <password>]".encode(encoding="UTF-8"))
            writer.write("\n\n\r>> Command 'delete' to delete the user conforming with <username> from the server.[delete <username> <password>]".encode(encoding="UTF-8"))
            writer.write("\n\n\r>> Command 'quit' to leave and close the page.[quit]".encode(encoding="UTF-8"))


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
                        privilages = data.decode().strip()

                        if privilages == 'admin' or privilages == 'user':

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

                            if privilages != 'admin' or privilages != 'user':
                                writer.write("\n\rYour privilage must be 'user' or 'admin'!\n\r".encode(encoding="UTF-8"))
                                Flag == True

                        if privilages == 'user':

                            user_password = data.decode().strip()
                            user_name = data.decode().strip()
                            if not os.path.exists('M:\python_bth\my_assignment_3\Folder_User'):
                                os.makedirs("M:\python_bth\my_assignment_3\Folder_User")
                            os.chdir('M:\python_bth\my_assignment_3\Folder_User')
                            if os.path.exists(user_name + ".txt"):
                                writer.write("\n>> This username is already exist!".encode(encoding="UTF-8"))

                            if not os.path.exists('M:\python_bth\my_assignment_3\Folder_User\pictures_of_dogs'):
                                os.makedirs("M:\python_bth\my_assignment_3\Folder_User\pictures_of_dogs")

                            else:
                                user_folder = open(user_name + ".txt", "w+")
                                user_folder.write("User name >> " + user_name)
                                user_folder.write("\nPassword >> " + user_password )
                                writer.write("\nYour username and password have created successfully...".encode(encoding="UTF-8"))
                                writer.write("\n\rWaiting to connect to server.....".encode(encoding="UTF-8"))
                            user_folder.close()


                            # os.chdir('M:\python_bth\my_assignment_3/Root')
                            # if not os.path.exists('M:\python_bth\my_assignment_3\Root\User_Folder'):
                            #     os.makedirs("M:\python_bth\my_assignment_3\Root\User_Folder")
                            # os.chdir('M:\python_bth\my_assignment_3\Root\User_Folder')
                            # user_folder = open(user_name + ".txt", "w+")
                            # os.chdir('M:\python_bth\my_assignment_3\Root\Admin\Top_secret_data')
                            # else:
                                # writer.write("The directory with this name is already created!".encode(encoding="UTF-8"))
                            # if os.path.exists(user_name + ".txt"):
                            #     writer.write("\n>> This username is already exist!".encode(encoding="UTF-8"))
                            
                            # else:
                            #     user_folder = open(user_name + ".txt", "w+")
                            #     user_folder.write("User name >> " + user_name)
                            #     user_folder.write("\nPassword >> " + user_password )
                            #     writer.write("\n\rYour username and password have created successfully...".encode(encoding="UTF-8"))
                            #     writer.write("\n\rWaiting to connect to server.....".encode(encoding="UTF-8"))
                            # user_folder.close()

                            # if privilages != 'user':
                            #     writer.write("\n\rYour privilage must be 'user' or 'admin'!\n\r".encode(encoding="UTF-8"))
                            #     Flag == True         

        elif message == "login":
            user_name = writer.write("\n\r >> User name: ".encode(encoding="UTF-8"))
            password = writer.write("\n\r >> Password: \n\r".encode(encoding="UTF-8"))
            user_name = data.decode().strip()
            password = data.decode().strip()
            await writer.drain()
            with open (f'{user_name.txt}', 'r') as file:
                if file.read() == user_name and file.read() == password:
                    writer.write("Authentication pass...You are successfully logged in...".encode(encoding="UTF-8"))
                else:
                    writer.write("Authentication failed... Your username or password is not valid...!".encode(encoding="UTF-8"))

                            
        if message == 'quit':
            close_msg = f'{addr!r} wants to close the connection.'
            writer.write(close_msg.encode(encoding="UTF-8"))
            break
       

        else:
            await asyncio.sleep(random.randint(0, 10))
            # The Streamwriter.write() is just a regular function
            writer.write('\n\r...[From server]: '.encode(encoding='UTF-8')+data[::-1])
            await writer.drain()  
    writer.close()


async def main():
    server = await asyncio.start_server(send_back, '127.0.0.4', 8080)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}'.encode(encoding='UTF-8'))
    async with server:
        await server.serve_forever()

asyncio.run(main())





# async def main():
#     server = await asyncio.start_server(send_back, '127.0.0.1', 8080)
#     addr = server.sockets[0].getsockname()
#     print(f'Serving on {addr}')
#     async with server:
#         await server.serve_forever()


# def user_test(user, user_list):
#     for i in range(0, len(user_list)-1):
#         if user == user_list[i]:
