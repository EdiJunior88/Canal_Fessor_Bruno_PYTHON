#AULA 16 - MATRIZES

"""
carros = ['HVR', 'Golf', 'Focus', 'Argo'] #Array ou Lista (List)

carros[2] = 'Fusion' #Trocar 'Focus' por 'Fusion'

for x in carros:
    print(x)
"""

carros = [
    ['Modelo','HVR'],
    ['Fabricante','Honda'],
    ['Ano',2016]
]

carros.append(['Cor','Prata']) #adicionando uma coluna e um item na matriz

#carros[2][1] = 2019 #mudando o valor '2016' para '2019'

#print(carros[2][0]) #imprimindo somente o valor 'Ano'

#imprimindo uma linha e coluna utilizando o FOR

for linha, coluna in carros:
    print("Linha:", linha, " |  Coluna:", coluna)