# SuperFastPython.com
# Sobreescrevendo a classe Thread
from time import sleep
from threading import Thread


class CustomThread(Thread):
    def run(self):
        sleep(5)
        print('Dentro do novo thread')


#programa
thread = CustomThread()
thread.start()
print('Main: Continuando a executar')
thread.join()