from geometric.Triangulo import funcTriangulo
from geometric.Quadrado import funcQuadrado
from geometric.Retangulo import funcRetangulo
from geometric.Trapezio import funcTrapezio
from geometric.Circulo import funcCirculo
from util.leitura import le_opcao


def apresentacao():
    print("\n+----------------------------------------------+")
    print("|            Programa Feito em Python          |")
    print("+----------------------------------------------+")
    print("| Calcula a Area e Perimetro de um Geometrico  |")
    print("|            Feito por: Luiz Gustavo           |")
    print("|       Contribuidores: Ricardo Sena           |")
    print("|                       Otto                   |")
    print("|                       Arthur                 |")
    print("|                       João Castro            |")
    print("+----------------------------------------------+\n")


def opcoes():
    print("\n0 - Sair")
    print("1 - Triangulo")
    print("2 - Quadrado")
    print("3 - Retangulo")
    print("4 - Trapezio")
    print("5 - Circulo")
    print("6 - Losango")
    print("7 - Paralelogramo")
    print("8 - Hexagono")
    print("9 - Octogono")
    print("10 - Pentagono")
    print("11 - Decagono")
    

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
    # elif opcao == 6:
    #     funcLosango()
    # elif opcao == 7:
    #     funcParalelogramo()      
    # elif opcao == 8:
    #     funcHexagono()  
    # elif opcao == 9: 
    #     funcOctogono()
    # elif opcao == 10: 
    #     funcPentagono()
    # elif opcao == 11:
    #     funcDecagono()


if __name__ == '__main__':
    apresentacao()

    opcoes()

    opcao = le_opcao()

    while opcao != 0:
        escolhe_opcao(opcao)

        opcoes()

        opcao = le_opcao()
    
    print("\nVocê Saiu :(\n")