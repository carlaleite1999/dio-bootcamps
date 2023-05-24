menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

while True:
    try:
        opcao = input(menu)
        if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
         if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor: .2f}\n'
        else:
            print("Operação falhou! O valor informado é inválido. Tente novamente!")
    except ValueError:
    print("O valor digitado é inválido, tente novamente")

        if opcao == '2':

            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insufuciente.")

        elif excedeu_limite:
        print("Operação falhou! O valor excedeu o limite disponível para saque.")
        
        elif excedeu_saques:
            print("Operação falhou! Número de saques foi excedido.")

        elif valor > 0:
            saldo -= valor

            extrato += f'Saque: R$ {valor: .2f}\n'

            numero_saques += 1

        else: 
            print("Operação falhou! O valor informado é inválido.")

    if opcao == "3":

        print("\n-------------------EXTRATO-------------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("------------------------------")        

    elif opcao =="4":
          break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")