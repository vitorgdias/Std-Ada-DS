# Avaliação Bancos de Dados I

# Alunos: Fernanda Polga, Gabriel Melo, Jaqueline Bonnevialle, Rafael Bittencourt, Vitor Galves.

### Modelagem e normalização de bancos de dados relacionais
Certo dia, um dos gestores do banco em que você trabalha como cientista de dados procurou você pedindo ajuda para projetar um pequeno banco de dados com o objetivo de mapear os clientes da companhia pelos diferentes produtos financeiros que eles contrataram.

O gestor explicou que o banco tinha uma grande quantidade de clientes e oferecia uma variedade de produtos financeiros, como cartões de crédito, empréstimos, seguros e investimentos. No entanto, eles estavam tendo dificuldades para entender quais produtos eram mais populares entre os clientes e como esses produtos estavam interagindo entre si.

Como ponto de partida, o gestor deixou claro que um cliente pode contratar vários produtos diferentes ao passo que um mesmo produto pode também estar associado a vários clientes diferentes e elaborou um rústico esboço de banco de dados com duas tabelas, da seguinte forma:

**Tabela 1**

- Nome da tabela: cliente
- Colunas: `codigo_cliente, nome_cliente, sobrenome_cliente, telefones_cliente, municipio_cliente, codigo_tipo_cliente, tipo_cliente`

**Tabela 2**

- Nome da tabela: produto
- Colunas: `codigo_produto, nome_produto, descricao_produto, codigo_tipo_produto, tipo_produto, codigo_diretor_responsavel, nome_diretor_responsavel, email_diretor_responsavel`


1) Ainda sem fazer normalizações, apresente o modelo conceitual deste esboço oferecido pelo gestor, destacando atributos chaves e multivalorados, caso existam, e apresentando também a cardinalidade dos relacionamentos. 
-->> **Aqui eu entendi que é pra fazer o esboço no draw.io*

2) Agora apresente um modelo lógico que expresse as mesmas informações e relacionamentos descritos no modelo original, mas decompondo-os quando necessário para que sejam respeitadas as 3 primeiras formas normais. Destaque atributos chaves e multivalorados, caso existam, e apresente também a cardinalidade dos relacionamentos.
-->> **Aqui é para fazer oa modelagem do final da Aula 04, com o db.diagrams*


### Consultas SQL simples e complexas em um banco de dados postgres

Um exemplo de modelo de banco de dados com relacionamento muitos-para-muitos pode ser o de um e-commerce que tem produtos e categorias, onde um produto pode pertencer a várias categorias e uma categoria pode estar associada a vários produtos. Nesse caso, teríamos duas tabelas: "produtos" e "categorias", com uma tabela intermediária "produtos_categorias" para relacionar os produtos às suas categorias.

-

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
);

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE produtos_categorias (
    produto_id INTEGER REFERENCES produtos(id),
    categoria_id INTEGER REFERENCES categorias(id),
    PRIMARY KEY (produto_id, categoria_id)
);


Assim, usando o subconjunto da "structured query language" chamado de DQL , produza consultas postgres de modo a atender cada uma das seguintes solicitações:

3) Liste os nomes de todos os produtos que custam mais de 100 reais, ordenando-os primeiramente pelo preço e em segundo lugar pelo nome. Use **alias* para mostrar o nome da coluna nome como "Produto" e da coluna preço como "Valor". A resposta da consulta não deve mostrar outras colunas de dados.

4) Liste todos os ids e preços de produtos cujo preço seja maior do que a média de todos os preços encontrados na tabela "produtos".

5) Para cada categoria, mostre o preço médio do conjunto de produtos a ela associados. Caso uma categoria não tenha nenhum produto a ela associada, esta categoria não deve aparecer no resultado final. A consulta deve estar ordenada pelos nomes das categorias.



### Inserções, alterações e remoções de objetos e dados em um banco de dados postgres

Você está participando de um processo seletivo para trabalhar como cientista de dados na Ada, uma das maiores formadoras do país em áreas correlatadas à tecnologia. Dividido em algumas etapas, o processo tem o objetivo de avaliar você nos quesitos Python, Machine Learning e Bancos de Dados. Ainda que os dois primeiros sejam o cerne da sua atuação no dia-a-dia, considera-se que Bancos de Dados também constituem um requisito importante e, por isso, esta etapa pode ser a oportunidade que você precisava para se destacar dentre os seus concorrentes, demonstrando um conhecimento mais amplo do que os demais.

6) Com o objetivo de demonstrar o seu conhecimento através de um exemplo contextualizado com o dia-a-dia da escola, utilize os comandos do subgrupo de funções DDL para construir o banco de dados simples abaixo, que representa um relacionamento do tipo 1,n entre as entidades "aluno" e "turma":

Tabela 1

Nome da tabela: aluno
Colunas da tabela: `id_aluno (INT), nome_aluno (VARCHAR), aluno_alocado (BOOLEAN), id_turma (INT)`


Tabela 2

Nome da tabela: turma
Colunas da tabela: `id_turma (INT), código_turma (VARCHAR), nome_turma (VARCHAR)`


7) Agora que você demonstrou que consegue ser mais do que um simples usuário do banco de dados, mostre separadamente cada um dos códigos DML necessários para cumprir cada uma das etapas a seguir:

a) Inserir pelo menos duas turmas diferentes na tabela de turma;

b) Inserir pelo menos 1 aluno alocado em cada uma destas turmas na tabela aluno (todos com `NULL` na coluna aluno_alocado);

c) Inserir pelo menos 2 alunos não alocados em nenhuma turma na tabela aluno (todos com `NULL` na coluna aluno_alocado);

d) Atualizar a coluna aluno_alocado da tabela aluno, de modo que os alunos associados a uma disciplina recebam o valor True e alunos não associdos a nenhuma disciplina recebam o falor False para esta coluna.



# Respostas dos Exercícios:

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- CRIANDO AS TABELAS
CREATE TABLE project_db.telefone (
    codigo UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    comecial varchar(100) NULL,
    pessoal varchar(20) NOT NULL
);

CREATE TABLE project_db.endereco (
    codigo UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    rua varchar(100) NOT NULL,
    numero varchar(20) NOT NULL,
    complemento varchar(50) NULL,
    bairro varchar(50) NOT NULL,
    CEP varchar(50) NOT NULL,
    municipio varchar(50) NOT NULL,
    estado varchar(50) NOT NULL,
    pais varchar(50) NOT NULL
);

