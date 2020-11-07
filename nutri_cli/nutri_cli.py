import cmd

from nutri_cli.lista_paciente import Lista_Paciente

class NutriCLI(cmd.Cmd):
    intro = 'Bem vindo ao Nutri CLI, Marina! Digite help ou ? para ver a lista de comandos\n'
    active = 'paciente'
    prompt = '({}): '.format(active)
    pacientes = Lista_Paciente()

    # funções basicas
    def do_bye(self, arg):
        'Finaliza o CLI'
        print('Obrigado por usar o Nutri CLI')
        return True

    # funções de pacientes

    def do_paciente(self, args):
        """
        Ações para criar, atualizar, selecionar e remover pacientes do sistema\n
        \t: -s <nome do paciente> >> retorna uma lista de nomes relacionados ao nome dado\n
        \t\tse houver apenas um nome na lista, este será selecionado\n
        \t: -s <nome do paciente> <numero> >> seleciona o paciente com o numero da posição na lista
        \t\tse houver apenas um nome na lista, este será selecionado\n
        \t: -u >> atualiza os dados do paciente ativo\n
        \t: -d >> deleta os dados do paciente ativo\n
        \t: -c >> cria o paciente na lista de pacientes\n
        """

        try:
            res = args.split(maxsplit=1)
            acao = res[0]
        
        except IndexError as identifier:
            if not self.pacientes.retorna_paciente():
                print('Lista vazia - insira pacientes para começar')
            else:
                print(self.pacientes.retorna_paciente())
        
        else:
            if acao == '-c': # criar paciente
                self.pacientes.insere_paciente()

            elif acao == '-s': # selecionar paciente
                print('selecionar paciente')
                if len(res) != 2:
                    res.append((input('Nome do paciente: ')))
                
                list_nomes = self.pacientes.retorna_paciente(res[1])
                if len(list_nomes) > 1:
                    print(self.pacientes.retorna_paciente(res[1]))
                elif len(list_nomes) == 1:
                    self.active = list_nomes[0]['nome']
                    self.prompt = '({}): '.format(self.active)
                else:
                    print('não foi encontrado pacientes com {}'.format(res[1]))
                    # TODO: iniciar o processo de criação de paciente


                # self.active = paciente
                # self.prompt = '({}): '.format(self.active)
            
            elif acao == '-u': # atualizar paciente
                print('atualizar paciente')
            
            elif acao == '-d': # deletar paciente
                print('deletar paciente')
            
            elif acao == '-f': # fechar paciente
                self.active = 'paciente'
                self.prompt = '({}): '.format(self.active)

    # funções de consultas

    def do_consulta(self, args):
        """
        Ações para criar, atualizar, selecionar e remover consultas do sistema\n
        \t: >> cria uma consulta direcionada ao paciente ativo\n
        \t: -l >> lista as consultas que o paciente ativo tem
        \t: -u >> atualiza os dados da consulta mais recente\n
        \t: -u <numero> >> atualiza os dados da consulta com o índice indicado\n
        \t: -d >> deleta as consultas do paciente ativo\n
        """

        if self.active == 'paciente':
            print('selecione um paciente primeiro')
            return
        print(args)

    # funções de calorias
    def do_calorias(self, args):
        print(args)