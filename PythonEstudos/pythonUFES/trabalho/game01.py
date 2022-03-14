import time
import random
import sys

def tempo_passado (verso) : 
    t1 = time.time()
    auxiliar = input("Cante (digite) a música:\n ")
    while auxiliar != verso :
        auxiliar = input("Cante corretamente a música: ")
    t2 = time.time()
    return(t2-t1)

def dano (verso,rapidez,vida1,vida2) : 
    if rapidez <= len(verso)*0.3 : 
            print("Você é rápido o sufuciente para impressioanar seus oponentes.\n")
            vida2 -= 1
    else :
            print("Você foi devagar e se sente um pouco envergonhado.\n")
            vida1 -= 1 
    return(vida1,vida2)

def stage1 (número_jog,modo_jogo,número_itens) : 
    vida = 3 
    op_vida = 3 
    #Stage1 
    print("Sua mente está em branco, mas com o passar do tempo você começa a enxergar 3 silhuetas.\n")  
    input("prissione enter, para continuar.\n")
    print("A branquitude acaba e as silhuetas estão visiveis a primeira é do Diomedes, a sengunda é do Nissin e a última do Baco.\n")
    input("prissione enter, para continuar.\n") 
    print("Eles olham para você, e começam a cantar...\n")
    input("prissione enter, para continuar.\n")     
    while vida or op_vida != 0 : 
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida}  "|Vida oponentes ⋋_⋌:" {op_vida} "|*
        -------------------------------------------------------------
        eles começam a cantar:
        *De um lado um público jovem, maldita massa despolitizada*
        """)
        input("prissione enter, para continuar.\n") 
        print("""Seus oponentes olham para você e esperam você cantar.
        Apesar de você não reconhecer a letra, sua mente reconhce a próxuma parte
        (Às vezes uns tão radical, mas base teórica nada)
        """)
        input("A partir de agora o tempo começara a contar, pressione enter para continuar.\n")
        auxiliar1 = "Às vezes uns tão radical, mas base teórica nada"
        tempo = tempo_passado(auxiliar1)
        vida, op_vida = dano(auxiliar1,tempo,vida,op_vida)
        print("---------------------------------------------------------------------\n")
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida}  "|Vida oponentes ⋋_⋌:" {op_vida} "|*
        -------------------------------------------------------------
        eles continuam a cantar:
        *Nunca invejei ninguém, na verdade ataquei a estrutura*
        """)
        print("""Da mesma forma que anterirormente você sabe como continuar: 
        (Uma grande manobra arriscada como Bukowski em literatura)
        """)
        input("Pressione enter para cantar.")
        auxiliar1 = "Uma grande manobra arriscada como Bukowski em literatura"
        tempo = tempo_passado(auxiliar1)
        vida, op_vida = dano(auxiliar1,tempo,vida,op_vida)
        print("---------------------------------------------------------------------\n")
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida}  "|Vida oponentes ⋋_⋌:" {op_vida} "|*
        -------------------------------------------------------------
        eles continuam a cantar:
        *Chinaski, o aprendiz, filho de Lula, não de Ustra*
        """)
        print("""Da mesma forma que anterirormente você sabe como continuar: 
        (Fui infeliz atacando MC's? Não! Questionei a indústria)
        """)
        input("Pressione enter para cantar.")
        auxiliar1 = "Fui infeliz atacando MC's? Não! Questionei a indústria"
        tempo = tempo_passado(auxiliar1)
        vida, op_vida = dano(auxiliar1,tempo,vida,op_vida)
        if vida == 0 or op_vida == 0 : 
            break 
        print("---------------------------------------------------------------------\n")
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida}  "|Vida oponentes ⋋_⋌:" {op_vida} "|*
        -------------------------------------------------------------
        eles continuam a cantar:
        *Direto do gueto, do gueto, do gueto, do gueto, do gueto, do gueto*
        """)
        print("""Da mesma forma que anterirormente você sabe como continuar: 
        (Riqueza pro gueto, riqueza pros pretos, uma vida melhor e mais justa)
        """)
        input("Pressione enter para cantar.")
        auxiliar1 = "Riqueza pro gueto, riqueza pros pretos, uma vida melhor e mais justa"
        tempo = tempo_passado(auxiliar1)
        vida, op_vida = dano(auxiliar1,tempo,vida,op_vida)
        if vida == 0 or op_vida == 0 : 
            break 
        print("---------------------------------------------------------------------\n")
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida}  "|Vida oponentes ⋋_⋌:" {op_vida} "|*
        -------------------------------------------------------------
        eles continuam a cantar:
        *Os irmãos tão morrendo por uma bermuda, um boné, um par de tênis*
        """)
        print("""Da mesma forma que anterirormente você sabe como continuar: 
        (Triste, né? Querem se matar, então que matem Michel Temer)
        """)
        input("Pressione enter para cantar.")
        auxiliar1 = "Triste, né? Querem se matar, então que matem Michel Temer"
        tempo = tempo_passado(auxiliar1)
        vida, op_vida = dano(auxiliar1,tempo,vida,op_vida)
        print("---------------------------------------------------------------------\n") 
    if op_vida == 0 : 
        print("Você conseguiu concluir o primeiro desafio!\n") 
        stage2(número_jog,modo_jogo,número_itens)
    else : 
        restart = str(input("Você não conseguiu concluir o desafio, deseja tentar outra vez?(s/n)\n "))
        if restart == "n":
            menu(número_jog,modo_jogo,número_itens)
        else: 
            campanha(número_jog,modo_jogo,número_itens)

def stage2 (número_jog,modo_jogo,número_itens):
    vida1 = 3 
    op_vida1 = 3 
    restart1 = 'sim'
    #Stage2 
    print("A silhueta do seu novo oponente aparece no horizonte, é um homem pensando.")
    input("Pressione enter para continuar.")
    print("A silhueta se aproxima e você a reconhce é Gabriel pensador. ")
    input("Pressione enter para continuar.")
    print("Ele olha para você começa a cantar...")
    input("Pressione enter para continuar.")
    while vida1 or op_vida1 != 0 : 
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida1}  "|Vida oponente  ⋋_⋌:" {op_vida1} "|*
        -------------------------------------------------------------
        Ele começa a cantar:
        *Às margens do Ipiranga nem ouvem o brado retumbante*
        """)
        input("prissione enter, para continuar.\n") 
        print("""Seu oponente olha para você e espera você cantar.
        Apesar de você não reconhecer a letra, sua mente reconhce a próxima parte
        (De um povo heroico sufocado de forma humilhante)
        """)
        input("A partir de agora o tempo começara a contar, pressione enter para continuar.\n")
        auxiliar5 = "De um povo heroico sufocado de forma humilhante"
        tempo1 = tempo_passado(auxiliar5)
        vida1, op_vida1 = dano(auxiliar5,tempo1,vida1,op_vida1)
        print("---------------------------------------------------------------------\n")
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida1}  "|Vida oponente  ⋋_⋌:" {op_vida1} "|*
        -------------------------------------------------------------
        Ele continua a cantar:
        *Um povo escravizado por um novo capataz*
        """)
        print("""Da mesma forma que anterirormente você sabe como continuar: 
        (Que executa os inocentes, arranca os filhos dos pais)
        """)
        input("Pressione enter para cantar.")
        auxiliar5 = "Que executa os inocentes, arranca os filhos dos pais"
        tempo1 = tempo_passado(auxiliar5)
        vida1, op_vida1 = dano(auxiliar5,tempo1,vida1,op_vida1)
        print("---------------------------------------------------------------------\n")
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida1}  "|Vida oponente  ⋋_⋌:" {op_vida1} "|*
        -------------------------------------------------------------
        Ele continuam a cantar:
        *Arranca os pais dos filhos, na caneta e no gatilho*
        """)
        print("""Da mesma forma que anterirormente você sabe como continuar: 
        (A morte a domicílio é a recompensa que o Estado traz)
        """)
        input("Pressione enter para cantar.")
        auxiliar5 = "A morte a domicílio é a recompensa que o Estado traz"
        tempo1 = tempo_passado(auxiliar5)
        vida1, op_vida1 = dano(auxiliar5,tempo1,vida1,op_vida1)
        if vida1 == 0 or op_vida1 == 0 : 
            break 
        print("---------------------------------------------------------------------\n")
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida1}  "|Vida oponente  ⋋_⋌:" {op_vida1} "|*
        -------------------------------------------------------------
        Ele continua a cantar:
        *O estado é estarrecedor, o filme é de terror*
        """)
        print("""Da mesma forma que anterirormente você sabe como continuar: 
        (Só que não tem final feliz porque o monstro é o diretor)
        """)
        input("Pressione enter para cantar.")
        auxiliar5 = "Só que não tem final feliz porque o monstro é o diretor"
        tempo1 = tempo_passado(auxiliar5)
        vida1, op_vida1 = dano(auxiliar5,tempo1,vida1,op_vida1)
        if vida1 == 0 or op_vida1 == 0 : 
            break 
        print("---------------------------------------------------------------------\n")
        print(f"""
        -------------------------------------------------------------
        *|Vidas ಠ▃ಠ :" {vida1}  "|Vida oponente  ⋋_⋌:" {op_vida1} "|*
        -------------------------------------------------------------
        Ele continua a cantar:
        *E o Oscar da covardia*
        """)
        print("""Da mesma forma que anterirormente você sabe como continuar: 
        (Vai pra quem vira as costas e silencia)
        """)
        input("Pressione enter para cantar.")
        auxiliar5 = "Vai pra quem vira as costas e silencia"
        tempo1 = tempo_passado(auxiliar5)
        vida1, op_vida1 = dano(auxiliar5,tempo1,vida1,op_vida1)
        print("---------------------------------------------------------------------\n") 
    if op_vida1 == 0 : 
        print("Ao terminar de cantar, você se sente caindo e acorda, você está de fone deitado na sua cama escutando uma playlist aleatória de rap do sp*tf*\n")
        print("Você conseguiu concluir os desafios!\n") 
        menu(número_jog,modo_jogo,número_itens)
    else : 
        restart1 = str(input("Você não conseguiu concluir o desafio, deseja tentar outra vez?(s/n)\n "))
        if restart1 == "n":
            menu(número_jog,modo_jogo,número_itens)
        else: 
            campanha(número_jog,modo_jogo,número_itens)

def campanha (número_jog,modo_jogo,número_itens) : 
    #Instruções
    print("Alguns rappers são conhecidos por cantarem rapidamente, seu desafio é cantar (no caso digitar) tão rápido quanto um rapper canta. ")
    input("prissione enter, para continuar.\n")
    stage1(número_jog,modo_jogo,número_itens) 
    return()

def jogar (njoga,mod,niten) :  
    lista_jogadores = []
    lista_tempo = [] 
    contador = 0 
    for i in range (0,njoga,1) : 
        auxiliar0 = str(input(f"Digite o nome do {i+1}° jogador: "))
        lista_jogadores.append(auxiliar0)
    print("---------------------------------------------------------------------------------------------------------------------------------\n")
    print("""Como funcuiona, a letra ou o número que você tera q digitar vai vir entre [] e enquanto você n acertar o tempo vai passar,
