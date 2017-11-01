notas = {}

def adicionar_nota(cod_filme, nota):
    cod = str(cod_filme)
    if cod in notas:
        n1 = notas[cod]
        n1 = (nota+n1)/2
        notas[cod] = n1
    else:
        notas[cod] = nota

def listar_notas():
    return notas

def buscar_nota(cod_filme):
    cod = str(cod_filme)
    if cod in notas:
        n1 = notas[cod]
        return n1
    else:
        return None

def inicializar_nota():
    adicionar_nota(0, 5)
    adicionar_nota(1, 4.75)
    adicionar_nota(2, 3)

def remover_todas_notas():
    global notas
    notas = {}

    
    
