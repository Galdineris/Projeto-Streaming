import unittest
from logica import nota

class TestNota(unittest.TestCase):

    def setUp(self):
        nota.remover_todas_notas()

    def test_sem_notas(self):
        notas =nota.listar_notas()
        self.assertEqual(0, len(notas))

    def test_adicionar_nota(self):
        nota.adicionar_nota(1,1)
        notas = nota.listar_notas()
        self.assertEqual(1, len(notas))

    def test_adicionar_duas_notas(self):
        nota.adicionar_nota(1,1)
        nota.adicionar_nota(2,1)
        notas = nota.listar_notas()
        self.assertEqual(2, len(notas))

    def test_buscar_notas(self):
        nota.adicionar_nota(1, 1)
        nota.adicionar_nota(2, 1)
        n = nota.buscar_nota(1)
        self.assertEqual(1, n)
