#AULA 07 - STRINGS PARTE 2

#usando in e not in

texto = "Curso de Python"
palavra = "python"

resposta = palavra.upper() in texto.upper() #O operador "in" verifica se o operando a sua esquerda, está contido na lista a sua direita
print(resposta)

resposta2 = palavra not in texto #O operador "not in" verifica se o operando a sua esquerda, não está contido na lista a sua direita
print(resposta2)

resposta3 = palavra in texto
print(resposta3)

print("--------------------------------")

#concatenação de strings

curso = "Curso de Python"
canal = "CBF Cursos"

concatenação = curso + " do canal " + canal
print(concatenação)

print("--------------------------------")

#uso de format e caracteres de escape

cidade = "Maceió"
dia = 17
mes = "Janeiro"
ano = 2020
canal = "CFB Cursos"
data = "{}, {} de {} de {}\n \"{}\"" #método .format()

print(data.format(cidade, dia, mes, ano, canal)) #O método format() serve para criar uma string que contem campos entre chaves a serem substituídos pelos argumentos de format.