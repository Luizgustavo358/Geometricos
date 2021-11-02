from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def le_opcao():
    opcao = int(input("\nEntre com um número: "))
    return opcao


def le_base():
    base = int(input("\nQual a base: "))
    return base


def le_altura():
    altura = int(input("\nQual é a altura: "))
    return altura


def le_lado():
    lado = int(input("\nQual é o tamanho do lado: "))
    return lado


def le_raio():
    raio = int(input("\nQual é o raio: "))
    return raio


def le_diagonal():
    diagonal = int(input("\nQual é a diagonal: "))
    return diagonal


def le_apotema():
    apotema = int(input("\nQual é o tamanho do apotema: "))
    return apotema


def pergunta():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área")

def pergunta_triagulo():
    print("\n0 - Nada")
    print("1 - Perímetro")
    print("2 - Área(Base/Altura)")
    print("3 - Área(Lado A, Lado B e Base)")
    print("4 - Tipo de Triangulo")