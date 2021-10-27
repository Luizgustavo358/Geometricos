from util.leitura import le_base, le_lado, le_altura

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


#
# Metodo que mostra as opcoes de calculo.
#
def pergunta():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área")
# end pergunta()


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
