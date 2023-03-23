'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores 
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
nformado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.
'''
from modulos.titulo import titulo

titulo('Vamos encontrar um número na Sequência de Fibonacci')
numero = int(input('Insira um número inteiro: '))

termo1 = 0
termo2 = 1
fibonacci = []

fibonacci.append(termo1), fibonacci.append(termo2) #Atribuição dos 2 primeiros termos na lista

#Gerando a sequência de fibonacci.
while True:
    termo3 = termo1 + termo2
    fibonacci.append(termo3)
    termo1 = termo2
    termo2 = termo3

    #Solução com tratamento de erros e exceções:
        
    if fibonacci[-1] >= numero: #Parando a sequência de Fibonacci com base no número digitado.
        try: 
            #Se retornar um index em qualquer posição, então o número existe na sequência de Fibonacci.
            if fibonacci.index(numero) > 0:
                print(f'\nCerto\U0001F609, o número {numero} EXISTE na sequência de Fibonacci.')

        #Se o index voltar limpo, ocorrerá um erro de Value Error. Então o número não existe na sequência de Fibonacci.       
        except (ValueError):
            print(f'\nErrado\U0001F616, o número {numero} NÃO EXISTE na sequência de Fibonacci.')
            
        break
