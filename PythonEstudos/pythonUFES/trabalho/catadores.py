import sys 
import csv  
from datetime import date as dt 
from prettytable import PrettyTable as pt
import matplotlib.pyplot as plt
import numpy as np

def coluna_do_gráfico (lista) : 
        colunas_gráfico = [] 
        for i in range (3,8,1) : 
                soma_coluna = 0
                for j in range (1, len(lista)) : 
                        lista[j][i] = float(lista[j][i] )
                        soma_coluna += lista[j][i]  
                colunas_gráfico.append(soma_coluna) 
        return(colunas_gráfico)

def transcrever_csv () :
        transcrição = []
        with open ('dados_catadores.csv', 'r', encoding='utf8') as csv_file : 
                        reader = csv.reader(csv_file, delimiter=";") 
                        for lines in reader : 
                                transcrição.append(lines) 
        return(transcrição)

def print_table (): 
        table = pt(['Nome','Contato','Contato de emergência','Quantidade ferro(kg)','Quantidade aluminio(kg)','Quantidade plástico(kg)','Quantidade isopor(kg)','Quantidade papelão(kg)','Total de pontos'])
        with open ('dados_catadores.csv', 'r', encoding='utf8') as csv_file : 
                reader = csv.reader(csv_file, delimiter=";") 
                reader.__next__()
                for linhas in reader : 
                        table.add_row(linhas)   
        print(table)

def cadastrar_catador () :
    continuar_cadastros = 's'
    arquivocsv = "dados_catadores.csv"
    while continuar_cadastros == 's' : 
        dados_pessoa = []
        auxiliar_Dados_pessoa = str(input("Por favor, digite o nome da pessoa a ser cadastrada: ")) 
        dados_pessoa.append(auxiliar_Dados_pessoa)
        auxiliar_Dados_pessoa = str(input(f'Digite o contato de {dados_pessoa[0]}: '))
        while auxiliar_Dados_pessoa.isdecimal() != True  :
                auxiliar_Dados_pessoa = str(input(f'Digite o contato de {dados_pessoa[0]} corretamente: '))
        if auxiliar_Dados_pessoa.find('3') == 0 : 
                while len(auxiliar_Dados_pessoa) != 8 : 
                        auxiliar_Dados_pessoa = str(input(f'Digite o contato de {dados_pessoa[0]} corretamente: '))
        else : 
                while len(auxiliar_Dados_pessoa) != 9 :
                        auxiliar_Dados_pessoa = str(input(f'Digite o contato de {dados_pessoa[0]} corretamente: '))
        ddd = str(input(f"O DDD de {dados_pessoa[0]} é do Espirito Santo ? (s/n) \n "))
        if ddd == 's' : 
                auxiliar_Dados_pessoa = '(27)'+auxiliar_Dados_pessoa 
        else : 
                ddd = str(input('Digite o número do DDD: '))
                while ddd.isdecimal != True and len(ddd) != 2 :
                        ddd = str(input('Digite o número do DDD corretamente: '))  
                auxiliar_Dados_pessoa = '('+ ddd +')' + auxiliar_Dados_pessoa
        dados_pessoa.append(auxiliar_Dados_pessoa)
        auxiliar_Dados_pessoa = str(input('Digite um contato para emergência: '))
        while auxiliar_Dados_pessoa.isdecimal() != True  :
                auxiliar_Dados_pessoa = str(input(f'Digite o contato de {dados_pessoa[0]} corretamente: '))
        if auxiliar_Dados_pessoa.find('3') == 0 : 
                while len(auxiliar_Dados_pessoa) != 8 : 
                        auxiliar_Dados_pessoa = str(input(f'Digite o contato de {dados_pessoa[0]} corretamente: '))
        else : 
                while len(auxiliar_Dados_pessoa) != 9 :
                        auxiliar_Dados_pessoa = str(input(f'Digite o contato de {dados_pessoa[0]} corretamente: '))
        ddd = str(input(f"O DDD de emergência {dados_pessoa[0]} é do Espirito Santo ? (s/n) \n "))
        if ddd == 's' : 
                auxiliar_Dados_pessoa = '(27)'+auxiliar_Dados_pessoa 
        else : 
                ddd = str(input('Digite o número do DDD: '))
                while ddd.isdecimal != True and len(ddd) != 2 :
                        ddd = str(input('Digite o número do DDD corretamente: '))  
                auxiliar_Dados_pessoa = '('+ ddd +')' + auxiliar_Dados_pessoa
        dados_pessoa.append(auxiliar_Dados_pessoa)
        trouxe_materiais = str(input(f'A/O {dados_pessoa[0]}, trouxe materiais ? (s/n) \n'))
        if trouxe_materiais == 's': 
                print("Digite a quantidade, em quilos, de cada um dos seguintes materiais ferro, aluminio, plástico, isopor e papelão: (separados por ',' exemplo: 1,2,3,...)\n  ")
                ferro, aluminio, plástico, isopor, papelão = map(int, sys.stdin.readline().split(','))
                dados_pessoa.append(ferro)
                dados_pessoa.append(aluminio)
                dados_pessoa.append(plástico)
                dados_pessoa.append(isopor)
                dados_pessoa.append(papelão)
                pontos = ferro + 3*aluminio + 2*plástico + 4*isopor + papelão 
                dados_pessoa.append(pontos)
        else : 
            for i in range (0,6):
                dados_pessoa.append(0)
        with open (arquivocsv, 'a', newline='') as csv_file : 
                writer = csv.writer(csv_file, delimiter = ';')
                writer.writerow(dados_pessoa)
        print_table()
        continuar_cadastros = input('Deseja realizar o cadastro de outra pessoa? (s/n)\n')
        menu()
       
