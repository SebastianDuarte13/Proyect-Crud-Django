CREATE DATABASE IF NOT EXIST crud_proyecto;

USE crud_proyecto;


CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    estado TINYINT(1) NOT NULL DEFAULT 1 -- Siempre inicia en 1 (activo)
);

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200),
    stock INT NOT NULL DEFAULT 0, -- Siempre inicia en 0
    estado TINYINT(1) NOT NULL DEFAULT 1 -- Siempre inicia en 1 (activo)
);

CREATE TABLE suministros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    id_proveedor INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0), -- No permite valores negativos o cero
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha de creación automática
    FOREIGN KEY (id_producto) REFERENCES productos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id) ON UPDATE CASCADE ON DELETE RESTRICT
);
