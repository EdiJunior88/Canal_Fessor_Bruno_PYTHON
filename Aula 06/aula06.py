#AULA 06 - STRINGS PARTE 1

curso = "Curso de Python"
curso2 = " Curso de Python "
a = curso.split(" ") #.split() substitui a string por outra string

print(curso[0])  #[0] é um array "lista" que irá imprimir a posição da string
print(curso[0:5])  #[0:5] é um array "lista" de tamanho determinado que irá imprimir a posição da string
print("Tamanho: " + str(len(curso)))
print(curso2.strip()) #.strip() remove os espaços do início e do fim da string
print(curso.lower()) #.lower() deixa a string em minúscula
print(curso.upper()) #.upper() deixa a string em maiúscula
print(curso.replace("Python", "C#")) #.replace() substitui a string por outra string
print(a[2]) #Python

