-- Criar tabela T_LEITURA
drop table t_irrigacao;
drop table t_leitura;


CREATE TABLE t_leitura (
    id_leitura           NUMBER NOT NULL,
    leitura_ph           FLOAT(3) NOT NULL,
    leitura_fosforo_p    FLOAT(3) NOT NULL,
    leitura_potassio_k   FLOAT(3) NOT NULL,
    leitura_umidade      FLOAT(3) NOT NULL,
    leitura_temperatura  NUMBER(4, 1) NOT NULL,
    data_hora            TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    status_irrigacao     CHAR(20),
    CONSTRAINT t_leitura_pk PRIMARY KEY (id_leitura)
);

-- Criar tabela T_IRRIGACAO
CREATE TABLE t_irrigacao (
    id_irrigacao      NUMBER NOT NULL,
    id_leitura        NUMBER NOT NULL,
    irrigacao_cultura VARCHAR(100) NOT NULL,
    CONSTRAINT t_irrigacao_pk PRIMARY KEY (id_irrigacao),
    CONSTRAINT t_irrigacao_t_leitura_fk FOREIGN KEY (id_leitura)
        REFERENCES t_leitura (id_leitura)
);

-- Criar sequência para T_IRRIGACAO



CREATE SEQUENCE irrigacao_seq START WITH 1 INCREMENT BY 1;


-- Criar trigger para o preenchimento automático do ID na T_IRRIGACAO
CREATE OR REPLACE TRIGGER trg_t_irrigacao_id
BEFORE INSERT ON t_irrigacao
FOR EACH ROW
BEGIN
    :NEW.id_irrigacao := irrigacao_seq.NEXTVAL;
END;
/


CREATE SEQUENCE leitura_seq START WITH 1 INCREMENT BY 1;

-- Pesquisas testes
SELECT i.id_irrigacao, i.irrigacao_cultura, l.status_irrigacao
FROM t_irrigacao i
JOIN t_leitura l ON i.id_leitura = l.id_leitura
WHERE TO_CHAR(data_hora, 'DD/MM/YY') LIKE '02/12/24';

select * from t_irrigacao;
select * from t_leitura;

SELECT i.irrigacao_cultura, TO_CHAR(l.data_hora, 'DD/MM/YYYY HH24:MI:SS') AS data_hora
FROM t_irrigacao i
JOIN t_leitura l ON i.id_leitura = l.id_leitura
WHERE TRUNC(l.data_hora) = TO_DATE('03/12/2024', 'DD/MM/YYYY')