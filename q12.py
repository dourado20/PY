n1 = int(input("escreva um numero:"))
n2 = int(input("escreva um número:"))
n3 = int(input("escreva outro número:"))
if n1 > n2 and n1 > n3:
    print(f"{n1}é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"{n2}é o maior número")
else:
    print(f"{n3}é o maior número")
