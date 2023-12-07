# Faça um programa que leia um vetor de 8 posições e, em seguida, leia também em dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respecƟvas posições X e Y


vetor = []

for i in range(8):
    valor = int(input("Digite um valor:"))
    vetor.append(valor)

x = int(input("digite o valor qualquer que esteja no vetor: "))
y = int(input("digite outro valor qualquer que esteja no vetor: "))
  

soma = x + y

print("A soma dos valores nas posições x e y é: ",soma)
