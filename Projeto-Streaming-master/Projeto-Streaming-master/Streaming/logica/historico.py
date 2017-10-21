from logica import filme
from logica import usuario

historico = []


def registrar_filme_assistido(cod_filme, cpf):
    historico.append[cpf, cod_filme]

def listar_filmes_assistidos(cpf):
    temp = []

    for item in historico:
        if cpf == item[0]:
            temp.append(filme.buscar_filme(item[1]))
        return temp

    return None
