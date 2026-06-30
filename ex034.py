s = float(input('Qual o seu salario: R$'))
if s > 1250.00:
    s *= 1.10
else:
    s *= 1.15
print(f'Seu novo salrio é R$ {s:.2f}')