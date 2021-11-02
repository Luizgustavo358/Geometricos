import math
from util.leitura import le_raio
from util.pergunta import pergunta

def funcCirculo():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Circulo")

    pergunta()

    tipo = int(input("\nQual tipo deseja: "))

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
    perimetro = 2 * math.pi + raio
    return perimetro


def area_circulo(raio):
    area = math.pi * (raio ** 2)
    return area