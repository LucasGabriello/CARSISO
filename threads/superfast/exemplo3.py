# SuperFastPython.com
#Retornando valores do thread
from time import sleep
from threading import Thread


# custom thread class
class CustomThread(Thread):
    def run(self):
        sleep(5)
        print('Dentro do novo thread')
        self.value = 99


#programa
thread = CustomThread()
thread.start()
print('Esperando o thread terminar')
thread.join()
# get the value returned from run
value = thread.value
print(f'VALUE: {value}')