CREATE TABLE project_db.clientes (
    codigo UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nome varchar(100) NOT NULL,
    sobrenome varchar(100) NOT NULL,
    cod_telefone UUID NULL,
    cod_endereco UUID NOT NULL,
    FOREIGN KEY (cod_telefone) REFERENCES project_db.telefone(codigo),
    FOREIGN KEY (cod_endereco) REFERENCES project_db.endereco(codigo)
);

CREATE TABLE project_db.tipo_conta (
    codigo UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nome varchar(100) NOT NULL
);

CREATE TABLE project_db.conta (
    codigo UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    cod_cliente UUID NOT NULL,
    cod_tipo_conta UUID NOT NULL,
    ativo BOOLEAN NOT NULL,
    FOREIGN KEY (cod_cliente) REFERENCES project_db.clientes(codigo),
    FOREIGN KEY (cod_tipo_conta) REFERENCES project_db.tipo_conta(codigo)
);

CREATE TABLE project_db.tipo_produto (
    codigo UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nome varchar(100) NOT NULL
);

CREATE TABLE project_db.diretor (
    codigo UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nome varchar(100) NOT NULL,
    email varchar(100) UNIQUE NOT NULL,
    ativo BOOLEAN NOT NULL
);

CREATE TABLE project_db.produto (
    codigo UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    cod_tipo_produto UUID NOT NULL,
    cod_diretor UUID NOT NULL,
    nome varchar(100) NOT NULL,
    descricao varchar(100) NOT NULL,
    ativo BOOLEAN NOT NULL,
    custo_mensal FLOAT NOT NULL,
    FOREIGN KEY (cod_tipo_produto) REFERENCES project_db.tipo_produto(codigo),
    FOREIGN KEY (cod_diretor) REFERENCES project_db.diretor(codigo)
);

CREATE TABLE project_db.produto_conta (
    cod_conta UUID NOT NULL,
    cod_produto UUID NOT NULL,
    FOREIGN KEY (cod_conta) REFERENCES project_db.conta(codigo),
    FOREIGN KEY (cod_produto) REFERENCES project_db.produto(codigo)
);

```

```sql
-- PREENCHENDO AS TABELAS

