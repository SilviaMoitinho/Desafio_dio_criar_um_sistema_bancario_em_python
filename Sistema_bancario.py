menu = """
========== Menu ==========

[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Extrato
[ O ] Sair
=>"""

saldo = 0
limite =500
extrato = ""
numero_de_saques = 0
limite_de_saques = 4

while True:
    
    opcao = input(menu)

    if opcao== "1" :
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0 :
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operaçao falhou. Valor que voce inseriu nao é aceite, por favor tente denovo.")
        
    elif opcao== "2" :
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_limite_de_saques = numero_de_saques >= limite_de_saques

        if excedeu_saldo:
            print("Operaçao falhou, por saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operaçao falhou, voce excedeu o limite.")

        elif excedeu_limite_de_saques:
            print("Operaçao falhou, voce excedeu o limite de saques diarios, por favor tente novamente amanha.")

        elif valor > 0:
            saldo-=valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        
        else :
            print("Operaçao falhou, o valor informado é invalido")

    elif opcao== "3" :
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao== "O" :
        break

    else:
        print("Operação inválida, selecione uma das opçoes do menu.")


