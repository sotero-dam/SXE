# Manual de Instalación: Odoo 18 e PgAdmin con Docker Compose

## Introdución

Este documento serve como un manual de instrucións detallado sobre como configurei e executei a aplicación Odoo 18
Community xunto coa ferramenta de xestión de bases de datos PgAdmin 4, utilizando Docker Compose para despregar todos os servizos.

## Preparación do meu IDE (Visual Studio Code)

O primeiro que fixen foi preparar o meu editor de código para traballar con Docker.

<img width="632" height="410" alt="image" src="https://github.com/user-attachments/assets/a40f0616-368f-41b7-93c1-80047c02b716" />


### Instalación de Extensións

Para ter unha boa xestión do meu contorno de desenvolvemento, instalei Visual Studio Code (VS Code) e o seguinte paquete de extensións:

  * Docker Essentials Extension Pack 2023 (TechieCouch):
      * Docker Compose: Permíteme xestionar os servizos de Docker Compose.
      * Docker Explorer: Úsoa para xestionar contedores e imaxes de Docker.
    <img width="1384" height="958" alt="image" src="https://github.com/user-attachments/assets/5e44b571-9f4e-4d7e-b0f6-c27b7f2c446b" />


### Captura de Funcionamento

<img width="1798" height="1056" alt="image" src="https://github.com/user-attachments/assets/91e11752-4ff8-4fca-90aa-3de8bb5e53ff" />


## Instalación de Odoo 18 e PgAdmin con Docker Compose

Utilicei docker-compose.yaml para definir e executar tres servizos interconectados: Odoo, a base de datos PostgreSQL , e PgAdmin.

### Meu Ficheiro docker-compose.yaml

Este é o contido do ficheiro que subín ao meu repositorio.

```
services:
  odoo:
    image: odoo:18 # Imaxe de Odoo v18
    container_name: odoo
    restart: unless-stopped
    ports:
      - "8069:8069" # Odoo accesible no porto 8069 do host
    depends_on:
      - db # Odoo depende de que a base de datos estea levantada
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
      - HOST_USER_ID=999
    volumes:
      - odoo_data:/var/lib/odoo

  db:
    image: postgres:16 # Imaxe de PostgreSQL v16
    container_name: odoo_db
    environment:
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_DB=postgres
    volumes:
      - db_data:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4:latest # Última imaxe de PgAdmin 4
    restart: unless-stopped
    depends_on:
      - db
    environment:
      - PGADMIN_DEFAULT_EMAIL=sofia@gmail.com
      - PGADMIN_DEFAULT_PASSWORD=sofia
    ports:
      - "8081:80" # PgAdmin accesible no porto 8081 do host

volumes:
  odoo_data:
  db_data:
```
#### A. Acceso e Configuración de PgAdmin

1.  Accedín a PgAdmin no porto 8081 e iniciei sesión coas credenciais por defecto: sofia@gmail.com e contrasinal sofia.
2.  Rexistrei o servidor de base de datos db (PostgreSQL) usando a configuración:

      * Host name/address: odoo_db.
      * Port: 5432.
      * Maintenance database: postgres.
      * Username: odoo.
      * 
<img width="1798" height="1056" alt="image" src="https://github.com/user-attachments/assets/76500c25-ba32-4fab-9376-1a8e9093a3bf" />

<img width="1646" height="986" alt="image" src="https://github.com/user-attachments/assets/df13372d-1a90-4a6f-a780-f68dcc93879b" />


####  Creación da Base de Datos de Odoo

1.  Accedín ao xestor de bases de datos de Odoo no porto 8069.
2.  Para a instalación, creei a miña base de datos co nome sofia.
3.  Establecín o meu email de administrador como admin@sofia.com.
4.  Asegureime de marcar a caixa para Cargar datos de demostracION.
5.  
<img width="1556" height="1054" alt="image" src="https://github.com/user-attachments/assets/b16dc131-d9ac-442c-8d5c-11b4ac3e58c6" />

<img width="848" height="952" alt="image" src="https://github.com/user-attachments/assets/cb52543d-0bfe-4a44-a658-6d33505d64a9" />


## Exploración de Odoo con Datos de Demo

Unha vez creada a base de datos con datos de demostración, iniciei sesión en Odoo co meu email sofia@gmail.com.


### Instalación de Módulos

Fun á sección de Aplicacións para instalar módulos básicos, o que engade máis datos de exemplo á miña base de datos.

  * Instalei módulos como Sales, CRM, e Website.
<img width="2232" height="776" alt="image" src="https://github.com/user-attachments/assets/5632a7f3-db0f-4eef-bdbb-62b9f7eed998" />


### Inspección da Base de Datos con PgAdmin

Finalmente, volvín a PgAdmin. Ao inspeccionar a base de datos a través da conexión ao servidor odoo_db, puiden ver todas as táboas e os datos de exemplo que Odoo creou tras a instalación dos módulos.

<img width="2238" height="684" alt="image" src="https://github.com/user-attachments/assets/a128e5fd-2066-4fae-a844-e893b831dd46" />

<img width="1213" height="702" alt="image" src="https://github.com/user-attachments/assets/ae2db075-cf6b-4787-b371-a6001ec057de" />



