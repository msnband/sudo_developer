# importing required libraries

import signal
import asyncio

signal.signal(signal.SIGINT, signal.SIG_DFL) # press Ctrl + C to stop client

class my_client:

    def __init__(self):
        self.commandList = []

    async def client(self, address, portNumber):
        # check and return proper error if IP is not valid.
        for j in address:
            assert(j.isnumeric() or j == "."), " The IP contains wrong or invalid charachters"

        assert 1022 < portNumber < 65535, "Port number is out of range!"

        # Establish a TCP connection to server
        reader,writer = await asyncio.open_connection(address, portNumber)
        
        # assert proper error if TCP connection has problem.
        assert isinstance(reader,asyncio.streams.StreamReader), "Streamreader on server is not working (message from client)"
        assert isinstance(writer, asyncio.streams.StreamWriter), "Streamwriter on server is not working (message from client)"

        print("\n insert command 'register' or 'login' to access the server")

        while true:
            user_command = input("\n Client is waiting...\n")

            user_command = user_command.strip()
            
            # Spliting input commands
            command_split = user_command.split()
            if len(command_split) == 0:
                continue
            # Recording user input commands (command history)
            self.commandList.append(user_command)

            if user_command == 'quit':
                # sending command 'quit' to server
                writer.write(user_command.encode())
                incoming_command = await reader.read(12000)
                # showing proper message to user coming from server and client
                print("\n Signal received: ", incoming_command.decode())
                print("Good Bye, Connection is closed.")
                writer.close()
                break












    if __name__ == "__main__":
        client = my_client()
        portNumber = 8080
        asyncio.run(client.client('127.0.0.1', portNumber))