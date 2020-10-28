filmes = []
cod_filme = 0

consultas = []
codigo_geral = 0

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
    temp = []
    for i in filmes:
        if (i[2] == genero):
            temp.append(i)

    if temp != []:
        return temp
    else:
        return None

def remover_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            filmes.remove(f)
            return True
    return False

def remover_todos_filmes():
    global filmes
    filmes = []

def iniciar_filmes():
    adicionar_filme("Scarface", "Ação", 1983)
    adicionar_filme("Rambo", "Ação", 1982)
    adicionar_filme("Jamaica Abaixo de Zero", "Comédia", 2000)
    adicionar_filme("Hackers - Piratas do Computador", "Comédia", 1995)
    adicionar_filme("Nada", "", 2017)
    
    
def gerar_cod_filme():
    global cod_filme
    cod_filme+=1
    return cod_filme
