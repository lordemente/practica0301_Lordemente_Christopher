import cProfile

def file():
    import csv
    dicionario = {}
    letra = list("TRWAGMYFPDXBNJZSQVHLCKE")
    resto = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22

    for j in range(len(letra)):
        dicionario[resto[j]] = letra[j]

    with open("50.csv") as file:
        lectura = csv.reader(file)
        for i in lectura:
            letra_numero = int(i[1]) % 23
            # print(f"Nombre: {i[0].capitalize():35} DNI: {i[1]}{dicionario[letra_numero]}")

cProfile.run("file()")
