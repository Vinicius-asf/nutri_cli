from datetime import datetime, time


class Lista_Consulta():
    lista_de_consultas = {
        'vinicius':[],
        'vitor':[],
    }

    # lista_de_consultas
    # - {paciente 1: [
    # - - consulta 1
    # - - consulta 2 ]}
    # - {paciente 2: [
    # - - consulta 1 ]}

    def listar_consultas(self, paciente=False):
        """
        Lista as consultas do paciente ou a quantidade de consultas de todos os pacientes
        """
        # print(paciente)
        # print(self.lista_de_consultas[paciente['nome']])
        if paciente:
            if not self.lista_de_consultas[paciente['nome']]:
                print('Paciente sem consultas')
                return
            for consulta in self.lista_de_consultas[paciente['nome']]:
                print('Consulta {}'.format(self.lista_de_consultas[paciente['nome']].index(consulta)))
                for param, val in consulta.items():
                    print('{}:{}\t'.format(param,val), end=' ')
                print('\n____________________________________________')
        
        elif len(self.lista_de_consultas) > 0:
            for paciente, consultas in self.lista_de_consultas.items():
                print('Paciente: {}\t-- {} consultas'.format(paciente, len(consultas)))

    def retorna_ultima_consulta(self, paciente):
        """
        Retorna a última consulta do paciente informado
        """
        if self.lista_de_consultas[paciente['nome']]:
            return self.lista_de_consultas[paciente['nome']][len(self.lista_de_consultas[paciente['nome']])-1]
        else:
            raise Exception('não existe consulta')
    
    def retornar_consulta(self, paciente, idx=False):
        """
        Retornar a consulta informada do paciente informado
        """

        if not self.lista_de_consultas[paciente['nome']]:
            raise Exception('não existe consulta')
        elif idx > len(self.lista_de_consultas[paciente['nome']])-1:
            raise Exception('não existe consulta')
        else:
            return self.lista_de_consultas[paciente['nome']][idx]

    def cria_consulta(self, paciente):
        """
        Processo de criação de uma consulta nova do paciente dado
        """
        consulta = {}
        # tempo = datetime.now().date()
        consulta['data'] = datetime.now().date()
        consulta['horario'] = datetime.now().time()
        consulta['peso'] = int(input('Peso: '))
        consulta['gordura'] = int(input('Porcentagem de gordura corporal: '))
        consulta['sensacao'] = input('Sensação física: ')
        consulta['restricao'] = input('Restrições alimentares: ')
        self.lista_de_consultas.setdefault(paciente['nome'],[])
        self.lista_de_consultas[paciente['nome']].append(consulta)        

    def atualiza_consulta(self, consulta, paciente):
        """
        Atualiza a consulta dada do paciente informado
        """
        if consulta not in self.lista_de_consultas[paciente['nome']]:
            raise Exception('Consulta não existe para este paciente')

        nova_consulta = {}
        nova_consulta['data'] = consulta['data']
        nova_consulta['horario'] = consulta['horario']
        nova_consulta['peso'] = input('Peso: ')
        nova_consulta['gordura'] = input('Porcentagem de gordura corporal: ')
        nova_consulta['sensacao'] = input('Sensação física: ')
        nova_consulta['restricao'] = input('Restrições alimentares: ')

        self.lista_de_consultas[paciente['nome']][self.lista_de_consultas[paciente['nome']].index(consulta)] = nova_consulta
        

    def deleta_consulta(self, paciente, consulta=False):
        """
        docstring
        """
        try:
            if consulta:
                return self.lista_de_consultas[paciente['nome']].pop(self.lista_de_consultas[paciente['nome']].index(consulta))
            else:
                return self.lista_de_consultas[paciente['nome']].pop(len(self.lista_de_consultas[paciente['nome']])-1)
        except IndexError as identifier:
            print('não tem consulta')
            return
