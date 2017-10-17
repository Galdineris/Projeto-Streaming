filmes = []
cod_filme = 0

def adicionar_filme(titulo, genero, ano):
    filme = [titulo, genero, ano]
    filmes.append(filme)

def listar_filmes():
    return filmes

def buscar_filme(cod_filme):
    for i in filmes:
        if (i[0] == cod_filme):
            return i
    return None

def buscar_filme_por_genero(genero):
    pass

def remover_filme(cod_filme):
    for i in filmes:
        if (i[0] == cod_filme):
            filmes.remove[i]
            return True
    return False

def iniciar_filmes():
    adicionar_filme("Scarface", "ação", 1983)
    adicionar_filme("Rambo", "ação", 1982)
    
def gerar_cod_filme():
    global cod_filme
    cod_filme+=1
    return cod_filme