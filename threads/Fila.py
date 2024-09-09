import threading
import queue
import time

def produtor(fila):
    for i in range(200):
        time.sleep(200)  # Simula algum trabalho
        mensagem = "Mensagem {i}"
        fila.put(mensagem)
        print("Produzido: {mensagem}")
def consumidor(fila):
    while True:
        mensagem = fila.get()
        print("Consumido: {mensagem}")
        fila.task_done()
fila = queue.Queue
produtor_thread = threading.Thread(target=produtor, args=(fila,))
consumidor_thread = threading.Thread(target=consumidor, args=(fila,))
produtor_thread.start()
consumidor_thread.start()
produtor_thread.join()
consumidor_thread.join()
print("Threads finalizadas")