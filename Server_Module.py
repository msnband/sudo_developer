import asyncio
import random
import os

# class color:
#     RED = '\033[91m'
#     BOLD = '\033[1m'
#     GREEN = '\033[92m'


async def send_back(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    
    user_list = []
    # 'peername' is remote address connected to
    addr = writer.get_extra_info('peername')
    message = f'{addr!r} is connected !!!!' # !r calls the __repr__ method
    print(message)

    while message != 'exit':
        writer.write("\n\rYou are connected to SERVER...".encode(encoding="UTF-8"))
        writer.write("\n\rPlease press ' R ' to Register or ' L ' to Log in...:".encode(encoding="UTF-8"))
        
        data = await reader.readline()
        # Transfer format is bytes, decode() makes it a string
        message = data.decode().strip()

        if message == "R":
            Flag = True
            while Flag:

                exist_check = False
                writer.write("\n\rPlease insert your Username: \n\r".encode(encoding="UTF-8"))
                data = await reader.readline()
                user_name = data.decode().strip()
                if exist_check == False:
                    for items in user_list:
                        if items == user_name:
                            writer.write("\n\rThis username is already exist. Please try another username: ".encode(encoding="UTF-8"))
                            exist_check = True

                    if exist_check == False:        
                        user_list.append(user_name)
                        writer.write("\n\rPlease insert your Password: \n\r".encode(encoding="UTF-8"))
                        data = await reader.readline()
                        user_password = data.decode().strip()

                        writer.write("\n\rPlease insert your Privilages: \n\r".encode(encoding="UTF-8"))
                        data = await reader.readline()
                        user_privilages = data.decode().strip()

                        if user_privilages == 'user' or user_privilages == 'admin' :

                            user_file = open(user_name + ".txt", "w+")
                            user_file.write("User name = " + user_name)
                            user_file.write("\nPassword = " + user_password )
                            user_file.close()

                        # if user_privilages != 'user' and user_privilages != 'admin':
                        else:
                            writer.write("Your privilage must be 'user' or 'admin'!".encode(encoding="UTF-8"))

                        
                
                        
        elif message == "L":
            writer.write("\n\r Password: \n\r".encode(encoding="UTF-8"))
            await writer.drain()


        else:
            # writer.write()
            await asyncio.sleep(random.randint(0, 10))
            # The Streamwriter.write() is just a regular function
            writer.write('\n[From server]: '.encode(encoding='UTF-8')+data[::-1])
            await writer.drain()

        if message == 'exit':
            close_msg = f'{addr!r} wants to close the connection.'
            writer.write(close_msg.encode(encoding="UTF-8"))
            break
    writer.close()



async def main():
    server = await asyncio.start_server(send_back, '127.0.0.1', 8080)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
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
