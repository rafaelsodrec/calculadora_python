# Calculadora simples

# Entrada dos números e da operação
while True:
    num1 = int(input("Digite o Primeiro Numero: "))
    operacao = input("identifique a Operação: ")
    num2 = int(input("Digite o Segundo Numero: "))
    resultado = 0

# Verificação da operação
    if operacao == "+":
        resultado = num1 + num2
        print("o resultado é", resultado)
    elif operacao == "+":
        resultado = num1 + num2
        print("o resultado é", resultado)
    elif operacao == "-":
        resultado = num1 - num2
        print("o resultado é", resultado)
    elif operacao == "*":
        resultado = num1 * num2
        print("o resultado é", resultado)
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
            print("o resultado é", resultado)
        else:
             print("Erro: Divisão por zero!")
    else:
        print("Operaçao não identificada")

