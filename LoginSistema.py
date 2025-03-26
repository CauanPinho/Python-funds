# Crie um programa que avalia se uma pessoa pode fazer login num sistema.
# Ela só pode fazer login se:

# O nome de usuário for "sidia"

# E a senha for "2025"

# Você deve criar:

# uma variável usuario com um nome qualquer

# uma variável senha com um valor qualquer

# uma variável acesso_liberado que será True ou False com base nos critérios acima

# Nada de print(). Apenas as 3 variáveis finais.


usuario=input("digite  seu login")
senha=(int(input("digite sua senha")))

if usuario== "sidia" and senha == "2025":
    acesso_liberado=True
else:
    acesso_liberado=False