-- TELEFONE
INSERT INTO project_db.telefone (codigo, comecial, pessoal) 
VALUES 
(uuid_generate_v4(), '11-3333-4444', '11-99999-8888'),
(uuid_generate_v4(), '11-2222-5555', '11-98888-7777'),
(uuid_generate_v4(), '21-3333-1111', '21-99999-0000'),
(uuid_generate_v4(), '31-3333-2222', '31-99999-1111'),
(uuid_generate_v4(), '61-3555-6666', '61-99999-5555'),
(uuid_generate_v4(), '41-3333-7777', '41-99999-8888'),
(uuid_generate_v4(), '51-3333-4444', '51-99999-5555'),
(uuid_generate_v4(), '71-3333-9999', '71-99999-0000'),
(uuid_generate_v4(), '81-3555-3333', '81-99999-2222'),
(uuid_generate_v4(), '85-3333-5555', '85-99999-6666'),
(uuid_generate_v4(), '31-3222-1111', '31-98888-2222'),
(uuid_generate_v4(), '61-3222-4444', '61-99999-6666'),
(uuid_generate_v4(), '21-3222-8888', '21-99999-7777'),
(uuid_generate_v4(), '11-3111-5555', '11-98888-4444'),
(uuid_generate_v4(), '41-3111-9999', '41-99999-1111'),
(uuid_generate_v4(), '51-3111-3333', '51-99999-4444'),
(uuid_generate_v4(), '71-3111-7777', '71-99999-8888'),
(uuid_generate_v4(), '81-3222-1111', '81-99999-3333'),
(uuid_generate_v4(), '85-3222-4444', '85-99999-7777'),
(uuid_generate_v4(), '61-3111-5555', '61-99999-9999'),
(uuid_generate_v4(), '31-3333-8888', '31-99999-4444'),
(uuid_generate_v4(), '11-3777-9999', '11-99999-3333'),
(uuid_generate_v4(), '21-3555-1111', '21-99999-2222'),
(uuid_generate_v4(), '71-3555-4444', '71-99999-5555'),
(uuid_generate_v4(), '41-3555-6666', '41-99999-7777'),
(uuid_generate_v4(), '31-3555-8888', '31-99999-9999'),
(uuid_generate_v4(), '85-3555-2222', '85-99999-1111'),
(uuid_generate_v4(), '81-3555-9999', '81-99999-8888'),
(uuid_generate_v4(), '61-3777-1111', '61-99999-4444'),
(uuid_generate_v4(), '31-3777-5555', '31-99999-6666'),
(uuid_generate_v4(), '21-3777-8888', '21-99999-9999'),
(uuid_generate_v4(), '41-3222-1111', '41-99999-3333'),
(uuid_generate_v4(), '51-3222-5555', '51-99999-7777'),
(uuid_generate_v4(), '71-3777-2222', '71-99999-4444'),
(uuid_generate_v4(), '85-3777-6666', '85-99999-8888'),
(uuid_generate_v4(), '81-3777-4444', '81-99999-5555'),
(uuid_generate_v4(), '31-3111-9999', '31-99999-7777'),
(uuid_generate_v4(), '21-3111-8888', '21-99999-6666'),
(uuid_generate_v4(), '11-3111-4444', '11-99999-5555'),
(uuid_generate_v4(), '41-3111-3333', '41-99999-6666'),
(uuid_generate_v4(), '51-3111-5555', '51-99999-7777'),
(uuid_generate_v4(), '71-3111-6666', '71-99999-9999'),
(uuid_generate_v4(), '85-3111-8888', '85-99999-1111'),
(uuid_generate_v4(), '81-3111-2222', '81-99999-3333'),
(uuid_generate_v4(), '61-3333-4444', '61-99999-5555'),
(uuid_generate_v4(), '31-3333-6666', '31-99999-7777'),
(uuid_generate_v4(), '11-3222-1111', '11-99999-4444'),
(uuid_generate_v4(), '41-3222-3333', '41-99999-5555'),
(uuid_generate_v4(), '51-3222-4444', '51-99999-6666'),
(uuid_generate_v4(), '71-3222-5555', '71-99999-7777'),
(uuid_generate_v4(), '85-3222-6666', '85-99999-8888'),
(uuid_generate_v4(), '81-3222-7777', '81-99999-9999'),
(uuid_generate_v4(), '31-3111-1111', '31-99999-2222'),
(uuid_generate_v4(), '21-3111-5555', '21-99999-3333'),
(uuid_generate_v4(), '11-3111-6666', '11-99999-7777'),
(uuid_generate_v4(), '41-3111-2222', '41-99999-8888'),
(uuid_generate_v4(), '51-3111-1111', '51-99999-3333'),
(uuid_generate_v4(), '71-3111-9999', '71-99999-4444'),
(uuid_generate_v4(), '85-3111-6666', '85-99999-5555'),
(uuid_generate_v4(), '81-3111-5555', '81-99999-6666'),
(uuid_generate_v4(), '61-3333-1111', '61-99999-2222'),
(uuid_generate_v4(), '31-3333-3333', '31-99999-4444'),
(uuid_generate_v4(), '11-3222-6666', '11-99999-5555'),
(uuid_generate_v4(), '41-3222-8888', '41-99999-6666'),
(uuid_generate_v4(), '51-3222-1111', '51-99999-7777'),
(uuid_generate_v4(), '71-3222-2222', '71-99999-8888'),
(uuid_generate_v4(), '85-3222-4444', '85-99999-9999'),
(uuid_generate_v4(), '81-3222-5555', '81-99999-1111'),
(uuid_generate_v4(), '31-3111-4444', '31-99999-6666'),
(uuid_generate_v4(), '21-3111-3333', '21-99999-4444'),
(uuid_generate_v4(), '11-3111-1111', '11-99999-5555'),
(uuid_generate_v4(), '41-3111-5555', '41-99999-7777'),
(uuid_generate_v4(), '51-3111-8888', '51-99999-9999'),
(uuid_generate_v4(), '71-3111-3333', '71-99999-1111'),
(uuid_generate_v4(), '85-3111-4444', '85-99999-3333'),
(uuid_generate_v4(), '81-3111-6666', '81-99999-7777'),
(uuid_generate_v4(), '61-3555-4444', '61-99999-8888'),
(uuid_generate_v4(), '31-3555-1111', '31-99999-9999'),
(uuid_generate_v4(), '11-3777-2222', '11-99999-1111'),
(uuid_generate_v4(), '41-3777-3333', '41-99999-4444'),
(uuid_generate_v4(), '51-3777-5555', '51-99999-6666'),
(uuid_generate_v4(), '71-3777-8888', '71-99999-7777'),
(uuid_generate_v4(), '85-3777-9999', '85-99999-1111'),
(uuid_generate_v4(), '81-3777-3333', '81-99999-4444'),
(uuid_generate_v4(), '61-3222-7777', '61-99999-5555'),
(uuid_generate_v4(), '31-3222-8888', '31-99999-6666'),
(uuid_generate_v4(), '11-3222-9999', '11-99999-7777'),
(uuid_generate_v4(), '62-3333-1111', '62-99999-2222'),
(uuid_generate_v4(), '62-3555-3333', '62-99999-4444'),
(uuid_generate_v4(), '62-3777-5555', '62-99999-6666'),
(uuid_generate_v4(), '63-3222-1111', '63-99999-2222'),
(uuid_generate_v4(), '63-3555-3333', '63-99999-4444'),
(uuid_generate_v4(), '63-3777-5555', '63-99999-6666'),
(uuid_generate_v4(), '64-3222-1111', '64-99999-2222'),
(uuid_generate_v4(), '64-3555-3333', '64-99999-4444'),
(uuid_generate_v4(), '64-3777-5555', '64-99999-6666'),
(uuid_generate_v4(), '65-3222-1111', '65-99999-2222'),
(uuid_generate_v4(), '65-3555-3333', '65-99999-4444'),
(uuid_generate_v4(), '65-3777-5555', '65-99999-6666'),
(uuid_generate_v4(), '66-3222-1111', '66-99999-2222'),
(uuid_generate_v4(), '66-3555-3333', '66-99999-4444'),
(uuid_generate_v4(), '66-3777-5555', '66-99999-6666'),
(uuid_generate_v4(), '67-3222-1111', '67-99999-2222'),
(uuid_generate_v4(), '67-3555-3333', '67-99999-4444'),
(uuid_generate_v4(), '67-3777-5555', '67-99999-6666'),
(uuid_generate_v4(), '68-3222-1111', '68-99999-2222'),
(uuid_generate_v4(), '68-3555-3333', '68-99999-4444');
```

```sql
-- ENDEREÇOS

