#!/bin/sh

# nombre de la base de datos
DATABASE='is2db'
# usuario de la base de datos
USUARIO='reservasis2'
# contrasenha de la base de datos
CONTRASENA='reservasis2'

# configuramos la base de datos
sudo -u postgres psql -c "CREATE DATABASE $DATABASE;"
sudo -u postgres psql -c "CREATE USER $USUARIO WITH PASSWORD '$CONTRASENA';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET client_encoding TO 'utf-8';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET timezone TO 'UTC';"
sudo -u postgres psql -c "ALTER USER $USUARIO CREATEDB;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DATABASE TO $USUARIO;"

# instalamos los paquetes necesarios
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib apache2 libapache2-mod-wsgi-py3

# instalamos el virtualenv
sudo pip3 install virtualenv

# nos mudamos al directorio personal del usuario
cd /home/$USER/

# clonamos el repositorio
git clone https://gitlab.com/matiasSanabria/is2.git

# ingresamos al directorio creado
cd /home/$USER/is2/

# creamos el virtualenv
virtualenv desarrollo

# activamos el entorno virtual
source desarrollo/bin/activate

pip3 install -r requirements.txt

pwd 
# ingresamos al directorio del proyecto
cd resourceman

# migramos la base de datos inicial
./manage.py migrate

# creamos un usuario administrador
./manage.py createsuperuser

# para el administrador del sistema tenemos:
# username: admin
# email: example@example.com
# password: Administrador
# password: Administrador

# recogemos el contenido estatico 
./manage.py collectstatic --no-input

# corremos el servidor
./manage.py runserver 0.0.0.0:8000

# desactivamos el virtualenv
deactivate