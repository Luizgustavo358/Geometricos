from util.leitura import le_base, le_lado, le_altura

''' Classe Quadrado '''
class Quadrado(object):

    # Metodo que calcula o perimetro de um quadrado.
    # @param lado -> passado pelo usuario.
    # @return perimetro -> retorna o perimetro.
    #
    def perimetro_quadrado(self, lado):
        # somando lados
        perimetro = 4 * lado
        return perimetro
    # end perimetro_quadrado()

    def diagonal_quadrado(self, lado):
        diagonal = lado * sqrt(2)
        return diagonal

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

def pergunta_quadrado():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área")
    
def funcQuadrado():
    print("\n-------------------------------------------------")
    print("\nVocê escolheu: Quadrado")
    pergunta_quadrado() 
    tipo = int(input("\nQual tipo deseja: "))
    # instancia o objeto quadrado
    quadrado = Quadrado()
    
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

        # calcula a diagonal
        diagonal = quadrado.diagonal_quadrado(lado)

        # mostra a area
        print("\nA Área do Quadrado é de: ", area)
        print("\nA Diagonal do Quadrado é de: ", diagonal)
    # end if

    print("\n-------------------------------------------------")
# end funcQuadrado()
    


    
    
    