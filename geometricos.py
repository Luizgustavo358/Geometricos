'''
    Nome do Programa: geometricos.py
    Autor: Luiz Gustavo Bragança dos Santos
    Objetivo: Faz a soma dos lados dos geometricos e faz a area.
'''

# importando Classe
import math


''' Classe Triangulo '''
class Triangulo(object):

    def perimetro_triangulo(self, lado1, lado2, base):
        # somando lados
        result = lado1 + lado2 + base
        return result
    # end perimetro_triangulo()


    def area_triangulo(self, base, altura):
        # calculando a area
        area = (base * altura) / 2
        return area
    # end area_triangulo()
# end class Triangulo


''' Classe Quadrado '''
class Quadrado(object):

    # definir dados
    lado = None


    def __init__(lado):
        self.lado = lado
    # end construtor


    def perimetro_quadrado(self, lado):
        # somando lados
        perimetro = 4 * lado
        return perimetro
    # end perimetro_quadrado()


    def area_quadrado(self, lado):
        # achando a area
        area = lado ** 2
        return area
    # end area_quadrado()
# end class Quadrado


''' Classe Retangulo '''
class Retangulo(object):

    # definir dados
    base = None
    altura = None


    def __init__(base, altura):
        self.base = base
        self.altura = altura
    # end construtor


    def perimetro_retangulo(self, base, altura):
        # fazendo a soma dos lados
        perimetro = 2 * (base + altura)
        return perimetro
    # end perimetro_retangulo()


    def area_retangulo(self, base, altura):
        # achando a area
        area = base * altura
        return area
    # end area_retangulo()
# end class Retangulo

''' Classe Trapezio '''
class Trapezio(object):

    # definir dados
    base_maior = None
    base_menor = None
    altura = None


    def __init__(base_maior, base_menor, altura):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura
    # end construtor


    def perimetro_trapezio(self, base_maior, base_menor, lado1, lado2):
        # achando o perimetro do Trapezio
        perimetro = base_maior + base_menor + lado1 + lado2
        return perimetro
    # end perimetro_trapezio()


    def area_trapezio(self, base_menor, base_maior, altura):
        # achando a area do Trapezio
        area = ((base_menor + base_maior) * altura) / 2
        return area
    # end area_trapezio()
# end class Trapezio

''' Classe Circulo '''
class Circulo(object):

    # definir dados
    raio = None


    def __init__(lado):
        self.lado = lado
    # end construtor


    def perimetro_circulo(self, raio):
        # achando o perimetro do Circulo
        perimetro = 2 * math.pi + raio
        return perimetro
    # end perimetro_circulo()


    def area_circulo(self, raio):
        # achando a area do Circulo
        area = math.pi * (raio ** 2)
        return area
    # end area_circulo()
# end class Circulo


''' Classe Losango '''
class Losango(object):

    # definir dados
    lado = None
    diagonal_maior = None
    diagonal_menor = None


    def __init__(lado, diagonal_maior, diagonal_menor):
        self.lado = lado
        self.diagonal_maior = diagonal_maior
        self.diagonal_menor = diagonal_menor
    # end construtor


    def perimetro_losango(self, lado):
        # achando o perimetro do Losango
        perimetro = 4 * lado
        return perimetro
    # end perimetro_losango()


    def area_losango(self):
        # achando a area do Losango
        area = (diagonal_maior * diagonal_menor) / 2
        return area
    # end area_losango()
# end class Losango

''' Classe Paralelogramo '''
class Paralelogramo(object):

    # definir dados
    lado_a = None
    lado_b = None
    base = None
    altura = None


    def __init__(lado_a, lado_b, base, altura):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.base = base
        self.altura = altura
    # end construtor


    def perimetro_paralelogramo(self, lado_a, lado_b):
        # achando o perimetro do Paralelogramo
        perimetro = 2 * (lado_a + lado_b)
        return perimetro
    # end perimetro_paralelogramo()


    def area_paralelogramo(self):
        # achando area do Paralelogramo
        area = base * altura
        return area
    # end area_paralelogramo()
# end class Paralelogramo


# -------------------------------- Aqui comeca o programa


def apresentacao():
    print("\n+----------------------------------------------+")
    print("|            Programa Feito em Python          |")
    print("+----------------------------------------------+")
    print("| Calcula a Area e Perimetro de um Geometrico  |")
    print("|            Feito por: Luiz Gustavo           |")
    print("+----------------------------------------------+\n")
# end apresentacao()


def opcoes():
    print("\n0 - Sair")
    print("1 - Triangulo")
    print("2 - Quadrado")
    print("3 - Retangulo")
    print("4 - Trapezio")
    print("5 - Circulo")
    print("6 - Losango")
    print("7 - Paralelogramo")
# end opcoes()


def le_opcao():
    opcao = int(input("\nEntre com um número: "))
    return opcao
# end le_opcao()


def escolhe_opcao(opcao):
    if opcao == 1:
        funcTriangulo()
    elif opcao == 2:
        funcQuadrado()
    elif opcao == 3:
        funcRetangulo()
    elif opcao == 4:
        funcTrapezio()
    elif opcao == 5:
        funcCirculo()
    elif opcao == 6:
        funcLosango()
    elif opcao == 7:
        funcParalelogramo()        
    # end if
# end escolhe_opcao()


def funcTriangulo():
    print("-------------------------------------------------")
    print("\nVocê escolheu: Triangulo")

    pergunta()

    tipo = int(input("\nQual tipo deseja: "))

    if tipo == 1:
        # perimetro do triangulo
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()

        triangulo = Triangulo()

        # calcula
        perimetro = triangulo.perimetro_triangulo(lado1, lado2, base)

        # mostra o perimetro
        print("\nO Perímetro do Triângulo é de: ", perimetro)
        
    elif tipo == 2:
        # area do triangulo
        base = le_base()
        altura = le_altura()

        # calcula
        area = triangulo.area_triangulo(base, altura)

        # mostra o perimetro
        print("\nA Área do Triângulo é de: ", area)
    # end if

    print("-------------------------------------------------")
# end funcTriangulo


def le_base():
    base = int(input("\nQual a base: "))
    return base
# end le_base

def le_altura():
    altura = int(input("\nQual é a altura: "))
    return altura
# end le_altura


def le_lado():
    lado = int(input("\nQual é o tamanho do lado: "))
    return lado
# end le_lado()


def pergunta():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área")
# end pergunta()


def quadrado():
    print("Quadrado")
# end quadrado()


def retangulo():
    print("Retangulo")
# end retangulo()


def trapezio():
    print("Trapezio")
# end trapezio()


def circulo():
    print("Circulo")
# end circulo()


def losango():
    print("Losango")
# end losango()


def paralelogramo():
    print("Paralelogramo")
# end paralelogramo()


if __name__ == '__main__':
    # apresentando programa
    apresentacao()

    # mostrando opcoes
    opcoes()

    # lendo opcao
    opcao = le_opcao()

    while opcao != 0:
        # escolhendo opcao
        escolhe_opcao(opcao)

        # mostrando opcoes
        opcoes()

        # lendo opcoes
        opcao = le_opcao()
    # end while
    
    print("\nVocê Saiu :(\n")
# end main
