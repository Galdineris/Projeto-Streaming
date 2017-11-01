import unittest
from logica import historico

class TestHistorico(unittest.TestCase):

    def setUp(self):
        historico.remover_historico()

    def test_sem_historico(self):
        historicos = historico.listar_historico()
        self.assertEqual(0, len(historicos))
    
    def test_registrar_filme(self):
        historico.registrar_filme_assistido(1, 303030)
        historicos = historico.listar_historico()
        self.assertEqual(1, len(historicos))

    def test_registrar_dois_filmes(self):
        historico.registrar_filme_assistido(1,303030)
        historico.registrar_filme_assistido(2,303030)
        historicos = historico.listar_historico()
        self.assertEqual(2, len(historicos))


    def test_listar_historico(self):

if __name__ == "__main__":
    unittest.main(exit = False)


        
        
