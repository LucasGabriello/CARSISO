import threading
import primos
import math

def minha_funcao():
    n=100
    for i in range(n):
        if primos.isPrimo(i) == True:
            print(i)
    print("Thread MINHA FUNCAO finalizada")

# Criação de uma instância de Thread
thread = threading.Thread(target=minha_funcao)
# Inicia a thread
thread.start()
# Espera pela thread terminar
thread.join()

print("Thread principal finalizada")