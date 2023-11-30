import pyautogui as pg
import time
import pandas as pd

# Função para escolher qual sistema sera utilizado e a captura de login e senha do sistema
def logar():
    microsys = pg.prompt('Digite qual microsys? EX: SJC, MG, RJ,UBER,GOI,CAMP,SP,BH: ').lower()
    if microsys == "sjc":
         microsys = "microsys sjc"

    elif microsys == "mg":
         microsys = "microsys mg"

    elif microsys == "RJ":
         microsys = "microsys rj"

    elif microsys == "uber":
         microsys = "microsys uber"

    elif microsys == "camp":
         microsys = "microsys campinas"

    elif microsys == "goi":
         microsys = "microsys goianina"

    elif microsys == "sp":
         microsys = "microsys sp"

    elif microsys == "bh":
         microsys = "microsys bh"

    log = pg.prompt('Digite o Usuário: ')
    sen = pg.prompt('Digite a Senha: ')
    return microsys,log,sen

# Função para acesso ao microsys e adicionando Login e senha
def microsys(microsys,login,senha):
    time.sleep(3)
    pg.press('win')
    time.sleep(3)
    pg.write(microsys)
    time.sleep(3)
    pg.press("enter")
    time.sleep(4)
    if login == 'paul moraes' and senha == 'paul1289':
        time.sleep(3)
        pg.write(login)
        time.sleep(3)
        pg.press('tab')
        time.sleep(3)
        pg.write(senha)
        time.sleep(3)
        pg.press('enter')
        pg.press('enter')
        time.sleep(1)

# Função para acessar a configuração dos Usuários
def configurar():
    time.sleep(1)
    pg.click(x=429 , y=35)# Configuração
    time.sleep(2)
    pg.click(x=451,y=58)#usuarios
    time.sleep(2)
    pg.click(x=910,y=402)#Pesquisa

# Função para percorrer uma lista de usuários e verificar se esta ativo ou não
def pesquisa():
    #Opção só para pesquisa
        x_inicial=358
        y_inicial=165
        pg.moveTo(x_inicial,y_inicial)
        time.sleep(1)
        pg.mouseDown()
        x_final=121 
        y_final=165
        pg.moveTo(x_final, y_final)
        time.sleep(1)
        pg.mouseUp()
        time.sleep(1)
        pg.press('backspace')

# Função para desativar cadastros de Usuários
def desativarCadastro():
    #Continuação codigo 
    time.sleep(1)
    pg.press('enter')
    pg.click(x=748,y=478)# Campo Cadastro Ativo
    time.sleep(2)
    pg.click(x=714,y=512)#Cadastro Ativo Não
    time.sleep(2)
    pg.press('f5')
    time.sleep(2)
    pg.click(x=910,y=402)#Pesquisa
    time.sleep(2)

# Função para alertar que finalizou o Processo
def finalizou():
     pg.alert("Terminou")    

# Função para carregar a planilha e carregar a função de Pesquisar ou Desativar Cadastro
def planilha():
    dados = pd.read_csv("usuariosmicrosysmg.csv",sep=',', encoding="ISO-8859-1")
    dados['USU_NOME'] = dados['USU_NOME'].str.replace(';','')
    for index, row in dados.iterrows():
        nomes = row['USU_NOME']
        print(nomes)
        time.sleep(1)
        pg.click(x=271,y=168)#Formulario de pesquisa Microsys
        pg.write(nomes)
        pg.press('enter')
     
        # Função apenas para pesquisa
        # pesquisa()

        # #Continuação codigo d
        desativarCadastro()

#Chamando cada Função
micro,login,senha = logar()
microsys(micro,login,senha)
configurar()
planilha()
finalizou()
