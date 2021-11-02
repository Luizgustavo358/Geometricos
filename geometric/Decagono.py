import math
from util.funcoesUteis import pergunta, clear, le_lado

def funcDecagono():
    clear()

    print("\nVocê escolheu: Decagono")

    pergunta()

    tipo = int(input("\nQual tipo deseja: "))

    clear()

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
    return 10 * lado
 

def area_decagono(lado):
    return ((5 / 2) * math.pow(lado, 2)) * math.sqrt(5 + (2 * math.sqrt(5)))