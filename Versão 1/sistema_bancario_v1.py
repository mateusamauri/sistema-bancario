

menu = """ 
========== Menu ==========

Selecione uma opção

[a] Saque
[b] Depósito
[c] Extrato
[d] Sair

=========================
Obrigado Por usar nosso sistema
"""
saldo_disponivel = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite = 500


while True :

    opcao = input(f"""{menu} 
                  Digite a opção desejada: """)            
                  

    if opcao == "a":
        print("""
              ========== SAQUE ==========
              """)
        
        valor_saque = float(input("Qual valor deseja sacar: "))
        excedeu_numero_de_saques = numero_saques >= LIMITE_SAQUES

                
        if valor_saque > limite:
           print("\nNão foi possível realizar o saque, o valor excede seu limite diário\n")

        elif valor_saque > saldo_disponivel:
            print("\nNão foi possível realizar o saque, valor insuficiente em sua conta\n")
        
        elif excedeu_numero_de_saques:
            print("\nNão foi possível realizar o saque, você excedeu o numero de saques diários\n")
        
        else:
           saldo_disponivel -= valor_saque
           numero_saques += 1
           extrato += f"Valor do saque: R${valor_saque: .2f}\n"
           print("\nSaque realizado com sucesso\n")
        

    elif opcao == "b":
        print("""
              ========== DEPÓSITO ==========
              """)

        valor_deposito = float(input("Qual valor deseja depositar: "))
    
        if valor_deposito > 0:
           saldo_disponivel += valor_deposito
           extrato += f"Valor do depósito: R${valor_deposito: .2f}\n"
           print("\nDepósito realizado com sucesso\n")
        
        else:
          print("\nNão foi possivel realizar o depósito, o valor precisa ser maior que zero\n")
          
       
    elif opcao == "c":
        print(f""" 
        ==========  Extrato ==========  
        """) 
        print("Não foram realizadas operações\n" if not extrato else extrato)
        print(f"\nSaldo disponível: R${saldo_disponivel: .2f}")
         
        

    elif opcao == "d":
        print("Saindo do sistema ...")
        break

    else:
        print( """ 
              Opção inválida, selecione outra opção""")
        



 

    











