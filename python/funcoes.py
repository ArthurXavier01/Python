def soma(x, y):

    return x+y

def aoquadrado(x):

    return x * x

def perimetro(x, y):

    return (2*x) + (2*y)

def getMedia(x, y, z):
    media = (x + y + z) / 3
    if (media >= 7):
        return "Aprovado"
    else:
        return "Reprovado"
    
def verificarVogais(lista):
    vogais = ["a", "e", "i", "o", "u"]
    for letra in lista:
        if (letra in vogais):
            print(letra)
    return True

