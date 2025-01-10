# Função que calcula a sequência de Fibonatti
def fibonacci(n):
    f1, f2 = 0, 1
    while f1 < n:
        f1, f2 = f2, f1 + f2
    return f1 == n

# Entrada de dados, no caso o usuário digita o número que será verificado
numero = int(input("Digite um numero: "))

# Verificação se o número digitado está ou não na sequência de Fibonatti
if fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")