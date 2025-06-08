CREATE DATABASE IF NOT EXISTS sky_route;
USE sky_route;

-- Tabla cliente: almacena los datos de los clientes.
CREATE TABLE `cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `razon_social` varchar(100) NOT NULL,
  `cuit` varchar(20) NOT NULL,
  `correo_contacto` varchar(100) NOT NULL,
  `tipo_cliente` enum('Persona','Agencia') NOT NULL DEFAULT 'Persona',
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `cuit` (`cuit`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla destino: almacena los destinos disponibles.
CREATE TABLE `destino` (
  `id_destino` int NOT NULL AUTO_INCREMENT,
  `ciudad` varchar(100) NOT NULL,
  `pais` varchar(100) NOT NULL,
  `costo_base` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_destino`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla venta: registra las ventas realizadas.
CREATE TABLE `venta` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_destino` int NOT NULL,
  `fecha_venta` date NOT NULL,
  `costo_total` decimal(10,2) NOT NULL,
  `estado` enum('Activa','Anulada') NOT NULL DEFAULT 'Activa',
  PRIMARY KEY (`id_venta`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_destino` (`id_destino`),
  CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`id_destino`) REFERENCES `destino` (`id_destino`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla arrepentimiento: registra anulaciones de ventas.
CREATE TABLE `arrepentimiento` (
  `id_arrepentimiento` int NOT NULL AUTO_INCREMENT,
  `id_venta` int NOT NULL,
  `fecha_anulacion` date NOT NULL,
  `motivo` text,
  PRIMARY KEY (`id_arrepentimiento`),
  UNIQUE KEY `id_venta` (`id_venta`),
  CONSTRAINT `arrepentimiento_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

