# работает!
import asyncio
import sys

# запуск сервера
async def run_server(host, port):
    # обработка входящих соединений
    server = await asyncio.start_server(serve_client, host, port)
    print(f'Server up, running, and waiting for call on {host}: {port}')
    await server.serve_forever()

# обработка входящих соединений
async def serve_client(reader, writer):
    global counter
    # номер подключенного клиента
    cid = counter
    # адрес подключенного клиента
    cli_address = (writer.get_extra_info('peername'))
    # добавляем адрес подключенного клиента в список подключенных клиентов
    cli_list.append(cli_address)
    print(f'Клиент #{cid} подключен')
    counter += 1  # Потоко-безопасно, так все выполняется в одном потоке

    # прием данных от клиента
    request = await read_request(reader, writer, cli_address, cid)
    if request is None:
        print(f'Клиент #{cid} неожиданно отключился.')
        cli_list.remove(cli_address)
    else:
        # обработка запросов клиента
        response = await handle_request(request)
        # отправка данных клиенту
        await write_response(writer, response, cid)

# прием данных от клиента
async def read_request(reader, writer, cli_address, cid, delimiter=b'!'):
    request = bytearray()
    # бесконечны цикл приема данных
    while True:
        # чтение строки
        chunk = await reader.readline()
        # убираем \r\n в конце приннимаемой строки
        chunk = chunk.rstrip()

        print('Получено %r от %r' % (chunk, cli_address))

        cli_echo(chunk, writer)

        if not chunk:
          # Клиент преждевременно отключился, переход к if request is None:
          break

        request += chunk
        if delimiter in request:
            print('read_request')
            return request

    return None

async def handle_request(request):
    print('handle_request')
    await asyncio.sleep(5)
    return request[::-1]

async def write_response(writer, response, cid):
    print('write_response')
    writer.write(response)
    await writer.drain()
    writer.close()
    print(f'Клиент #{cid} был обслужен')


def cli_echo(chunk, writer):
    return

# номер входяего клиента
counter = 0
# список адресов подключенных клиентов
cli_list = []

if __name__ == '__main__':
    asyncio.run(run_server('127.0.0.1', 8080))
