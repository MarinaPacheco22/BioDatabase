#Consultas para crear la tabla enfermedad y sus respectivas columnas.
CREATE TABLE enfermedad (id_enfermedad int(20) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria',
PRIMARY KEY (id_enfermedad)) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='tabla de enfermedades';

ALTER TABLE enfermedad ADD nombre varchar(100);
INSERT INTO enfermedad (nombre) (SELECT nombre FROM datos_enfermedad group by nombre order by nombre ASC );

ALTER TABLE enfermedad ADD orphanumber varchar(255);
UPDATE enfermedad e inner join datos_enfermedad d on e.nombre = d.nombre SET e.orphanumber = d.orphanumber;

ALTER TABLE enfermedad ADD edad_comienzo varchar(255);
UPDATE enfermedad e inner join datos_enfermedad d on e.nombre = d.nombre SET e.edad_comienzo = d.edad_comienzo WHERE d.edad_comienzo IS NOT NULL;

ALTER TABLE enfermedad ADD edad_fallecimiento varchar(255);
UPDATE enfermedad e inner join datos_enfermedad d on e.nombre = d.nombre SET e.edad_fallecimiento = d.edad_fallecimiento WHERE d.edad_fallecimiento IS NOT NULL;

ALTER TABLE enfermedad ADD herencia varchar(255);
UPDATE enfermedad e inner join datos_enfermedad d on e.nombre = d.nombre SET e.herencia = d.herencia WHERE d.herencia IS NOT NULL;

SELECT * FROM enfermedad; 	#Así quedaría la tabla enfermedad

#Consultas para crear la tabla localizacion y sus columnas
CREATE TABLE localizacion (id_Localizacion int(20) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria',
PRIMARY KEY (id_Localizacion)) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='tabla de localizaciones';

ALTER TABLE localizacion ADD Localizacion varchar(50);
INSERT INTO localizacion (Localizacion) (SELECT nombre_localizacion FROM datos_enfermedad group by nombre_localizacion order by nombre_localizacion ASC);

SELECT * FROM localizacion; 	#Así quedaría la tabla localización

#A continuación vamos a crear una columna en la tabla enfermedad en las que aparezca la id de la localización correspondiente.
#Lo haremos mediante un foreign key.
ALTER TABLE enfermedad ADD id_localizacion int(11);
UPDATE enfermedad e inner join datos_enfermedad d on e.nombre = d.nombre inner join localizacion l on d.nombre_localizacion = l.Localizacion SET e.id_localizacion = l.id_localizacion;

ALTER TABLE enfermedad ADD FOREIGN KEY fk_localizacion (id_localizacion) REFERENCES localizacion (id_Localizacion);

SELECT * FROM enfermedad; 	#Finalmente, la tabla enfermedad quedaría así

#Consultas para crear la tabla gen y sus respectivas columnas.
CREATE TABLE gen (id_gen int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria',
PRIMARY KEY (id_gen)) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='tabla de genes';

ALTER TABLE gen ADD nombre varchar(255);
INSERT INTO gen (nombre) (SELECT gene FROM datos_gen group by gene order by gene ASC);

ALTER TABLE gen ADD simbolo varchar(255);
UPDATE gen g inner join datos_gen dat on g.nombre = dat.gene SET simbolo = dat.symbol_gene;

ALTER TABLE gen ADD localizacion varchar(255);
UPDATE gen g inner join datos_gen dat on g.nombre = dat.gene SET localizacion = dat.gene_locus WHERE dat.gene_locus IS NOT NULL;

ALTER TABLE gen ADD tipo varchar(255);
UPDATE gen g inner join datos_gen dat on g.nombre = dat.gene SET tipo = gene_type;

SELECT * FROM gen; 	#La tabla gen quedaría así.

#A continuación vamos a crear la tabla enfermedad_gen que relaciona el id_enfermedad de la tabla enfermedad con el id_gen de la tabla gen.
#Lo haremos también añadiendo foreign keys
CREATE TABLE enfermedad_gen AS SELECT e.id_enfermedad, g.id_gen FROM enfermedad e join datos_gen d on e.nombre = d.nombre_enfermedad join gen g on d.gene = g.nombre group by g.id_gen order by e.id_enfermedad;

ALTER TABLE enfermedad_gen ADD FOREIGN KEY fk_enfermedad (id_enfermedad) REFERENCES enfermedad (id_enfermedad);
ALTER TABLE enfermedad_gen ADD  FOREIGN KEY fk_gen (id_gen) REFERENCES gen (id_gen);

#Creacion de la tabla fenotipo y sus columnas.
CREATE TABLE fenotipo (id_fenotipo int(10) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria',
PRIMARY KEY (id_fenotipo)) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='tabla de los fenotipos';

ALTER TABLE fenotipo ADD fenotipo_id varchar(12);
INSERT INTO fenotipo (fenotipo_id) (SELECT id_fenotipo FROM datos_fenotipo group by id_fenotipo order by id_fenotipo ASC);

ALTER TABLE fenotipo ADD frecuencia varchar(255);
UPDATE fenotipo f inner join datos_fenotipo dat on f.fenotipo_id = dat.id_fenotipo SET f.frecuencia = dat.frecuencia_sale;

ALTER TABLE fenotipo ADD nombre_fenotipo varchar(255);
UPDATE fenotipo f inner join datos_fenotipo dat on f.fenotipo_id = dat.id_fenotipo SET f.nombre_fenotipo = dat.fenotipo_nombre;

ALTER TABLE fenotipo ADD criterio_diagnostico varchar(255);
UPDATE fenotipo f inner join datos_fenotipo dat on f.fenotipo_id = dat.id_fenotipo SET f.criterio_diagnostico = dat.diagnostico_criterio;

SELECT * FROM fenotipo; 	#Así quedaría la tabla fenotipo

#A continuación vamos a crear la tabla enfermedad_fenotipo, que relacionará id_enfermedad de la tabla enfermedad con id_fenotipo de la tabla fenotipo.
#Se hará como hemos hecho antes, mediante foreign keys.
CREATE TABLE enfermedad_fenotipo AS SELECT e.id_enfermedad, f.id_fenotipo FROM enfermedad e join datos_fenotipo d on e.nombre = d.enfermedad_nombre join fenotipo f on d.id_fenotipo = f.fenotipo_id group by f.fenotipo_id order by e.id_enfermedad;

ALTER TABLE enfermedad_fenotipo ADD FOREIGN KEY fk_enfermedad (id_enfermedad) REFERENCES enfermedad (id_enfermedad);
ALTER TABLE enfermedad_fenotipo ADD FOREIGN KEY fk_fenotipo (id_fenotipo) REFERENCES fenotipo (id_fenotipo);

SELECT * FROM enfermedad_fenotipo; 		#De esta manera quedaría la tabla enfermedad_fenotipo

#Finalmente, vamos a eliminar las tablas de donde hemos obtenido los datos.

DROP TABLE datos_enfermedad, datos_gen, datos_fenotipo;