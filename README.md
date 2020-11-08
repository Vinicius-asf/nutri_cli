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
- - modificações e exclusão de dados devem ser feitas somente com pacientes ativos (previamente selecionados)

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
- - Nome : string
- - Endereço : string
- - Telefones : array(int)
- - Email : string
- - Data de nascimento : string

- Consultas
- - Data : string
- - Horário : string
- - Peso : int
- - % de gordura corporal : int
- - Sensação física : string
- - Restrições alimentares : string

- Alimentos
- - Alimento: string
- - Grupo : int
- - Calorias : int
- - Porção(em gramas) : int
- - Proteínas(em gramas) : int
- - Gorduras(em gramas) : int
- - Carboidratos(em gramas) : int