from logica import filme
from logica import historico
from logica import nota

def imprimir_filme(filme):
    codigo = filme[0]
    titulo = filme[1]
    genero = filme[2]
    ano = filme[3]
    avaliacao = nota.buscar_nota(codigo)
    
    
    print("Codigo do filme: ", codigo)
    print("Título: ", titulo)
    print("Gênero: ", genero)
    print("Ano: ", ano)
    print ("Avaliação: ", avaliacao)
    print()

def menu_avaliar():
    print ("\n Avaliar filme \n")
    codigo = int(input("Código do filme: "))
    avaliacao = int(input("Nota: "))
    while avaliacao < 0 and avaliacao > 5:
        avaliacao = int(input("Nota inválida. Digite apenas de 0 a 5"))
    ava = nota.adicionar_nota(codigo, avaliacao)

    print ("Filme avaliado")
    
    
    
def menu_adicionar():
    print("\n Adicionar filme \n")
    titulo = str(input("Título do filme: "))
    genero = str(input("Gênero: "))
    ano = int(input("Ano: "))
    adc = filme.adicionar_filme(titulo, genero, ano)
    print("Filme adicionado ao catálogo")
    
def menu_listar():
    print ("\n listar filmes \n")
    filmes = filme.listar_filmes()
    for i in filmes:
        imprimir_filme(i)
        
def menu_buscar():
    print ("\n Buscar filme \n")
    cod = int(input("Código: "))
    f = filme.buscar_filme(cod)
    if (f == None):
        print ("filme não encontrado")
    else:
        imprimir_filme(f)
    
        
def menu_buscar_por_gênero():
    print ("\n Buscar filme \n")
    gen = str(input("Gênero: "))
    f = filme.buscar_filme_por_genero(gen)
    if (f == None):
        print ("Gênero não encontrado")
    else:
        for i in f:
            imprimir_filme(i)

def menu_remover():
    print ("\nRemover filme do catálogo\n")
    codigo = int(input("Código: "))
    c = filme.remover_filme(codigo)
    if (c == False):
        print ("Filme não encontrado")
    else:
        print ("Filme removido do catálogo")

def menu_listar_historico():
    print("\n Listar histórico de filmes por usuário \n")
    cpf = int(input("CPF: "))
    h = historico.listar_filmes_assistidos(cpf)
    if (h == None):
        print("Não há filmes no seu histórico")
    else:
        for item in h:
            imprimir_filme(item)
        
def mostrar_menu():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar filme ao catálogo \n" +
             "(2) Listar filmes \n" +
             "(3) Buscar filme por código \n" +
             "(4) Buscar filme por gênero \n" +
             "(5) Remover filme do catálogo\n"
             "(6) Listar filmes assistidos \n" +
             "(7) Avaliar filme \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_filme):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_buscar_por_gênero()
        elif (op == 5):
            menu_remover()
        elif (op == 6):
            menu_listar_historico()
        elif (op == 7):
            menu_avaliar()
        elif (op == 0):
            run_filme = False

if __name__ == "__main__":
    mostrar_menu()

        
        
