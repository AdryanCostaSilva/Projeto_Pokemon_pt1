from time import sleep
from random import choice, choices
#1 Introdução do Professor carvalho
print("=" * 70)
print("POKÉMON WORLD".center(70))
print("=" * 70)
print("Carvalho: Olá, bem vindo ao pokémon world,")
print("          eu serei seu professor, meu nome")
print("          é Carvalho e o seu nome qual é? ")
nome = str(input("          >>>"))
sleep(0.5)
print(f"Carvalho: Muito prazer {nome},")
print("          vamos para a aventura!\n")

#2 Exploração de Ambientes

pokedex = []
caverna = ["Larvitar","Aron","Rockruff","Swinub","Diglett","Rhyhorn","Meltan","Skarmory","Steelix","Meowth"]
matagal = ["Caterpie","Pinsir","Wurmple","Paras","Chikorita","Bulbasaur","Hoppip","Pidgey","Zubat","Mantine"]
while True:
    print("Oque você deseja fazer?")
    escolha = str(input(" [1] Entrar na caverna\n [2] Entrar no matagal\n [3] Listar Pokémon da Pokédex\n [4] Sair\n >>> "))
    captura = [1,2]
    probabilidade = []
    encontrado = ''  
    if escolha not in "1234":
        print("Ambiente inválido! Tente novamente.")
        continue
    elif escolha == "1":
        print("Boa escolha, o ambiente o Caverna é ótimo para pokémons do tipo pedra, terra e aço.")
        encontrado = choice(caverna)
        sleep(1)
        print(f"Você entrou na caverna e encontrou um {encontrado}!")
        probabilidade = [50,50]
    elif escolha == "2":
        print("Boa escolha, o ambiente Matagal é ótimo para pokémons do tipo inseto, planta e voador.")
        encontrado = choice(matagal)
        sleep(1)
        print(f"Você entrou no matagal e encontrou um {encontrado}!")
        probabilidade = [35,65]
    elif escolha == "3":
        print("="*70)
        print(f"Lista de pokémons na sua pokedex: {pokedex}")
        print("="*70)
        continue
    elif escolha == "4":
        break
    if encontrado in pokedex:
        print("Este pokémon já está no seu pokedex, não haverá processo de captura!")
    else:
        cont = 0
        while True:
            resp = str(input("Deseja capturar este pokémon? [S/N]:"))
            if resp.lower() != "s" and resp.lower() != "n":
                print("Comando desconhecido! Informe novamente.")
            elif resp == "s":
                cont += 1
                num = choice(choices(captura, probabilidade, k=100))
                if num == 1:
                    print(f"Você capturou um {encontrado}!")
                    pokedex.append(encontrado)
                    sleep(1)
                    break
                elif num == 2:
                    if cont != 3:
                        print("Você não conseguiu captura-lo!")
                        continue
                    if cont == 3:
                        print("O pokémon fugiu!")
                        sleep(1)
                        break
            elif resp == "n":
                break
print("Até mais aventureiro!")
