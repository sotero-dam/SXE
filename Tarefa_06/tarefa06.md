# Tarefa Docker Compose 
**Desenvolvido por**: Sofía Otero  
**Asignatura**: SXE

## Nivel 1 (obligatorio):
Crear un fichero docker-compose.yml que defina los siguientes servicios:
prestashop, db (MySQL o MariaDB) y phpMyAdmin.

● El fichero debe configurar las dependencias (depends_on) entre servicios y
las variables de entorno necesarias para la conexión.

● En este nivel, las contraseñas y otros datos de configuración pueden estar
escritos directamente en el fichero docker-compose.yml.

● El despliegue debe levantarse con un solo comando: docker-compose up.

● El README.md debe explicar la estructura del fichero y cómo utilizarlo.

● Incluir capturas de pantalla de los servicios funcionando. La captura de
pantalla de phpmyAdmin no vale que se vea que el servicio phpmyadmin
está corriendo, tienen que verse las tablas de la bbdd de prestashop.

![alt text](<image copy.png>)
![alt text](<image-2 copy.png>)
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)
## Nivel 2 (opcional):
● Configuración Segura: Modificar el docker-compose.yml para que no
contenga ninguna contraseña o dato sensible. Toda esta información debe
cargarse desde un fichero .env externo.

<img width="483" height="341" alt="image" src="https://github.com/user-attachments/assets/20c177fb-e025-439f-ae33-a6482f6e6e79" />

● Persistencia de Datos: Utilizar volúmenes de Docker (volumes) para que
los datos de la base de datos (/var/lib/mysql) y los ficheros de
PrestaShop (/var/www/html) persistan aunque los contenedores se eliminen
y se vuelvan a crear.

<img width="240" height="146" alt="image" src="https://github.com/user-attachments/assets/48020e6f-595a-4fd0-8275-592d2a633bb9" />

## Nivel 3 (opcional):

● Añadir una directiva healthcheck al servicio de la base de datos (db). Esta
comprobación debe verificar activamente que el servicio de base de datos
está operativo.

<img width="1053" height="179" alt="image" src="https://github.com/user-attachments/assets/5b99e5b4-c0e3-4701-bf3f-85ce68979b6c" />


● Modificar la directiva depends_on del servicio prestashop y phpMyAdmin
para que esperen a que el healthcheck sea correcto.

<img width="1011" height="99" alt="image" src="https://github.com/user-attachments/assets/63aa0489-da8e-4967-800b-ddef77862727" />

![alt text](image-1.png)
![alt text](image-2.png)

## Captura Resultado Final
![alt text](image.png)
