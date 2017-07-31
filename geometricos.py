'''
    Nome do Programa: area_de_geometricos.py
    Autor: Luiz Gustavo Bragança dos Santos
    Objetivo: Faz a soma dos lados dos geometricos e faz a area.
'''

''' Classe Triangulo '''
class Triangulo(object):

    # definir dados
    base = None
    altura = None
    lado1 = None
    lado2 = None

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

    def perimetro_retangulo(self, base, altura):
        # fazendo a soma dos lados
        perimetro = 2 * (base + altura)
        return perimetro
    # end perimetro_retangulo()
# end class Retangulo

''' Classe Trapezio '''
class Trapezio(object):
    # definir dados
# end class Trapezio

def apresentacao():
    print("")
# end apresentacao()

if __name__ == '__main__':

# end main