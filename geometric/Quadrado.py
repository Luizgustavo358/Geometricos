from math import sqrt
from util.funcoesUteis import le_lado, clear, pergunta

def funcQuadrado():
    clear()

    print("\nVocê escolheu: Quadrado")
    
    pergunta()
    tipo = int(input("\nQual tipo deseja: "))
   
    clear()

    if tipo == 1:
        lado = le_lado()
        perimetro = perimetro_quadrado(lado)
        print("\nO Perímetro do Quadrado é de: ", perimetro)
        
    elif tipo == 2:
        lado = le_lado()
        area = area_quadrado(lado)
        diagonal = diagonal_quadrado(lado)
        print("\nA Área do Quadrado é de: ", area)
        print("\nA Diagonal do Quadrado é de: ", diagonal)

    print("\n-------------------------------------------------")
    

def perimetro_quadrado(lado):
    return 4 * lado


def diagonal_quadrado(lado):
    return lado * sqrt(2)


def area_quadrado(lado):
    return lado ** 2