def metas_catador () :
        pontos = []
        auxiliar_pontos = []
        linha_auxiliar = []
        with open ('dados_catadores.csv', 'r', encoding='utf8') as csv_file : 
                reader = csv.reader(csv_file, delimiter=";") 
                for lines in reader : 
                        auxiliar_pontos.append(lines)
        for i in range (1,len(auxiliar_pontos)) :
                for j in range(0,9,8) : 
                        linha_auxiliar.append(auxiliar_pontos[i][j]) 
        pontos.append(linha_auxiliar)
        linha_auxiliar = []

        print(pontos)

        table = pt(['Nome','Total de pontos'])
        for item in pontos : 
                table.add_row(item)
        print(table)

        for i in range (0,len(pontos)) :
                pontos[i][1] = float(pontos[i][1])
        if pontos[i][1] > 200 : 
                print(f'O/A {pontos[i][0]} atingiu a meta de pontos para a cesta básica. ')

        menu()

def dados_mês () : 
        print("""
******************************
*1-Mostrar os dados do mês   *
*2-Encerrar o mês atual      *
*3-Sair para o menu          *
******************************
""")
        opção_mês = int(input("Digite a opção desejada:")) 
        while not 1 <= opção_mês <= 3  :  
                opção_mês = int(input("Digite a opção desejada de 1 a 3:"))  
        if opção_mês == 1 :
                transcrever_tabela = transcrever_csv()
                coluna = coluna_do_gráfico(transcrever_tabela)
                labels = ['Ferro','Aluminio','Plástico','Isopor','Papelão']
                x = np.arange(len(labels)) 
                width = 0.35 
                fig, ax = plt.subplots() 
                rects1 = ax.bar(x , coluna, width, label='Lixo para reciclagem')
                ax.set_ylabel('Kg')
                ax.set_title('Do mês atual')
                ax.set_xticks(x)
                ax.set_xticklabels(labels)
                ax.legend()
                ax.bar_label(rects1, padding=3)
                fig.tight_layout() 
                plt.show()
                ok = input('Você será movido para o menu principal, digite "ok" para continuar. ')
                while ok != 'ok' :
                        ok = input('Digite "ok" para continuar.') 
                menu()
        elif opção_mês == 2: 
                auxiliar_transcrição = []
                auxiliar_transcrição2 = []
                auxiliar_transcrição3 = []
                auxiliar_transcrição = transcrever_csv()
                data_hj = dt.today() 
                mês = data_hj.month
                if mês < 10 :
                        mês = str(mês)   
                        with open ("dados_catadores0"+mês+".csv", 'w', newline='', encoding='utf8') as csv_file :
                                writer = csv.writer(csv_file, delimiter=';') 
                                for line in auxiliar_transcrição : 
                                        writer.writerow(line)
                else :   
                        mês = str(mês)   
                        with open ("dados_catadores"+mês+".csv", 'w', newline='', encoding='utf8') as csv_file :
                                writer = csv.writer(csv_file, delimiter=';') 
                                for line in auxiliar_transcrição : 
                                        writer.writerow(line)
                recadastrar = input('Deseja recadastrar alguma pessoa? (s/n)')
                if recadastrar == 's' : 
                        print_table()
                        loop_cadastro = 's' 
                        auxiliar_transcrição2.append(auxiliar_transcrição[0])
                        while loop_cadastro == 's' : 
                                nome_recadastro = input('Digite o nome da pessoa que você deseja recadastrar: ')
                                contador = 0 
                                for i in range (1,len(auxiliar_transcrição),1) :
                                        if auxiliar_transcrição[i][0] == nome_recadastro :
                                                contador += 1 
                                        else : 
                                                contador += 0
                                if contador == 1 : 
                                        for i in range (1,len(auxiliar_transcrição)) :
                                                if auxiliar_transcrição[i][0] == nome_recadastro : 
                                                        auxiliar_transcrição3.append(nome_recadastro) 
                                                        auxiliar_transcrição3.append(auxiliar_transcrição[i][1])
                                                        auxiliar_transcrição3.append(auxiliar_transcrição[i][2])
                                                        for j in range (0,6) :
                                                                auxiliar_transcrição3.append(0) 
                                                        auxiliar_transcrição2.append(auxiliar_transcrição3) 
                                        auxiliar_transcrição3 = [] 
                                        tabela_recadastro = pt(['Nome','Contato','Contato de emergência','Quantidade ferro(kg)','Quantidade aluminio(kg)','Quantidade plástico(kg)','Quantidade isopor(kg)','Quantidade papelão(kg)','Total de pontos'])
                                        for i in range(1,len(auxiliar_transcrição2)) : 
                                                tabela_recadastro.add_row(auxiliar_transcrição2[i])
                                        print(tabela_recadastro)
                                        loop_cadastro = input("Deseja recadastrar outra pessoas? (s/n)") 
                                else : 
                                        print('O nome foi gitado incorretamente.') 
                                        loop_cadastro = input("Deseja tentar outra vez? (s/n)") 
                        with open ('dados_catadores.csv', 'w', newline='',encoding='utf8') as csv_file :
                                writer = csv.writer(csv_file, delimiter=';') 
                                for line in auxiliar_transcrição2 : 
                                        writer.writerow(line) 
                        print('A planilha do mês foi emcerrada e uma para o mês atual foi criada, você será realocado/a para o menu principal. ')
                        menu() 
        else : 
                menu()

