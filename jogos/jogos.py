import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("******** ESCOLHA O JOGO *********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = (int(input("Qual jogo você quer jogar? ")))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()