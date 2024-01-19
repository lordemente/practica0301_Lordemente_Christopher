import datetime


comienzo = datetime.datetime.now()
def recursiva(n):
    '''una función que reciba un número entero positivo n y calcule el
        número de fibonacci asociado a ese número de manera recursiva
        Parametros:
            n --> Introducida por el usuario'''
    if n <= 1:
        return 1
    else:
        return recursiva(n-1) + recursiva(n-2)
   
user = int(input("Número: "))
print(recursiva(user))




final = datetime.datetime.now()
print(final - comienzo)