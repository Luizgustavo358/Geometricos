from util.leitura import le_base, le_lado, le_altura

def pergunta():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área")


def funcTrapezio():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Trapezio")

    # mostra as opcoes de calculo
    pergunta()

    tipo = int(input("\nQual tipo deseja: "))

    if tipo == 1:
        base_maior = le_base()
        base_menor = le_base()
        lado1 = le_lado()
        lado2 = le_lado()

        perimetro = perimetro_trapezio(base_maior, base_menor, lado1, lado2)

        print("\nO Perímetro do Trapezio é de: ", perimetro)
        
    elif tipo == 2:
        base_maior = le_base()
        base_menor = le_base()
        altura = le_altura()

        area = area_trapezio(base_maior, base_menor, altura)

        print("\nA Área do Trapezio é de: ", area)
    
    print("\n-------------------------------------------------")


def perimetro_trapezio(base_maior, base_menor, lado1, lado2):
    return base_maior + base_menor + lado1 + lado2
   
    
def area_trapezio(base_menor, base_maior, altura):
    return ((base_menor + base_maior) * altura) / 2
