import forca
import advinhacao
import taboada

print('*********************')
print('escolha seu jogo')
print('*********************')

print('(1) Forca (2) advinhação (3) Taboada')

jogo = int(input('Qual jogo? '))

if (jogo == 1):
    print('jogando forca')
    forca.jogar()
    
elif (jogo == 2):
    print('jogando advinhação')
    advinhacao.jogar()

elif (jogo == 3):
    print('jogando taboada')
    taboada.jogar()

    
