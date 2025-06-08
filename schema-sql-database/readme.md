
# SkyRoute - Base de Datos

Este repositorio contiene la estructura de la base de datos **sky_route** utilizada en el sistema de gestión de pasajes.

## Contenido

- `database/sky_route_estructura.sql`: Script completo con la creación de la base de datos y sus tablas, con comentarios explicativos y orden correcto.

## Cómo levantar la base de datos en MySQL Workbench

1. Abrí **MySQL Workbench**.
2. Conectate a tu servidor local o remoto.
3. Abrí una nueva pestaña de query (query tab).
4. Cargá el archivo `sky_route_estructura.sql` (Archivo → Abrir SQL Script).
5. Ejecutá el script completo presionando el rayo (⚡) o con `Ctrl + Shift + Enter`.

> Esto creará la base de datos `sky_route` y todas sus tablas asociadas en el orden correcto.

##  Requisitos

- MySQL 8.0 o superior
- Usuario con permisos para crear bases de datos

## Estructura de tablas (orden de creación por dependencias)

1. `cliente`: Información de clientes.
2. `destino`: Ciudades y países disponibles.
3. `venta`: Registro de pasajes vendidos, con referencias a cliente y destino.
4. `arrepentimiento`: Cancelaciones o anulaciones de ventas, con referencia a venta.
