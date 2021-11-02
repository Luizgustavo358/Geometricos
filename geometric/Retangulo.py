from util.funcoesUteis import clear, le_base, le_altura, pergunta

def funcRetangulo():
    clear()

    print("\nVocê escolheu: Retangulo")
    
    pergunta()
    tipo = int(input("\nQual tipo deseja: "))

    clear()

    if tipo == 1:
        base = le_base()
        altura = le_altura()
        perimetro = perimetro_retangulo(base, altura)
        print("\nO Perímetro do Retangulo é de: ", perimetro)
        
    elif tipo == 2:
        base = le_base()
        altura = le_altura()
        area = area_retangulo(base, altura)
        print("\nA Área do Retangulo é de: ", area)

    print("\n-------------------------------------------------")


def perimetro_retangulo(base, altura):
    perimetro = 2 * (base + altura)
    return perimetro


def area_retangulo(base, altura):
    area = base * altura
    return area