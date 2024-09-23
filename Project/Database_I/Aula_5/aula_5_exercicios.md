# Exercícios

## Exercício 1

Gravadora

> Você foi contratado por uma grande gravadora para trabalhar como projetista de banco de dados no projeto de desenvolvimento de um site para a comercialização e download de músicas em formato MP3.
> 
> Para proporcionar uma interface amigável e poderosa o site deverá permitir a pesquisa de músicas a partir do autor (que pode ser um artista solo ou uma banda), do álbum, do número da trilha no álbum, do título da música ou do estilo musical (Rock, Blues, Instrumental, etc.) do álbum. 
> 
> Lembre-se que muitas músicas são disponibilizadas em mais de um álbum (no álbum de lançamento e novamente em coletâneas, por exemplo), mas é importante saber qual a trilha em que elas foram gravadas em cada álbum.

&nbsp;

Fazer a modelagem física a partir do modelo lógico construído para o caso acima.

Inserir no mínimo 8 registros para cada uma das tabelas
Atualizar 3 dos registros diferentes
Remover 2 registros

&nbsp;

### Modelagem conceitual:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/exercicios/exercicio_1_diagrama_gravadora.jpg width=400>

### Modelagem lógica:

&nbsp;

### Modelagem física:

&nbsp;

## Exercício 2

> App OurNote
>
> &nbsp;
> 
> O OurNote permite registrar Anotações e Lembretes.
>
> Cada Anotação tem um título, um texto formatado, uma data de criação e uma data de alteração. É possível atribuir Rótulos às Anotações. Os Rótulos têm um nome e uma cor.
>
> É possível, ainda, vincular uma Anotação a um Lembrete. Os Lembretes têm uma data e uma hora para serem dados. Um Lembrete pode dar ou não um sinal visual ou sonoro com uma antecedência definida em minutos em relação a sua data e hora.
>
> As Anotações, Lembretes e Rótulos são criados pelos Usuários, que possuem login e senha.

&nbsp;

Fazer a modelagem física a partir do modelo lógico construído para o caso acima.

Inserir no mínimo 8 registros para cada uma das tabelas
Atualizar 3 dos registros diferentes
Remover 2 registros

&nbsp;

### Modelagem conceitual:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/exercicios/exercicio_2_diagrama_our_note.png width=400>

&nbsp;

### Modelagem lógica:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/exercicios/exercicio_4_diagrama_our_note.png width=400>

&nbsp;

### Modelagem Física:

```sql
-- Modelo criado conforme opção 1 da modelagem lógica
create table anotacoes (
	id_anotacao numeric(7) not null,
	titulo varchar(100) not null,
	texto text,
	dt_criacao datetime not null,
	dt_alteracao datetime,
	id_lembrete numeric(7)
	login varchar(30) not null,
	constraint pk_anotacoes primary key (id_anotacao)
)

create table lembretes (
	id_lembrete numeric(7) not null,
	antecedencia numeric(5) not null,
	sinal_visual char(1),
	sinal_sonoro char(1),
	datahora datetime not null,
	login varchar(30) not null,
	constraint pk_lembretes primary key (id_lembrete)
)

create table rotulos (
	id_rotulo numeric(3) not null,
	nome varchar(30) not null,
	cor char(6) not null,
	login varchar(30) not null,
	constraint pk_rotulos primary key (id_rotulo)
)

create table usuarios (
	login varchar(30) not null,
	senha varchar(32) not null,
	constraint pk_usuarios primary key (login)
)

create table rotulos_anotacoes (
	id_rotulo numeric(3),
	id_anotacao numeric(7),
	constraint pk_rotulos_anotacoes (id_rotulo, id_anotacao)
)

alter table anotacoes add constraint fk_usu_anot foreign key(login) references usuarios (login);
alter table lembretes add constraint fk_anot_lembr foreign key(id_anotacao) references anotacoes (id_anotacao);
alter table lembretes add constraint fk_usu_lembr foreign key(login) references usuarios (login);
alter table rotulos add constraint fk_usu_rot foreign key(login) references usuarios (login);
alter table rotulos_anotacoes add constraint fk_rot_rotanot foreign key(id_rotulo) references rotulos (id_rotulo);
alter table rotulos_anotacoes add constraint fk_anot_rotanot foreign key(id_anotacao) references anotacoes (id_anotacao);
```

&nbsp;

## Exercício 3

Academia de ginástica

> Nesse sistema, a recepcionista realiza a manutenção do cadastro de clientes e do cadastro de modalidades esportivas. Ao realizar sua inscrição na academia, o cliente informa à recepcionista a modalidade esportiva que deseja realizar (conforme tabela a seguir). Ao terminar o registro da inscrição do cliente, a recepcionista libera um cartão de acesso.
> 
Modalidade | Descrição | Valor (R$)
--- | --- | ---
Academia 3x (7h-17h) | Acesso a todos os equipamentos da academia, até no máximo 3 vezes por semana, restrito ao horário das 7h às 17h. | 136,00
Academia 3x | Acesso a todos os equipamentos da academia, até no máximo 3 vezes por semana, em qualquer horário. | 151,00
Academia livre | Acesso a todos os equipamentos da academia, em qualquer dia da semana (seg a dom), em qualquer horário. | 180,00

> Para poder acessar a academia, o cliente deverá antes realizar o pagamento para o caixa, no setor financeiro. Somente são aceitos pagamentos por cartão de crédito.
> 
> Para ingressar na academia, o cliente deve passar seu cartão de acesso na roleta, a qual somente será liberada se o pagamento estiver em dia e o acesso estiver conforme as restrições da modalidade contratada (horário, número de vezes por semana ou acesso livre).
> 
> A recepcionista do sistema deverá poder emitir o relatório de frequência de um aluno. A recepcionista também é responsável pela manutenção das inscrições dos clientes, assim como pelo cancelamento ou suspensão de determinada inscrição.
> 
> Nessa academia, os instrutores cadastram os treinos dos alunos e são responsáveis pela sua manutenção. Dentro da academia, o aluno poderá imprimir o seu treino.

Fazer a modelagem lógica em texto, a partir do Diagrama Entidade Relacionamento construído, conforme exemplo

> Entidade (CodigoEntidade,Atributo1,Atributo2,CodigoEntidadeEstrangeira)    
>     CodigoEntidadeEstrangeira referencia EntidadeEstrangeira

&nbsp;

Fazer a modelagem física a partir do modelo lógico construído para o caso acima.

Inserir no mínimo 8 registros para cada uma das tabelas
Atualizar 3 dos registros diferentes
Remover 2 registros


&nbsp;

### Modelagem conceitual:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/exercicios/exercicio_3_diagrama_academia.png width=400>

&nbsp;

### Modelagem lógica:

&nbsp;