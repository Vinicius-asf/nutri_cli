
def qtd_telefones(text = False):
    try:
        if text:
            qtd = int(input(text))
        else:
            qtd = int(input('Quantidade de telefones para registrar: '))
    except ValueError as identifier:
        return qtd_telefones('Insira somente numeros inteiros: ')
    else:
        if qtd <= 0:
            return qtd_telefones('Insira um número maior do que zero:')
    return qtd

class Lista_Paciente():
    lista_de_pacientes = [
        {'nome':'vinicius'},
        {'nome':'vitor'},
    ]

    def insere_paciente(self):
        """
        docstring
        """
        paciente = {}
        paciente['nome'] = input('Nome: ')
        paciente['endereco'] = input('Endereço: ')
        n_telefones = qtd_telefones()
        paciente['telefones'] = [input('Telefone {}: '.format(x)) for x in range(1,n_telefones+1)]
        paciente['e-mail'] = input('E-mail: ')
        paciente['nascimento'] = input('Data de nascimento: ')
        self.lista_de_pacientes.append(paciente)

    def retorna_paciente(self, nome=False):
        if nome:
            return [paciente for paciente in self.lista_de_pacientes if paciente['nome'].startswith(nome)]
        else:
            return self.lista_de_pacientes
    
    def atualiza_paciente(self, parameter_list):
        """
        docstring
        """
        pass
    
    def deleta_paciente(self, parameter_list):
        """
        docstring
        """
        pass

    def limpa_lista(self, parameter_list):
        """
        docstring
        """
        pass