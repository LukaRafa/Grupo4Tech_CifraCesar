# Grupo 4
# Lucas Santos
# Maria Eduarda Fontana
# Maria Eduarda Góes

def criptografa(frase, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    fraseCriptografada = ''
    for a in frase:
        posição = alfabeto.find(a)
        if posição == -1:
            fraseCriptografada = fraseCriptografada + a
        else:
            nova_posição = posição + chave
            nova_posição = nova_posição % len(alfabeto)
            fraseCriptografada = fraseCriptografada + \
                alfabeto[nova_posição:nova_posição+1]
    return fraseCriptografada

# Incluímos a função para decriptografar uma frase.
def decriptografa(frase, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    fraseDecriptografada = ''
    for a in frase:
        posição = alfabeto.find(a)
        if posição == -1:
            fraseDecriptografada = fraseDecriptografada + a
        else:
            nova_posição = posição - chave
            nova_posição = nova_posição % len(alfabeto)
            fraseDecriptografada = fraseDecriptografada + \
                alfabeto[nova_posição:nova_posição+1]
    return fraseDecriptografada


sentenca = input('Insira uma frase: ')
sentenca = sentenca.lower()
numero = int(input('Digite um número para ser a chave: '))
#Definida a variável que contém a escolha do usuário.
escolha = int(input('Deseja criptografar ou decriptografar a frase? \n1 - Criptografar \n2 - Decriptografar \n'))

#Criado um if para direcionar a escolha do usuário.
if escolha == 1:
    cripto = criptografa(sentenca, numero)
    print('Frase criptografada: ', cripto)
elif escolha == 2:
    print('Decriptografar')
    decripto = decriptografa(sentenca, numero)
    print('Frase decriptografada: ', decripto)
else:
    print('Você deve escolher uma opção válida')




