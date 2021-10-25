from util.leitura import le_base, le_lado, le_altura

def pergunta_triagulo():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área(Base/Altura)")
    print("3 - Área(Lado A, Lado B e Base)")
    print("4 - Tipo de Triangulo")


def funcTriangulo():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Triangulo")
    
    pergunta_triagulo()

    tipo = int(input("\nQual tipo deseja: "))

    if tipo == 1:
        # perimetro do triangulo
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()

        # calcula o perimetro
        perimetro = perimetro_triangulo(lado1, lado2, base)

        # mostra o perimetro
        print("\nO Perímetro do Triângulo é de: ", perimetro)
        
    elif tipo == 2:
        # area do triangulo
        base = le_base()
        altura = le_altura()

        # calcula a area
        area = area_triangulo(base, altura)

        # mostra a area
    
        print("\nA Área do Triângulo é de: ", area)

    elif tipo == 3:
        #ler todos lados
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()

        # calcula a area
        area = area_triangulo_heron(lado1, lado2, base)

        # mostra a area
    
        print("\nA Área do Triângulo é de: ", area)
    elif tipo == 4:
        #ler todos lados
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()

        #descobrir o lado
        ladoT = tipo_triangulo(lado1, lado2, base)

        #mostra lado
        print("\nO Tipo de triangulo é: ", ladoT)

    print("\n-------------------------------------------------")


def perimetro_triangulo(lado1, lado2, base):
    # somando lados
    perimetro = lado1 + lado2 + base
    return perimetro


def area_triangulo(base, altura):
    # calculando a area
    area = (base * altura) / 2
    return area


def area_triangulo_heron(lado1, lado2, base):
    semiPerimetro = (lado1 + lado2 + base)/2
    area = (semiPerimetro*(semiPerimetro-lado1)*(semiPerimetro-lado2)*(semiPerimetro-base))**(1/2.0)
    return area


def tipo_triangulo(lado1, lado2, base):
    tipo = ""

    # se for isosceles 
    if lado1 == lado2 and lado1 != base:
        tipo = "isosceles"
        return tipo
    # se for escaleno    
    elif lado1 != lado2 and lado1 != base and lado2 != base:
        tipo = "escaleno"
        return tipo
    else:
        tipo = "equilatero"
        return tipo