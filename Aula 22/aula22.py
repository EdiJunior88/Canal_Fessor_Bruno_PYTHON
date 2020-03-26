#AULA 22 - LAMDA OU FUNÇÕES ANÔNIMAS

"""
#Não utiliza return por ser uma função simples
soma = lambda a, b: a + b
mult = lambda a, b, c: (a + b) * c

print(soma(2, 5))
print(mult(2, 5, 3))
"""

"""
#Modo simplificado
print((lambda a, b: a + b)(3, 2))
"""

#Utilizando função
r = lambda x, func: x + func(x)
res = r(2, lambda x: x * x)
print(res)
res = r(2, lambda x: x + x)
print(res)
res = r(2, lambda x: x + 3)
print(res)