--######################################################################
--########################### DATABASE #################################
--######################################################################


CREATE DATABASE avaliaE;
Go

USE avaliaE;
Go

--######################################################################
--########################### TABELAS ##################################
--######################################################################

CREATE TABLE ESTUDANTE (
	matricula INT PRIMARY KEY,
	senha VARCHAR(10),
	nome VARCHAR(100),
	email VARCHAR(100),
	imagem IMAGE,
	adm INT
);
GO

CREATE TABLE DEPARTAMENTO (
	codigo INT PRIMARY KEY,
	nome VARCHAR(100)
);
GO

CREATE TABLE PROFESSOR (
	matricula INT PRIMARY KEY,
	senha VARCHAR(10),
	departamento INT,
	nome VARCHAR(100),
	email VARCHAR(100)
);
GO

ALTER TABLE PROFESSOR
	ADD CONSTRAINT fk_departamento_prof
	FOREIGN KEY (departamento)
	REFERENCES DEPARTAMENTO(codigo);
GO

CREATE TABLE DISCIPLINA (
	codigo INT PRIMARY KEY,
	departamento INT,
	nome VARCHAR(100)
);

ALTER TABLE DISCIPLINA
	ADD CONSTRAINT fk_departamento_disc
	FOREIGN KEY (departamento)
	REFERENCES DEPARTAMENTO(codigo);
GO

CREATE TABLE TURMA (
	codigo INT IDENTITY(1,1) PRIMARY KEY,
	disciplina INT,
	professor INT
);
GO
ALTER TABLE TURMA
	ADD CONSTRAINT fk_professor_turma
	FOREIGN KEY (professor)
	REFERENCES PROFESSOR(matricula);
GO
ALTER TABLE TURMA
	ADD CONSTRAINT fk_disciplina_turma
	FOREIGN KEY (disciplina)
	REFERENCES DISCIPLINA(codigo);
GO

CREATE TABLE AVALIACAO (
	codigo INT IDENTITY(1,1) PRIMARY KEY, --ALTERAR CONFORME FOR O SGBD UTILIZADO
	estudante INT,
	turma INT,
	avaliacao VARCHAR(300),
	denuncia INT
);
GO

ALTER TABLE AVALIACAO
	ADD CONSTRAINT fk_estudante_av
	FOREIGN KEY(estudante)
	REFERENCES ESTUDANTE(matricula)
GO

ALTER TABLE AVALIACAO
	ADD CONSTRAINT fk_turma_av
	FOREIGN KEY(turma)
	REFERENCES TURMA(codigo);
GO


--######################################################################
--########################### PROCEDURES ###############################
--######################################################################

--###############  AUTENTICAÇÃO ###################
CREATE OR ALTER PROCEDURE Auth_ESTUDANTE
	@matricula INT,
	@senha INT
AS
BEGIN
	IF EXISTS (
		SELECT 1
		FROM ESTUDANTE
		WHERE matricula = @matricula AND senha = @senha)
		BEGIN
			IF (
				SELECT adm 
				FROM ESTUDANTE 
				WHERE matricula = @matricula) = 1 
				BEGIN
					SELECT 2 AS STATUS
				END
			ELSE
				BEGIN
					SELECT 1 AS STATUS 
				END
		END
	ELSE
		BEGIN
			SELECT 0 AS STATUS
		END
END
GO

CREATE OR ALTER PROCEDURE Auth_PROFESSOR
	@matricula INT,
	@senha INT
AS
BEGIN
	IF EXISTS (
		SELECT 1
		FROM PROFESSOR
		WHERE matricula = @matricula AND senha = @senha
	)
		BEGIN
			SELECT 1 AS STATUS 
		END
	ELSE
		BEGIN
			SELECT 0 AS STATUS
		END
END
GO

--###############  ESTUDANTE ###################

CREATE PROCEDURE C_ESTUDANTE
	@matricula INT,
	@senha VARCHAR(10),
	@nome VARCHAR(100),
	@email VARCHAR(100)
