import math
from util.funcoesUteis import pergunta, clear, le_raio

def funcCirculo():
    clear()

    print("\nVocê escolheu: Circulo")

    pergunta()
    tipo = int(input("\nQual tipo deseja: "))

    clear()

    if tipo == 1:
        raio = le_raio()
        perimetro = perimetro_circulo(raio)
        print("\nO Perímetro do Circulo é de: ", perimetro)
        
    elif tipo == 2:
        raio = le_raio()
        area = area_circulo(raio)
        print("\nA Área do Circulo é de: ", area)
    
    print("\n-------------------------------------------------")


def perimetro_circulo(raio):
    return 2 * math.pi + raio


def area_circulo(raio):
    return math.pi * (raio ** 2)