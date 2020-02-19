#AULA 15 - O QUE SÃO TUPLAS EM PYTHON?

listas_carros = ['HRV', 'Golf', 'Argo'] #LISTA
tuplas_carros = ('HVR', 'Golf', 'Argo') #TUPLA

#CONVERSÃO DE TUPLAS PARA LISTAS (mei gambiarra)
tuplas_carros2 = list(tuplas_carros) #converter conteúdo de uma tupla em uma lista pelo comando list()
tuplas_carros2[2] = 'Kombi'
tuplas_carros = tuple(tuplas_carros2) #convertendo novamente de lista para tuplas

for tupla_carro in tuplas_carros:
    print(tupla_carro)

# TUPLAS são imutáveis, ou seja, não podem ser mudadas o seu conteúdo.
# LISTAS são mutáveis, ou seja, podem alterar quaisquer valores do seu conteúdo.
