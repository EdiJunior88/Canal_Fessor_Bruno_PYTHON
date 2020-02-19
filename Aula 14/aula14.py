#AULA 13 - LOOP WHILE

"""
regra básica de um WHILE

inicialização de variável de controle
while (teste lógico)
    comando 1
    comando 2
    comando X
    incremento ou decremento ou controle
"""

"""
i = 0
while i < 10:
    print(i)
    i += 1
    if(i >= 5):
        break
print("Fim do Loop")
"""

"""
carros = ['HRV', 'Golf', 'Argo', 'Onix', 'Focus']
i = 0
tamanho = len(carros)
while i < tamanho:
    print(carros[i])
    i += 1
print("\nFim do Loop")
"""

carros = []
carro = input("Digite o nome do novo carro: ")
while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro: ")

for x in carros:
    print(x)

print("\nFim do Loop")