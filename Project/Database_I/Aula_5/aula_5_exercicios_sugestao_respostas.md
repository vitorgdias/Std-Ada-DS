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
    Table musicas {
        id int [primary key]
        titulo varchar(100)
    }

    Table albuns {
        id int [primary key]
        nome varchar(100)
        id_estilo int [ref: - estilos.id]
    }

    Table autores {
        id int [primary key]
        nome varchar(100)
        id_tipo_autor int [ref: - tipos_de_autores.id]
    }

    Table estilos {
        id int [primary key]
        descricao varchar(100)
    }

    Table tipos_de_autores {
        id int [primary key]
        descricao varchar(100)
    }

    Table musicas_albuns {
        id int [primary key]
        id_musica int [ref: <> musicas.id]
        id_album int [ref: <> albuns.id]    
        trilha int
    }

    Table musicas_autores {
        id int [primary key]
        id_musica int [ref: <> musicas.id]
        id_autor int [ref: <> autores.id]
    }

### Modelagem física:

```sql
-- Tabela de Estilos
CREATE TABLE estilos (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(100)
);

-- Tabela de Tipos de Autores
CREATE TABLE tipos_de_autores (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(100)
);

-- Tabela de Músicas
CREATE TABLE musicas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100)
);

-- Tabela de Álbuns
CREATE TABLE albuns (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    id_estilo INT REFERENCES estilos(id) -- Chave estrangeira para a tabela de estilos
);

-- Tabela de Autores
CREATE TABLE autores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    id_tipo_autor INT REFERENCES tipos_de_autores(id) -- Chave estrangeira para a tabela de tipos de autores
);

-- Tabela de Músicas e Álbuns
CREATE TABLE musicas_albuns (
    id SERIAL PRIMARY KEY,
    id_musica INT NOT NULL REFERENCES musicas(id),
    id_album INT NOT NULL REFERENCES albuns(id),
    trilha INT,
    CONSTRAINT unique_musica_album UNIQUE (id_musica, id_album) -- Garante que a combinação seja única
);

-- Tabela de Músicas e Autores
CREATE TABLE musicas_autores (
    id SERIAL PRIMARY KEY,
    id_musica INT NOT NULL REFERENCES musicas(id),
    id_autor INT NOT NULL REFERENCES autores(id),
    CONSTRAINT unique_musica_autor UNIQUE (id_musica, id_autor) -- Garante que a combinação seja única
);
```

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

Etapa 1: Mapear as entidades

    anotacoes (id_anot, titulo, conteudo, dt_criacao, dt_atualizacao)
        id_anot PK

    rotulos (id_rot, nome, cor)
        id_rot PK


    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia)
        id_lembr PK

    usuarios (login, senha)
        login PK

&nbsp;

Etapa 2: Mapear os relacionamentos 1:1

    vinculada:
    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia, id_anot)
        id_lembr PK
        id_anot FK anotacoes

&nbsp;

Etapa 3: Mapear os relacionamentos 1:N
    
    criar lembrete:
    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia, id_anot, login_usuario)
        id_lembr PK
        id_anot FK anotacoes
        login_usuario FK usuarios

    criar anotacao:
    anotacoes (id_anot, titulo, conteudo, dt_criacao, dt_atualizacao, login_usuario)
        id_anot PK
        login_usuario FK usuarios

    criar rotulos:
    rotulos (id_rot, nome, cor, login_usuario)
        id_rot PK
        login_usuario FK usuarios

&nbsp;

Etapa 4: Mapear os relacionamentos N:N

    possui:
    anotacoes_rotulos (id_anot, id_rotulo)
        id_anot PK / FK anotacoes
        id_rotulo PK / FK rotulos

&nbsp;

Etapa 5: Mapear os atributos multivalorados
    
    N/A

&nbsp;

Resultado final: Juntar tudo

    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia, id_anot, login_usuario)
        id_lembr PK
        id_anot FK anotacoes
        login_usuario FK usuarios

    anotacoes (id_anot, titulo, conteudo, dt_criacao, dt_atualizacao, login_usuario)
        id_anot PK
        login_usuario FK usuarios

    rotulos (id_rot, nome, cor, login_usuario)
        id_rot PK
        login_usuario FK usuarios

    usuarios (login, senha)
        login PK

    anotacoes_rotulos (id_anot, id_rotulo)
        id_anot PK / FK anotacoes
        id_rotulo PK / FK rotulos

