a=int(input("Coloque o valor para calcular: "))
operacao=(input("Coloque o símbolo da operação a ser calculada: "))
b=int(input("Coloque o segundo valor para calcular: "))

def calculadora(operacao):
    if operacao == '+':
        soma =  a + b
        print('O resultado da soma é: ', soma)
        
    elif operacao == '-':
        subtracao = a - b
        print('O resultado da subtracao é: ', subtracao)
        
    elif operacao == '*':
        mult =  a * b
        print('O resultado da multiplicação é: ', mult)
        
    elif operacao == '/':
        if b != 0:
            div = a / b
            print('O resultado da divisão é: ', div)
        else:
           print('Erro: divisão por zero')
            
calculadora(operacao)
