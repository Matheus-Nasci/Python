import random


def jogar():
    imprimir_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 6

    while (not enforcou and not acertou):
        print("Tentativas: {}".format(tentativas))
        chute = pedir_chute()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                    letras_acertadas[index] = letra
                    print(letras_acertadas)
                index += 1
        else:
            tentativas -= 1

        enforcou = tentativas == 0
        acertou = "_" not in letras_acertadas
        if (acertou):
            print(letras_acertadas)
            print("Parabéns, você ganhou o jogo")
        elif (enforcou):
            print("Você perdeu!")
            print("Fim do jogo")


def pedir_chute():
    chute = input("Qual a letra? ").strip().upper()
    return chute


def imprimir_mensagem_abertura():
    print("***************************")
    print("Bem-vindo ao jogo da Forca!")
    print("***************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


if (__name__ == "__main__"):
    jogar()
