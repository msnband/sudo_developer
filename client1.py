# importing required libraries

import signal
import asyncio

signal.signal(signal.SIGINT, signal.SIG_DFL) # press Ctrl + C to stop client

class my_client:


















    if __name__ == "__main__":
        client = my_client()
        port = 8080
        asyncio.run(client.client('127.0.0.1', port))