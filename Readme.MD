Proyecto de stream de data y procesamiento, usando Kafka y Spark. Por Fabian Manrique.

Ejecutar el notebook de "Ingesta y procesamiento.ipynb en el ambiente de pyspark. 

Adicionalmente, es necesario instalar el [driver de mysql para java.](https://downloads.mysql.com/archives/c-j/).

En el archivo stackoverflow.py, se encuentra el script para la descarga de las preguntas de stackoverflow y pasarlas al topico de kafka.

En el notebook, se extraen las preguntas del consumer, se procesan para obtener el número de preguntas por tag, y finalmente se carga cada batch a una base de datos de MySQL.

En la carpeta MySQLdocker, se encuentra en el docker-compose.yml, para correr un servidor de mysql de forma local.