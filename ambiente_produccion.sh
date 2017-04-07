#!/bin/sh

# nombre de la base de datos
DATABASE='is2dbprod'

# usuario de la base de datos
USUARIO='is2prod'

# contrasenha de la base de datos
CONTRASENA='is2prod'

# instalando paquetes necesarios
#sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 libpq-dev postgresql postgresql-contrib 

# nos movemos a la carpeta /var/www/html para descargar el proyecto
cd /var/www/html

# descargamos el proyecto
sudo git clone https://gitlab.com/matiasSanabria/is2

# modificamos los permisos de la carpeta del proyecto
sudo chmod 777 -R is2/

# borramos el archivo settings.py de desarrollo
sudo rm is2/is2/is2/settings.py

# modificamos el archivo settings para  el entorno de produccion

sudo cp is2/settings_prod.py is2/is2/is2/settings.py

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
virtualenv produccion

# activamos el virtualenv
source produccion/bin/activate

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

# agregamos a nuestra BD local los modelos existentes en el
# proyecto de acuerdo a las aplicaciones que tenga
./manage.py makemigrations
./manage.py migrate

# guardamos los modelos de las tablas de la base de datos
<<<<<<< HEAD
./manage.py inspectdb > test_inicial/models.py
=======
./manage.py inspectdb > tests/models.py
>>>>>>> matt

# copiamos el archivo del test inicial 
cp ../tests.py tests/

# ejecutamos el test
./manage.py test

# configuracion del firewall para permitir el trafico 
# a nuestro servidor
sudo ufw allow 8000

cd ..

# CONFIGURACION DEL APACHE
# configuramos el paso del wsgi
#sudo cp 000-default.conf /etc/apache2/sites-available/000-default.conf

# agregamos una excepcion para permitir al apache procesar el trafico
sudo ufw delete allow 8000
sudo ufw allow 'Apache Full'

# probamos si no existe algun error en los archivos del apache
sudo apache2ctl configtest

# reiniciamos el apache
sudo service apache2 restart

# abrimos una pestaña del navegador en la pagina inicial del proyecto
google-chrome http://localhost:80/

# desactivamos el virtualenv
deactivate