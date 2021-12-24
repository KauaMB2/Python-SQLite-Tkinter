import sqlite3
from sqlite3 import Error
import os
#Localizando o arquivo do banco de dados
pastaApp = os.path.dirname(__file__) #Encontra a localização do arquivo no PC
nomeBanco = pastaApp + "\\dados.db" #Soma a localização do arquivo com o banco
#Conexão com o banco
def ConexaoBanco(): #função de conexão com o banco de dados
    con = None #Valor vazio
    try: #Tenta os comandos abaixo
        con = sqlite3.connect(nomeBanco) #Tenta conectar
    except Error as ex: #Caso não tenha conectado
        print(ex) #Printa o erro
    return con #Retorna o valor de con para a função ConexaoBanco()
###########################################################
def dql(query): #SELECT
    vcon = ConexaoBanco() #Tenta estabelecer uma conexão com o banco
    c = vcon.cursor() #Cursor de vcon
    c.execute(query) #Executa a query
    res = c.fetchall() #Retorna o resultado para a variável res
    vcon.close() #Fecha a conexão com o banco de dados
    return res #retorna o valor de res para a função dql
###########################################################
def dml(query): #INSERT, UPDATE, DELETE
    try:
        vcon = ConexaoBanco() #Tenta estabelecer uma conexão com o banco 
        c = vcon.cursor() #Cursor de vcon
        c.execute(query) #Executa a query
        vcon.commit() #Faz o envio da informação
        vcon.close() #Fecha a conexão com o banco de dados
    except Error as ex: #Caso não tenha dado certo o envio ou atualização ou deletar
        print(ex) #Exibe o erro