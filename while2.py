usuário = input("Escreva o seu nome de usuário: ")
senha = input("Escreva a sua senha: ")

while usuário == senha:
    print("Nome e Usuário incorretos, tente novamente!")
    usuário = input("Escreva o seu nome de usuário: ")
    senha = input("Escreva a sua senha: ")
  
print("Nome e usuário aceito!")