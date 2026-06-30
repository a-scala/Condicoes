n1 = int(input('Escolha um numero: '))
n2 = int(input('Escolha outro numero: '))
n3 = int(input('Escolha o ultimo numero: '))
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2 
else:
    menor = n3
print(f'O maior numero é {maior}')
print(f'E o menor numero é {menor}')