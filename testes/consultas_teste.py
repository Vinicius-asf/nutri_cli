import unittest
from unittest import mock
from unittest.mock import patch

from nutri_cli.lista_consulta import Lista_Consulta

consulta_teste = dict(x=1)

class ConsultaTestes(unittest.TestCase):

    def setUp(self):
        self.consultas = Lista_Consulta()
        self.paciente = dict(nome='vinicius',endereco='rua 123',telefone=['12312312'],email='vini@gmail.com',nascimento='1/1/2001')
    
    def retorna_sem_chave(self):
        with self.assertRaises((KeyError)):
            self.consultas.retornar_consulta(self.paciente)
    
    def teste_retorna_vazio(self):
        with self.assertRaises(IndexError):
            self.consultas.retornar_consulta(self.paciente)
    
    # @patch('builtins.input', side_effet=1)
    def teste_retorna_espec_vazio(self):
        with self.assertRaises(IndexError):
            self.consultas.retornar_consulta(self.paciente,2)

    def retorna_ultima_consulta(self):
        self.assertEqual(type(self.consultas.retorna_ultima_consulta(self.paciente)),dict)

    @patch('builtins.input', side_effect=[12,12,'asdasd','asdasda'])
    def teste_insere(self, mock_input):
        self.consultas.cria_consulta(self.paciente)
        self.assertEqual(len(self.consultas.listar_consultas(self.paciente)),1)
    
    @patch('builtins.input', side_effect=[21,21,'qweqweqw','qwqweqweq'])
    def teste_atualiza(self, mock_input):
        ultima_consulta = consulta_teste
        with self.assertRaises(IndexError):
            self.consultas.atualiza_consulta(ultima_consulta,self.paciente)
    
    def teste_delete(self):
        ultima_consulta = consulta_teste
        with self.assertRaises((IndexError,ValueError)):
            self.consultas.deleta_consulta(self.paciente,ultima_consulta)