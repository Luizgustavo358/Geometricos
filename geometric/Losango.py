from util.funcoesUteis import pergunta, clear, le_lado, le_diagonal

def funcLosango():
    clear()

    print("\nVocê escolheu: Losango")

    pergunta()
    tipo = int(input("\nQual tipo deseja: "))

    clear()

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
    return 4 * lado


def area_losango(diagonal_menor, diagonal_maior):
    return (diagonal_maior * diagonal_menor) / 2