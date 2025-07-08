BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 37e6c288abe8

CREATE TABLE users (
    id UUID NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    username VARCHAR(16) NOT NULL, 
    password VARCHAR(60) NOT NULL, 
    PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_users_username ON users (username);

INSERT INTO alembic_version (version_num) VALUES ('37e6c288abe8') RETURNING alembic_version.version_num;

COMMIT;
