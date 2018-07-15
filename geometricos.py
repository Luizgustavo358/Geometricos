'''
    Nome do Programa: geometricos.py
    Autor: Luiz Gustavo Bragança dos Santos
    Objetivo: Calcula a Area e Perimetro de um Geometrico.
'''

# importando Classe
import math


''' Classe Triangulo '''
class Triangulo(object):

    #
    # Metodo que calcula o perimetro de um triangulo.
    # @param int lado1, lado2, base -> passados pelo usuario.
    # @return int result -> retorna o perimetro.
    #
    def perimetro_triangulo(self, lado1, lado2, base):
        # somando lados
        perimetro = lado1 + lado2 + base
        return perimetro
    # end perimetro_triangulo()


    #
    # Metodo que calcula a area de um triangulo.
    # @param int base, altura -> passados pelo usuario.
    # @return int area -> retorna a area.
    #
    def area_triangulo(self, base, altura):
        # calculando a area
        area = (base * altura) / 2
        return area
    # end area_triangulo()
# end class Triangulo


''' Classe Quadrado '''
class Quadrado(object):

    #
    #
    #
    def perimetro_quadrado(self, lado):
        # somando lados
        perimetro = 4 * lado
        return perimetro
    # end perimetro_quadrado()


    #
    #
    #
    def area_quadrado(self, lado):
        # achando a area
        area = lado ** 2
        return area
    # end area_quadrado()
# end class Quadrado


''' Classe Retangulo '''
class Retangulo(object):

    #
    #
    #
    def perimetro_retangulo(self, base, altura):
        # fazendo a soma dos lados
        perimetro = 2 * (base + altura)
        return perimetro
    # end perimetro_retangulo()


    #
    #
    #
    def area_retangulo(self, base, altura):
        # achando a area
        area = base * altura
        return area
    # end area_retangulo()
# end class Retangulo

''' Classe Trapezio '''
class Trapezio(object):

    #
    #
    #
    def perimetro_trapezio(self, base_maior, base_menor, lado1, lado2):
        # achando o perimetro do Trapezio
        perimetro = base_maior + base_menor + lado1 + lado2
        return perimetro
    # end perimetro_trapezio()

    
    #
    #
    #
    def area_trapezio(self, base_menor, base_maior, altura):
        # achando a area do Trapezio
        area = ((base_menor + base_maior) * altura) / 2
        return area
    # end area_trapezio()
# end class Trapezio

''' Classe Circulo '''
class Circulo(object):

    #
    #
    #
    def perimetro_circulo(self, raio):
        # achando o perimetro do Circulo
        perimetro = 2 * math.pi + raio
        return perimetro
    # end perimetro_circulo()


    #
    #
    #
    def area_circulo(self, raio):
        # achando a area do Circulo
        area = math.pi * (raio ** 2)
        return area
    # end area_circulo()
# end class Circulo


''' Classe Losango '''
class Losango(object):

    #
    #
    #
    def perimetro_losango(self, lado):
        # achando o perimetro do Losango
        perimetro = 4 * lado
        return perimetro
    # end perimetro_losango()


    #
    #
    #
    def area_losango(self):
        # achando a area do Losango
        area = (diagonal_maior * diagonal_menor) / 2
        return area
    # end area_losango()
# end class Losango

''' Classe Paralelogramo '''
class Paralelogramo(object):

    #
    #
    #
    def perimetro_paralelogramo(self, lado_a, lado_b):
        # achando o perimetro do Paralelogramo
        perimetro = 2 * (lado_a + lado_b)
        return perimetro
    # end perimetro_paralelogramo()


    #
    #
    #
    def area_paralelogramo(self):
        # achando area do Paralelogramo
        area = base * altura
        return area
    # end area_paralelogramo()
# end class Paralelogramo


# -------------------------------- Aqui comeca o programa


#
# Metodo de apresentacao.
#
def apresentacao():
    print("\n+----------------------------------------------+")
    print("|            Programa Feito em Python          |")
    print("+----------------------------------------------+")
    print("| Calcula a Area e Perimetro de um Geometrico  |")
    print("|            Feito por: Luiz Gustavo           |")
    print("+----------------------------------------------+\n")
# end apresentacao()


#
# Metodo que mostra as opcoes.
#
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


#
# Metodo que le as opcoes.
# @retun int opcao -> numero escolhido.
#
def le_opcao():
    opcao = int(input("\nEntre com um número: "))
    return opcao
# end le_opcao()


#
# Metodo escolhe a opcao.
# @param int opcao -> escolhida pelo usuario.
#
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


#
# Metodo que le a base de um geometrico.
# @return int base -> escolhida pelo usuario.
#
def le_base():
    base = int(input("\nQual a base: "))
    return base
# end le_base


#
# Metodo que le a Altura de um geometrico.
# @return int altura -> escolhida pelo usuario.
#
def le_altura():
    altura = int(input("\nQual é a altura: "))
    return altura
# end le_altura


#
# Metodo que le o lado de um geometrico.
# @return int lado -> escolhida pelo usuario.
#
def le_lado():
    lado = int(input("\nQual é o tamanho do lado: "))
    return lado
# end le_lado()


#
# Metodo que mostra as opcoes de calculo.
#
def pergunta():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área")
# end pergunta()


#
# Metodo para o triangulo, onde calcula e mostra o perimetro ou area.
#
def funcTriangulo():
    print("-------------------------------------------------")
    print("\nVocê escolheu: Triangulo")

    # instancia o objeto triangulo
    triangulo = Triangulo()

    # mostra as opcoes de calculo
    pergunta()

    # escolhe a opcao
    tipo = int(input("\nQual tipo deseja: "))

    # testa as opcoes
    if tipo == 1:
        # perimetro do triangulo
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()

        # calcula o perimetro
        perimetro = triangulo.perimetro_triangulo(lado1, lado2, base)

        # mostra o perimetro
        print("\nO Perímetro do Triângulo é de: ", perimetro)
        
    elif tipo == 2:
        # area do triangulo
        base = le_base()
        altura = le_altura()

        # calcula a area
        area = triangulo.area_triangulo(base, altura)

        # mostra a area
        print("\nA Área do Triângulo é de: ", area)
    # end if

    print("-------------------------------------------------")
# end funcTriangulo


#
# Metodo para o quadrado, onde calcula e mostra o perimetro ou area.
#
def funcQuadrado():
    print("Quadrado")
# end quadrado()


#
# Metodo para o retangulo, onde calcula e mostra o perimetro ou area.
#
def funcRetangulo():
    print("Retangulo")
# end retangulo()


#
# Metodo para o trapezio, onde calcula e mostra o perimetro ou area.
#
def funcTrapezio():
    print("Trapezio")
# end trapezio()


#
# Metodo para o circulo, onde calcula e mostra o perimetro ou area.
#
def funcCirculo():
    print("Circulo")
# end circulo()


#
# Metodo para o losango, onde calcula e mostra o perimetro ou area.
#
def funcLosango():
    print("Losango")
# end losango()


#
# Metodo para o paralelogramo, onde calcula e mostra o perimetro ou area.
#
def funcParalelogramo():
    print("Paralelogramo")
# end paralelogramo()


#
# Main.
#
if __name__ == '__main__':
    # apresentando programa
    apresentacao()

    # mostrando opcoes
    opcoes()

    # lendo opcao
    opcao = le_opcao()

    # roda ate a opcao ser igual a 0
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
