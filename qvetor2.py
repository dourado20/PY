# Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

vetor = []
cont_pares = 0

for i in range(10):
    valor = int(input("Digite um valor:"))
    vetor.append(valor)
    if valor % 2 == 0:
        cont_pares += 1

print("O vetor possui", cont_pares,"valores pares.")