def jogar():
    print("***************************")
    print("Bem-vindo ao jogo da Forca!")
    print("***************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        print(tentativas)
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        if (acertou):
            print(letras_acertadas)
            print("Parabéns, você ganhou o jogo")


print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
