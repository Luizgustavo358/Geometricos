'''
    Nome do Programa: geometricos.py
    Autor: Luiz Gustavo Bragança dos Santos
    Autor: Ricardo Xavier Sena
    Objetivo: Calcula a Area e Perimetro de um Geometrico.
'''

# importando Classe
import math


''' Classe Triangulo '''
class Triangulo(object):

    #
    # Metodo que calcula o perimetro de um triangulo.
    # @param lado1, lado2, base -> passados pelo usuario.
    # @return perimetro -> retorna o perimetro.
    #
    def perimetro_triangulo(self, lado1, lado2, base):
        # somando lados
        perimetro = lado1 + lado2 + base
        return perimetro
    # end perimetro_triangulo()


    #
    # Metodo que calcula a area de um triangulo.
    # @param base, altura -> passados pelo usuario.
    # @return area -> retorna a area.
    #
    def area_triangulo(self, base, altura):
        # calculando a area
        area = (base * altura) / 2
        return area
    # end area_triangulo()

    #
    # Metodo que classifica triangulos.
    # @param base, altura -> passados pelo usuario.
    # @return tipo -> qual o tipo de triangulo temos.
    #
    def tipo_triangulo(self, lado1, lado2, base):
        tipo = ""

        # se for isosceles 
        if lado1 == lado2 and lado1 != base
            tipo = "isosceles"
            return tipo
        # se for escaleno    
        if else lado1 != lado2 and lado1 != base and lado2 != base
            tipo = "escaleno"
            return tipo
        else
            tipo = equilatero
            return tipo
    # end tipo_triangulo()


# end class Triangulo


''' Classe Quadrado '''
class Quadrado(object):

    #
    # Metodo que calcula o perimetro de um quadrado.
    # @param lado -> passado pelo usuario.
    # @return perimetro -> retorna o perimetro.
    #
    def perimetro_quadrado(self, lado):
        # somando lados
        perimetro = 4 * lado
        return perimetro
    # end perimetro_quadrado()


    #
    # Metodo que calcula a area de um quadrado.
    # @param lado -> passado pelo usuario.
    # @return area -> retorna a area.
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
    # Metodo que calcula o perimetro de um retangulo.
    # @param base, altura -> passados pelo usuario.
    # @return perimetro -> retorna o perimetro.
    #
    def perimetro_retangulo(self, base, altura):
        # fazendo a soma dos lados
        perimetro = 2 * (base + altura)
        return perimetro
    # end perimetro_retangulo()


    #
    # Metodo que calcula a area de um retangulo.
    # @param base, altura -> passados pelo usuario.
    # @return area -> retorna a area.
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
    # Metodo que calcula o perimetro de um trapezio.
    # @param base_menor, base_maior, lado1, lado2 -> passados pelo usuario.
    # @return perimetro -> retorna o perimetro.
    #
    def perimetro_trapezio(self, base_maior, base_menor, lado1, lado2):
        # achando o perimetro do Trapezio
        perimetro = base_maior + base_menor + lado1 + lado2
        return perimetro
    # end perimetro_trapezio()

    
    #
    # Metodo que calcula a area de um trapezio.
    # @param base_menor, base_maior, altura -> passados pelo usuario.
    # @return area -> retorna a area.
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
    # Metodo que calcula o perimetro de um circulo.
    # @param raio -> passado pelo usuario.
    # @return perimetro -> retorna o perimetro.
    #
    def perimetro_circulo(self, raio):
        # achando o perimetro do Circulo
        perimetro = 2 * math.pi + raio
        return perimetro
    # end perimetro_circulo()


    #
    # Metodo que calcula a area de um circulo.
    # @param raio -> passado pelo usuario.
    # @return area -> retorna a area.
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
# @retun opcao -> numero escolhido.
#
def le_opcao():
    opcao = int(input("\nEntre com um número: "))
    return opcao
# end le_opcao()


#
# Metodo escolhe a opcao.
# @param opcao -> escolhida pelo usuario.
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
# @return base -> escolhida pelo usuario.
#
def le_base():
    base = int(input("\nQual a base: "))
    return base
# end le_base


#
# Metodo que le a Altura de um geometrico.
# @return altura -> escolhida pelo usuario.
#
def le_altura():
    altura = int(input("\nQual é a altura: "))
    return altura
# end le_altura


#
# Metodo que le o lado de um geometrico.
# @return lado -> escolhida pelo usuario.
#
def le_lado():
    lado = int(input("\nQual é o tamanho do lado: "))
    return lado
# end le_lado()


#
# Metodo que le o raio de um geometrico.
# @return raio -> escolhida pelo usuario.
#
def le_raio():
    raio = int(input("\nQual é o raio: "))
    return raio
