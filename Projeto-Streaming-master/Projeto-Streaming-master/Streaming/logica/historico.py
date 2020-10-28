from logica import filme
from logica import usuario

historico = []


def registrar_filme_assistido(cod_filme, cpf):
    h1 = [cpf, cod_filme]
    historico.append(h1)

def listar_historico():
    return historico

def listar_filmes_assistidos(cpf):
    temp = []

    for item in historico:
        if cpf == item[0]:
            print(item[0])
            print(item[1])
            temp.append(filme.buscar_filme(item[1]))
    if temp == []:
        return None
    else:
        return temp

def remover_historico():
    global historico
    historico = []