INSERT INTO project_db.endereco (codigo, rua, numero, complemento, bairro, CEP, municipio, estado, pais) 
VALUES 
(uuid_generate_v4(), 'Rua Augusta', '123', 'Apt 10', 'Consolação', '01413-000', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Avenida Paulista', '1500', NULL, 'Bela Vista', '01310-100', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua das Palmeiras', '300', 'Apt 20', 'Pinheiros', '05422-010', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Avenida Brasil', '100', 'Bloco B', 'Centro', '30130-100', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Rua Rio de Janeiro', '50', NULL, 'Centro', '30160-030', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Avenida Atlântica', '450', 'Cobertura', 'Copacabana', '22070-010', 'Rio de Janeiro', 'RJ', 'Brasil'),
(uuid_generate_v4(), 'Rua Visconde de Pirajá', '500', NULL, 'Ipanema', '22410-003', 'Rio de Janeiro', 'RJ', 'Brasil'),
(uuid_generate_v4(), 'Rua Oscar Freire', '700', NULL, 'Jardins', '01426-001', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Avenida Brigadeiro Faria Lima', '3500', 'Apt 101', 'Jardim Paulistano', '01452-000', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua XV de Novembro', '800', NULL, 'Centro', '80020-310', 'Curitiba', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua Marechal Deodoro', '100', 'Sala 12', 'Centro', '80010-020', 'Curitiba', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua das Laranjeiras', '200', 'Apt 15', 'Laranjeiras', '22240-002', 'Rio de Janeiro', 'RJ', 'Brasil'),
(uuid_generate_v4(), 'Rua das Flores', '250', NULL, 'Centro', '70040-010', 'Brasília', 'DF', 'Brasil'),
(uuid_generate_v4(), 'Avenida Goiás', '1700', NULL, 'Centro', '74025-010', 'Goiânia', 'GO', 'Brasil'),
(uuid_generate_v4(), 'Rua 24 de Outubro', '100', NULL, 'Independência', '90510-000', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua dos Andradas', '900', NULL, 'Centro Histórico', '90020-000', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Frei Caneca', '80', 'Apt 12', 'Centro', '01307-001', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua Vergueiro', '650', NULL, 'Paraíso', '01504-001', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua Marechal Floriano', '400', NULL, 'Centro', '86010-090', 'Londrina', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua Amazonas', '500', NULL, 'Savassi', '30130-009', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Rua João Pessoa', '120', 'Bloco A', 'Centro', '90010-150', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Avenida Ipiranga', '900', 'Apt 34', 'Consolação', '01046-010', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua São João', '210', NULL, 'Centro', '01035-100', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua Doutor Bacelar', '130', NULL, 'Vila Clementino', '04026-000', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Avenida 9 de Julho', '2000', NULL, 'Jardim Paulista', '01313-000', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua Barata Ribeiro', '1100', 'Apt 100', 'Copacabana', '22011-001', 'Rio de Janeiro', 'RJ', 'Brasil'),
(uuid_generate_v4(), 'Rua do Catete', '300', 'Cobertura', 'Catete', '22220-001', 'Rio de Janeiro', 'RJ', 'Brasil'),
(uuid_generate_v4(), 'Rua Itacolomi', '120', NULL, 'Higienópolis', '01239-020', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua Pará', '60', 'Apt 5', 'Centro', '86020-150', 'Londrina', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua 15 de Novembro', '400', NULL, 'Centro', '80020-301', 'Curitiba', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua Silva Jardim', '300', 'Apt 12', 'Batel', '80420-021', 'Curitiba', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua Tupis', '140', NULL, 'Centro', '30190-060', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Avenida Rio Branco', '200', 'Bloco A', 'Centro', '20090-003', 'Rio de Janeiro', 'RJ', 'Brasil'),
(uuid_generate_v4(), 'Rua da Glória', '450', NULL, 'Glória', '20241-180', 'Rio de Janeiro', 'RJ', 'Brasil'),
(uuid_generate_v4(), 'Rua São Luís', '100', 'Apt 101', 'Liberdade', '01504-030', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua dos Timbiras', '300', NULL, 'Centro', '30140-060', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Avenida Presidente Vargas', '100', 'Sala 20', 'Centro', '20070-002', 'Rio de Janeiro', 'RJ', 'Brasil'),
(uuid_generate_v4(), 'Avenida das Nações', '700', 'Apt 15', 'Asa Norte', '70070-010', 'Brasília', 'DF', 'Brasil'),
(uuid_generate_v4(), 'Rua Fernando de Noronha', '250', NULL, 'Batel', '80430-010', 'Curitiba', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Avenida Getúlio Vargas', '1500', 'Apt 18', 'Funcionários', '30112-000', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Rua Tamoios', '1000', NULL, 'Centro', '30150-090', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Rua Visconde do Rio Branco', '1200', 'Bloco C', 'Centro', '80010-210', 'Curitiba', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua da Consolação', '2200', NULL, 'Consolação', '01302-001', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua do Príncipe', '500', 'Sala 5', 'Centro', '80010-210', 'Curitiba', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Avenida Dom Pedro II', '600', NULL, 'Jardim América', '04340-001', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua Paraná', '400', 'Apt 34', 'Centro', '86020-150', 'Londrina', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua Major Sertório', '350', 'Apt 102', 'Vila Buarque', '01222-000', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua Maranhão', '650', 'Casa 1', 'Higienópolis', '01240-000', 'São Paulo', 'SP', 'Brasil'),
(uuid_generate_v4(), 'Rua Vicente Machado', '850', NULL, 'Batel', '80440-020', 'Curitiba', 'PR', 'Brasil'),
(uuid_generate_v4(), 'Rua Álvares Cabral', '950', 'Bloco A', 'Centro', '30170-001', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Avenida Amazonas', '1000', 'Apt 20', 'Centro', '30130-050', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Rua Curitiba', '500', NULL, 'Centro', '30170-120', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Avenida Sete de Setembro', '1200', 'Apt 25', 'Centro', '40060-000', 'Salvador', 'BA', 'Brasil'),
(uuid_generate_v4(), 'Rua Chile', '450', NULL, 'Centro Histórico', '40020-010', 'Salvador', 'BA', 'Brasil'),
(uuid_generate_v4(), 'Rua Carlos Gomes', '300', NULL, 'Centro', '40060-000', 'Salvador', 'BA', 'Brasil'),
(uuid_generate_v4(), 'Rua Tobias Barreto', '100', NULL, 'Ponta Verde', '57035-250', 'Maceió', 'AL', 'Brasil'),
(uuid_generate_v4(), 'Avenida Jatiúca', '900', 'Apt 34', 'Jatiúca', '57035-380', 'Maceió', 'AL', 'Brasil'),
(uuid_generate_v4(), 'Rua do Comércio', '650', 'Sala 101', 'Centro', '57020-010', 'Maceió', 'AL', 'Brasil'),
(uuid_generate_v4(), 'Rua do Sol', '700', 'Cobertura', 'Centro', '57020-110', 'Maceió', 'AL', 'Brasil'),
(uuid_generate_v4(), 'Rua Visconde de Suassuna', '800', NULL, 'Centro', '50050-540', 'Recife', 'PE', 'Brasil'),
(uuid_generate_v4(), 'Rua do Hospício', '350', 'Sala 201', 'Boa Vista', '50040-320', 'Recife', 'PE', 'Brasil'),
(uuid_generate_v4(), 'Rua Aurora', '500', NULL, 'Boa Vista', '50050-000', 'Recife', 'PE', 'Brasil'),
(uuid_generate_v4(), 'Avenida Conde da Boa Vista', '1000', NULL, 'Boa Vista', '50060-900', 'Recife', 'PE', 'Brasil'),
(uuid_generate_v4(), 'Rua da Praia', '700', 'Apt 20', 'Centro', '90010-060', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Miguel Tostes', '500', NULL, 'Rio Branco', '90430-060', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Dona Laura', '300', NULL, 'Rio Branco', '90430-011', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Avenida Bento Gonçalves', '1500', 'Apt 23', 'Partenon', '90650-001', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua João Alfredo', '800', NULL, 'Cidade Baixa', '90050-230', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Santana', '1200', 'Casa 2', 'Santana', '90040-370', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Marquês do Herval', '100', 'Bloco A', 'Centro', '96020-290', 'Pelotas', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Anchieta', '500', 'Sala 10', 'Centro', '96010-220', 'Pelotas', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua General Telles', '200', NULL, 'Centro', '96020-010', 'Pelotas', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Osório', '300', NULL, 'Centro', '96030-010', 'Pelotas', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Independência', '900', 'Bloco B', 'Centro', '96200-010', 'Rio Grande', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Marechal Deodoro', '450', NULL, 'Centro', '96200-020', 'Rio Grande', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Benjamin Constant', '650', 'Casa 3', 'Centro', '96210-090', 'Rio Grande', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Doutor Nilo Peçanha', '800', 'Apt 12', 'Centro', '96200-210', 'Rio Grande', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua João Pessoa', '350', NULL, 'Centro', '96200-150', 'Rio Grande', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua General Osório', '500', NULL, 'Centro', '96200-250', 'Rio Grande', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Júlio de Castilhos', '300', 'Sala 10', 'Centro', '96200-060', 'Rio Grande', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua João de Barro', '500', NULL, 'Jardim América', '60511-030', 'Fortaleza', 'CE', 'Brasil'),
(uuid_generate_v4(), 'Avenida Beira Mar', '1200', 'Apt 102', 'Meireles', '60165-120', 'Fortaleza', 'CE', 'Brasil'),
(uuid_generate_v4(), 'Rua das Flores', '150', 'Casa 5', 'Centro', '69005-070', 'Manaus', 'AM', 'Brasil'),
(uuid_generate_v4(), 'Rua do Comércio', '300', NULL, 'Centro', '69020-110', 'Manaus', 'AM', 'Brasil'),
(uuid_generate_v4(), 'Rua Carlos Gomes', '400', NULL, 'Centro', '40060-120', 'Salvador', 'BA', 'Brasil'),
(uuid_generate_v4(), 'Avenida Tancredo Neves', '800', NULL, 'Caminho das Árvores', '41820-020', 'Salvador', 'BA', 'Brasil'),
(uuid_generate_v4(), 'Rua São Francisco', '200', NULL, 'Centro', '64001-040', 'Teresina', 'PI', 'Brasil'),
(uuid_generate_v4(), 'Rua dos Pássaros', '700', 'Bloco B', 'Horto', '64002-030', 'Teresina', 'PI', 'Brasil'),
(uuid_generate_v4(), 'Rua Santa Clara', '650', NULL, 'Santa Efigênia', '30150-210', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Rua Timbiras', '980', 'Apt 12', 'Lourdes', '30160-030', 'Belo Horizonte', 'MG', 'Brasil'),
(uuid_generate_v4(), 'Rua Padre Chagas', '120', NULL, 'Moinhos de Vento', '90570-080', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Avenida Icaraí', '750', NULL, 'Cristal', '90810-000', 'Porto Alegre', 'RS', 'Brasil'),
(uuid_generate_v4(), 'Rua Tobias Barreto', '400', NULL, 'Farolândia', '49030-480', 'Aracaju', 'SE', 'Brasil'),
(uuid_generate_v4(), 'Avenida São João', '550', NULL, 'Jabotiana', '49095-020', 'Aracaju', 'SE', 'Brasil'),
(uuid_generate_v4(), 'Rua das Orquídeas', '700', NULL, 'Centro', '76804-110', 'Porto Velho', 'RO', 'Brasil'),
(uuid_generate_v4(), 'Avenida Sete de Setembro', '300', NULL, 'Centro', '76804-400', 'Porto Velho', 'RO', 'Brasil'),
(uuid_generate_v4(), 'Rua Ceará', '100', 'Casa 3', 'Centro', '79100-040', 'Campo Grande', 'MS', 'Brasil'),
(uuid_generate_v4(), 'Avenida Mato Grosso', '850', NULL, 'Centro', '79120-010', 'Campo Grande', 'MS', 'Brasil'),
(uuid_generate_v4(), 'Rua Goiás', '200', 'Apt 5', 'Centro', '74810-070', 'Goiânia', 'GO', 'Brasil'),
(uuid_generate_v4(), 'Avenida Tocantins', '900', NULL, 'Setor Central', '74030-030', 'Goiânia', 'GO', 'Brasil');
```

```sql
-- CLIENTES

INSERT INTO project_db.clientes (codigo, nome, sobrenome, cod_telefone, cod_endereco) 
VALUES 
(uuid_generate_v4(), 'Carlos', 'Silva', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 0), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 0)),
(uuid_generate_v4(), 'Ana', 'Souza', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 1), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 1)),
(uuid_generate_v4(), 'João', 'Pereira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 2), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 2)),
(uuid_generate_v4(), 'Mariana', 'Oliveira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 3), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 3)),
(uuid_generate_v4(), 'Pedro', 'Alves', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 4), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 4)),
(uuid_generate_v4(), 'Fernanda', 'Costa', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 5), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 5)),
(uuid_generate_v4(), 'Lucas', 'Ferreira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 6), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 6)),
(uuid_generate_v4(), 'Beatriz', 'Gomes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 7), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 7)),
(uuid_generate_v4(), 'Mateus', 'Rodrigues', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 8), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 8)),
(uuid_generate_v4(), 'Camila', 'Martins', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 9), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 9)),
(uuid_generate_v4(), 'Juliana', 'Mendes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 10), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 10)),
(uuid_generate_v4(), 'Ricardo', 'Santana', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 11), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 11)),
(uuid_generate_v4(), 'Gabriela', 'Lima', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 12), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 12)),
(uuid_generate_v4(), 'Thiago', 'Barbosa', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 13), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 13)),
(uuid_generate_v4(), 'Patrícia', 'Sousa', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 14), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 14)),
(uuid_generate_v4(), 'Felipe', 'Almeida', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 15), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 15)),
(uuid_generate_v4(), 'Isabela', 'Rocha', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 16), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 16)),
(uuid_generate_v4(), 'André', 'Fernandes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 17), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 17)),
(uuid_generate_v4(), 'Raquel', 'Moraes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 18), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 18)),
(uuid_generate_v4(), 'Bruno', 'Ribeiro', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 19), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 19)),
(uuid_generate_v4(), 'Letícia', 'Vargas', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 20), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 20)),
(uuid_generate_v4(), 'Diego', 'Silveira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 21), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 21)),
(uuid_generate_v4(), 'Daniela', 'Campos', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 22), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 22)),
(uuid_generate_v4(), 'Eduardo', 'Dias', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 23), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 23)),
(uuid_generate_v4(), 'Larissa', 'Pinto', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 24), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 24)),
(uuid_generate_v4(), 'Rodrigo', 'Melo', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 25), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 25)),
(uuid_generate_v4(), 'Vanessa', 'Cardoso', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 26), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 26)),
(uuid_generate_v4(), 'Henrique', 'Pereira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 27), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 27)),
(uuid_generate_v4(), 'Rafael', 'Moreira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 28), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 28)),
(uuid_generate_v4(), 'Júlia', 'Monteiro', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 29), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 29)),
(uuid_generate_v4(), 'Flávio', 'Nascimento', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 30), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 30)),
(uuid_generate_v4(), 'Adriana', 'Lopes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 31), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 31)),
(uuid_generate_v4(), 'Gustavo', 'Teixeira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 32), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 32)),
(uuid_generate_v4(), 'Rogério', 'Vieira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 33), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 33)),
(uuid_generate_v4(), 'Verônica', 'Carvalho', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 34), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 34)),
(uuid_generate_v4(), 'Marcelo', 'Santana', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 35), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 35)),
(uuid_generate_v4(), 'Roberta', 'Neves', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 36), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 36)),
(uuid_generate_v4(), 'Fábio', 'Azevedo', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 37), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 37)),
(uuid_generate_v4(), 'Simone', 'Queiroz', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 38), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 38)),
(uuid_generate_v4(), 'Vitor', 'Oliveira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 39), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 39)),
(uuid_generate_v4(), 'Tatiana', 'Ramos', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 40), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 40)),
(uuid_generate_v4(), 'Caio', 'Sousa', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 41), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 41)),
(uuid_generate_v4(), 'Rafaela', 'Silva', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 42), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 42)),
(uuid_generate_v4(), 'Ivan', 'Santos', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 43), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 43)),
(uuid_generate_v4(), 'Fabiana', 'Macedo', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 44), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 44)),
(uuid_generate_v4(), 'César', 'Leite', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 45), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 45)),
(uuid_generate_v4(), 'Marta', 'Castro', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 46), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 46)),
(uuid_generate_v4(), 'Wilson', 'Barros', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 47), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 47)),
(uuid_generate_v4(), 'Elaine', 'Dias', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 48), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 48)),
(uuid_generate_v4(), 'Márcia', 'Xavier', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 49), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 49)),
(uuid_generate_v4(), 'Patrícia', 'Freitas', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 50), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 50)),
(uuid_generate_v4(), 'Patrícia', 'Freitas', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 51), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 51)),
(uuid_generate_v4(), 'Robson', 'Martins', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 52), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 52)),
(uuid_generate_v4(), 'Helena', 'Moraes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 53), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 53)),
(uuid_generate_v4(), 'Fernando', 'Ramos', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 54), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 54)),
(uuid_generate_v4(), 'Sérgio', 'Cunha', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 55), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 55)),
(uuid_generate_v4(), 'Marcela', 'Silveira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 56), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 56)),
(uuid_generate_v4(), 'Joana', 'Azevedo', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 57), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 57)),
(uuid_generate_v4(), 'Eduardo', 'Borges', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 58), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 58)),
(uuid_generate_v4(), 'Alice', 'Moreira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 59), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 59)),
(uuid_generate_v4(), 'Marcos', 'Siqueira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 60), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 60)),
(uuid_generate_v4(), 'Cecília', 'Vaz', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 61), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 61)),
(uuid_generate_v4(), 'Bruno', 'Lacerda', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 62), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 62)),
(uuid_generate_v4(), 'Letícia', 'Fonseca', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 63), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 63)),
(uuid_generate_v4(), 'Matheus', 'Tavares', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 64), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 64)),
(uuid_generate_v4(), 'Marina', 'Assis', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 65), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 65)),
(uuid_generate_v4(), 'Thiago', 'Menezes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 66), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 66)),
(uuid_generate_v4(), 'Flávia', 'Coelho', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 67), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 67)),
(uuid_generate_v4(), 'Gustavo', 'Cardoso', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 68), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 68)),
(uuid_generate_v4(), 'Priscila', 'Rezende', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 69), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 69)),
(uuid_generate_v4(), 'Felipe', 'Pinto', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 70), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 70)),
(uuid_generate_v4(), 'Rafaela', 'Sousa', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 71), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 71)),
(uuid_generate_v4(), 'Leandro', 'Barbosa', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 72), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 72)),
(uuid_generate_v4(), 'Camila', 'Dias', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 73), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 73)),
(uuid_generate_v4(), 'Paulo', 'Miranda', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 74), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 74)),
(uuid_generate_v4(), 'Viviane', 'Araújo', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 75), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 75)),
(uuid_generate_v4(), 'Renato', 'Cavalcanti', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 76), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 76)),
(uuid_generate_v4(), 'Adriana', 'Lemos', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 77), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 77)),
(uuid_generate_v4(), 'Carlos', 'Queiroz', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 78), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 78)),
(uuid_generate_v4(), 'Vanessa', 'Ferreira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 79), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 79)),
(uuid_generate_v4(), 'Pedro', 'Moraes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 80), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 80)),
(uuid_generate_v4(), 'Júlia', 'Carvalho', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 81), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 81)),
(uuid_generate_v4(), 'Danilo', 'Freitas', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 82), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 82)),
(uuid_generate_v4(), 'Tatiana', 'Lima', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 83), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 83)),
(uuid_generate_v4(), 'Luciana', 'Ribeiro', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 84), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 84)),
(uuid_generate_v4(), 'Rodrigo', 'Teixeira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 85), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 85)),
(uuid_generate_v4(), 'Fernanda', 'Barros', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 86), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 86)),
(uuid_generate_v4(), 'Bruno', 'Correia', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 87), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 87)),
(uuid_generate_v4(), 'Aline', 'Gomes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 88), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 88)),
(uuid_generate_v4(), 'Vinícius', 'Rocha', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 89), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 89)),
(uuid_generate_v4(), 'Juliana', 'Alves', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 90), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 90)),
(uuid_generate_v4(), 'Rafael', 'Santos', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 91), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 91)),
(uuid_generate_v4(), 'Mariana', 'Lopes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 92), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 92)),
(uuid_generate_v4(), 'Renata', 'Cunha', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 93), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 93)),
(uuid_generate_v4(), 'Caio', 'Martins', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 94), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 94)),
(uuid_generate_v4(), 'Jéssica', 'Siqueira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 95), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 95)),
(uuid_generate_v4(), 'Lucas', 'Andrade', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 96), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 96)),
(uuid_generate_v4(), 'Tatiane', 'Pereira', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 97), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 97)),
(uuid_generate_v4(), 'José', 'Monteiro', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 98), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 98)),
(uuid_generate_v4(), 'Paulo', 'Nunes', (SELECT codigo FROM project_db.telefone LIMIT 1 OFFSET 99), (SELECT codigo FROM project_db.endereco LIMIT 1 OFFSET 99));
```

```sql
-- TIPO DE CONTA
INSERT INTO project_db.tipo_conta (codigo, nome) 
VALUES 
(uuid_generate_v4(), 'Pessoa Jurídica'),
(uuid_generate_v4(), 'Pessoa Física');
```

```sql
-- CONTA
INSERT INTO project_db.conta (codigo, cod_cliente, cod_tipo_conta, ativo) 
VALUES 
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 0), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 1), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 2), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 3), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 4), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 5), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 6), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 7), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 8), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 9), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 10), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 11), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 12), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 13), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 14), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 15), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 16), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 17), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 18), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 19), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 20), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 21), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 22), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 23), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 24), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 25), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 26), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 27), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 28), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 29), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 30), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 31), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 32), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 33), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 34), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 35), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 36), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 37), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 38), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 39), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 40), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 41), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 42), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 43), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 44), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 45), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 46), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 47), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 48), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 49), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 50), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 51), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 52), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 53), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 54), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 55), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 56), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 57), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 58), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 59), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 60), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 61), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 62), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 63), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 64), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 65), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 66), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 67), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 68), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 69), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 70), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 71), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 72), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 73), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 74), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 75), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 76), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 77), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 78), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 79), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 80), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 81), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 82), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 83), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 84), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 85), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 86), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 87), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 88), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 89), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 90), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 91), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 92), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 93), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 94), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 95), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 96), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 97), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 98), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Jurídica' LIMIT 1), true),
(uuid_generate_v4(), (SELECT codigo FROM project_db.clientes LIMIT 1 OFFSET 99), (SELECT codigo FROM project_db.tipo_conta WHERE nome = 'Pessoa Física' LIMIT 1), true);
```

```sql

