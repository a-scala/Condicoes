'''
tempo = int(input("Quantos anos tem seu carro? "))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('fim')
'''
'''
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('fim')
'''
'''
nome = str(input('Qual é seu nome? '))
a = nome.upper()
if a == 'BIANCA':
    print('Que nome bonito você tem! ')
else:
    print('Nome comum o seu 😂 ')
print(f'Bom dia, {nome}!')
'''
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua media foi {m:.1f}')
if m >=6:
    print('Nota azul')
else:
    print('Nota vermelha')
'''