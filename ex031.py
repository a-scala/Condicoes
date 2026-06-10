distancia = int(input('Qual a distancia da viagem? '))
if distancia <=200:
    print(f'O valor da passagem é R${distancia * 0.50:.2f}')
else:
    print(f'O valor da passagem é R${distancia * 0.45:.2f}')