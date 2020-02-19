#AULA 12 - LOOP FOR

carros = ['HVR', 'Golf', 'Argo', 'Focus', 'Fit', 'Fusion', 'Polo']

#formas de utilização do comando FOR

"""
for x in carros:
    print(x)
"""
"""
for x in carros:
    print(x)
    if (x == 'Golf'):
        print("  VW")
"""
"""
for x in "CFB Cursos":
    print(x)
"""

for x in carros:
    if (x == "Fit"):
        break
    print(x)

print("Fim do programa!")