import math
def isPrimo (numero):
    if numero==2:
        return True
    if numero % 2 ==0:
        return False
    limite = math.ceil(math.sqrt(numero)+1)
    i=3
    while (i< limite):
        if numero%i==0:
            return False
        i = i + 2
    if numero==1:
        return False

    return True


