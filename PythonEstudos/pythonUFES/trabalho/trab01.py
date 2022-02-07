import sys 
import csv  

def loop_maquina (maquina) : 
    if maquina == "maquina1" : 
        return(1) 
    elif maquina == "maquina2" : 
        return(1) 
    elif maquina == "maquina3" : 
        return(1) 
    else: 
        return(0)

def Indicador_de_Desempenho(dadosMaquina1) :
    tmEntreFalhas1 = dadosMaquina1[1][3] / dadosMaquina1[1][12]
    indDesem = ( tmEntreFalhas1 / ( tmEntreFalhas1 + dadosMaquina1[1][5] ) ) * 100
    print(f" O indicador de desempenho é de {indDesem:.2f}%")
    return(menu(dadosMaquina1))

def indicadores_de_Disponibilidade (dadosMaquina2) :
    tempoManutenção = dadosMaquina2[1][10]/24
    tempoCalendário = dadosMaquina2[1][9] * 30 
    indiDisp =  ( ( tempoCalendário - tempoManutenção ) / tempoCalendário ) * 100
    print(f'A disponibilidade é {indiDisp:.2f}%') 
    return(menu(dadosMaquina2))
 
def Indicador_de_Confiabilidade(dadosMaquina3) :
    indiConf = ( dados_de_maquina[1][3] / dadosMaquina3[1][0])
    print(f" O indicador de confiabilidade é de {indiConf:.2f}")
    return(menu(dadosMaquina3))

def taxa_de_falha(dadosMaquina4) : 
    taxaFalha = dadosMaquina4[1][0]/(dadosMaquina4[1][1]*dadosMaquina4[1][2])
    print(f'A taxa de falhas é de {taxaFalha:.2f}%')
    return(menu(dadosMaquina4))

def tempo_medio_entre_falhas(dadosMaquina5) : 
    TMEF = dadosMaquina5[1][3] / dadosMaquina5[1][12]
    print(f'O tempo médio entre falhas é {TMEF:.2f}dias') 
    return(menu(dadosMaquina5)) 

def menu (dados_de_maquina) : 
    print("""
              -=Menu=-
***************************************
*1- Indicadores de desempenho         *  
*2- Indicadores de disponibilidade    *
*3- Indicadores de confiabilidade     * 
*4- Taxa de falha                     * 
*5- Tempo médio entre falhas          *
*6- Sair                              *
***************************************""")
    opção = int(input("Digite a opção desejada:")) 
    while not 1 <= opção <= 6  :  
        opção = int(input("Digite a opção desejada de 1 a 6:"))        
    if opção == 1 :
        Indicador_de_Desempenho(dados_de_maquina)
    elif opção == 2 : 
        indicadores_de_Disponibilidade(dados_de_maquina)
    elif opção == 3 : 
        Indicador_de_Confiabilidade(dados_de_maquina)
    elif opção == 4 :     
        taxa_de_falha(dados_de_maquina)
    elif opção == 5 :   
        tempo_medio_entre_falhas(dados_de_maquina)
    else :
        sys.exit() 

maquina  =  str(input("Digite o nome do arquivo csv que você deseja analisar(maquina1,maquina2 ou maquina3): \n"))
loop1 = loop_maquina(maquina)
while loop1  == 0 : 
    maquina  =  str(input("Digite corretamente o nome do arquivo csv que você deseja analisar(maquina1,maquina2 ou maquina3): \n"))
    loop1 = loop_maquina(maquina)
maquina = "dados_"+maquina+".csv"
print(maquina)
dados_de_maquina = []
with open(maquina, 'r', encoding='utf8') as csv_file : 
    leitor = csv.reader(csv_file, delimiter = ';')
    for linha in leitor : 
        dados_de_maquina.append(linha) 
for i in range (0,13):  
    dados_de_maquina[1][i] = int(dados_de_maquina[1][i]) 
print(dados_de_maquina)
menu(dados_de_maquina) 