-- DIRETOR
-- Inserindo 10 diretores na tabela diretor
INSERT INTO project_db.diretor (codigo, nome, email, ativo)
VALUES 
(uuid_generate_v4(), 'Marcos Silva', 'marcos.silva@exemplo.com', true),
(uuid_generate_v4(), 'Ana Souza', 'ana.souza@exemplo.com', true),
(uuid_generate_v4(), 'Carlos Mendes', 'carlos.mendes@exemplo.com', true),
(uuid_generate_v4(), 'Juliana Pereira', 'juliana.pereira@exemplo.com', true),
(uuid_generate_v4(), 'Rodrigo Lima', 'rodrigo.lima@exemplo.com', true),
(uuid_generate_v4(), 'Fernanda Alves', 'fernanda.alves@exemplo.com', true),
(uuid_generate_v4(), 'Rafael Costa', 'rafael.costa@exemplo.com', false),
(uuid_generate_v4(), 'Patrícia Martins', 'patricia.martins@exemplo.com', true),
(uuid_generate_v4(), 'Leonardo Fernandes', 'leonardo.fernandes@exemplo.com', true),
(uuid_generate_v4(), 'Bianca Castro', 'bianca.castro@exemplo.com', true);
```

```sql
-- TIPO_PRODUTO
INSERT INTO project_db.tipo_produto (codigo, nome)
VALUES
(uuid_generate_v4(), 'Conta Digital'),
(uuid_generate_v4(), 'Cartão de Crédito'),
(uuid_generate_v4(), 'Conta de Pagamento'),
(uuid_generate_v4(), 'Investimento'),
(uuid_generate_v4(), 'Seguro'),
(uuid_generate_v4(), 'Empréstimo'),
(uuid_generate_v4(), 'Financiamento'),
(uuid_generate_v4(), 'Crédito'),
(uuid_generate_v4(), 'Cashback'),
(uuid_generate_v4(), 'Portabilidade de Salário'),
(uuid_generate_v4(), 'Connect Car');
```

```sql
-- PRODUTO
INSERT INTO project_db.produto (codigo, cod_tipo_produto, cod_diretor, nome, descricao, ativo, custo_mensal) 
VALUES 
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Conta Digital' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 0), 'Conta Digital Premium', 'Conta com benefícios adicionais, sem tarifas mensais.', true, 29.90),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Conta Digital' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 1), 'Conta Digital Padrão', 'Conta básica sem tarifas mensais.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Cartão de Crédito' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 2), 'Cartão de Crédito Internacional', 'Cartão de crédito sem anuidade com cobertura internacional.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Cartão de Crédito' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 3), 'Cartão de Crédito Platinum', 'Cartão de crédito com vantagens exclusivas e anuidade grátis no primeiro ano.', true, 49.90),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Cartão de Crédito' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 4), 'Cartão de Crédito Black', 'Cartão de crédito com benefícios exclusivos e cashback em compras.', true, 79.90),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Conta de Pagamento' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 5), 'Conta de Pagamento Instantâneo', 'Conta para transações instantâneas, sem custos adicionais.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Investimento' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 6), 'Investimento Renda Fixa', 'Produto de investimento com rendimentos previsíveis.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Investimento' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 7), 'Investimento Renda Variável', 'Produto de investimento com maior rentabilidade e maior risco.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Seguro' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 8), 'Seguro Cartão Protegido', 'Seguro para proteger transações feitas com o cartão de crédito.', true, 9.90),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Empréstimo' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 9), 'Empréstimo Pessoal Digital', 'Empréstimo pessoal com taxas competitivas e aprovação rápida.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Empréstimo' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 0), 'Empréstimo com Garantia', 'Empréstimo com garantia de veículo ou imóvel.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Financiament' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 1), 'Financiamento de Veículos', 'Produto de financiamento de veículos com juros baixos.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Financiamento' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 2), 'Financiamento Imobiliário Digital', 'Produto de financiamento imobiliário com aprovação online.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Crédito' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 3), 'Crédito Consignado Digital', 'Empréstimo consignado com taxas reduzidas.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Cashback' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 4), 'Cashback Rewards', 'Programa de recompensas com cashback em compras.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Seguro' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 5), 'Seguro de Vida Digital', 'Seguro de vida com cobertura ampla e preços acessíveis.', true, 15.90),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Investimento' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 6), 'Investimento Multimercado', 'Produto de investimento que combina renda fixa e variável.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Portabilidade de Salário' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 7), 'Portabilidade de Salário', 'Serviço de portabilidade de salário sem custos adicionais.', true, 0.00),
(uuid_generate_v4(), (SELECT codigo FROM project_db.tipo_produto WHERE nome = 'Crédito' LIMIT 1), (SELECT codigo FROM project_db.diretor LIMIT 1 OFFSET 8), 'Crédito Rotativo Flex', 'Linha de crédito rotativo com pagamento flexível.', true, 0.00);
```

```sql
UPDATE project_db.produto
SET custo_mensal = ROUND((random() * 200)::numeric, 2)
WHERE custo_mensal = 0;
```

```sql
-- PRODUTO_CONTA
DO $$
DECLARE
    conta_uuid UUID;
    produto_uuid UUID;
