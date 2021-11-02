import math
from util.pergunta import pergunta
from util.leitura import le_lado

def funcDecagono():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Decagono")

    pergunta()

    tipo = int(input("\nQual tipo deseja: "))

    if tipo == 1:
        lado = le_lado()
        perimetro = perimetro_decagono(lado)
        print("\nO Perímetro do Decagono é de: ", perimetro)
        
    elif tipo == 2:
        lado = le_lado()
        area = area_decagono(lado)
        print("\nA Área do Decagono é de: ", area)
    
    print("\n-------------------------------------------------")


def perimetro_decagono(lado):
    perimetro = 10 * lado
    return perimetro
 

def area_decagono(lado):
    area = ((5 / 2) * math.pow(lado, 2)) * math.sqrt(5 + (2 * math.sqrt(5)))
    return area