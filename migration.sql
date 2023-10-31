CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 422ce43dda4a

INSERT INTO alembic_version (version_num) VALUES ('422ce43dda4a');

-- Running upgrade 422ce43dda4a -> 1aabfbda1eab

ALTER TABLE patients ADD COLUMN is_deceased VARCHAR(30) NOT NULL;

UPDATE alembic_version SET version_num='1aabfbda1eab' WHERE alembic_version.version_num = '422ce43dda4a';

