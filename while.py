opcao = -1
saldo = 5000
limite = 0

print("""========== - Olá, bem-vindo ao banco, o que deseja fazer? - ==========
      """)

while opcao !=0:
    limite = limite +1
    opcao = int(input(" [1] Realizar saque \n [2] Ver extrato \n [0] Sair \n Digite sua opcao: "))

    if opcao == 1:
        print("Ok, você decidiu sacar, qual o valor deseja?")
        saque = int(input("Digite o valor: "))
        if saque <= saldo:
            saldo = saldo - saque
        else:
            print(f"Valor desejado é maior que o saldo disponivel de: {saldo}!")
    elif opcao == 2:
        print("Exibindo extrato... ")
        print(f"Você possui {saldo}")
    else:
        print("Obrigado por usar o nosso banco!")

    if limite == 5:
        print("Você excedeu o limite diario de operações! Tente novamente amanhã! ")
        break
        
exit()
