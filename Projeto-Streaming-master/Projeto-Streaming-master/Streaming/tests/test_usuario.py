import unittest
from logica import usuario

class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        usuario.remover_todos_usuarios()

    def test_sem_usuarios(self):
        usuarios = usuario.listar_usuarios()
        self.assertEqual(0, len(usuarios))

    def test_adicionar_usuario(self):
        usuario.adicionar_usuario(40404040, "Han Solo", "cutechewie@millenium.com", "leiaandluke123")
        usuarios = usuario.listar_usuarios()
        self.assertEqual(1, len(usuarios))
        u = usuarios[0]
        self.assertEqual(40404040, u[0])
        self.assertEqual("Han Solo", u[1])
        self.assertEqual("cutechewie@millenium.com",u[2])
        self.assertEqual("leiaandluke123", u[3])

    def test_adicionar_dois_usuarios(self):
        usuario.adicionar_usuario(40404040, "Han Solo", "cutechewie@millenium.com", "leiaandluke123")
        usuario.adicionar_usuario(50505050, "Yoda", "ssfontrab@sehloiro.com", "melhorkatbr")
        usuarios = usuario.listar_usuarios()
        self.assertEqual(2, len(usuarios))

    def test_buscar_usuario(self):
        usuario.adicionar_usuario(40404040, "Han Solo", "cutechewie@millenium.com", "leiaandluke123")
        usuario.adicionar_usuario(50505050, "Yoda", "ssfontrab@sehloiro.com", "melhorkatbr")
        u = usuario.buscar_usuario(40404040)
        self.assertEqual(40404040, u[0])

    def test_remover_todos_usuarios(self):
        usuario.adicionar_usuario(40404040, "Han Solo", "cutechewie@millenium.com", "leiaandluke123")
        usuario.adicionar_usuario(50505050, "Yoda", "ssfontrab@sehloiro.com", "melhorkatbr")
        usuario.remover_todos_usuarios()
        u = usuario.listar_usuarios()
        self.assertEqual([], u)

    def test_iniciar_usuarios(self):
        usuario.iniciar_usuarios()
        usuarios = usuario.listar_usuarios()
        self.assertEqual(2, len(usuarios))
        

if __name__ == "__main__":
    unittest.main(exit=False)
