# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual número ele deseja ver a tabuada. 
# A saída deve ser conforme o exemplo abaixo:

# Tabuada de 5:
# 5 X 1 = 5

# 5 X 2 = 10

# ...

# 5 X 10 = 50
numero = int(input('Digite un numero inteiro entre 1 a 10: '))
print(f'Tabuada de {numero}: ')

for i in range(1, 11):
    print(f'{numero} x {i} = {numero*i} ')