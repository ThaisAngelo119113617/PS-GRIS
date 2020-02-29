#UFRJ
#Thais Angelo Ferreira de Oliveira
#TAG de criptografia
#Set 1 challenge 2


import binascii
# importanto a biblioteca para usar suas funçoes


def xor(a, b):
    # funçao que realiza aoperaçao xor
    
    valor =bytes([ x^y for (x,y) in zip(a, b)])
    
    return valor  # retorna o valor em binario


def main():

    valor1= input('valor1: ')
    valor2= input('valor2: ')
    # recebendo os valores

    if len(valor1)== len(valor2):
    # comparando se os valores recebidos possuem o mesmo tamanho
    #especificação do desafio
        
        a = binascii.unhexlify(valor1)
        b =binascii.unhexlify(valor2)
        # convertendo os valores recebidos para binario
        resultbin = xor(a,b)# chamando a funçao que realiza a operaçao xor

        resulthexa=  binascii.hexlify(resultbin)
        # convertendo o resultado da operaçao para hexadecinal

        print(resulthexa) # printando o resultado na tela
    else:
        print('Entre com números de tamanhos iguais!')
        # caso os valores  recebidos nao tenha o mesmo tamanho, essa mensagem será mostrada na tela

main()
