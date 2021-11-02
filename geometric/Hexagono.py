import math
from util.funcoesUteis import pergunta, clear, le_lado

def funcHexagono():
    clear()

    print("\nVocê escolheu: Hexagono")

    pergunta()
    tipo = int(input("\nQual tipo deseja: "))

    clear()

    if tipo == 1:
        lado = le_lado()
        perimetro = perimetro_hexagono(lado)
        print("\nO Perímetro do Hexagono é de: ", perimetro)
        
    elif tipo == 2:
        lado = le_lado()
        area = area_hexagono(lado)
        print("\nA Área do Hexagono é de: ", area)

    print("\n-------------------------------------------------")


def perimetro_hexagono(lado):
    return lado * 6

def area_hexagono(lado):
    cateto = lado/2
    h = (lado ** 2) - (cateto ** 2)
    h = math.sqrt(h)
    area = (h * cateto) * 6
    return area