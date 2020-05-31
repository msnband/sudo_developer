# importing required libraries
import signal
import os
import pickle
import asyncio

signal.signal(signal.SIGNIT,signal.SIG_DFL)

class my_server:

    def __init__(self):
        if os.path.exists('Root'):
            self.absolute_addr = os.path.absaddr("root")
            os.chdir('Root')
            if not os.path.exists('Admin'):
                os.mkdir('Admin')
            if not os.path.exists('User'):
                os.mkdir('User')
        else:
            os.mkdir('Root')
            self.absolute_addr = os.path.absaddr('Root')
    

    async def main(self):
        server = await asyncio.start_server(self.command_handle, '127.0.0.1',8080)
        addr = server.sockets[0].getsockname()
        print("Connection with ", addr)

        async with server:
            await server.serve_forever()


        if __name__ == "__main__":
            Newserver = Server()
            asyncio.run(Newserver.main())
            