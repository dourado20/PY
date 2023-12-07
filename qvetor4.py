#Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa

vetor = []

for i in range(6):
    n = int(input("Digite um número:"))
    vetor.append(n)

print("Valores em ordem: ")
print(vetor)

print("Valores em ordem inversa: ")
vetor.reverse()
print(vetor)
