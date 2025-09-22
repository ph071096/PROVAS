# Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
numero = int
qnt_numero = 0
soma = 0

while numero != 0:
    numero = int(input('Digite um numero inteiro ou 0 para sair: '))
    if numero != 0:
        qnt_numero += 1
        soma += numero
        media = soma / qnt_numero

else:
    print(f'Quantidade de numeros digitados: {qnt_numero} ')
    print(f'Soma: {soma} ')
    print(f'Média: {media} ')