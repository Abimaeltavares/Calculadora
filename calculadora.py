while True:
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Divisão Inteira")
    print("6 - Módulo (Resto)")
    print("7 - Exponenciação")
    print("0 - Sair")
    
    opcao = int(input("Informe a opção: "))
    
    if opcao == 0:
        print("Saindo...")
        break
    
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    
    match opcao:
        case 1:
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        case 2:
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        case 3:
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        case 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero")
        case 5:
            if num2 != 0:
                resultado = num1 // num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero")
        case 6:
            if num2 != 0:
                resultado = num1 % num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero")
        case 7:
            resultado = num1 ** num2
            print(f"Resultado: {resultado}")
        case _:
            print("Opção inválida. Tente novamente.")