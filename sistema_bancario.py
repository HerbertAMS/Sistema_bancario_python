menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
VALOR_MAX_SAQUE = 500


while True:
    print(menu)
    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Digite o valor a depositar: "))
        if valor > 0:        
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depositado com sucesso! Novo saldo: R${saldo:8.2f}")
        else:
            print("Valor inválido. Tente novamente.")
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques permitido.")
        else:
            valor = float(input("Digite o valor a sacar: "))
            if valor < 0:
                print("Valor inválido. Tente novamente.")
            elif valor > VALOR_MAX_SAQUE:
                print("Valor do saque excede o limite máximo.")
            elif valor <= saldo:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Saque efetuado com sucesso! Novo saldo: R${saldo:8.2f}")
            else:
                print("Saldo insuficiente.")
    elif opcao == "e":
        if extrato == "":
            print("Nenhum extrato disponível.")
        else:
            print("\n================ EXTRATO ================")
            print(extrato)
            print("==========================================")
            print(f"Saldo: R${saldo:8.2f}")
            print("==========================================")
    elif opcao == "q":
        print("Saindo do sistema...")
        break
    else:
menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
VALOR_MAX_SAQUE = 500


while True:
    print(menu)
    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Digite o valor a depositar: "))
        if valor > 0:        
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depositado com sucesso! Novo saldo: R${saldo:8.2f}")
        else:
            print("Valor inválido. Tente novamente.")
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques permitido.")
        else:
            valor = float(input("Digite o valor a sacar: "))
            if valor < 0:
                print("Valor inválido. Tente novamente.")
            elif valor > VALOR_MAX_SAQUE:
                print("Valor do saque excede o limite máximo.")
            elif valor <= saldo:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Saque efetuado com sucesso! Novo saldo: R${saldo:8.2f}")
            else:
                print("Saldo insuficiente.")
    elif opcao == "e":
        if extrato == "":
            print("Nenhum extrato disponível.")
        else:
            print("\n================ EXTRATO ================")
            print(extrato)
            print("==========================================")
            print(f"Saldo: R${saldo:8.2f}")
            print("==========================================")
    elif opcao == "q":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")