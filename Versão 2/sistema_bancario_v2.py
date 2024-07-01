
def menu(): 
    menu = """ 
========== Menu ==========

Selecione uma opção

[a] Saque
[b] Depósito
[c] Extrato
[d] Cadastro de usuário
[e] Cadastro de conta bancária
[f] Sair


=========================
Obrigado Por usar nosso sistema
"""
    return input((menu))

def saque(saldo_disponivel, valor_saque, extrato, numero_saques, limite_saques, limite):
   

    excedeu_saldo = valor_saque > saldo_disponivel
    excedeu_numero_de_saques = numero_saques > limite_saques
    excedeu_limite_diario = valor_saque > limite

    if excedeu_saldo:
        print("\nNão foi possivel realizar o saque, valor insuficiente em sua conta")

    elif excedeu_numero_de_saques:
        print("\nNão foi possivel realizar o saque, você excedeu o número de saques diários")

    elif excedeu_limite_diario:
        print("\nNão foi possível realizar o saque, o valor excede seu limite diário")

    elif valor_saque > 0:
        saldo_disponivel -= valor_saque
        numero_saques += 1
        extrato += f"Valor do saque: R${valor_saque: .2f}\n"
        print("\nSaque realizado com sucesso\n")

    return saldo_disponivel, extrato    

def deposito(saldo_disponivel, valor_deposito, extrato):
    
    if valor_deposito > 0:
           saldo_disponivel += valor_deposito
           extrato += f"Valor do depósito: R${valor_deposito: .2f}\n"
           print("\nDepósito realizado com sucesso\n")
    return saldo_disponivel, extrato

def exibir_extrato(saldo_disponivel, extrato):

   
    print("Não foram realizadas operações\n" if not extrato else extrato)
    print(f"\nSaldo disponível: R${saldo_disponivel: .2f}")
   
def cadastro_usuario(usuarios):
    cpf = input("\nInforme o seu CPF (somente números): ") 
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\n Usuário ja existente")
        return
    
    nome = input("\nInforme o seu nome: ")
    data_de_nascimento = input("\nInforme a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nInforme o seu endereço (Nome da rua, numero , cidade / Estado): ")   


    usuarios.append({"cpf": cpf, "nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco})

    print("\nUsuário criado com sucesso")

def criacao_de_conta(agencia, numero_da_conta, usuarios):
    

    cpf = input("Informe o seu CPF ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_da_conta, "usuario": usuario}

    print("\nUsuário não encontrado")

def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    

def main():
    saldo_disponivel = 0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    limite = 500
    usuarios = []
    contas = []


    while True :

       opcao = menu()           
                  
       if opcao == "a":
          print(""" ========== SAQUE ========== """)
                 
          valor_saque = float(input("\nQual valor deseja sacar: "))
        
          saldo_disponivel, extrato = saque(saldo_disponivel = saldo_disponivel, valor_saque = valor_saque, extrato = extrato, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES, limite = limite)
       
       elif opcao == "b":
          print(""" ========== DEPÓSITO ========== """)

          valor_deposito = float(input("\nQual valor deseja depositar: "))
    
          saldo_disponivel, extrato = deposito(saldo_disponivel, valor_deposito, extrato)
          
       
       elif opcao == "c":
          print(""" ==========  Extrato ========== """) 
        
          exibir_extrato(saldo_disponivel, extrato)
         
     
       elif opcao == "d":
          print(""" ========== Cadastro de Usuário ========== """)
            
          cadastro_usuario(usuarios)
    
       elif opcao == "e":
          print(""" ========== Criação de conta corrente ========== """)

          numero_conta = len(contas) + 1
          conta = criacao_de_conta(AGENCIA, numero_conta, usuarios)
            
       elif opcao == "f":
          print("\nSaindo do sistema ...")
          break
 

       else:
          print( """ 
              Opção inválida, selecione outra opção""")
        

main()