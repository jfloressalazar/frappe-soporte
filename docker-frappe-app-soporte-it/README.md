# Separar por fases

## Fase de desarrollo

# Guía de Implementación de la Aplicación Soporte IT en Contenedores Docker

## Índice
1. [Requisitos](#requisitos)
2. [Creación e inicio de contenedores](#creacion-de-contenedores)
3. [Acceso al Contenedor](#acceso-al-contenedor)
4. [Configuración de la aplicación](#configuración-de-la-aplicación)
   1. [Creación de sitio y aplicación de Frappe](#creación-de-sitio-y-aplicación-de-frappe)
   3. [Configuración del Sitio](#configuración-del-sitio)
   4. [Clonación de repositorio](#clonación-de-repositorio)
   5. [Configuración final, importe de roles y ejecución de seeders](#configuración-final-y-ejecución-de-seeders)
5. [Inicio de la aplicación](#inicio-de-la-aplicación)
9. [Resolución de Problemas Comunes](#resolución-de-problemas-comunes)

---


## Creacion de contenedores

#### 1. Construccion de contenedores

Con la aplicación Docker Desktop iniciada y usando la terminal de windows, navegue hasta la carpeta donde se encuentra el archivo *`docker-compose.yml`* y ejecute el comando:

    docker-compose -f ./docker-compose.yml build


#### 2. Inicio de contenedores

Si todo ha marchado bien, luego de esa construcción, ejecute el comando para iniciar los contenedores:

    docker-compose -f ./docker-compose.yml up -d

---

## Acceso al Contenedor

Deberá acceder al contendor en ejecución haciendo uso de la extensión **Dev Containers** de VSC.

##### 1. Inicie VSC y presione *`Ctrl+Shift+P`*
##### 2. Escriba *`Dev Containers`* y seleccione la opción *`Adjuntar al contenedor que está en ejecución`*
##### 3. Si los conenedores están iniciados aparecerán en la lista, deberá seleccionar el conentedor llamado *`soporte-app-backend-1`*

---

## Configuración de la aplicación

En este apartado que se divide en secciones encontrará todos los comandos para poner en marcha la aplicación.
Se parte del entendido que hasta este punto usted ya está conectado a su contenedor haciendo uso de VSC.
Abra una terminal de VSC presionando `Ctrl+Ñ`

#### Creación de sitio y aplicación de Frappe

En este apartado se crea el entorno de Frappe, tanto el sitio ``(site)`` como la aplicacion ``(app)`` para ello se debe ejecutar los siguientes comandos:

Antes debemos asegurarnos de que no estamos en la carpeta frappe-bench, de ser así nos salimos con
   
   cd ~

  1. Iniciar el entorno virutal de python que permite la ejecición de comandos `bench`

    source frappe/bin/activate && cd frappe-bench

  2. Moverse a carpeta de Frappe

    cd frappe-bench

  3. Crear nuevo sitio (site) de Frappe `frontend`, solicitará la contraseña de base de datos, **tambien solicitará que se establesca una contraseña para el usuario 'Administrator' para el sistema de Frappe** 

    bench new-site frontend --db-host soporte-app-db-1 --db-root-username root 

  4. Crear una nueva aplicación (app) de Frappe `soporte`, en este caso se solicitará cierta información, como el nombre de la aplicación, descripción, autor, correo, licencia, rama de repositorio. Lo importante es que en el titulo de aplicacion coloque `Soporte`  por defecto

    bench new-app soporte

#### Configuración del Sitio

  1. Incorporar la app al site

    bench --site frontend install-app soporte

  2. Iniciar el modo desarrollador para el sitio

    bench --site frontend set-config developer_mode 1

  3. Iniciar el scheduler del sitio

    bench --site frontend enable-scheduler

  4. Establecer el sitio `frontend` como sitio por defecto

    bench use frontend

  5. Volver a establecer el modo desarrollador para el sitio

    bench --site frontend set-config developer_mode 1

  6. Haciendo uso del explorador de archivos de VS localice el archivo `common_sites_config.json` que se encuentra en el directorio `frappe-bench/sites/` y remmplace las lineas siguientes:

    "redis_cache": "redis://soporte-app-queue-short-1:6379",
    "redis_queue": "redis://soporte-app-queue-long-1:6379",
    "redis_socketio": "redis://soporte-app-socketio:3000",
    "socketio_port": 3000,

### << -- Aqui debemos escribir la dirección en el navegador -->>

   1. Iniciar el servidor de desarrollo de frappe, este comado quedará en ejecución en esta consola

      bench start

   1. Introducimos la dirección en el navegador:
      http://localhost:8977

   2. Seguimos la configuración del sistema, estableciendo:
      a. Idioma: Español (Guatemala)
      b. País: El Salvador
      c. Moneda: USD
    
#### Clonación de repositorio

##### >> Importante: Recuerde especificar la `[rama]` desde  la cual se realizará la copia del repositorio.

  1. Cambiar al directorio donde se realizará la copia del repositorio

    cd apps/soporte

  2. Borrar el contenido de la carpeta

    rm -rf .[^.]* *

  3. Clonar la aplicación desde el repositorio especificando la `[rama]`

    git clone --branch [rama] https://ddit-gobernacionsv:[token]@github.com/ddit-gobernacionsv/Frappe-soporte-app.git .

  4. Volver al directorio de frappe

    cd ../..
    
  5. Volver a establecer el modo desarrollador para el sitio
    
    bench --site frontend set-config developer_mode 1


#### Configuración final y ejecución de seeders

  1. Iniciar el servidor de desarrollo de frappe, este comado quedará en ejecución en esta consola

    bench start

  2. Para continuar con la ejecución de comandos en otra consola, abrir una nueva terminal en VSC `Ctrl+Shift+Ñ`

  3. En la nueva terminal, ejecutar el siguiente comando para activar el entorno virtual de python

    source frappe/bin/activate

  4. En la nueva terminal, ejecutar el siguiente comando para moverse al directorio de frappe

    cd frappe-bench

  5. En la nueva terminal, ejecutar el siguiente comando para sincronizar la aplicación con los archivos clonados desde el repositorio de GitHub

    bench --site frontend migrate
  
  6. Importe de ROLES, en la nueva terminal, ejecutar el siguiente comando para activar la consola de frappe y empezar la importanción:

    bench console

  7. Al activar la consola deberá ejecutar los comandos ordenados uno por linea:

    from soporte.scriptpararoles.rolesrrhh import import_roles_and_permissions
    import_roles_and_permissions()
    from soporte.scriptpararoles.rolesauditoria import import_roles_and_permissions
    import_roles_and_permissions()
    from soporte.scriptpararoles.rolestransporte import import_roles_and_permissions
    import_roles_and_permissions()
    exit;
    
  
  8. Ejecución de SEEDERS, en la nueva terminal, ejecutar el siguiente comando para ejecutar los seeders de la aplicación, uno por linea



## Inicio de la aplicación

- Ingrese al navegador y escriba la siguiente URL: http://localhost:8977

- Inicie sesion con las credenciales 'Administrator' y la contraseña que usted espeficicó.

- En la pantalla principal, seleccione el idioma principal `Español(Guatemala)` 

- La configuración ha finalizado

## Resolución de Problemas Comunes


## Fase de producción
