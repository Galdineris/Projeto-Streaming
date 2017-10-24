import unittest
import historico

class TestHistorico(unittest.TestCase):
    
    def test_registrar_filme(self):
        historico.registrar_filme_assistido(303030, 1)
        historicos = historico.listar_filmes_assistidos(303030)
        self.assertEqual(2, len(historicos))

if __name__ == "__main__":
    unittest.main(exit = False)


        
        
