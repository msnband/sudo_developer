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
            self.loggedIn = {}

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

        # Check if the username is already exists, return proper message
        print("Username you enterd is not valid or already exists")
        return "Username you enterd is not valid or already exists"

    def login(self, user_name, password, tcpIP):
        os.chdir(self.absolute_addr)
        with open('reg.pickle', 'rb') as listFile:
            user_list = pickle.load(listFile)

        # Check if client is already logged in.
        if tcpIP in self.loggedIn.keys():
            if user_name in [user.user_name for user in self.loggedIn.values()]:
                return 'The port is already occupied with the same username'
            return 'The port is already occupied with another username'

        # Check user is logged in
        if user_name not in [user.user_name for user in self.loggedIn.values()]:
            pass
        else:
            return "This user is logged in with different port"

        if user_name in [User.user_name for User in user_list]:
            pass
        else:
            print('Insert a valid username...')
            return 'You inserted invalid username'

        for i in user_list:
            if i.user_name == user_name:
                user = i
                break
        
        # Check password wether it is correct or not showing proper message.
        if password == user.password:
            print('Password is correct.')
        else:
            return('Wrong password!')
        print('You logged in successfully.')

        group = user.privilege.capitalize() + 's'
        print(f'your group is {group}.')
        user.currentPath = os.path.join(self.absolute_addr, group, user_name)

        self.loggedIn.update({tcpIP: user})
        print(f"Successfully logged in, You are now in root/{group}/{user_name}")
        return f"Successfully logged in, You are now in root/{group}/{user_name}"

    async def command_handle(self, reader, writer):

        assert isinstance(read, asyncio.streams.StreamReader), \
            '* Stream reader in server Error *'

        assert isinstance(write, asyncio.streams.StreamWriter), \
            '* Stream writer in server Error *'

        while True:
            """ server waiting for new commands from clients """
            incoming_command = await reader.read(12000)
            commands = incoming_command.decode()
            address = writer.get_extra_info("peername")
            print(f"Received {commands!r} cooming from {address!r}")
            commands_spilit = commands.split('')

            # Check if Ip contains invalid charachters showing proper error.
            for wrd in address[0]:
                assert(wrd.isnumeric() or wrd == "."), \
                    "* Your have entered invalid charachte in your IP *"
            # Check to make sure port number is in this range.
            assert 1022 < address[1] < 65535, \
                "* Port number is out of range *" 

            try:
                user = self.loggedIn[address]
                print(f"{address} is related to {user}")

                if commands == 'list':
                    writer.write(list_file().encode())
                    await writer.drain()
                    os.chdir(self.absolute_addr)
                    continue

                if commands_spilit[0] == 'change_folder':
                    try:
                        writer.write(user.change_directory(commands_spilit[1]).encode())
                        await writer.drain()
                        os.chdir(self.absolute_addr)
                        continue

        






















    async def main(self):
        server = await asyncio.start_server(self.command_handle, '127.0.0.1',8080)
        address = server.sockets[0].getsockname()
        print("Connection with ", address)

        async with server:
            await server.serve_forever()


        if __name__ == "__main__":
            Newserver = Server()
            asyncio.run(Newserver.main())
            