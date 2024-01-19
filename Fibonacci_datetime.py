import datetime


inicio = datetime.datetime.now()


def finbonacci(n):
    '''una función que reciba un número entero positivo n y calcule el
        número de fibonacci asociado a ese número con bucles.
        Parametros:
            n --> Introducida por el usuario'''
   
    v1 = 0
    v2 = 1
    lista = [v1,v2]
    for i in range(n-1):
        r3 = v1 + v2
        lista.append(r3)
        v1 = v2
        v2 = r3
    numero = lista[n]
    return f'{lista}\n{numero}'
 
n = int(input("Número: "))
print(finbonacci(n))
   
fin = datetime.datetime.now()
print(fin - inicio)