&nbsp;

    Resultado final no dbdiagram.io

    TABLE lembretes {
        id int [primary key]
        data_hora timestamp
        sinal_visual bool
        sinal_sonoro bool
        antecedencia_minutos int
        id_anotacao int [ref: - anotacoes.id]
        login_usuario varchar(50) [ref: - usuarios.login]
    }

    TABLE anotacoes {
        id int [primary key]
        titulo varchar(50)
        conteudo varchar(500)
        dt_criacao timestamp
        dt_atualizacao timestamp
        login_usuario varchar(50) [ref: - usuarios.login]
    }

    TABLE rotulos {
        id int [primary key]
        nome varchar(50)
        id_cor int [ref: - cores.id]
        login_usuario varchar(50) [ref: - usuarios.login]
    }

    TABLE cores {
        id int [primary key]
        nome varchar(50)
    }

    TABLE usuarios {
        login varchar(50) [primary key]
        senha varchar(50)
    }

    TABLE anotacoes_rotulos {
        id_anotacao int [primary key, ref: <> anotacoes.id]
        id_rotulo int [primary key, ref: <> rotulos.id]
    }

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/exercicios/exercicio_4_diagrama_our_note.png width=400>

&nbsp;

### Modelagem Física:

```sql
-- Create the 'cores' table
CREATE TABLE cores (
  id SERIAL PRIMARY KEY, -- Use SERIAL for auto-incrementing integer ID
  nome VARCHAR(50) NOT NULL UNIQUE -- Enforce unique color names
);

-- Create the 'rotulos' table
CREATE TABLE rotulos (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  id_cor INTEGER REFERENCES cores(id) ON DELETE SET NULL, -- Allow null for id_cor if the referenced core is deleted
  login_usuario VARCHAR(50) REFERENCES usuarios(login) ON DELETE SET NULL -- Allow null for login_usuario if the user is deleted
);

-- Create the 'anotacoes' table
CREATE TABLE anotacoes (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(50) NOT NULL,
  conteudo VARCHAR(500) NOT NULL,
  dt_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Set default creation time
  dt_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Set default update time (can be updated later)
  login_usuario VARCHAR(50) REFERENCES usuarios(login) ON DELETE SET NULL -- Allow null for login_usuario if the user is deleted
);

-- Create the 'lembretes' table (last, as it references other tables)
CREATE TABLE lembretes (
  id SERIAL PRIMARY KEY,
  data_hora TIMESTAMP NOT NULL,
  sinal_visual BOOLEAN DEFAULT FALSE, -- Set default visual signal to false
  sinal_sonoro BOOLEAN DEFAULT FALSE, -- Set default sound signal to false
  antecedencia_minutos INTEGER NOT NULL,
  id_anotacao INTEGER REFERENCES anotacoes(id) ON DELETE SET NULL, -- Allow null for id_anotacao if the referenced note is deleted
  login_usuario VARCHAR(50) REFERENCES usuarios(login) ON DELETE SET NULL -- Allow null for login_usuario if the user is deleted
);

-- Create the 'anotacoes_rotulos' table for many-to-many relationship
CREATE TABLE anotacoes_rotulos (
  id_anotacao INTEGER PRIMARY KEY REFERENCES anotacoes(id) ON DELETE CASCADE, -- Cascade delete to related labels
  id_rotulo INTEGER PRIMARY KEY REFERENCES rotulos(id) ON DELETE CASCADE, -- Cascade delete to related notes
  CONSTRAINT anotacoes_rotulos_pk PRIMARY KEY (id_anotacao, id_rotulo) -- Composite primary key for uniqueness
);
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

Etapa 1: Mapear as entidades

    modalidades (id_modalidade, nome_modalidade, descricao, valor)
        id_modalidade PK

    clientes (id_cliente, nome_cliente, situacao)
        id_cliente PK
    
    pagamentos (ano, mes, valor_pago, data_pagamento, band_cartao_credito, numero_cartao_credito)
        ano PK
        mes PK
    
    treinos (data, desc_treino, presente)
        data PK
    
    instrutores (id_instrutor, nome_instrutor)
        id_instrutor PK

    
&nbsp;

Etapa 2: Mapear os relacionamentos 1:1

    N/A


&nbsp;

Etapa 3: Mapear os relacionamentos 1:N
    
    faz:
    pagamentos (ano, mes, valor_pago, data_pagamento, band_cartao_credito, numero_cartao_credito, id_cliente)
        ano PK
        mes PK
        id_cliente PK / FK clientes

    executa:
    treinos (dt_treino, desc_treino, presente, id_cliente)
        dt_treino PK
        id_cliente PK / FK clientes
    
    prescreve:
    treinos (dt_treino, desc_treino, presente, id_cliente, id_instrutor)
        dt_treino PK
        id_cliente PK / FK clientes
        id_instrutor FK instrutores

&nbsp;

Etapa 4: Mapear os relacionamentos N:N

    escolhe:
    clientes_modalidades (id_cliente, id_modalidade, dt_inicio, dt_fim)
        id_cliente PK / FK clientes
        id_modalidade PK / FK modalidades

&nbsp;

Etapa 5: Mapear os atributos multivalorados
    
    N/A

&nbsp;

Resultado final: Juntar tudo

    modalidades (id_modalidade, nome_modalidade, descricao, valor)
        id_modalidade PK

    clientes (id_cliente, nome_cliente, situacao)
        id_cliente PK
    
    pagamentos (ano, mes, valor_pago, data_pagamento, band_cartao_credito, numero_cartao_credito, id_cliente)
        ano PK
        mes PK
        id_cliente PK / FK clientes
    
    treinos (dt_treino, desc_treino, presente, id_cliente, id_instrutor)
        dt_treino PK
        id_cliente PK / FK clientes
        id_instrutor FK instrutores
    
    instrutores (id_instrutor, nome_instrutor)
        id_instrutor PK
    
    clientes_modalidades (id_cliente, id_modalidade, dt_inicio, dt_fim)
        id_cliente PK / FK clientes
        id_modalidade PK / FK modalidades

&nbsp;

### Modelagem física

```sql
CREATE TABLE modalidades (
  id_modalidade SERIAL PRIMARY KEY,
  nome_modalidade VARCHAR(50) NOT NULL,
  descricao VARCHAR(500),
  valor NUMERIC(10,2)
);

