from util.funcoesUteis import clear, le_base, le_lado, le_altura, pergunta

def funcTrapezio():
    clear()

    print("\nVocê escolheu: Trapezio")
    
    pergunta()
    tipo = int(input("\nQual tipo deseja: "))

    clear()

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
