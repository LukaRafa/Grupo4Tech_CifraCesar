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


sentenca = input('Insira uma frase: ')
sentenca = sentenca.lower()
numero = int(input('Digite um número para ser a chave: '))
cripto = criptografa(sentenca, numero)
print('Frase criptografada: ', cripto)
