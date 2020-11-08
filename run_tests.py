import unittest

from testes.pacientes_teste import PacientesTestes
from testes.consultas_teste import ConsultaTestes

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PacientesTestes('deleta_de_vazio'))
    suite.addTest(PacientesTestes('retorna_vazio'))
    suite.addTest(PacientesTestes('retorna_vazio_nome'))
    suite.addTest(PacientesTestes('teste_insere'))
    suite.addTest(PacientesTestes('teste_atualiza'))
    suite.addTest(PacientesTestes('teste_insere_multiplo'))
    
    suite.addTest(ConsultaTestes('retorna_sem_chave'))
    suite.addTest(ConsultaTestes('teste_insere'))
    suite.addTest(ConsultaTestes('teste_retorna_espec_vazio'))
    suite.addTest(ConsultaTestes('retorna_ultima_consulta'))
    suite.addTest(ConsultaTestes('teste_atualiza'))
    suite.addTest(ConsultaTestes('teste_delete'))


    runner = unittest.TextTestRunner()
    runner.run(suite)