BEGIN
    -- Para cada conta, atribua entre 1 e 5 produtos aleatórios
    FOR conta_uuid IN (SELECT codigo FROM project_db.conta)
    LOOP
        -- Atribuindo de 1 a 5 produtos aleatórios para cada conta
        FOR i IN 1..(1 + floor(random() * 3))::integer
        LOOP
            -- Selecionando um produto aleatório
            SELECT codigo INTO produto_uuid FROM project_db.produto
            OFFSET floor(random() * (SELECT COUNT(*) FROM project_db.produto));
            
            -- Inserindo a associação de conta e produto
            INSERT INTO project_db.produto_conta (cod_conta, cod_produto)
            VALUES (conta_uuid, produto_uuid)
            ON CONFLICT DO NOTHING;  -- Evita inserções duplicadas
        END LOOP;
    END LOOP;
END $$;
```

```sql
-- Consulta questao 03
select
	nome as PRODUTO,
	custo_mensal  as VALOR
from 
	produto p
where
	custo_mensal > 100
order by
	custo_mensal,
	nome
```

```sql	
-- Consulta questao 04
SELECT 
    p.codigo AS ID, 
    p.custo_mensal AS VALOR
FROM 
    produto p
WHERE 
    p.custo_mensal > (SELECT AVG(custo_mensal) FROM produto)
	
