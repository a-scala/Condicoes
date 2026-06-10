velocidade = int(input('Qual foi a sua velocidade?: ')print('km'))
multa = (velocidade - 80) * 7
if velocidade >80:
    print('Ultrapassou a velocidade permitida')
    print(f'Sua multa foi de R${multa:.2f}')
else:
    print('Dentro do limite de velocidade.')
    print('Tenha um bom dia!')
