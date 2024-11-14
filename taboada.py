import random  # Certifique-se de importar o módulo random

def jogar():
    
    print('***********************')
    print('Jogo da Taboada')
    print('***********************')
    
    try:
        arquivo = open("/home/gabriellsf9/alura 1/taboada.txt", "r")
        calculos = []
        
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                calculos.append(linha)
        
        arquivo.close()
        
        if not calculos:
            print("Nenhum cálculo encontrado no arquivo.")
            return
        
        calculo = random.choice(calculos)
        
        resultado_correto = eval(calculo)  
        acertou = False
      
        while (not acertou):
            tentativas = int(input('tente acertar o valor de: {} = '.format(calculo)))
        
            if tentativas == resultado_correto: 
                print('parabens você acertou!')
                acertou = True  
                return(calculo)
            else:
                print('Ops Você errou tente novamente!')  
            
             
    except Exception as e:  
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    jogar()