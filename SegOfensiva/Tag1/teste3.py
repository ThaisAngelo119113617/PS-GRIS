

#'Este programa nao possui uma funçao para descriptografar o arquivo, entao  execute-o  em um arquivo teste'


def esconde(msg):
# funçao que criptografa o arquivo
   
    s = ''
   
    for c in msg:
        if c  in 'ABCDFGHJKLM' :
            s += 'JNRijfeipjPWRPRUWPGOMÇVDLQQ.97RWTṔW9P2RPHOYNLÇ,E-I0Y59UH'
   
        elif c in 'OQRSTUVXWÇ':
            s += 'LGRJpojfrpijdksmca,xsdfjihtngmvcdwoirpjhtnlgm dojhtkng'
        
        elif c in 'abcdfgjkl':
            s += 'UOJF56213F56DIJASOUE98R08RFJMLASCganbf864\RHTNG'
        
        elif c in 'Zz':
            s += 'P'
        
        elif c in 'Ee':
            s += 'O'
        
        elif c in 'Nn':
            s += 'L'
        
        elif c in 'Ii':
            s += 'A'
        
        elif c in 'Tt':
            s += 'R'

        elif c in 'Pp':
            s += 'Z'
        elif c in 'Oo':
            s += 'E'
        elif c in 'Ll':
            s += 'N'

        elif c in 'aA':
            s +='I'
    
        else:
            s += '6gbdk.md75iurjwnd=[/.,06rtgolvekmls kdo9fjv'

    return s


print('Este programa nao possui uma funçao para descriptografar o arquivo, entao  execute-o  em um arquivo teste')

lala = open('teste2', 'r')
# abrindo o arquivo de teste

l = lala.read()
# lendo o arquivo

v = esconde(l)
# atribuindo a uma variavel o arquivo criptografado

lala.close()
# fechando o arquivo

lala2 = open('teste2','w')
# abrindo o arquivo novamete na forma de reescrever nele

lala2.write(v)
# reescrevendo no arquivo a sua forma criptografada

lala2.close()
# fechando o arquivo
print('Arquivo criptografado')

