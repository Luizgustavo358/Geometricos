from util.funcoesUteis import pergunta, clear, le_lado, le_apotema

def funcPentagono():
    clear()

    print("\nVocê escolheu: Pentagono")

    pergunta()
    tipo = int(input("\nQual tipo deseja: "))

    clear()

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
    return 5 * lado


def area_pentagono(lado, apotema):
    return (5 * lado) * apotema