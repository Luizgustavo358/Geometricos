from util.funcoesUteis import clear, le_base, le_lado, le_altura, pergunta_triagulo

def funcTriangulo():
    clear()

    print("\nVocê escolheu: Triangulo")
    
    pergunta_triagulo()
    tipo = int(input("\nQual tipo deseja: "))

    clear()
    
    if tipo == 1:
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()
        perimetro = perimetro_triangulo(lado1, lado2, base)
        print("\nO Perímetro do Triângulo é de: ", perimetro)
        
    elif tipo == 2:
        base = le_base()
        altura = le_altura()
        area = area_triangulo(base, altura)
        print("\nA Área do Triângulo é de: ", area)

    elif tipo == 3:
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()
        area = area_triangulo_heron(lado1, lado2, base)
        print("\nA Área do Triângulo é de: ", area)
    elif tipo == 4:
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()
        ladoT = tipo_triangulo(lado1, lado2, base)
        print("\nO Tipo de triangulo é: ", ladoT)

    print("\n-------------------------------------------------")


def perimetro_triangulo(lado1, lado2, base):
    return lado1 + lado2 + base


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_triangulo_heron(lado1, lado2, base):
    semiPerimetro = (lado1 + lado2 + base) / 2
    area = (semiPerimetro * (semiPerimetro - lado1) * (semiPerimetro - lado2) * (semiPerimetro - base)) ** (1 / 2.0)
    return area


def tipo_triangulo(lado1, lado2, base):
    tipo = ""

    if lado1 == lado2 and lado1 != base:
        tipo = "isosceles"
        return tipo
    elif lado1 != lado2 and lado1 != base and lado2 != base:
        tipo = "escaleno"
        return tipo
    else:
        tipo = "equilatero"
        return tipo