# end le_raio()

#
# Metodo que mostra as opcoes de calculo.
#
def pergunta():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área")
    print("3 - Tipo Triangulo")
# end pergunta()


#
# Metodo para o triangulo, onde calcula e mostra o perimetro ou area.
#
def funcTriangulo():
    print("\n-------------------------------------------------")
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
    elif tipo == 3:
        #ler todos lados
        base = le_base()
        lado1 = le_lado()
        lado2 = le_lado()

        #descobrir o lado
        ladoT - triangulo.tipo_triangulo(lado1, lado2, base)

        #mostra lado
        print("\nO Tipo de triangulo é: ", ladoT)
    # end if

    print("\n-------------------------------------------------")
# end funcTriangulo


#
# Metodo para o quadrado, onde calcula e mostra o perimetro ou area.
#
def funcQuadrado():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Quadrado")

    # instancia o objeto quadrado
    quadrado = Quadrado()

    # mostra as opcoes de calculo
    pergunta()

    # escolhe a opcao
    tipo = int(input("\nQual tipo deseja: "))

    # testa as opcoes
    if tipo == 1:
        # perimetro do quadrado
        lado = le_lado()

        # calcula o perimetro
        perimetro = quadrado.perimetro_quadrado(lado)

        # mostra o perimetro
        print("\nO Perímetro do Quadrado é de: ", perimetro)
        
    elif tipo == 2:
        # area do quadrado
        lado = le_lado()

        # calcula a area
        area = quadrado.area_quadrado(lado)

        # mostra a area
        print("\nA Área do Quadrado é de: ", area)
    # end if

    print("\n-------------------------------------------------")
# end funcQuadrado()


#
# Metodo para o retangulo, onde calcula e mostra o perimetro ou area.
#
def funcRetangulo():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Retangulo")

    # instancia o objeto retangulo
    retangulo = Retangulo()

    # mostra as opcoes de calculo
    pergunta()

    # escolhe a opcao
    tipo = int(input("\nQual tipo deseja: "))

    # testa as opcoes
    if tipo == 1:
        # perimetro do quadrado
        base = le_base()
        altura = le_altura()

        # calcula o perimetro
        perimetro = retangulo.perimetro_retangulo(base, altura)

        # mostra o perimetro
        print("\nO Perímetro do Retangulo é de: ", perimetro)
        
    elif tipo == 2:
        # area do quadrado
        base = le_base()
        altura = le_altura()

        # calcula a area
        area = retangulo.area_retangulo(base, altura)

        # mostra a area
        print("\nA Área do Retangulo é de: ", area)
    # end if

    print("\n-------------------------------------------------")
# end retangulo()


#
# Metodo para o trapezio, onde calcula e mostra o perimetro ou area.
#
def funcTrapezio():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Trapezio")

    # instancia o objeto trapezio
    trapezio = Trapezio()

    # mostra as opcoes de calculo
    pergunta()

    # escolhe a opcao
    tipo = int(input("\nQual tipo deseja: "))

    # testa as opcoes
    if tipo == 1:
        # perimetro do quadrado
        base_maior = le_base()
        base_menor = le_base()
        lado1 = le_lado()
        lado2 = le_lado()

        # calcula o perimetro
        perimetro = trapezio.perimetro_trapezio(base_maior, base_menor, lado1, lado2)

        # mostra o perimetro
        print("\nO Perímetro do Trapezio é de: ", perimetro)
        
    elif tipo == 2:
        # area do quadrado
        base_maior = le_base()
        base_menor = le_base()
        altura = le_altura()

        # calcula a area
        area = trapezio.area_trapezio(base_maior, base_menor, altura)

        # mostra a area
        print("\nA Área do Trapezio é de: ", area)
    # end if

    print("\n-------------------------------------------------")
# end trapezio()


#
# Metodo para o circulo, onde calcula e mostra o perimetro ou area.
#
def funcCirculo():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Circulo")

    # instancia o objeto trapezio
    circulo = Circulo()

    # mostra as opcoes de calculo
    pergunta()

    # escolhe a opcao
    tipo = int(input("\nQual tipo deseja: "))

    # testa as opcoes
    if tipo == 1:
        # perimetro do circulo
        raio = le_raio()

        # calcula o perimetro
        perimetro = circulo.perimetro_circulo(raio)

        # mostra o perimetro
        print("\nO Perímetro do Circulo é de: ", perimetro)
        
    elif tipo == 2:
        # area do quadrado
        raio = le_raio()

        # calcula a area
        area = circulo.area_circulo(raio)

        # mostra a area
        print("\nA Área do Circulo é de: ", area)
    # end if

    print("\n-------------------------------------------------")
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
