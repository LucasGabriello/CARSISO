import random
import threading
import queue
from time import sleep

def gerar_cpf():
    #9 dígitos aleatorios
    primeiros_digitos = [random.randint(0, 9) for _ in range(9)]

    #Calcula primeiro erificador
    soma = sum([(i+2) * d for i, d in enumerate(reversed(primeiros_digitos))])
    resto = soma % 11
    digito1 = 11 - resto if resto < 2 else 0

    #Calcula segundo verificador
    soma = sum([(i+2) * d for i, d in enumerate(reversed(primeiros_digitos + [digito1]))])
    resto = soma % 11
    digito2 = 11 - resto if resto < 2 else 0

    # Formatar o CPF
    cpf = f"{primeiros_digitos[0:3]}.{primeiros_digitos[3:6]}.{primeiros_digitos[6:9]}-{digito1}{digito2}"
    # cpf = f"{primeiros_digitos[0:3]}{primeiros_digitos[3:6]}{primeiros_digitos[6:9]}{digito1}{digito2}"
    return cpf

def validar_cpf(cpf):
    # Remove caracteres especiais??? (remover formatação do gerar cpf)
    cpf = [int(d) for d in cpf if d.isdigit()]

    #confirmar 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum([(i+2) * d for i, d in enumerate(reversed(cpf[:-2]))])
    resto = soma % 11
    digito1 = 11 - resto if resto < 2 else 0

    # Calcula o segundo dígito verificador
    soma = sum([(i+2) * d for i, d in enumerate(reversed(cpf[:-1]))])
    resto = soma % 11
    digito2 = 11 - resto if resto < 2 else 0

    # Compara os dígitos verificadores calculados com os dígitos do CPF
    return digito1 == cpf[-2] and digito2 == cpf[-1]

def gerar_cpfs(queue):
    for _ in range(1000):
        cpf = gerar_cpf()
        queue.put(cpf)
    # Flag não há mais itens
    queue.put(None)

def validar_cpfs(queue):
    while True:
        cpf = queue.get()
        if cpf is None:
            # Flag fim do processamento
            queue.put(None)
            break
        if validar_cpf(cpf):
            print(f"CPF válido: {cpf}")
        else:
            print(f"CPF inválido: {cpf}")

if __name__ == "__main__":
    q = queue.Queue()

    #Cria threads
    thread_gerador = threading.Thread(target=gerar_cpfs, args=(q,))
    thread_validador = threading.Thread(target=validar_cpfs, args=(q,))

    #inicia threads
    thread_gerador.start()
    thread_validador.start()

    #Espera até o fim
    thread_gerador.join()
    thread_validador.join()
