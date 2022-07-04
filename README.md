
# MoonLight-Lab
Laboratorio Local de Pentesting basado en la vulnerabilidad del Reto llamado Impossible de la plataforma HackTheBox, adaptandose a una maquina y su carnada (BD)

## Sistema de seguridad
Moonlight cuenta con un alto sistema de seguridad, sin embargo existe el script de base de datos el cual lo hace vulnerable para encontrar la flag o el acceso encriptado del sistema y poder tener control de la terminal. **¿Podrás entrar?**
![SISTEMA DE SEGURIDAD](https://i.imgur.com/AA4nhDH.png)**Organización:** Visualizando el esquema podemos deducir que se necesita engañar a la carnada SQL, luego lograr un acceso no temporal en el puerto configurado y obtener envío de comandos remotamente.

*Pista:No todo se trata de la base de datos, mira las puertas aquellas que no se abren y dile que no eres tu.*

### Configuración
Para configurar correctamente la máquina, se necesita ingresar a la base de datos llamada **moonlight.db** y una vez allí editar los datos de los usuarios para la prueba de SQL: 

![IMAGEN](https://i.imgur.com/5FOgL5E.png)
![IMAGEN](https://i.imgur.com/B8M09nl.png)Aparte del script SQL, se encuentra el archivo de configuración que lleva las variables que se manejaran por defecto y sus datos son posibles de cambiar.
En el script encontramos las variables:
>host = "127.0.0.1"

La variable **Host** contiene la IP por defecto del localhost , por lo general la configuración es *127.0.0.1*.
>port = 8070

La variable **port** contiene el puerto en el que trabajará máquina objetivo.
>DBFILE = moonlight.db

La variable **DBFILE** contiene el nombre exacto del archivo de la base de datos, por defecto se encuentra como *moonlight.db*.
### Ejecución
Su ejecución basta con tener alguna de las últimas versiones de python3 instalada en el sistema.
Ejemplos de ejecución:
*En Linux y/o Mac:*
> python3.7 machine.py

*En Windows:*
>py.exe machine.py

#### Screenshot de ejecución:
![IMAGEN1](https://i.imgur.com/V2xM2kf.png) 
**Nota:** Si deseas complejidad, quita el "#" en la linea **39** del archivo *machine.py* , esto hará que borre el archivo de la base de datos automaticamente una vez se ejecute la máquina, asegurandose así que no hay vuelta atras para las pruebas de penetración de la base de datos.
