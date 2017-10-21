usuarios = []


def adicionar_usuario(cpf, nome, email, senha):
    usuario = [cpf, nome, email, senha]
    usuarios.append(usuario)
    
def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for i in usuarios:
        if (i[0] == cpf):
            return i
    return None

def remover_usuario(cpf):
    for i in usuarios:
        if (i[0] == cpf):
            usuarios.remove(i)
            return True
    return False 

def iniciar_usuarios():
    adicionar_usuario(30303030, "Luke Skywalker", "luky_force@jedi.com", "leiaandsolo123")
    adicionar_usuario(20202020, "Umaru", "umaru-chan@shinigamitensei.com", "oniichan")