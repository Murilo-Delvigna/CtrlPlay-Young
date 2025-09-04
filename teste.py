import unittest
from aula14 import sobrenomeordem

class NomeTest(unittest.TestCase):

    def test_sobrenomenaordem(self):

        nomeCompleto = sobrenomeordem("Joao", "Madureira", "silva")
        self.assertEqual(nomeCompleto, "Joao Madureira Silva")

unittest.main(argv= [''],exit=False)