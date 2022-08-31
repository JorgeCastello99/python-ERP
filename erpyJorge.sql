#He modificado ciertas cosas de mi tabla como el AI una referencia y un campo a Varchar
DROP DATABASE IF EXISTS erpy;
CREATE DATABASE erpy;
USE erpy;

DROP TABLE IF EXISTS clientes;
CREATE TABLE clientes (
DNI VARCHAR(9) NOT NULL,
nombre VARCHAR(30) NOT NULL,
apellidos VARCHAR(45) NULL,
genero VARCHAR(1) NULL,
direccion VARCHAR(45) NULL,
FNacimiento DATE NULL,
Codigo_Postal INT NULL,
PRIMARY KEY (DNI)
);

DROP TABLE IF EXISTS proveedor;
CREATE TABLE proveedor (
CIF VARCHAR(9) NOT NULL,
nomempresa VARCHAR(25) NOT NULL,
direccion VARCHAR(35) NOT NULL,
diudad VARCHAR(20) NULL,
telefono INT NOT NULL,
logo LONGBLOB NULL,
PRIMARY KEY (CIF)
);

DROP TABLE IF EXISTS producto;
CREATE TABLE producto (
ISBN float(13) NOT NULL,
titulo VARCHAR(45) NULL,
autor VARCHAR(45) NULL,
editorial VARCHAR(45) NULL,
genero VARCHAR(45) NULL,
precio_venta DECIMAL NULL,
año_edicion INT(4) NULL,
stock VARCHAR(9) NULL,
puede_reservarse TINYINT NULL,
precio_coste DECIMAL NULL,
foto BLOB NULL,
CIF VARCHAR(9) NULL,
PRIMARY KEY (ISBN),
FOREIGN KEY (CIF) REFERENCES proveedor(CIF)
);

DROP TABLE IF EXISTS factura;
CREATE TABLE factura (
idFactura int(11) NOT NULL AUTO_INCREMENT,
fecha date NOT NULL,
cantidad int(11) DEFAULT NULL,
es_compra tinyint(4) NOT NULL,
producto float DEFAULT NULL,
precio decimal(10,2) DEFAULT NULL,
cliente varchar(9) DEFAULT NULL,
proveedor varchar(9) DEFAULT NULL,
observaciones varchar(100) DEFAULT NULL,
PRIMARY KEY (idFactura),
FOREIGN KEY (producto) REFERENCES producto (ISBN),
FOREIGN KEY (cliente) REFERENCES clientes (DNI),
FOREIGN KEY (proveedor) REFERENCES proveedor (CIF)
);

DROP TABLE IF EXISTS movimientos;
CREATE TABLE movimientos (
id INT NOT NULL AUTO_INCREMENT,
factura_compra_venta VARCHAR(20) NULL,
producto float(13) NULL DEFAULT NULL,
cantidad INT NULL DEFAULT NULL,
precio DECIMAL(9) NULL DEFAULT NULL,
cliente VARCHAR(9) DEFAULT NULL,
proveedor VARCHAR(9) DEFAULT NULL,
observaciones VARCHAR(45) NULL DEFAULT NULL,
PRIMARY KEY (id),
FOREIGN KEY (producto) REFERENCES producto(ISBN),
FOREIGN KEY (cliente) REFERENCES clientes(DNI),
FOREIGN KEY (proveedor) REFERENCES proveedor (CIF)
);

DELIMITER //
CREATE TRIGGER insert_fact after insert on factura
FOR EACH ROW
BEGIN
if new.es_compra=1 then
insert into movimientos(factura_compra_venta,producto,cantidad,precio,cliente,proveedor,observaciones) values('Compra',NEW.producto,NEW.cantidad,NEW.precio,null,new.proveedor,new.observaciones);
end if;

if new.es_compra=0 then
insert into movimientos(factura_compra_venta,producto,cantidad,precio,cliente,proveedor,observaciones) values('Venta',NEW.producto,NEW.cantidad,NEW.precio,new.cliente,null,new.observaciones);
end if;

END //

INSERT INTO clientes Values	('15406478T', 'Jofian', 'Rufian', 'V', 'inframundo, 666', '1966-06-06','00666');
INSERT INTO clientes Values	('14785545L', 'Alejandro', 'Vagno', 'V', 'toletum, 45', '1994-08-26','45887');
INSERT INTO clientes Values	('08544554S', 'Paco', 'León', 'V', 'Arsenal, 50', '1980-06-16','48785');
INSERT INTO clientes Values	('14055500N', 'Eva', 'Castrano', 'H', 'Paraiso, 6', '1980-12-06','47588');
INSERT INTO clientes Values	('03004584T', 'Maria', 'Patiño', 'H', 'Pala, 47', '1996-04-04','25666');
INSERT INTO clientes Values	('34594565N', 'Jaime', 'Citroen', 'V', 'España, 155', '1977-02-19','78766');

INSERT INTO proveedor Values ('U0400698G', 'El mundo', 'Av America, 25', 'Madrid', 914435000, NULL);
INSERT INTO proveedor Values ('F6418740D', 'Planeta', 'C/ Cruces, 12', 'Barcelona', 985451685, NULL);
INSERT INTO proveedor Values ('N5696018J', 'Grupo Santillana', 'C/ falsa, 3', 'Toledo', 956825865, NULL);
INSERT INTO proveedor Values ('A34220020', 'HarperCollins', 'C/ Valencia, 65', 'Sevilla', 987458525, NULL);
INSERT INTO proveedor Values ('Q9862363J', 'Norma Editorial', 'C/ Vacia, 10', 'Malaga', 968525486, NULL);
INSERT INTO proveedor Values ('F0836777C', 'Alfaguara', 'C/ Amargura, 3', 'Toledo', 987514664, NULL);
INSERT INTO proveedor Values ('B88093109', 'Minotauro', 'Av. La Comarca, 7', 'Barcelona', 987634567, NULL);
INSERT INTO proveedor Values ('P1100499A', 'Grupo Anaya', 'C/ Llena, 89', 'Madrid', 987536565, NULL);
INSERT INTO proveedor Values ('W2982597C', 'Ediciones Destino', 'Av. Barbara, 99', 'Valencia', 987464136, NULL);
INSERT INTO proveedor Values ('F1068207H', 'Minon S. A.', 'Av. Traidor, 101', 'Consuegra', 984361465, NULL);

INSERT INTO producto Values ('1234567890123', 'El señor de los anillos', 'J.R. Tolkien', 'Acuario', 'Fantasía', 22.0, 1970, 5, 1, 15.0, null, 'F6418740D');

INSERT INTO factura Values (1,'2019-10-07',1,1,1234567890123,13.50,'15406478T','U0400698G','a');
INSERT INTO factura Values (2,'2019-10-07',3,1,1234567890123,189.50,'14785545L','U0400698G','El producto se distruye dos días después');
INSERT INTO factura Values (3,'2019-09-07',1,1,1234567890123,1.50,'14055500N','U0400698G','');


commit;

