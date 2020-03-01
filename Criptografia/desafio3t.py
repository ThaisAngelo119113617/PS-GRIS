#UFRJ
#Thais Angelo Ferreira de Oliveira
#TAG de criptografia
#Set 1 challenge 3



def xor(inputb, k):
    # funçao que retorna o resultado da operaçao xor
   
    output = b'' # inicializando uma variavel vazia que guarda um valor binario

    for byte in inputb: # varrendo o paramentro dado para realizar o xor de cada byte com a chave tambem dada

        output += bytes([byte ^ k])# acumulando na varriavel criada o resultado de cada operaçao

    return output # retornando o valor completo



def englishscore(inputb):
    # funçao que faz a contagem da pontuaçao

    frequencia = { 'a': .08167, 'b': .01492, 'c': .02782,
        'd': .04253, 'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153,'k': .00772, 'l': .04025, 'm': .02406,
        'n': .06749,'o': .07507, 'p': .01929,'q': .00095, 'r': .05987,
        's': .06327, 't': .09056,'u': .02758, 'v': .00978,'w': .02360,
        'x': .00150,'y': .01974, 'z': .00074, ' ': .13000}
    # dicionario com a porcentagem da frequencia de cada letra

    valor = sum([frequencia.get(chr(b), 0) for b in inputb.lower()])

    # A funçao 'sum' realiza a soma de itens em estruturas como listas, tupulas e etc. 

    # A funçao .get() esta sendo usada para pegar o valor da chave, nesse caso a porcentagem de cada letra 

    #Esta sendo utilizada a funçao .lower()para deixar todas as letras minúsculas para evitar conflito com as estabelecidas no dicionario

    #No segundo argumento da fuçao get(), que esta definido como zero, esta dizendo que caso a chave procurada nao for achada, retornar o valor zero
    
    return valor # retornando o valor

def main():
    string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736' #Variavel com o valor da mensagem

    stringbytes = bytes.fromhex(string)#Transformando a mensagem para binário

    mensagens = [] # criando uma lista para conter todas as  256 possibilidades em que  cada elemento da lista seja um dicionario 'dados'  com os dados da mensagem com uma chave especifica

    for k in range(256): #For para varrer todas as 256 possibilidades 

        mensagem = xor(stringbytes, k)#Realizando a operaçao xor da mensagem com cada possibilidade

        score = englishscore(mensagem)# Realizando a contagem da pontuaçao de cada mensagem

        dados = {'Mensagem': mensagem,  'Chave': k ,'Score': score}#Salvando a mensagem, a chave e sua pontuação em um dicionário, diferente para cada chave

        mensagens.append(dados)# Adicionando no final da lista um dicionáro com os dados na mesagem 

    melhorscore = sorted(mensagens,key=lambda x: x['Score'],reverse=True)[0]
    # Ordenando a lista 'mensagens' de forma decrescente (reverse = True)e tendo como comparação o valor dentro da chave 'Score'
    # Este [0] esta indicando para guardar somente o primeiro valor da lista, ou seja, o dicionario com a mensagem de maior pontuaçao

    for item in melhorscore: # varrendo o dicionario salo em 'melhorscore' para imprimir as chaves e seus valores

        print(item,': ', melhorscore[item])

main()
