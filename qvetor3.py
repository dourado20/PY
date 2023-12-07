# Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição que ele se encontra.

vetor = []
maior_elemento = float('-inf')
posição_maior = 0



for i in range(10):
   n = int(input("Digite um número:"))
   vetor.append(n)
    
   if n > maior_elemento:
        maior_elemento = n
        posição_maior = i
  
print("Vetor: ", vetor)
print("Maior elemento: ", maior_elemento)
print("Posição do maior elemento: ", posição_maior)