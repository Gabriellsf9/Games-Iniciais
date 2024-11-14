import random

def jogar():

    print('')
    print('*********************')
    print('')
    print('Jogo da advinhação')
    print('')
    print('*********************')

    numero = random.randint(1,100)
    total_tentativas = 0

    print('Digite o nível de dificuldade que deseja jogar!')
    print('(1) Facil')
    print('(2) Medio')
    print('(3) dificil')

    nivel = int(input('Qual o nível desejado: '))

    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3

    for rodada in range (1, total_tentativas + 1):
        print(f'tentativa {rodada} de {total_tentativas}')
        chute = int(input("Digite um número de 1 a 100: "))
        
        if (chute < 1 or chute >100):
            print('Você deve digitar um numero entre 1 e 100!')
            continue
        
        acertou = chute == numero
        maior = chute > numero
        menor = chute < numero
        
        if (acertou):
            print('você acertou!')
            break
            
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
                
            elif(menor):
                print("Você errou! O Seu chute foi menor que o numero secreto")
            print(f'o número correto era: {numero}') #comentar quando for jogar pois apresenta a resposta do game!
            

    print('Fim do Jogo')

if __name__ == "__main__":
    jogar()