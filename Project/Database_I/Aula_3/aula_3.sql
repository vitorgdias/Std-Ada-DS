-- Restrições de chave estrangeira do SQL
-- Criação das tabelas dept e emp
CREATE TABLE dept (
    CodigoDepto INT PRIMARY KEY,
    NomeDepto VARCHAR(200)
);

CREATE TABLE emp (
    CodigoEmp INT PRIMARY KEY,
    Nome VARCHAR(200),
    CodigoDepto INT REFERENCES dept(CodigoDepto),
    CategFuncional VARCHAR(200)
);

-- insert de valores na tabela dept
INSERT INTO dept(CodigoDepto, NomeDepto) VALUES(1, 'Compras'); -- insert informando as colunas
INSERT INTO dept VALUES(2, 'Engenharia'); -- insert com as colunas na ordem de criação. Não precisa especificar as colunas, mas tem que incluir TODAS que foram criadas
INSERT INTO dept VALUES(3, 'Compras');
INSERT INTO dept (NomeDepto, CodigoDepto) VALUES('Financeiro', 4); -- insert informando as colunas fora de ordem

-- insert de valores na tabela emo
INSERT INTO emp VALUES(1, 'Souza', 1)
INSERT INTO emp VALUES(1, 'Souza', 6) -- Falha na inserção pois não existe a chave estrangeira 6 na tabela dept
INSERT INTO emp VALUES(2, 'Santos', 2, 'C5')

DELETE FROM dept WHERE CodigoDepto = 1 -- Falha no delete pois primeiro tem que deletar ou fazer update do CodigoDepto que está na tabela emp
SELECT * FROM emp
SELECT * FROM dept

DELETE FROM emp WHERE CodigoEmp = 1 -- Deletado com sucesso
SELECT * FROM emp

DELETE FROM dept WHERE CodigoDepto = 1 -- Deletado com sucesso
SELECT * FROM emp