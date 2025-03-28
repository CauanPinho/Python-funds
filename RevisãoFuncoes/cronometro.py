# Escreva uma função que recebe uma string como parâmetro e retorna o comprimento da string.

# Tente agora e me envie! 🚀
import time

def cronometro(a):
    while a>0:
        print(a)
        a-=1
        time.sleep(1)



tempousuario=int(input("quantos segundos o senhor quer no seu cronometro"))
cronometro(tempousuario)