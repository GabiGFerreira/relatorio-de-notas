import unittest

from gerenciamento_de_notas import calcular_media, verificar_aprovacao



class TestCalcularMedia(unittest.TestCase):
    def test_calcular_media(self):
        result = calcular_media([7, 3.5, 6])
        self.assertEqual(result, 5.5)

class TestMediaComListaVazia(unittest.TestCase):
    def test_calcular_media(self):
        result = calcular_media([])
        self.assertEqual(result, 0)
   
class VerificarAprovacaoMediaMinima0(unittest.TestCase):
    def test_aprovacao_com_media_zero(self):
        result = verificar_aprovacao(0, media_minima=0)
        self.assertEqual(result, "Aprovado")

class VerificarAprovacaoMediaCorte(unittest.TestCase):
    def test_aprovacao_com_media_corte(self):
        result = verificar_aprovacao(7)
        self.assertEqual(result, "Aprovado")

class VerificarReprovacaoMediaBaixa(unittest.TestCase):
    def test_reprovacao_media_baixa(self):
        result = verificar_aprovacao(6)
        self.assertEqual(result, "Reprovado")
 

if __name__ == '__main__':
    unittest.main()


