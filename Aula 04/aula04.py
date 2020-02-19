#AULA 04 - TIPOS DE DADOS EM PYTHON

x=1 #inteiro
x="CFB Cursos" #string
x=15.6 #float
x=False #bool
x=True #bool
n1=5; n2=2; x=complex(n1, n2) #complex
x=["Carro", "Avião", "Navio", 1, 58.3, True] #list /  array
x=("Carro", "Avião", "Navio", 1, 58.3, True) #tupla
x=range(0, 100, 1) #list
x={ #dict
    "canal":"CFB Cursos",
    "curso":"Curso de Python",
    "nome":"Bruno"
}
x={5,7,4,5,7,4,8} #set
x=frozenset({5,7,4,5,7,4,8}) #set

print("Valor: " + str(x))
print("Tipo: " + str(type(x)))