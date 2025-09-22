# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina.
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0.
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

quantidade_aluno = int(input('Digite a quantidade de alunos: '))

for _ in range(quantidade_aluno):
    nome = input('Nome do aluno: ')
    notas = []
    for j in range(1, 4):
        nota = float(input(f'Nota {j}: '))
        notas.append(nota)

    media = sum(notas) / 3
    status = 'Aprovado' if media >= 7.0 else 'Reprovado'

    print('-' * 40)
    print(f'Aluno: {nome}')
    print(f"Notas: {notas[0]:.1f}, {notas[1]:.1f}, {notas[2]:.1f}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")