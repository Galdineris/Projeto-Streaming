from logica import usuario

def imprimir_usuario(usuario):
    cpf = usuario[0]
    nome = usuario[1]
    email = usuario[2]
    senha = usuario[3]
    
    print ("Nome: ", nome)
    print ("CPF do usuário: ", cpf)
    print ("E-mail do usuário: ", email)
    print ("Senha do usuário: ", senha)
    
    print()
    
def menu_adicionar():
    print("\n Adicionar Usuário \n")
    nome = str(input("Insira o nome do usuário: "))
    cpf = int(input("Insira o CPF: "))
    email = str(input("Insria o e-mail: "))
    senha = str(input("Insira a senha: "))
    
    user = usuario.adicionar_usuario(cpf, nome, email, senha)
    print ("Usuário incluso")
    
def menu_listar():
    print ("\n Listar usuários \n")
    usuarios = usuario.listar_usuarios()
    for i in usuarios:
        imprimir_usuario(i)

def menu_buscar():
    print ("\n Listar Usuários \n")
    cod = int(input("CPF do usuário: "))
    c = usuario.buscar_usuario(cod)
    if (c == None):
        print ("Usuário não localizado")
    else:
        imprimir_usuario(c)
        
def menu_remover():
    print ("\n Remover usuário \n")
    codigo = int(input("CPF do usuário: "))
    user = usuario.remover_usuario(codigo)
    if (user == False):
        print ("Usuário não encontrado")
    else:
        print("Usuário removido")
    
def mostrar_menu():
    run_usuario = True
    menu = ("\n----------------\n"+
             "(1) Adicionar usuário \n" +
             "(2) Listar Usuários \n" +
             "(3) Buscar usuário por código \n" +
             "(4) Remover usuário \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_usuario):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run_consulta = False
        