AS
BEGIN
	INSERT INTO 
	ESTUDANTE(
				matricula,
				senha,
				nome,
				email)
	VALUES( 
				@matricula,
				@senha,
				@nome,
				@email);
END;
GO

CREATE PROCEDURE R_ESTUDANTE
	@matricula INT
AS
	BEGIN
		SELECT * 
		FROM ESTUDANTE
		WHERE matricula = @matricula
	END
GO

CREATE PROCEDURE U_ESTUDANTE
	@matricula INT,
	@senha VARCHAR(10),
	@nome VARCHAR(100),
	@email VARCHAR(100)
AS
BEGIN
	UPDATE ESTUDANTE
	SET 
		senha = @senha,
		nome = @nome,
		email = @email
	WHERE matricula = @matricula
END;
GO

CREATE OR ALTER PROCEDURE D_ESTUDANTE
	@matricula INT
AS
BEGIN

	DELETE
	FROM AVALIACAO
	WHERE estudante = @matricula

	DELETE 
	FROM ESTUDANTE
	WHERE matricula = @matricula
	SELECT 1 AS STATUS
END
GO

--###############  PROFESSOR ###################

CREATE PROCEDURE C_PROFESSOR
	@matricula INT,
	@senha VARCHAR(10),
	@departamento INT,
	@nome VARCHAR(100),
	@email VARCHAR(100)
AS
BEGIN
	INSERT INTO 
	PROFESSOR(
				matricula,
				senha,
				departamento,
				nome,
				email)
	VALUES( 
				@matricula,
				@senha,
				@departamento,
				@nome,
				@email);
END;
GO

CREATE OR ALTER PROCEDURE R_PROFESSOR
	@matricula INT
AS
	BEGIN
		SELECT * 
		FROM PROFESSOR
		WHERE matricula = @matricula
	END
GO

CREATE OR ALTER PROCEDURE U_PROFESSOR
	@matricula INT,
	@senha VARCHAR(10),
	@departamento INT,
	@nome VARCHAR(100),
	@email VARCHAR(100)
AS
BEGIN
	UPDATE PROFESSOR
	SET 
		senha = @senha,
		departamento = @departamento,
		nome = @nome,
		email = @email
	WHERE matricula = @matricula
END;
GO

CREATE OR ALTER PROCEDURE D_PROFESSOR
	@matricula INT
AS
BEGIN
	IF EXISTS(
				SELECT 1
				FROM TURMA
				WHERE professor = @matricula)
		BEGIN
			SELECT 0 AS STATUS
		END
	ELSE
		BEGIN
			DELETE 
			FROM PROFESSOR
			WHERE matricula = @matricula
		END
END
GO


--###############  TURMA #######################
CREATE OR ALTER PROCEDURE R_TURMA
	@codigo INT
AS
BEGIN
	SELECT *
	FROM TURMA
	WHERE codigo = @codigo
END
GO

--###############  AVALIACAO ###################

CREATE OR ALTER PROCEDURE C_AVALIACAO
	@estudante INT,
	@turma INT,
	@avaliacao VARCHAR(300),
	@denuncia INT
AS
BEGIN
	INSERT INTO AVALIACAO (
							estudante,
							turma,
							avaliacao,
							denuncia)
	VALUES (
							@estudante,
							@turma,
							@avaliacao,
							@denuncia)

END
GO

CREATE OR ALTER PROCEDURE lista_AVALIACAO
	@turma INT
AS
BEGIN
	SELECT estudante, avaliacao  
	FROM AVALIACAO 
	WHERE turma = @turma
END
GO

CREATE OR ALTER PROCEDURE lista_estudante_AVALIACAO
	@turma INT,
	@estudante INT
AS
BEGIN
	SELECT codigo, avaliacao  
	FROM AVALIACAO 
	WHERE turma = @turma AND estudante = @estudante
END
GO

CREATE OR ALTER PROCEDURE U_AVALIACAO
	@codigo INT,
	@avaliacao VARCHAR(300),
	@denuncia INT