def previsões_materiais () :
        auxiliar_materiais = transcrever_csv 
        materiais = coluna_do_gráfico(auxiliar_materiais)
        print(f"""
A quantidade dos materiais disponíveis são: 
Ferro {materiais[0]}Kg =  {materiais[0]*0.75}Kg para reutilizar
Aluminio {materiais[1]}Kg = {materiais[1]*0.50}Kg para reutilizar
Plástico {materiais[2]}Kg = {materiais[2]*0.90}Kg para reutilizar 
Isopor {materiais[3]}Kg = {materiais[3]*0.40}Kg para reutilizar
Papelão {materiais[4]}Kg = {materiais[4]*0.95}Kg para reutilizar 
 """) 
        input('Aperte enter para ser retornado para o menu principal')
        menu()
        

def doações () :
        continuar_att_doações = 's'
        auxiliar_doações = []
        while continuar_att_doações == 's' :
                with open ('doações.csv', 'r', encoding='utf8') as csv_file : 
                        reader = csv.reader(csv_file, delimiter=";") 
                        for lines in reader : 
                                auxiliar_doações.append(lines)  
                pessoa_doadora = input('Digite o nome da pessoa que contribuiu para o programa : ') 
                doação1 = input(f'Digite a quantidade de reais que {pessoa_doadora} contribuiu : ') 
                doação2 = input(f'Digite a quantidade de alimentos não pereciveis que {pessoa_doadora} contribuiu :') 
                auxiliar_doações2 = [] 
                auxiliar_doações2.append(pessoa_doadora)
                auxiliar_doações2.append(doação1) 
                auxiliar_doações2.append(doação2) 
                auxiliar_doações.append(auxiliar_doações2) 
                with open ('doações.csv', 'w', newline='') as csv_file : 
                        writer = csv.writer(csv_file, delimiter = ';')
                        for item in auxiliar_doações : 
                                writer.writerow(item)    
                tabela_doações = pt(['Nome','Dinheiro(R$)','Alimentos(Kd)'])
                for i in  range (1,len(auxiliar_doações)) :
                        tabela_doações.add_row(auxiliar_doações[i]) 
                print(tabela_doações)            
                continuar_att_doações = input('Deseja cadastrar outro doador ? (s/n)') 
        menu()
    
