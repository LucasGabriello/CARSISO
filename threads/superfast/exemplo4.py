# SuperFastPython.com
#  passando função com argumentos
from time import sleep
from threading import Thread


def task(sleep_time, message):
    sleep(sleep_time)
    print(message)


thread = Thread(target=task, args=(1.5, 'Mensagem do thread novo'))
thread.start()
print('Esperando o thread..')
thread.join()