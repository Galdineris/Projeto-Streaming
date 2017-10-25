from logica import filme

def ver_filme(cod_filme):
    f = filme.buscar_filme(cod_filme)
    if f == None:
        return None
    else:
        print("Assistindo: ", f[1])
        print()
        print()
        print("Filme finalizado!")
        return f
    
    
