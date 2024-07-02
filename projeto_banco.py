import datetime

menu = """
=============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=============
=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 

    opcao = input(menu)

    data_hora_atual = datetime.datetime.now()
    data_em_texto = data_hora_atual.strftime('%d/%m/%Y %H:%M')

    if opcao == "d":
        print(""" ============ Depósito ============ 
              """)
        valor = float(input("Qual valor você gostaria de depositar: "))

        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f} no dia ({data_em_texto})\n")

    elif opcao == "s":
        print(" ============ Saque ============")

        saque = float(input("Qual valor deseja sacar?: "))
        
        if numero_saques == LIMITE_SAQUES:
            print("A quantidade diaria de saque permitido chegou ao limite. Favor tente novamente amanhã.")
        elif saque > saldo:
            print("O valor deseja é maior do que seu saldo atual! Operação cancelada.")
        elif saque > limite:
            print(f"O limite máximo por transação é de {limite} reais, tente um valor menor!")
        elif saque > 0:
            numero_saques = numero_saques + 1
            saldo = saldo - saque
            extrato += (f"Saque de: R$ {saque:.2f} no dia ({data_em_texto})\n")
        else:
            print("Operação falhou! O valor informado é inválido!")
            
    elif opcao == "e":
        print(f"============ Extrato ============ ")
        print(f"============ Não foram realizadas movimentações ============ " if not extrato else extrato)
        print(f"============ Seu saldo atual é de R${saldo:.2f} ============ ")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
