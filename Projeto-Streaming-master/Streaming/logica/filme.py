filmes = []
cod_filme = 0

consultas = []
codigo_geral = 0

def _gerar_codigo():
    global codigo_geral
    codigo_geral += 1
    return codigo_geral

def adicionar_filme(titulo, genero, ano):
    filme = [gerar_cod_filme(),titulo, genero, ano]
    filmes.append(filme)

def listar_filmes():
    return filmes

def buscar_filme(cod_filme):
    for i in filmes:
        if (i[0] == cod_filme):
            return i
    return None

def buscar_filme_por_genero(genero):
    for i in filmes:
        if (i[2] == genero):
            return i
    return None

def remover_filme(cod_filme):
    for i in filmes:
        if (i[0] == cod_filme):
            filmes.remove[i]
            return True
    return False

def iniciar_filmes():
    adicionar_filme("Scarface", "Ação", 1983)
    adicionar_filme("Rambo", "Ação", 1982)
    
def gerar_cod_filme():
    global cod_filme
    cod_filme+=1
    return cod_filme
