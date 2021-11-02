from util.pergunta import pergunta
from util.leitura import le_lado, le_diagonal

def funcLosango():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Losango")

    pergunta()

    tipo = int(input("\nQual tipo deseja: "))

    if tipo == 1:
        lado = le_lado()

        perimetro = perimetro_losango(lado)

        print("\nO Perímetro do Losango é de: ", perimetro)
        
    elif tipo == 2:
        diagonal_menor = le_diagonal()
        diagonal_maior = le_diagonal()

        area = area_losango(diagonal_menor, diagonal_maior)

        print("\nA Área do Losango é de: ", area)

    print("\n-------------------------------------------------")


def perimetro_losango(lado):
    perimetro = 4 * lado
    return perimetro


def area_losango(diagonal_menor, diagonal_maior):
    area = (diagonal_maior * diagonal_menor) / 2
    return area