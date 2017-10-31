from logica import filme
from GUI import menu_filme

from logica import usuario
from GUI import menu_usuario

from logica import nota

def inicializar_dados():
    filme.iniciar_filmes()
    usuario.iniciar_usuarios()
    nota.iniciar_nota()
    
def mostrar_menu():
    run_menu = True
    
    inicializar_dados()
    
    menu = ("\n----------------\n"+
             "(1) Menu Filme \n" +
             "(2) Menu Usuário \n" +
             "(0) Sair\n"+
            "----------------")
    while (run_menu):
        print(menu)
        op = int(input("Digite sua escolha: "))
        
        if (op == 1):
            menu_filme.mostrar_menu()
        elif (op == 2):
            menu_usuario.mostrar_menu()
        elif (op == 0):
            print("Saindo")
            run_menu == false
        else:
            print ("Valor invalido")
            
