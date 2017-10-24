import unittest
import filme

class TestFilme(unittest.TestCase):
    
    def setUp(self):
        filme.remover_todos_filmes()

    def test_sem_filmes(self):
        filmes = filme.listar_filmes()
        self.assertEqual(0, len(filmes))

    def test_adicionar_filme(self):
        filme.adicionar_filme("Homem aranha", "Herói", 2001)
        filmes = filme.listar_filmes()
        self.assertEqual(1, len(filmes))
        f = filmes[0]
        self.assertEqual("Homem aranha", f[1])
        self.assertEqual("Herói", f[2])
        self.assertEqual(2001, f[3])

    def test_adicionar_dois_filmes(self):
        filme.adicionar_filme("Homem aranha", "Herói", 2001)
        filme.adicionar_filme("Filme y", "aventura", 2000)
        filmes = filme.listar_filmes()
        self.assertEqual(2, len(filmes))

    def test_buscar_filme(self):
        filme.adicionar_filme("Homem aranha", "Herói", 2001)
        filme.adicionar_filme("Filme y", "aventura", 2000)

        f = filme.buscar_filme(4)
        self.assertEqual(4, f[0])
        self.assertEqual("Homem aranha", f[1])

    def test_buscar_filme_por_genero(self):
        filme.adicionar_filme("Homem aranha", "Herói", 2001)
        filme.adicionar_filme("Filme y", "aventura", 2000)

        f = filme.buscar_filme_por_genero("Herói")
        x = len(f)
        for i in range(0,x):
            self.assertEqual("Herói", f[i][2])
           

    def test_remover_todos_filmes(self):
         filme.adicionar_filme("Homem aranha", "Herói", 2001)
         filme.adicionar_filme("Filme y", "aventura", 2000)

         filme.remover_todos_filmes()
         f = filme.listar_filmes()
         self.assertEqual([], f)

    def test_iniciar_filmes(self):
        filme.iniciar_filmes()
        filmes = filme.listar_filmes()
        self.assertEqual(5, len(filmes))

if __name__ == "__main__":
    unittest.main(exit=False)
