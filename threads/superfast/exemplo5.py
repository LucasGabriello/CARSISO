# SuperFastPython.com
# exemplo (mutex) lock
from math import ceil
from time import sleep
from random import random
from threading import Thread
from threading import Lock

def task(lock, identifier, value):
    with lock:
        print(f'>thread {identifier} entrou em LOCK, dormindo por {value} segundos')
        sleep(value)

#programa
lock = Lock()
for i in range(10):
    t= ceil(random() * 3)
    Thread(target=task, args=(lock, i, t )).start()

