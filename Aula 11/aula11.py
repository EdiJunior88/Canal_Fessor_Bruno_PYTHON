#AULA 10 - CONDICIONAL IF/ELIF/ELSE

"""
a = 10
b = 5
operação = "+"
resultado = 0

if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operador inválido!")

print(a, operação, b, " = ", resultado)
"""

clima = "sol"
dinheiro = 650
lugar = ""

if clima == "sol" or (dinheiro >= 300 and dinheiro <= 500):
    lugar = "clube"
else:
    lugar = "cinema"

print("Vou ao", lugar)