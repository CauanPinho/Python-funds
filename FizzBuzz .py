# Imprima os números de 1 a 30, mas com as seguintes regras:

# Se o número for múltiplo de 3, imprima "Fizz" em vez do número.

# Se o número for múltiplo de 5, imprima "Buzz" em vez do número.

# Se o número for múltiplo de 3 e 5 ao mesmo tempo, imprima "FizzBuzz".

# Caso contrário, imprima o número normalmente.

# 📌 Regras:

# Usar for ou while (você escolhe).

# Sem listas prontas!

# Nada de "if" desnecessário, quero código limpo!

# Esse é um teste clássico em entrevistas, e a Sidia pode perguntar algo assim!
# Manda seu código! 🚀

x=1

while x<31:
        if x%15==0:
            print("FizzBuzz")
        else:
            if x%3==0:
                print("Fizz")
            else: print(x)
            if x%5==0:
                print("Buzz")
            else:
                 print(x)

x+=1
