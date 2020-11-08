import unittest
from unittest import mock
from unittest.mock import patch

from nutri_cli.lista_paciente import Lista_Paciente

paciente_teste = dict(nome='vinicius',endereco='rua 123',telefone=['12312312'],email='vini@gmail.com',nascimento='1/1/2001')

class PacientesTestes(unittest.TestCase):
    def setUp(self,):
        self.pacientes = Lista_Paciente()
        self.pacientes.lista_de_pacientes
    
    def deleta_de_vazio(self):
        with self.assertRaises(IndexError):
            self.pacientes.deleta_paciente(dict(nome='vinicius'))

    def retorna_vazio(self):
        self.assertEqual(self.pacientes.retorna_paciente(),[])
    
    def retorna_vazio_nome(self):
        self.assertEqual(self.pacientes.retorna_paciente(dict(nome='vinic')),[])
    # ['vinicius','rua 123','1','12312312','vini@gmail.com','1/1/2001']

    @patch('builtins.input', side_effect=['vinicius','rua 123','1','12312312','vini@gmail.com','1/1/2001'])
    def teste_insere(self, mock_input):
        self.pacientes.insere_paciente()
        self.assertGreater(len(self.pacientes.retorna_paciente()),0)
    
    @patch('builtins.input', side_effect=['vitor','rua 123','1','12312312','vitor@gmail.com','1/1/2001'])
    def teste_atualiza(self, mock_input):
        self.pacientes.atualiza_paciente(self.pacientes.lista_de_pacientes[0])
        self.assertEqual(len(self.pacientes.retorna_paciente()),1)
    
    @patch('builtins.input', side_effect=['vitor','rua 123','1','12312312','vini@gmail.com','1/1/2001','vinicius','rua 123','1','12312312','vitor@gmail.com','1/1/2001','andre','rua 123','1','12312312','andre@gmail.com','1/1/2001'])
    def teste_insere_multiplo(self, mock_input):
        self.pacientes.insere_paciente()
        self.pacientes.insere_paciente()
        self.pacientes.insere_paciente()
        self.assertEqual(len(self.pacientes.retorna_paciente()),4)

if __name__ == "__main__":
    unittest.main()