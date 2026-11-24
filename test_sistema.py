import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from cadastrar import cadastrar
from consultar import consultar
from listar import listar
from excluir import excluir


class TestSistema(unittest.TestCase):
    def setUp(self):
        pasta = tempfile.TemporaryDirectory()
        self.addCleanup(pasta.cleanup)
        self.arquivo = Path(pasta.name) / "alunos.json"
        patcher = patch("armazenamento.ARQUIVO", self.arquivo)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_fluxo_completo_e_persistencia(self):
        self.assertEqual(listar(), [])
        cadastrar("2", "Bruno", "Computação")
        cadastrar("1", "Ana", "Engenharia")
        self.assertTrue(self.arquivo.exists())
        self.assertEqual(consultar(" 1 ")["nome"], "Ana")
        self.assertEqual([m for m, a in listar()], ["1", "2"])
        self.assertTrue(excluir("1"))
        self.assertIsNone(consultar("1"))
        self.assertFalse(excluir("999"))
        self.assertEqual(len(listar()), 1)

    def test_duplicado_e_campos_vazios(self):
        cadastrar("1", "Ana", "Computação")
        with self.assertRaises(ValueError):
            cadastrar("1", "Outro", "Outro")
        for dados in [("", "Ana", "Curso"), ("2", " ", "Curso"), ("2", "Ana", "")]:
            with self.assertRaises(ValueError):
                cadastrar(*dados)
        self.assertEqual(consultar("1")["nome"], "Ana")

    def test_arquivo_invalido_preservado(self):
        self.arquivo.write_text("inválido", encoding="utf-8")
        with self.assertRaises(ValueError):
            cadastrar("1", "Ana", "Curso")
        self.assertEqual(self.arquivo.read_text(encoding="utf-8"), "inválido")


if __name__ == "__main__":
    unittest.main()
