# Imagen base de Ubuntu
FROM ubuntu:latest

# Establecer variables de entorno necesarias para no interactuar durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualiza la lista de paquetes e instala cron y tzdata
RUN apt-get update && \
    apt-get install -y cron tzdata

# Configura la zona horaria
ENV TZ=America/El_Salvador

# Actualizar el sistema operativo e instalar las dependencias básicas
RUN apt-get update && apt-get install -y \
    nano \
    file \
    supervisor \
    git \
    python3-full \
    python3-dev \
    python3-pip \
    python3-venv \
    curl \
    redis-server \
    software-properties-common \
    postgresql-client \
    gnupg2 \
    build-essential \
    xvfb \
    libfontconfig \
    xfonts-75dpi \
    wget && \
    apt-get clean

# Instalar Node.js (versión LTS) y Yarn
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g yarn

# Instalar wkhtmltox para la exportación de PDFs en Frappe
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb && \
    apt-get install -y fontconfig && \
    dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb && \
    rm wkhtmltox_0.12.6.1-2.jammy_amd64.deb


RUN apt-get update && \
    echo "America/El_Salvador" > /etc/timezone && \
    ln -sf /usr/share/zoneinfo/America/El_Salvador /etc/localtime

RUN apt-get update && apt-get install -y locales \
    && locale-gen es_SV.UTF-8 \
    && update-locale LANG=es_SV.UTF-8 LANGUAGE=es_SV:es LC_ALL=es_SV.UTF-8

# Actualizar los repositorios e instalar sudo
RUN apt-get update && apt-get install -y sudo

# Crear usuario para la instalación, asignar contraseña, agregarlo a sudoers
RUN adduser --disabled-password --gecos "" frappe && \
    echo "frappe:desarrollo" | chpasswd && \
    usermod -aG sudo frappe

RUN sudo apt update && sudo apt install -y mysql-client

# Cambiar a usuario frappe
USER frappe
WORKDIR /home/frappe



# Crear y activar un entorno virtual
RUN python3 -m venv frappe && \
    . frappe/bin/activate && \
    pip install --upgrade pip && \
    pip install frappe-bench

# Instalar Frappe Bench y crear un nuevo proyecto
RUN . frappe/bin/activate && \
    bench init --frappe-branch v15.21.0 frappe-bench && \
    cd frappe-bench && \
    bench pip install python-barcode


# Exponer el puerto que usará Frappe
EXPOSE 8000 80 443

# Comando para iniciar el servidor Frappe
CMD ["bash"]
