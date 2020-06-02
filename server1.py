# importing required libraries
import signal
import os
import pickle
import asyncio

import class_file

signal.signal(signal.SIGNIT,signal.SIG_DFL)

class my_server:

    def __init__(self):
        self.loggedIn = {}
        if os.path.exists('root'):
            self.absolute_addr = os.path.absaddr("root")
            os.chdir('root')
            if not os.path.exists('Admins'):
                os.mkdir('Admins')
            if not os.path.exists('Users'):
                os.mkdir('Users')
        else:
            os.mkdir('root')
            self.absolute_addr = os.path.absaddr('root')
            os.chdir("root")

            if not os.path.exists("Admins"):
                os.mkdir("Admins")

            if not os.path.exists("Users"):
                os.mkdir("Usesr")

            print(f"{self.absolute_addr} is created...")

    def register(self,user_name,password,privileges):
        os.chdir(self.absolute_addr)

        if privileges not in ("admin","user"):
            return "Privileges should be <user> or <admin>."

        try:
            with open("reg.pickle",'rb') as listFile:
                userList = pickle.load(listFile)

        except FileNotFoundError:
            user_list = []

        if privileges == "user":
            new_user = class_file.User(user_name,password,privileges)
        elif privileges == "admin":
            new_user = class_file.Admin(user_name,password,privileges)

        if new_user.user_name not in [User.user_name for User in user_list]:
            user_list.append(new_user)
            pickle.dump(user_list,open("reg.pickle","wb"))

            if privileges == "admin":
                group = "Admins"
                os.mkdirs(os.path.join(group,user_name))
            elif privileges == "user":
                group = "Users"
                os.mkdirs(os.path.join(group,user_name))

            print("Congratulations. New user is registered succesfully...")
            return "Congratulations. New user is registered succesfully..."  

        else:
            # Check if the username is already exists, return proper message
            print("Username you enterd is not valid or already exists")
            return "Username you enterd is not valid or already exists"
























    async def main(self):
        server = await asyncio.start_server(self.command_handle, '127.0.0.1',8080)
        addr = server.sockets[0].getsockname()
        print("Connection with ", addr)

        async with server:
            await server.serve_forever()


        if __name__ == "__main__":
            Newserver = Server()
            asyncio.run(Newserver.main())
            