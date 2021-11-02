from util.pergunta import pergunta
from util.leitura import le_lado, le_apotema

def funcPentagono():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Pentagono")

    pergunta()

    tipo = int(input("\nQual tipo deseja: "))

    if tipo == 1:
        lado = le_lado()

        perimetro = perimetro_pentagono(lado)

        print("\nO Perímetro do Pentagono é de: ", perimetro)
        
    elif tipo == 2:
        lado = le_lado()
        apotema = le_apotema()

        area = area_pentagono(lado,apotema)

        print("\nA Área do Pentagono é de: ", area)

    print("\n-------------------------------------------------")


def perimetro_pentagono(lado):
    perimetro = 5 * lado
    return perimetro


def area_pentagono(lado, apotema):
    area = (5* lado) * apotema
    return area