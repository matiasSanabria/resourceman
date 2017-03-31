#!/bin/sh

# clonamos el repositorio
git clone https://gitlab.com/matiasSanabria/is2

# nombre de la base de datos
DATABASE='is2db'

# usuario de la base de datos
USUARIO='reservasis2'

# contrasenha de la base de datos
CONTRASENA='reservasis2'

# instalando paquetes necesarios
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 libpq-dev postgresql postgresql-contrib 

# configurando un virtual environment
sudo pip3 install virtualenv

# configuramos la base de datos
sudo -u postgres psql -c "CREATE DATABASE $DATABASE;"
sudo -u postgres psql -c "CREATE USER $USUARIO WITH PASSWORD '$CONTRASENA';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET client_encoding TO 'utf-8';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET timezone TO 'UTC';"
sudo -u postgres psql -c "ALTER USER $USUARIO CREATEDB;"
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

# instalamos el gestor de documentacion
pip install Sphinx==1.5.3

# configuramos el sphinx
sphinx-quickstart

# ejecutamos el sphinx
sphinx-build -b html source/ build/

# obtenemos todo el contenido estatico del proyecto
./manage.py collectstatic

# configuracion del firewall para permitir el trafico 
# a nuestro servidor
sudo ufw allow 8000

# agregamos a nuestra BD local los modelos existentes en el
# proyecto de acuerdo a las aplicaciones que tenga
./manage.py makemigrations
./manage.py migrate

# guardamos los modelos de las tablas de la base de datos
./manage.py inspectdb > tests/models.py

# copiamos el archivo del test inicial 
cp ../tests.py test/

# ejecutamos el test
./manage.py test

# abrimos una pestaña del navegador en la pagina inicial del proyecto
google-chrome http://localhost:8000

# corremos el servidor de desarrollo
./manage.py runserver 0.0.0.0:8000

# desactivamos el virtualenv
deactivate