[X] para erros e [O] para acertos ,o jogador que acertar os itens em menos tempos é ganhador. """)
    input("Aperte enter para continuar.\n")
    print("---------------------------------------------------------------------------------------------------------------------------------\n")
    if mod == "L" : 
        lista_modo = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p'
        ,'Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']  
        for i in range (0,njoga,1) :
            auxiliar_tempo = 0  
            print(f"É a rodada do {lista_jogadores[i]}, prepare-se;")
            input("Aperte enter para começar:")        
            for j in range (0,niten,1): 
                auxiliar_aleatória = random.choice(lista_modo)
                t3 = time.time() 
                entrada_jogador = input(f"O item da vez é [{auxiliar_aleatória}]: ") 
                while entrada_jogador != auxiliar_aleatória : 
                    print("[X]")
                    entrada_jogador = input(f"O item da vez é [{auxiliar_aleatória}]: ")
                t4 = time.time()
                print("[O]")
                auxiliar_tempo += t4 - t3
                if j == niten-1 :
                    lista_tempo.append(auxiliar_tempo) 
            print("---------------------------------------------------------------------------------------------------------------------------------\n")
    else : 
        for i in range (0,njoga,1) :
            auxiliar_tempo = 0  
            print(f"É a rodada do {lista_jogadores[i]}, prepare-se;")
            input("Aperte enter para começar:")        
            for j in range (0,niten,1): 
                auxiliar_aleatória = random.randint(1,99)
                t3 = time.time() 
                entrada_jogador = int(input(f"O item da vez é [{auxiliar_aleatória}]: ")) 
                while entrada_jogador != auxiliar_aleatória : 
                    print("[X]")
                    entrada_jogador = int(input(f"O item da vez é [{auxiliar_aleatória}]: "))
                t4 = time.time()
                print("[O]")
                auxiliar_tempo += t4 - t3
                if j == niten-1 :
                    lista_tempo.append(auxiliar_tempo) 
                print(lista_tempo)
            print("---------------------------------------------------------------------------------------------------------------------------------\n")
    while len(lista_tempo) != 0 :
        contador += 1
        auxiliar_colocação = min(lista_tempo) 
        auxiliar_colocação2 = lista_tempo.index(auxiliar_colocação)
        print(f"O {contador}° lugar é {lista_jogadores[auxiliar_colocação2]} com o tempo de  {auxiliar_colocação:.2f}s") 
        del lista_tempo[auxiliar_colocação2] 
        del lista_jogadores[auxiliar_colocação2]
    print("---------------------------------------------------------------------------------------------------------------------------------\n")
    menu(njoga,mod,niten)

def game_config (Njogadores,modo,Nitens) :
    cont_alt = "s"
    while cont_alt != "n" :
        print(f"""
    -------------------------------------------------------
    |1- Número de jogadores : {Njogadores}                           |
    |2- Modo de jogo : {modo}                                  |   
    |3- Quantidade de itens em cada modo: {Nitens}               |
    |4- Sair                                              |
    -------------------------------------------------------                         
    """)
        opção_alteração = int(input("Seleciono a opção (1, 2, 3 ou 4): "))
        if opção_alteração == 1 :   
            print("O núemro máximo de jogadores permiridos é 4")
            Njogadores = int(input("Digite a quantidade de jogadores com al qual vc deseja jogar: "))
            while Njogadores < 1 or Njogadores > 4  : 
                Njogadores = int(input("Digite uma quantidade válida de jogadores: "))   
            cont_alt = str(input("Deseja continuar realizando alterações?(s/n)"))
            print("------------------------------------------------------------------\n") 
        elif opção_alteração == 2 :
            print("Existem 2 modos de jogos com letras ou números.\n") 
            modo = str(input("Digite L para letras e N para números:"))
            while not modo != ("L" or "N") : 
                modo = str(input("A opção digitada não é válida, por favor digite L ou N:")) 
            cont_alt = str(input("Deseja continuar realizando alterações?(s/n)"))
            print("------------------------------------------------------------------\n") 
        elif opção_alteração == 3 : 
            print("A quantidade de máxima de itens permitida é 10 e a mínima 5 :")
            Nitens = int(input("Escolha uma quantidade de itens entre 5 e 10 :"))
            while Nitens < 5 or Nitens > 10 : 
                Nitens = int(input("Digite uma quantidade válida de itens :"))
            cont_alt = str(input("Deseja continuar realizando alterações?(s/n)"))
            print("------------------------------------------------------------------\n") 
        else : 
            menu(Njogadores,modo,Nitens)       
    return(Njogadores,modo,Nitens)
    
def menu (número_jog,modo_jogo,número_itens) :
    saida = 0
    print("""                        -=MENU=-
        "***************************************
        "*0-Campanha                           *
        "*1-Jogar                              *  
        "*2-Alterar configurações de jogo      *
        "*3-sair                               *
        "***************************************""") 
    opção = int(input("Digite a opção desejada:"))
    while saida != "sair" :
        if opção == 0 : 
            campanha(número_jog,modo_jogo,número_itens)
        elif opção == 1 :
            jogar(número_jog,modo_jogo,número_itens)
            break
        elif opção == 2 : 
            número_jog, modo_jogo, número_itens = game_config(número_jog,modo_jogo,número_itens)
        else :
            sys.exit()

número_jog = 2
número_itens = 5
modo_jogo = "L" 
menu(número_jog,modo_jogo,número_itens)  
input("Fim")