CREATE TABLE clientes (
  id_cliente SERIAL PRIMARY KEY,
  nome_cliente VARCHAR(100) NOT NULL,
  situacao VARCHAR(20) NOT NULL
);

CREATE TABLE instrutores (
  id_instrutor SERIAL PRIMARY KEY,
  nome_instrutor VARCHAR(50) NOT NULL
);

CREATE TABLE pagamentos (
  ano INTEGER NOT NULL,
  mes INTEGER NOT NULL,
  valor_pago NUMERIC(10,2) NOT NULL,
  data_pagamento DATE NOT NULL,
  band_cartao_credito VARCHAR(20),
  numero_cartao_credito VARCHAR(19),
  id_cliente INTEGER NOT NULL,
  PRIMARY KEY (ano, mes, id_cliente),
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE treinos (
  dt_treino DATE NOT NULL,
  id_cliente INTEGER NOT NULL,
  desc_treino VARCHAR(100),
  presente BOOLEAN NOT NULL,
  id_instrutor INTEGER NOT NULL,
  PRIMARY KEY (dt_treino, id_cliente),
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
  FOREIGN KEY (id_instrutor) REFERENCES instrutores(id_instrutor)
);

CREATE TABLE clientes_modalidades (
  id_cliente INTEGER NOT NULL,
  id_modalidade INTEGER NOT NULL,
  dt_inicio DATE NOT NULL,
  dt_fim DATE,
  PRIMARY KEY (id_cliente, id_modalidade),
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
  FOREIGN KEY (id_modalidade) REFERENCES modalidades(id_modalidade)
);

-- Insert into clientes table
INSERT INTO academia.clientes (nome_cliente, situacao) 
VALUES ('João da Silva', 'Ativo');
INSERT INTO academia.clientes (nome_cliente, situacao) 
VALUES ('Maria Oliveira', 'Inativo');
INSERT INTO academia.clientes (nome_cliente, situacao) 
VALUES ('Pedro Santos', 'Ativo');
INSERT INTO academia.clientes (nome_cliente, situacao) 
VALUES ('Ana Silva', 'Ativo');
INSERT INTO academia.clientes (nome_cliente, situacao) 
VALUES ('Lucas Oliveira', 'Inativo');

-- Insert into instrutores table
INSERT INTO academia.instrutores (nome_instrutor) 
VALUES ('Fernanda Oliveira');
INSERT INTO academia.instrutores (nome_instrutor) 
VALUES ('Marcos Souza');
INSERT INTO academia.instrutores (nome_instrutor) 
VALUES ('Amanda Costa');

-- Insert into modalidades table
INSERT INTO academia.modalidades (nome_modalidade, descricao, valor) 
VALUES ('Academia 3x (7h-17h)', 'Acesso a todos os equipamentos da academia, até no máximo 3 vezes por semana, restrito ao horário das 7h às 17h.', 136.00);
INSERT INTO academia.modalidades (nome_modalidade, descricao, valor) 
VALUES ('Academia 3x', 'Acesso a todos os equipamentos da academia, até no máximo 3 vezes por semana, em qualquer horário.', 151.00);
INSERT INTO academia.modalidades (nome_modalidade, descricao, valor) 
VALUES ('Academia livre', 'Acesso a todos os equipamentos da academia, em qualquer dia da semana (seg a dom), em qualquer horário. ', 180.00);
INSERT INTO academia.modalidades (nome_modalidade, descricao, valor) 
VALUES ('Yoga', 'Prática de exercícios para harmonização do corpo e mente', 200.00);
INSERT INTO academia.modalidades (nome_modalidade, descricao, valor) 
VALUES ('Boxe', 'Prática de luta para desenvolvimento físico e mental', 150.00);

-- Insert into pagamentos table
INSERT INTO academia.pagamentos (ano, mes, valor_pago, data_pagamento, band_cartao_credito, numero_cartao_credito, id_cliente) 
VALUES (2022, 3, 180.00, '2022-03-01', 'Visa', '**** **** **** 1234', 1);
INSERT INTO academia.pagamentos (ano, mes, valor_pago, data_pagamento, band_cartao_credito, numero_cartao_credito, id_cliente) 
VALUES (2022, 4, 150.00, '2022-04-05', 'Mastercard', '**** **** **** 5678', 2);
INSERT INTO academia.pagamentos (ano, mes, valor_pago, data_pagamento, band_cartao_credito, numero_cartao_credito, id_cliente) 
VALUES (2022, 6, 200.00, '2022-06-03', 'Visa', '**** **** **** 4321', 3);
INSERT INTO academia.pagamentos (ano, mes, valor_pago, data_pagamento, band_cartao_credito, numero_cartao_credito, id_cliente) 
VALUES (2022, 6, 200.00, '2022-06-03', 'Mastercard', '**** **** **** 8765', 4);
INSERT INTO academia.pagamentos (ano, mes, valor_pago, data_pagamento, band_cartao_credito, numero_cartao_credito, id_cliente) 
VALUES (2022, 5, 151.00, '2022-05-02', 'Visa', '**** **** **** 1278', 5);

-- Insert into treinos table
INSERT INTO academia.treinos (dt_treino, desc_treino, presente, id_cliente, id_instrutor) 
VALUES ('2022-03-09', 'Treino de peito e tríceps', 1, 1, 2);
INSERT INTO academia.treinos (dt_treino, desc_treino, presente, id_cliente, id_instrutor) 
VALUES ('2022-04-10', 'Treino de pernas', 0, 2, 2);
INSERT INTO academia.treinos (dt_treino, desc_treino, presente, id_cliente, id_instrutor) 
VALUES ('2022-05-08', 'Treino de boxe', 1, 5, 3);
INSERT INTO academia.treinos (dt_treino, desc_treino, presente, id_cliente, id_instrutor) 
VALUES ('2022-06-05', 'Aula de Yoga', 1, 3, 1);
INSERT INTO academia.treinos (dt_treino, desc_treino, presente, id_cliente, id_instrutor) 
VALUES ('2022-06-05', 'Aula de Yoga', 1, 4, 1);

-- Insert into clientes_modalidades table
INSERT INTO academia.clientes_modalidades (id_cliente, id_modalidade, dt_inicio, dt_fim) 
VALUES (1, 1, '2022-03-01', '2022-04-01');
INSERT INTO academia.clientes_modalidades (id_cliente, id_modalidade, dt_inicio, dt_fim) 
VALUES (2, 2, '2022-04-05', '2022-05-05');
INSERT INTO academia.clientes_modalidades (id_cliente, id_modalidade, dt_inicio, dt_fim) 
VALUES (3, 4, '2022-06-03', '2022-07-03');
INSERT INTO academia.clientes_modalidades (id_cliente, id_modalidade, dt_inicio, dt_fim) 
VALUES (4, 4, '2022-06-03', '2022-07-03');
INSERT INTO academia.clientes_modalidades (id_cliente, id_modalidade, dt_inicio, dt_fim) 
VALUES (5, 5, '2022-05-02', '2022-06-02');
```