"""This module contains all classes and functions required in the task."""
#importing required libraries.
import signal
import asyncio
#press Ctrl + C to stop connection.
signal.signal(signal.SIGINT, signal.SIG_DFL) 
class my_client:
    """ The class "my_client" is designed to connect client to 
    server and handling some commands which asked in the task."""
    def __init__(self):
        """ Initializing a list to record user inputs commands."""
        self.commandList = [] 
    async def client(self, address, portNumber):
        """ Main function in client to establish connection with server and handling
        some required commands """
        #check and return proper error if IP is not valid.
        for j in address:
            assert(j.isnumeric() or j == "."), \
                " The IP contains wrong or invalid charachters"
        #Check the port number wether in specific range or not.
        assert 1023 < portNumber < 65535, "Port number is out of range!"
        #Establish a TCP connection to server
        reader, writer = await asyncio.open_connection(address, portNumber)
        #assert proper error if TCP connection has problem.
        assert isinstance(reader, asyncio.streams.StreamReader),\
             "Streamreader on server is not working (message from client)"
        assert isinstance(writer, asyncio.streams.StreamWriter),\
             "Streamwriter on server is not working (message from client)"
        #Client starting text...
        print("\n insert command 'register' or 'login' to access the server")
        while True:
            user_command = input("\n Client is waiting...\n")
            user_command = user_command.strip()
            #pliting input commands
            command_split = user_command.split()
            if len(command_split) == 0:
                continue
            #Recording user input commands (command history)
            self.commandList.append(user_command)
            #implementing 'quit' command.
            if user_command == 'quit':
                #sending command 'quit' to server
                writer.write(user_command.encode())
                incoming_command = await reader.read(12000)
                #showing proper message to user coming from server and client
                print(f"\n Signal received: {incoming_command.decode()}")
                print("Good Bye, Connection is closed.")
                writer.close()
                break
            #implementing 'commands' command.
            if user_command == 'commands':
                #list of available commands
                list_of_commands = """
                    service commands:                                    Description & Option

                change_folder <name>                            Change the current working directory to required directory.
                list                                            Show all files and folders in current working directory.
                read_file <name>                                Read the given name data from the file in current director.
                write_file <name> <input>                       Write data the end of given name file.
                create_folder <name>                            Creating the given name folder in current directory.
                register <username> <password> <privileges>     Register a new username with specific accesibility.
                login <username> <password>                     Login with registered username and password to its own directory.
                delete <username> <password>                    Delete the given username and password.
                """
                print(f">> {list_of_commands} << ")
                continue               
            #implementing 'issued & clear' options for 'commands'.
            if command_split[0] == "commands":
                if command_split[1] == "issued":
                    print("\n\t\t List of commands issued are: ")
                    for comd in self.commandList:
                        print(f"\t\t\n{comd}")
                if command_split[1] == 'clear':
                    self.commandList = []
                    print('\nHistory removed successfully')
                continue
            print("Command sent: ", user_command)
            writer.write(user_command.encode())
            incoming_command = await reader.read(12000)
            print("\nCommand received: \n\n ", incoming_command.decode())

if __name__ == "__main__":
    #creating object from 'my_client'.
    client = my_client()
    asyncio.run(client.client('127.0.0.1', 8080))
