# UFRJ
#Thais Angelo Ferreira de Oliveira
#TAG de criptografia
#Set 1 challege 1


import binascii

import base64
# Importando as bibliotecas para usar suas funções


def hexapara64(valor):
    # funçao que converte o valor hexadecimal para a base 64

    vbin = binascii.unhexlify(valor)
    # Valor convertido para binario
    
    vb64= base64.b64encode(vbin)
    # Valor convertido para base 64
    
    return vb64 # retornando o valor



string= input('valor: ')
#Pedindo o valor para o usuário

resultado = hexapara64(string)
#Chamando a funçao para converter o valor

print('O valor na base64 é: ' )
print(resultado)
# Imprimindo o valor na base 64


