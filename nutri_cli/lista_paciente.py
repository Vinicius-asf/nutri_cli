
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
            return qtd_telefones('Insira um número maior do que zero: ')
    return qtd

class Lista_Paciente():
    lista_de_pacientes = [
        {
            'nome': 'vinicius',
            'email': 'vini@gmail.com'
        },
        {
            'nome': 'vitor',
            'email': 'vitor@hotmail.com'
        },
    ]

    def insere_paciente(self):
        """
        Inicia o processo de inserção de um paciente na lista
        """
        paciente = {}
        paciente['nome'] = input('Nome: ')
        paciente['endereco'] = input('Endereço: ')
        n_telefones = qtd_telefones()
        paciente['telefones'] = [input('Telefone {}: '.format(x)) for x in range(1,n_telefones+1)]
        paciente['email'] = input('Email: ')
        paciente['nascimento'] = input('Data de nascimento: ')
        self.lista_de_pacientes.append(paciente)

    def print_paciente(self, nome):
        """
        Lista no console os dados de pacientes com o nome dado
        """
        lista = [paciente for paciente in self.lista_de_pacientes if paciente['nome'].startswith(nome)]
        if len(lista) > 0:
            for paciente in lista:
                print('ID:{}'.format(lista.index(paciente)))
                for param, val in paciente.items():
                    print('{}:{}\t'.format(param,val), end=' ')
                print('\n____________________________________________')

    def retorna_paciente(self, nome=False):
        """
        Retorna uma lista de pacientes com o nome dado ou a lista toda caso não houver o que procurar
        """
        if nome:
            self.print_paciente(nome)
            return [paciente for paciente in self.lista_de_pacientes if paciente['nome'].startswith(nome)]
        else:
            self.print_paciente('')
            return self.lista_de_pacientes
    
    def atualiza_paciente(self, paciente):
        """
        Atualiza os dados do paciente e retorna os novos dados
        """
        novo_paciente = {}
        novo_paciente['nome'] = input('Nome: ')
        novo_paciente['endereco'] = input('Endereço: ')
        n_telefones = qtd_telefones()
        novo_paciente['telefones'] = [input('Telefone {}: '.format(x)) for x in range(1,n_telefones+1)]
        novo_paciente['email'] = input('Email: ')
        novo_paciente['nascimento'] = input('Data de nascimento: ')
        
        self.lista_de_pacientes[self.lista_de_pacientes.index(paciente)] = novo_paciente
        return novo_paciente
    
    def deleta_paciente(self, paciente):
        """
        Deleta o paciente da lista de pacientes. Remove os dados de consultas também
        """
        return self.lista_de_pacientes.pop(self.lista_de_pacientes.index(paciente))

    def limpa_lista(self, parameter_list):
        """
        docstring
        """
        pass