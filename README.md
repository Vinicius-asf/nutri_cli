# Nutri CLI
## Sistema de gestão de um consultório de nutrição

### Premissas
- controlado por uma pessoa
- sem persistencia de dados
- não há pacientes repitidos

### Decisões de projeto

#### Sistema
- o sistema usa o pacote nativo "cmd" do Python como principal interface de usuário

#### Pacientes
- para executar ações específicas, um paciente deve estar ativo
  - modificações e exclusão de dados devem ser feitas somente com pacientes ativos (previamente selecionados)

#### Consultas
- uma consulta só pode ser criada, modificada ou excluída se houver um paciente ativo
- pode existir mais de uma consulta por paciente

#### Combinações de alimentos
- uma combinação é feita com um alimento de cada grupo
- uma combinação só é aceita caso ela não superar o limite de calorias dado
- o único critério de aceitação de uma combinação é o total de carboidratos dela
- as combinações não são armazenadas
- não há divisibilidade de porções

### Grupos de alimento
- Carnes (proteinas)
- Cereais (carboidratos)
- Outros (frutas e legumes)

### Modelagem
- Pacientes
  - Nome : string
  - Endereço : string
  - Telefones : array(string)
  - Email : string
  - Data de nascimento : string

- Consultas
  - Data : date
  - Horário : date
  - Peso : int
  - % de gordura corporal : int
  - Sensação física : string
  - Restrições alimentares : string

- Alimentos
  - Alimento: string
  - Grupo : int
  - Calorias : int
  - Porção(em gramas) : int
  - Proteínas(em gramas) : int
  - Gorduras(em gramas) : int
  - Carboidratos(em gramas) : int

### Execução

#### Requisitos
- Python 3.1 ou mais recente

#### Aplicativo
- No prompt de commando de sua escolha, execute:
> root\python app.py

#### Testes
- No prompt de commando de sua escolha, execute:
> root\python run_tests.py

#### Operações

##### Gerais
> help
- lista os comandos do sistema
  
> help {comando}
- acessa a descrição do comando especificado

> calorias {numero}
- mostra as diferentes combinações de alimentos com total de calorias menor do que os dado

##### Pacientes
Comando principal : **paciente**
  > paciente -s {nome do paciente}
  - seleciona paciente a partir de uma lista de nomes parecidos nome dado
    - se houver apenas um nome na lista, este será selecionado
  > paciente -u
  - atualiza os dados do paciente ativo
  > paciente -d
  - deleta os dados do paciente ativo
  > paciente -c
  - cria o paciente na lista de pacientes
  > paciente -f
  - fecha o paciente ativo


##### Consultas
Comando principal : **consulta**
 > consulta 
 - cria uma consulta direcionada ao paciente ativo
 > consulta -l
 - lista as consultas que o paciente ativo tem
 > consulta -u 
 - atualiza os dados da consulta mais recente
 > consulta -u {numero}
 - atualiza os dados da consulta com o índice indicado
 > consulta -d 
 - deleta a ultima consulta do paciente ativo
 > -d {numero}
 - deleta uma consulta especifica do paciente ativo