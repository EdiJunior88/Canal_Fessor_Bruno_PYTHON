#AULA 17 - DICTIONARY

#Ordem obrigatória de Dictionary: Chave/Key - Valor/Value

carro = {
    'Fabricante':'Honda',
    'Modelo':'HVR',
    'Ano':'2016',
    'Cor':'Prata'
}

carro['Cor'] = 'Preto' #Mudando o valor de 'Prata' para 'Preto'

print("Tamanho do Dictionary:", len(carro))  #len() verifica o tamanho de um Dictionary

carro['Câmbio'] = 'Automático' #Adicionando itens no Dictionary

carro.pop('Câmbio') #Remove um item específico no Dictionary

carro.clear()

#Verificando se existe algum elemento no Dictionary
if "Modelo" in carro:
    print("SIM, modelo é uma chave \n")

#Imprimindo a chave e o valor de um Dictionary
for chave, valor in carro.items():
    print(chave, ":", valor)

"""
#Podemos imprimir o valor de um Dictionary utilizando a função .get()
fabricante = carro.get('Fabricante')
print(fabricante)
"""

"""
#Utilizando um loop
for x in carro:
    print(x) #imprimir Chave
    print(carro[x]) #imprimir Valor
"""

