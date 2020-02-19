#AULA 03 - VARIÁVEIS EM PYTHON

num1=num2=res=0
#canal="CFB Cursos" #escopo global

def cn():
    global canal
    canal="CFB Cursos"

cn()

print(canal)