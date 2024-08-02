print("Bem-vindo a calculadora, por favor insira a operação desejada.")


saida = ""
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

def calculadora():
    while True:
        print("\nCalculadora")
        print("Selecione a operação desejada:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite a opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
                continue

            if escolha == '1':
                print(f"Resultado: {soma(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicacao(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {divisao(num1, num2)}")
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")


calculadora()