def att_catadores () :    
    alterar_dados = [] 

    with open ('dados_catadores.csv', 'r', encoding='utf8') as csv_file : 
            reader = csv.reader(csv_file, delimiter=";") 
            for lines in reader : 
                    alterar_dados.append(lines)

    print_table()

    procurar_pessoa = input("Por favor, digite o nome da pessoa que você deseja alterar os dados: ")
    auxiliar1 = 0
    auxiliar2 = 0
    pessoa_loop = 's'
    while pessoa_loop == 's' :
            for i in range (1, len(alterar_dados)) :
                    for j in range(0,1): 
                            if alterar_dados[i][j] == procurar_pessoa : 
                                    auxiliar1 = i 
                                    auxiliar2 = j 
                                    pessoa_loop = 'n' 
            if pessoa_loop == 's' :
                    procurar_pessoa = input("Digite corretamente o nome da pessoa que você deseja alterar os dados: ")

    continuar_alteração = 's'
    while continuar_alteração == 's' : 
            print("""
            --==Menu Alterações==--
            *********************************
            *1- Contato                     *
            *2- Cotato de emergência        *
            *3- Quantidade de ferro         *
            *4- Quantidade de aluminio      *
            *5- Quantidade de plástico      *
            *6- Quantidade de isopor        *
            *7- Quantidade de papelão       *
            *8- sair para o menu            *
            *********************************
            """)
            opção_alteração = int(input("Digite a opção desejada:")) 
            loop_alteração = 'n'
            while not 1 <= opção_alteração <= 8  :
                    opção_alteração = int(input("Digite a opção desejada de 1 a 8:")) 
            if opção_alteração == 1 : 
                    while loop_alteração == 'n' :
                            alterar_dados[auxiliar1][1] = str(input(f'Digite o novo contato de {alterar_dados[auxiliar1][auxiliar2]}:  '))
                            loop_alteração = str(input(f"O contato {alterar_dados[auxiliar1][1]} está correto? (s/n)\n"))
            elif opção_alteração == 2 : 
                    while loop_alteração == 'n' :
                            alterar_dados[auxiliar1][2] = str(input(f'Digite o novo contato de {alterar_dados[auxiliar1][auxiliar2]}:  '))
                            loop_alteração = str(input(f"O contato de emergência {alterar_dados[auxiliar1][2]} está correto? (s/n)\n"))
            elif  opção_alteração == 3 : 
                    while loop_alteração == 'n' :
                            auxiliar_alteração = float(input('Digite a quantidade de ferro (em Kg), que será somada na tabela: '))
                            loop_alteração = input(f'A quantidade {auxiliar_alteração} está correta: (s/n)\n')
                    alterar_dados[auxiliar1][3] = float(alterar_dados[auxiliar1][3])
                    alterar_dados[auxiliar1][3] += auxiliar_alteração 
            elif opção_alteração == 4 : 
                    while loop_alteração == 'n' :
                            auxiliar_alteração = float(input('Digite a quantidade de aluminio (em Kg), que será somada na tabela: '))
                            loop_alteração = input(f'A quantidade {auxiliar_alteração} está correta: (s/n)\n')
                    alterar_dados[auxiliar1][4] = float(alterar_dados[auxiliar1][4])
                    alterar_dados[auxiliar1][4] += auxiliar_alteração 
            elif opção_alteração == 5 : 
                    while loop_alteração == 'n' :
                            auxiliar_alteração = float(input('Digite a quantidade de plástico (em Kg), que será somada na tabela: '))
                            loop_alteração = input(f'A quantidade {auxiliar_alteração} está correta: (s/n)\n')
                    alterar_dados[auxiliar1][5] = float(alterar_dados[auxiliar1][5])
                    alterar_dados[auxiliar1][5] += auxiliar_alteração 
            elif opção_alteração== 6 : 
                    while loop_alteração == 'n' :
                            auxiliar_alteração = float(input('Digite a quantidade de isopor (em Kg), que será somada na tabela: '))
                            loop_alteração = input(f'A quantidade {auxiliar_alteração} está correta: (s/n)\n')
                    alterar_dados[auxiliar1][6] = float(alterar_dados[auxiliar1][6])
                    alterar_dados[auxiliar1][6] += auxiliar_alteração 
            elif opção_alteração == 7 : 
                    while loop_alteração == 'n' :
                            auxiliar_alteração = float(input('Digite a quantidade de papelão (em Kg), que será somada na tabela: '))
                            loop_alteração = input(f'A quantidade {auxiliar_alteração} está correta: (s/n)\n')
                    alterar_dados[auxiliar1][7] = float(alterar_dados[auxiliar1][7])
                    alterar_dados[auxiliar1][7] += auxiliar_alteração
            else: 
                menu() 
            continuar_alteração = input('Deseja continuar a alterar outro dado dado? (s/n)\n') 

    with open ('dados_catadores.csv', 'w', newline='',encoding='utf8') as csv_file :
            writer = csv.writer(csv_file, delimiter=';') 
            for line in alterar_dados : 
                    writer.writerow(line)

    tabela_de_dados = pt(['Nome','Contato','Contato de emergência','Quantidade ferro(kg)','Quantidade aluminio(kg)','Quantidade plástico(kg)','Quantidade isopor(kg)','Quantidade papelão(kg)','Total de pontos'])
    for i in  range (1,len(alterar_dados)) :
            tabela_de_dados.add_row(alterar_dados[i]) 
    print(tabela_de_dados) 
    menu()
    
def menu () :
    print("""
         --------menu---------
*****************************************
*1-Cadastrar catador                    *
*2-Metas                                *
*3-Dados dos meses                      *                   
*4-Materiais                            *
*5-Doações                              *
*6-Atualização de dados dos catadores   *
*7-Sair                                 *
*****************************************
""")
    opção = int(input("Digite a opção desejada:")) 
    while not 1 <= opção <= 7  :  
        opção = int(input("Digite a opção desejada de 1 a 7:")) 
    if opção == 1 : 
        cadastrar_catador() 
    elif opção == 2 : 
        metas_catador() 
    elif  opção == 3 : 
        dados_mês () 
    elif opção == 4 : 
        previsões_materiais() 
    elif opção == 5 : 
        doações()
    elif opção == 6 : 
        att_catadores()
    else : 
        sys.exit() 

menu()