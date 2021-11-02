import math
from util.funcoesUteis import pergunta, clear, le_lado

def funcOctogono():
    clear()

    print("\nVocê escolheu: Octogono")

    pergunta()
    tipo = int(input("\nQual tipo deseja: "))

    clear()

    if tipo == 1:
        lado = le_lado()
        perimetro = perimetro_octogono(lado)
        print("\nO Perímetro do octogono é de: ", perimetro)
        
    elif tipo == 2:
        lado = le_lado()
        area = area_octogono(lado)
        print("\nA Área do octogono é de: ", area)
    
    print("\n-------------------------------------------------")


def perimetro_octogono(lado):
    return lado * 8


def area_octogono(lado):
    area = 2 * lado**2 * (1 + math.sqrt(2))
    return area