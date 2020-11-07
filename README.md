# Nutri CLI
## Sistema de gestão de um consultório de nutrição

### Premissas
- controlado por uma pessoa
- sem persistencia de dados

### Decisões de projeto
- o sistema usa o pacote nativo "cmd" do Python como principal interface de usuário
- modificações em dados devem ser feitas somente com dados ativos (previamente selecionados)

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
- - Grupo : int
- - Calorias : int
- - Porção(em gramas) : int
- - Proteínas(em gramas) : int
- - Gorduras(em gramas) : int
- - Carboidratos(em gramas) : int