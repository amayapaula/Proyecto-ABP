**SkyRoute S.R.L. - Sistema de Gestión de Pasajes**
Versión Prototipo - Evidencia de Aprendizaje 3 

**Propósito del sistema** 
Este sistema fue desarrollado para simular el funcionamiento de una aplicación de gestión de pasajes aéreos para la empresa SkyRoute S.R.L. 
Su objetivo es organizar y facilitar el registro de clientes, destinos disponibles y operaciones de venta de pasajes. Además, incorpora una funcionalidad de "Botón de Arrepentimiento"
que permite simular la anulación de una venta reciente.

**Instalación** 
- Tener instalado Python.
- Descargá o cloná la carpeta del proyecto que contiene el archivo `main.py`.
- Abrí una terminal en la carpeta del archivo.
- Ejecutá el comando: python main.py
- Seguí las instrucciones en pantalla para navegar por el menú del sistema.

**Integrantes del grupo**
- Amaya, Paula. DNI: 40.403.171
- Martinez, Cristian. DNI: 31.819.114
- Guillermo, Bianco DNI: 35.669.345
- Valeria, Cortez DNI: 29.768.588

**Programación**
Contiene los archivos que conforman el código del sistema SkyRoute para la gestión de pasajes:
- clientes.py
 Funciones para ver, agregar, modificar, eliminar y buscar clientes.
destinos.py
 Funciones para listar y registrar nuevos destinos disponibles.
- ventas.py
 Lógica para registrar ventas y realizar consultas.
- arrepentimiento.py
 Implementación del botón de arrepentimiento que permite anular ventas recientes.
- conexion.py
 Archivo de conexión a la base de datos MySQL.
-  main.py
Contiene el menú principal de navegación del sistema. Sus funcionalidades incluyen:  
 Gestionar Clientes: Ver, agregar, modificar, eliminar y buscar clientes (agencias o personas).  
 Gestionar Destinos: Ver destinos disponibles y agregar nuevos.  
 Registrar Ventas: Registrar una venta seleccionando cliente, destino, clase, tipo de vuelo y costo.  
 Consultar Ventas:  Filtrar ventas por cliente, destino, estado o período.  
 Botón de Arrepentimiento: Permite anular una venta activa registrada dentro de los últimos 60 días hábiles.  
 Salir:  Finaliza la ejecución del sistema.  

**Base de Datos**
Carpeta: schema-sql-database. Contiene los archivos necesarios para crear, poblar y consultar la base de datos utilizada por el sistema de gestión de pasajes de SkyRoute S.R.L.
- readme.md: 
 Explica cómo está organizada e implementada la base de datos. Incluye instrucciones detalladas para crearla en MySQL Workbench, los requisitos técnicos y la descripción funcional de cada tabla del sistema.

- sky_route_estructura.sql
 Script que define la estructura completa de la base de datos sky_route. Crea las tablas necesarias: cliente, destino, venta y arrepentimiento, incluyendo claves primarias y foráneas.

- consultas_sql.txt
 Contiene un conjunto de consultas SQL (SELECT) orientadas a recuperar información útil del sistema.
 Listado de todos los clientes.
 Ventas realizadas en una fecha específica.
 Última venta registrada por cada cliente.
 Destinos que comienzan con la letra “S”.
 Cantidad de ventas por país.

- datos_sql.txt
 Incluye sentencias INSERT INTO para poblar la base de datos con datos de ejemplo.
 10 agencias (clientes tipo "Agencia").
 12 personas particulares (clientes tipo "Persona").
 4 destinos nacionales (ciudad, país, costo base).
 5 ventas simuladas (cliente, destino, fecha, costo, estado).

**Ética y Deontología Profesional.**
- readme-etica.md:  
 Este documento busca contar un poco sobre los aspectos legales y éticos que tuvimos en cuenta al desarrollar nuestro sistema. Hablamos de leyes importantes como la Ley 24.240, que protege los derechos del consumidor (por eso incluimos el botón de arrepentimiento), la Ley 25.326, que trata sobre el uso responsable de los datos personales, y la Ley 11.723, que nos recuerda respetar la propiedad intelectual, tanto nuestra como la de otros.Creemos que tener en cuenta estas normas no solo nos ayuda a hacer un sistema más completo, sino también a cuidar a todas las personas que lo van a usar: los clientes, las agencias y hasta nosotros mismos como desarrolladores.