-- OU
    
WITH media AS (SELECT AVG(custo_mensal) AS avg_custo FROM produto)
SELECT 
    p.codigo AS ID, 
    p.custo_mensal AS VALOR
FROM 
    produto p, media
WHERE 
    p.custo_mensal > media.avg_custo;
```

```sql
-- Consulta questao 05
   
WITH produto_categoria AS (
    SELECT
        p.codigo,
        p.nome AS produto,
        tp.nome AS categoria,
        p.custo_mensal 
    FROM 
        produto p
    LEFT JOIN tipo_produto tp 
    ON p.cod_tipo_produto = tp.codigo
)
SELECT
    categoria,
    ROUND(AVG(custo_mensal)::numeric, 2) AS preco_medio
FROM 
    produto_categoria
GROUP BY
    categoria
ORDER BY 
    categoria;
```

```sql
-- EXERCICIOS 6 E 7
   
-- Criando a tabela turma
CREATE TABLE project_db.turma (
    id_turma INT PRIMARY KEY,
    codigo_turma VARCHAR(50) NOT NULL,
    nome_turma VARCHAR(100) NOT NULL
);
```

```sql
-- Criando a tabela aluno
CREATE TABLE project_db.aluno (
    id_aluno INT PRIMARY KEY,
    nome_aluno VARCHAR(100) NOT NULL,
    aluno_alocado BOOLEAN DEFAULT NULL,
    id_turma INT,
    CONSTRAINT fk_turma FOREIGN KEY (id_turma) REFERENCES project_db.turma (id_turma)
);
```

```sql
-- Inserindo duas turmas na tabela turma
INSERT INTO project_db.turma (id_turma, codigo_turma, nome_turma)
VALUES (1, 'TURMA101', 'Matemática Básica'),
       (2, 'TURMA102', 'História Geral');
-- Inserindo alunos alocados em turmas, com a coluna aluno_alocado como NULL
INSERT INTO project_db.aluno (id_aluno, nome_aluno, aluno_alocado, id_turma)
VALUES (1, 'João da Silva', NULL, 1),  -- Aluno alocado na turma de Matemática
       (2, 'Maria Oliveira', NULL, 2);  -- Aluno alocado na turma de História
```

```sql
-- Inserindo alunos não alocados em nenhuma turma, com id_turma como NULL e aluno_alocado como NULL
INSERT INTO project_db.aluno (id_aluno, nome_aluno, aluno_alocado, id_turma)
VALUES (3, 'Pedro Santos', NULL, NULL),
       (4, 'Ana Pereira', NULL, NULL);
```

```sql
-- Atualizando a coluna aluno_alocado:
-- Se o aluno estiver associado a uma turma (id_turma não é NULL), ele recebe True (TRUE)
-- Se o aluno não estiver associado a uma turma (id_turma é NULL), ele recebe False (FALSE)

UPDATE project_db.aluno
SET aluno_alocado = CASE
    WHEN id_turma IS NOT NULL THEN TRUE
    ELSE FALSE
END;

select * from project_db.turma
````


