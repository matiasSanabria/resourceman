#!/bin/sh

# nombre de la base de datos
DATABASE='is2db'

# usuario de la base de datos
USUARIO='reservasis2'

# contrasenha de la base de datos
CONTRASENA='reservasis2'

# clonamos el repositorio
git clone https://matiasSanabria@gitlab.com/matiasSanabria/is2.git

# instalando paquetes necesarios
# sudo apt-get update
# sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 libpq-dev postgresql postgresql-contrib 

# configurando un virtual environment
# sudo pip3 install virtualenv

# configuramos la base de datos
sudo -u postgres psql -c "CREATE DATABASE $DATABASE;"
sudo -u postgres psql -c "CREATE USER $USUARIO WITH PASSWORD '$CONTRASENA';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET client_encoding TO 'utf-8';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DATABASE TO $USUARIO;"

# ingresamos a la carpeta del proyecto
cd is2/is2

# creamos el virtualenv
virtualenv desarrollo

# activamos el virtualenv
source desarrollo/bin/activate

# instalamos Django
pip install django==1.10.5

# instalamos psycopg2 para poder utilizar la BD en postgres con Django
pip install psycopg2==2.7.1

# obtenemos todo el contenido estatico del proyecto
./manage.py collectstatic

# configuracion del firewall para permitir el trafico 
# a nuestro servidor
sudo ufw allow 8000

# abrimos una pestaña del navegador en la pagina inicial del proyecto
google-chrome http://localhost:8000/admin

# desactivamos el virtualenv
deactivate

# agregamos a nuestra BD local los modelos existentes en el
# proyecto de acuerdo a las aplicaciones que tenga
./manage.py makemigrations
./manage.py migrate

# corremos el servidor de desarrollo
./manage.py runserver 0.0.0.0:8000

