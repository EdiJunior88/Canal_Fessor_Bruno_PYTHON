#AULA 20 - FUNÇÕES PARTE 2 / ARGUMENTOS DE ENTRADA

valores = [1, 5, 3, 2]
def somar(num): #Passando uma lista como parâmetro / argumento na função
    r = 0
    for n in num:
        r += n
    print("Soma =", r)
    print("youtube.com/cfbcursos\n")

somar(valores)

"""
def carros(c = "Golf"): #Parâmetro / Argumento padrão na função
    print("Modelo:", c)

carros() #Se não colocar argumento, ele irá imprimir o parâmetro padrão da função
"""

"""
def somar(n1, n2, n3, n4): #Parâmetros / Argumentos de entrada n1, n2
    r = n1 + n2 + n3 + n4
    print("Soma =", r)
    print("youtube.com/cfbcursos\n")
    
somar(5, 7, 3, 2) #É obrigatório passar os mesmos valores (4 valores = 5, 7, 3, 2) conforme os parâmetros de entrada na função def somar()
somar(12, 8, 1, 20)
somar(1, 2, 0, 0)
"""

"""
def textos(*txt): #argumentos arbitrários é usado quando não sabemos quantos argumentos serão passados na função
    for t in txt:
        print(t)

textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")
"""

"""
def somar(*num):
    r = 0
    for n in num:
        r += n
    print("Soma =", r)
    print("youtube.com/cfbcursos\n")

somar(5, 2, 3, 5, 20, 15, 0, 1, 37)
"""

