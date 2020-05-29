import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8080)
    message =''
    data = await reader.read(10000)
    print(f'Received: {data.decode()}')

    while True:
        data = await reader.read(10000)
        print(f'Received: {data.decode()}')
        # message = input('[Enter Message]\n')
        message = await user_input(writer)
        continue

        if message == 'exit':
            break

        # writer.write(message.encode())
        

    print('Close the connection')
    writer.close()

async def user_input(writer):
    message = input()
    writer.write(message.encode())
    return message

asyncio.run(tcp_echo_client())