import random 
computador = random.randint(1, 10)
jogador = int(input('Adivinha o numero que eu estou pensando: '))
if jogador == computador:
    print('Parabéns você acertou 🎊!' )
else:
    print('Que pena você errou 😢 ')
