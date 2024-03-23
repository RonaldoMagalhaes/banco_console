import os
import time

MENU = """
######################  MENU  ############################

    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Sair
    
##########################################################

Digite sua escolha: """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


while True:
    os.system('clear')
    opcao = input(MENU)
    
    if opcao == "2":
        os.system('clear')
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"            
            
        else:
            print("Operação falhou! O valor informado é inválido.")
            time.sleep(3)
            
    elif opcao == "1":
        os.system('clear')
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            time.sleep(3)
            
        elif excedeu_limite:    
            print("Operação falhou! O valor do saque excede o limite.")
            time.sleep(3)
            
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            time.sleep(3)
        
        elif valor>0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            
        else:
           print("Operação falhou! O valor informado é inválido.") 
           time.sleep(3)
           
    elif opcao == "3":
        os.system('clear')
        print("==================  Extrato ===========================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================================")
        continuar = input("Pressione <ENTER> para continuar....")
    
    elif opcao == "4":
        os.system('clear')
        print("Encerrando o programa... O Banco agradece sua preferência...")
        time.sleep(3) 
        break
    else:
           os.system('clear')
           print("Operação inválida, por favor selecione novamente a operação desejada.")   
           time.sleep(3)
              
        


