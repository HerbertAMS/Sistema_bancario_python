# 1️⃣ Criando um sistema bancário com Python
**Desafio**

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.


## Objetivo

Criar um sistema bancário com as operações:

- Sacar
o sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques dever ser armazenados em uma variável e exibidos na operação de extrato.

- Depositar
Deve ser possível depositar valores positivos para minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

- Visualizar extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ 000.00.

## Entradas
### Deposito
Digitar "d"
Digitar o valor no formato inteiro positivo

### Saque 
Digitar "s"
Digitar o valor no formato inteiro positivo

### Extrato
Digitar "e"

### Sair
Digitar "q"

### Operação invalida
Digitar qualquer outro valor

## Saída
### Deposito
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
- Mensagem: "Deposito realizado!"

### Saque
- Caso o usuário não tenha saldo em conta. Mostre a mensagem: "Saldo insuficiente". 
- Caso tenha saldo: "Saque realizado com sucesso!"
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Extrato
Listar todas as movimentações. No fim da listagem deve ser exibido o saldo atual da conta. Formato R$ 000,00.

### Sair
Sair do sistema.

### Operação invalida
Apresentar mensagem: "Operação invalida!"

Exemplo de saída:
1500.45 => R$ 1500.45
