# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário.
# O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.
# Ao final, exiba a soma dos números pares encontrados.
intervalo1 = int(input('Digite o primeiro intervalo: '))
intervalo2 = int(input('Digite o segundo intervalo: ')) + 1
pares = 0

for i in range(intervalo1, intervalo2):
    if i % 2 == 0:
        pares += i
        print(f'{i} é par, Soma dos pares: {pares}')
        print('-' * 40)
    else:
        print(f'{i} é impar, Soma dos pares: {pares}')
        print('-' * 40)