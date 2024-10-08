# Sistema bancário

**Objetivo:**

- Criar um sistema bancário com 3 versões, iniciando em sua versão mais básica e evoluindo com versões mais avançadas e otimizadas

## Versão 1
- Utilização apenas de conceitos básicos da linguagem Python como : Variáveis, Estruturas condicionais, estruturas de repetição e operadores
- Operações: Saque, Depósito, Visualizar extrato
- Saque: O sistema dever permitir apenas 3 saques diários com limite de R$ 500,00 cada um e todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
- Depósito : Precisa ser possível depositar apenas valores positivos, a primeira versão utiliza apenas 1 usuário então não é necessário identificar qual é o número da agência e conta e todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
- Extrato: Lista todos os depósitos e saques e no final exibe o saldo atual da conta

## Versão 2
- Otimização da primeira versão do sistema
- Utilização de Funções, Estruturas de dados(Listas, Tuplas, Conjuntos, Dicionarios) 
- Operações: Saque, Depósito, Visualizar extrato, Cadastro de usuario, Criação de conta corrente, Filtro de usuários (Todas divididas em funções) 
- Saque: O sistema dever permitir apenas 3 saques diários com limite de R$ 500,00 cada um e todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
- Depósito : Precisa ser possível depositar apenas valores positivos.
- Extrato: Lista todos os depósitos e saques e no final exibe o saldo atual da conta
- Cadastro de usuário: Realiza o cadastro coletando dados como nome, cpf, data de nascimento e endereço e então guarda os valores dentro de uma lista utilizando a função de filtragem para verificar se o usuário ja existe.
- Criação de conta corrente: Cria uma conta que é vinculada ao cpf do usuário atribuindo a ele um número de agência e um número de conta corrente, dentro da criação de conta também é utilizada a função de filtrar usuários para verificar se o usuário já é cadastrado. 
- Filtro de usuários: É utilizado para fazer a verificação do cpf de cada usuário, para o caso demja existir uma conta ou um cadastro de usuário ja vinculados com aquele cpf

## Versão 3
- Modelagem do sistema com programação orientada a objetos
- Utilização de todos os conceitos utilizados nas versões anteriores mas agora com todas as operações divididas em classes, métodos e atributos de cada classe
- Foi implementada uma atualização no sistema para armazenar os dados dos clientes e das contas bancárias em objetos e não mais em listas / dicionários.
- As regras das versões anteriores se mantém para todas as operações como Saque, Depósito, Extrato, Cadastro, Criação de conta, filtro de usuários etc.

## O que foi utilizado
![Vscode](https://img.shields.io/badge/Vscode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

