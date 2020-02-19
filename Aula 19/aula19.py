#AULA 19 - FUNÇÕES PARTE 1

n1 = 15
n2 = 7

#definindo uma função
def somar():
    r = n1 + n2
    print("Soma de", n1, "e", n2, "=", r)
    print("youtube.com/cfbcursos\n")

def subtrair():
    r = n1 - n2
    print("Subtração de", n1, "e", n2, "=", r)
    print("youtube.com/cfbcursos\n")

def multiplicar():
    r = n1 * n2
    print("Multiplicação de", n1, "e", n2, "=", r)
    print("youtube.com/cfbcursos\n")

#função que chama outra função
def calculos():
    somar()
    subtrair()
    multiplicar()

calculos()
# somar() #chamando a função
# subtrair()