AS
BEGIN
	UPDATE AVALIACAO
	SET avaliacao = @avaliacao, denuncia = @denuncia
	WHERE codigo = @codigo
END
GO

CREATE OR ALTER PROCEDURE D_AVALIACAO
	@codigo INT
AS
BEGIN
	DELETE FROM AVALIACAO
	WHERE codigo = @codigo
END
GO



--######################################################################
--############################### VIEW #################################
--######################################################################

CREATE VIEW lista_PROFESSOR_DEPARTAMENTO 
AS
SELECT p.nome, d.nome as departamento
FROM PROFESSOR  p
INNER JOIN DEPARTAMENTO d ON p.departamento = d.codigo;
GO

CREATE OR ALTER VIEW lista_DEPARTAMENTO
AS
SELECT CONCAT(codigo, ' - ', nome) as Departamento
FROM DEPARTAMENTO
GO

CREATE OR ALTER VIEW lista_TURMA
AS
SELECT CONCAT(T.codigo, ' - ', D.nome, ' - ', P.nome) as Turma
FROM TURMA T
INNER JOIN DISCIPLINA D ON T.disciplina = D.codigo
JOIN PROFESSOR P ON T.professor = P.matricula
GO



--######################################################################
--########### INSERÇÃO DE 3 LINHAS EM CADA TABELA ###################### 
--######################################################################

-- DEPARTAMENTO

INSERT INTO DEPARTAMENTO (codigo, nome) VALUES (643, 'CENTRO DE APOIO AO DESENVOLVIMENTO TECNOLÓGICO - BRASÍLIA')
INSERT INTO DEPARTAMENTO (codigo, nome) VALUES (640, 'CENTRO DE DESENVOLVIMENTO SUSTENTÁVEL - BRASÍLIA')
INSERT INTO DEPARTAMENTO (codigo, nome) VALUES (314, 'CENTRO DE EXCELÊNCIA EM TURISMO - BRASÍLIA')

-- ESTUDANTE

EXECUTE C_ESTUDANTE 123, '123', 'Bruno Miranda', 'bruno@'
EXECUTE C_ESTUDANTE 456, '456', 'Ruth Andrade', 'ruth@'
EXECUTE C_ESTUDANTE 789, '789', 'Mariana Amorim', 'mariana@'


-- PROFESSOR

EXECUTE C_PROFESSOR 123, '123', 314, 'Samira Suelen', 'suelen@'
EXECUTE C_PROFESSOR 456, '456', 640, 'David Soares', 'david@'
EXECUTE C_PROFESSOR 789, '789', 643, 'Cecilia Rosa', 'cecilia@'



-- DISCIPLINA

INSERT INTO DISCIPLINA (codigo, departamento, nome) VALUES (123, 643, 'Algoritmos')
INSERT INTO DISCIPLINA (codigo, departamento, nome) VALUES (456, 640, 'Floriculturismo')
INSERT INTO DISCIPLINA (codigo, departamento, nome) VALUES (789, 314, 'Português')

--TURMA

INSERT INTO TURMA (disciplina, professor) VALUES (789, 123)
INSERT INTO TURMA (disciplina, professor) VALUES (123, 456)
INSERT INTO TURMA (disciplina, professor) VALUES (456, 789)

-- AVALIACAO

INSERT INTO AVALIACAO (estudante, turma, avaliacao, denuncia) VALUES (456, 1, 'Aula chata', 1)
INSERT INTO AVALIACAO (estudante, turma, avaliacao, denuncia) VALUES (789, 2, 'Aula boa', 0)
INSERT INTO AVALIACAO (estudante, turma, avaliacao, denuncia) VALUES (123, 3, 'Aula media', 0)

------- CONFERÊNCIA

SELECT * FROM ESTUDANTE
SELECT * FROM PROFESSOR
SELECT * FROM DEPARTAMENTO
SELECT * FROM DISCIPLINA
SELECT * FROM TURMA
SELECT * FROM AVALIACAO

--