import cProfile


def DNI(archivo):
    import csv
    diccionario = {}
    letra = list("TRWAGMYFPDXBNJZSQVHLCKE")
    resto = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22


    for j in range(len(letra)):
        diccionario[resto[j]] = letra[j]


    if archivo == "50" or archivo == "1000":
        with open(f"{archivo}.csv") as file:
            lectura = csv.reader(file)
            for i in lectura:
                letra_numero = int(i[1]) % 23
                print(f"Nombre: {i[0].capitalize():35} DNI: {i[1]}{diccionario[letra_numero]}")
    else:
        print("Solo hay 2 archivos disponibles --> nombre: '50'   o   '1000'")


# user = input("Ingresa el nombre del archivo: ")
# DNI(user)
       
cProfile.run("DNI('archivo')")


# cProfile.run("DNI('50')", sort="time")
# cProfile.run("DNI('archivo')", sort= "cumtime")








