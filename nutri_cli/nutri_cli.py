import cmd

from nutri_cli.lista_paciente import Lista_Paciente

def seleciona_item_lista(lista, texto = False):
    try:
        if texto:
            idx = int(input(texto))
        else:
            idx = int(input('Selecione um ID: '))
    except ValueError as identifier:
        return seleciona_item_lista(lista, 'Insira somente numeros inteiros: ')
    else:
        if idx > len(lista):
            return seleciona_item_lista(lista, 'Insira um número correto: ')
    return idx

class NutriCLI(cmd.Cmd):
    intro = 'Bem vindo ao Nutri CLI, Marina! Digite help ou ? para ver a lista de comandos\n'
    active = {'nome' : 'paciente'}
    idp = 0
    prompt = '({}): '.format(active['nome'])
    pacientes = Lista_Paciente()

    # funções basicas
    def do_bye(self, arg):
        'Finaliza o CLI'
        print('Obrigado por usar o Nutri CLI')
        return True

    def atualizar_prompt(self, active):
        self.active = active
        self.prompt = '({}): '.format(self.active['nome'])

    # funções de pacientes

    def do_paciente(self, args):
        """
        Ações para criar, atualizar, selecionar e remover pacientes do sistema
        \t: -s <nome do paciente> >> seleciona paciente a partir de uma lista de nomes parecidos ao nome dado
        \t\tse houver apenas um nome na lista, este será selecionado\n
        \t: -u >> atualiza os dados do paciente ativo\n
        \t: -d >> deleta os dados do paciente ativo\n
        \t: -c >> cria o paciente na lista de pacientes\n
        \t: -f >> fecha o paciente ativo\n
        """

        try:
            res = args.split(maxsplit=1)
            acao = res[0]
        
        except IndexError as identifier:
            if not self.pacientes.retorna_paciente():
                print('Lista vazia - insira pacientes para começar')
        
        else:
            if acao == '-c': # criar paciente
                self.pacientes.insere_paciente()

            elif acao == '-s': # selecionar paciente
                list_nomes = []
                print('selecionar paciente')
                if len(res) < 2:
                    res.append((input('Nome do paciente: ')))
                    # list_nomes = self.pacientes.retorna_paciente(res[1])

                list_nomes = self.pacientes.retorna_paciente(res[1])
                if len(list_nomes) > 1:
                    # print(self.pacientes.retorna_paciente(res[1]))
                    self.idp = seleciona_item_lista(list_nomes)
                    self.atualizar_prompt(list_nomes[self.idp])
                elif len(list_nomes) == 1:
                    self.idp = 0
                    self.atualizar_prompt(list_nomes[self.idp])
                else:
                    print('não foi encontrado pacientes com {}'.format(res[1]))
                    res = input('deseja iniciar o processo de criação? (s)(n)').lower()
                    if res == 's' or res == 'sim':
                        self.atualizar_prompt(self.pacientes.insere_paciente()) #TODO ao inserir, retorna a posição do paciente na lista de nomes
                    elif res == 'n' or res == 'nao':
                        return
                    else:
                        print('instrução não foi clara - retornando para o inicio')

                # self.active = paciente
                # self.prompt = '({}): '.format(self.active)
            
            elif acao == '-u': # atualizar paciente
                print('atualizar paciente')
                # print(self.active)

                if self.active == 'paciente':
                    print('selecione um paciente primeiro')
                    return
                else:
                    self.active = self.pacientes.atualiza_paciente(self.active)
                    self.prompt = self.active['nome']

            elif acao == '-d': # deletar paciente
                print('deletar paciente')
                res = input('não tem como recuperar os dados. Deseja continuar? (s)(n)').lower()
                if res == 's' or res == 'sim':
                    print(self.pacientes.deleta_paciente(self.active)['nome'], ' foi deletado') #TODO ao deletar, deletar também as consultas
                    return self.atualizar_prompt({'nome' : 'paciente'})
                elif res == 'n' or res == 'nao':
                    return
                else:
                    print('instrução não foi clara - retornando para o inicio')
            
            elif acao == '-f': # fechar paciente
                return self.atualizar_prompt({'nome' : 'paciente'})

            else:
                print('instrução não foi clara - digite: help paciente')
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