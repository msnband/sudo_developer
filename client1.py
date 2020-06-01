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















    if __name__ == "__main__":
        client = my_client()
        port = 8080
        asyncio.run(client.client('127.0.0.1', port))