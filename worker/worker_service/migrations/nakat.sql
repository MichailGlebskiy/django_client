CREATE TABLE test.worker
(
	id uuid not null default uuid_generate_v1(),
    first_name CHARACTER VARYING,
    second_name CHARACTER VARYING,
    age INTEGER,
    man BOOLEAN,
	CONSTRAINT pk_worker PRIMARY KEY (id)
)
WITH(
    OIDS = FALSE
);
ALTER TABLE test.worker OWNER TO postgres;
CREATE TABLE test.projects
(
	id uuid not null default uuid_generate_v1(),
	workers_project CHARACTER VARYING,
	salary INTEGER not null,
	worker uuid not null,
	CONSTRAINT fk_worker FOREIGN KEY (worker)
	 REFERENCES test.worker (id)
)
WITH(
    OIDS = FALSE
);
ALTER TABLE test.projects OWNER TO postgres;