#AULA 09 - COLEÇÃO LIST

carros = ['HRV', 'Golf', 'Argo', 'Focus']
#carros[3] = "Fusion" #substitui o item Fusion no lugar do item Focus
carros.append("Fit") #adiciona o item na lista
carros.append("Fusion") #adiciona o item na lista
carros.append("Polo") #adiciona o item na lista
#carros.remove("Fusion") #remove um item da lista
#carros.pop() #remove sempre o último item da lista
#del carros[2] #remove um item específico da lista
#carros.clear() #remove todos os elementos da lista
#carros2 = list(carros) #list() copia todo o conteúdo de uma lista para uma outra lista

carros2 = ['Fusca', '147', 'Brasília', 'Celta']

carros3 = carros + carros2 #funde duas listas em uma nova lista "carros3"

print(str(len(carros3)) + " carros na lista") #len() mostra a quantidade de itens na lista

print(carros3)
