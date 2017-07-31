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

    def perimetro(self, lado1, lado2, base):
        # somando lados
        result = lado1 + lado2 + base
        return result
    # end perimetro()

    def area_triangulo(self, base, altura):
        # calculando a area
        area = (base * altura) / 2
        return area
    # end area_triangulo()
# end class Triangulo

''' Classe Triangulo '''
class Quadrado(object):
    # definir dados
# end class Quadrado

''' Classe Triangulo '''
class Retangulo(object):
    # definir dados
# end class Retangulo

''' Classe Triangulo '''
class Trapezio(object):
    # definir dados
# end class Trapezio

def apresentacao():
    print("")
# end apresentacao()

if __name__ == '__main__':

# end main