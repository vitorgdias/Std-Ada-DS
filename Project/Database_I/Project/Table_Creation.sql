CREATE TABLE project_db.telefone (
    codigo varchar(20) PRIMARY KEY,
    comecial varchar(100) NULL,
    pessoal varchar(20) NOT NULL
)

CREATE TABLE project_db.endereco (
    codigo varchar(20) PRIMARY KEY,
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
    codigo varchar(20) PRIMARY KEY,
    nome varchar(100) NOT NULL,
    sobrenome varchar(100) NOT NULL,
    cod_telefone varchar(20) NULL,
    cod_endereco varchar(20) NOT NULL,
    FOREIGN KEY (cod_telefone) REFERENCES project_db.telefone(codigo),
    FOREIGN KEY (cod_endereco) REFERENCES project_db.endereco(codigo)
);

CREATE TABLE project_db.tipo_conta (
    codigo varchar(20) PRIMARY KEY,
    nome varchar(100) NOT NULL
)

CREATE TABLE project_db.conta (
    codigo varchar(20) PRIMARY KEY,
    cod_cliente varchar(20) NOT NULL,
    cod_tipo_conta varchar(20) NOT NULL,
    ativo BOOLEAN NOT NULL,
    FOREIGN KEY (cod_cliente) REFERENCES project_db.clientes(codigo),
    FOREIGN KEY (cod_tipo_conta) REFERENCES project_db.tipo_conta(codigo)
)

CREATE TABLE project_db.tipo_produto (
    codigo varchar(20) PRIMARY KEY,
    nome varchar(100) NOT NULL
)

CREATE TABLE project_db.diretor (
    codigo varchar(20) PRIMARY KEY,
    nome varchar(100) NOT NULL,
    email varchar(100) UNIQUE NOT NULL,
    ativo BOOLEAN NOT NULL
)

CREATE TABLE project_db.produto (
    codigo varchar(20) PRIMARY KEY,
    cod_tipo_produto varchar(20) NOT NULL,
    cod_diretor varchar(20) NOT NULL,
    nome varchar(100) NOT NULL,
    descricao varchar(100) NOT NULL,
    ativo BOOLEAN NOT NULL,
    custo_mensal FLOAT NOT NULL,
    FOREIGN KEY (cod_tipo_produto) REFERENCES project_db.tipo_produto(codigo),
    FOREIGN KEY (cod_diretor) REFERENCES project_db.diretor(codigo)
)

CREATE TABLE project_db.produto_conta (
    cod_conta varchar(20) NOT NULL,
    cod_produto varchar(20) NOT NULL,
    FOREIGN KEY (cod_conta) REFERENCES project_db.conta(codigo),
    FOREIGN KEY (cod_produto) REFERENCES project_db.produto(codigo)
)