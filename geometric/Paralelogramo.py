from util.pergunta import pergunta
from util.leitura import le_lado, le_base, le_altura

def funcParalelogramo():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Paralelogramo")

    pergunta()

    tipo = int(input("\nQual tipo deseja: "))

    if tipo == 1:
        lado1 = le_lado()
        lado2 = le_lado()

        perimetro = perimetro_paralelogramo(lado1, lado2)

        print("\nO Perímetro do Paralelogramo é de: ", perimetro)
        
    elif tipo == 2:
        base = le_base()
        altura = le_altura()

        area = area_paralelogramo(base, altura)

        print("\nA Área do Paralelogramo é de: ", area)

    print("\n-------------------------------------------------")


def perimetro_paralelogramo(lado_a, lado_b):
    return 2 * (lado_a + lado_b)


def area_paralelogramo(base, altura):
    return base * altura
