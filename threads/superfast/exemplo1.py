# SuperFastPython.com
#Exemplo usando JOIN
from time import sleep
from threading import Thread

def tarefa():
    print('Dentro do novo thread')
    sleep(5) # espera cinco segundos
    print('Terminei o novo thread')

# programa
thread = Thread(target=tarefa)
print('Dentro do thread MAIN...')
thread.start()
thread.join() # comente essa linha para ver a diferença na ordem das mensagens
print('Main: Terminei thread MAIN')