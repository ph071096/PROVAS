# Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.
carro_velocidade = float(input('Qual a velocidade do carro: '))
if carro_velocidade > 80.0:
    print(f'Velocidade: {carro_velocidade}, ultrapassou o maximo da via ')
    multa = (carro_velocidade - 80.0) * 20
    print(f'Multa: R${multa} ')