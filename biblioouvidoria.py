from operacoesbd import *

#Funções de listar
def listarReclamacoes(conexao):

    listarReclamacoesSQL = "SELECT * FROM reclamacoes"

    listandoReclamacoes = listarBancoDados(conexao,listarReclamacoesSQL)

    return listandoReclamacoes

def listarSugestoes(conexao):

    listarSugestoesSQL = "SELECT * FROM sugestoes"

    listandoSugestoes = listarBancoDados(conexao,listarSugestoesSQL)

    return listandoSugestoes

def listarElogios(conexao):

    listarElogiosSQL = "SELECT * FROM elogios"

    listandoElogios = listarBancoDados(conexao,listarElogiosSQL)

    return  listandoElogios

#Funções de criar
def inserirReclamacoes(conexao,nome,assunto,reclamacao):

    inserirReclamacoesSQL = "INSERT INTO reclamacoes (nome,assunto,reclamacao) values(%s,%s,%s)"

    dados = (nome,assunto,reclamacao)

    inserindoReclamacoes = insertNoBancoDados(conexao,inserirReclamacoesSQL,dados)

    return inserindoReclamacoes


def inserirSugestoes(conexao, nome, assunto, sugestao):

    inserirSugestoesSQL = "INSERT INTO sugestoes (nome,assunto,sugestao) values(%s,%s,%s)"

    dados = (nome, assunto, sugestao)

    inserindoSugestoes = insertNoBancoDados(conexao, inserirSugestoesSQL, dados)

    return inserindoSugestoes

def inserirElogios(conexao, nome, assunto, elogio):
    
    inserirElogiosSQL = "INSERT INTO elogios (nome,assunto,elogio) values(%s,%s,%s)"
    
    dados = (nome,assunto,elogio)
    
    inserindoElogios = insertNoBancoDados(conexao, inserirElogiosSQL, dados)
    
    return inserindoElogios

#Funções de listar pelo código
def listarCodigoReclamacoes(conexao,codigo):

    listarCodigoRecSQL = "SELECT * FROM reclamacoes WHERE codigo = %s"

    dados = (codigo,)

    listandoCodigoReclamacoes = listarBancoDados(conexao,listarCodigoRecSQL,dados)
    
    return listandoCodigoReclamacoes

def listarCodigoSugestoes(conexao,codigo):
    listarCodigoSugSQL = "SELECT * FROM sugestoes WHERE codigo = %s"

    dados = (codigo,)

    listandoCodigoSugestoes = listarBancoDados(conexao, listarCodigoSugSQL, dados)
    
    return listandoCodigoSugestoes
    
def listarCodigoElogios(conexao,codigo):
    listarCodigoEloSQL = "SELECT * FROM elogios WHERE codigo = %s"
    
    dados = (codigo,)
    
    listandoCodigoElogios = listarBancoDados(conexao,listarCodigoEloSQL,dados)
    
    return listandoCodigoElogios

#Funções para exclusão por código
def excluirReclamacoes(conexao,codigo):
    excluirReclamacaoSQL = "DELETE FROM reclamacoes WHERE codigo = %s"

    dados = (codigo,)

    excluindoReclamacao = excluirBancoDados(conexao,excluirReclamacaoSQL,dados)

    return excluindoReclamacao

def excluirSugestoes(conexao,codigo):
    excluirSugestaoSQL = "DELETE FROM reclamacoes WHERE codigo = %s"

    dados = (codigo,)

    excluindoSugestao = excluirBancoDados(conexao,excluirSugestaoSQL,dados)

    return excluindoSugestao

def excluirElogios(conexao,codigo):
    excluirElogioSQL = "DELETE FROM elogios WHERE codigo = %s"

    dados = (codigo,)

    excluindoElogio = excluirBancoDados(conexao,excluirElogioSQL,dados)

    return excluindoElogio

