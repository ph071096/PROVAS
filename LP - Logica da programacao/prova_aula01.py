# A partir do que aprendemos até agora:
# Crie um exemplo de cada uma das principais tipagens de variáveis.
# Crie uma solicitação de dados ao usuário.
# Imprima a solicitação anterior na tela com uma mensagem personalizada.
nome = input('Qual seu nome: ')                                 # String
numero_int = int(input('Digite um numero inteiro: '))           # Int
numero_decimal = float(input('Digite um numero decimal: '))     # Float
verdade = True or False                                         # Bool

while verdade is True:
    print(f'Nome: {nome} TypeClass: {type(nome)} ')
    print(f'Numero inteiro: {numero_int} TypeClass: {type(numero_int)} ')
    print(f'Numero decimal: {numero_decimal} TypeClass: {type(numero_decimal)} ')
    print(f'?: {verdade} TypeClass: {type(verdade)} ')
    verdade = False

else:
    print(f'^^ by Mao')