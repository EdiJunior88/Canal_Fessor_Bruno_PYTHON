#AULA 21 - FUNÇÕES PARTE 3 / RETORNO DE VALORES

valores = [1, 5, 3, 2, 10, 4, 8]
def somar(num): #Passando uma lista como parâmetro / argumento na função
    r = 0
    for n in num:
        r += n
    return r #retorna um valor

r = somar(valores)

print(str(valores) +": Soma = " + str(r))