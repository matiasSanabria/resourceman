#! /bin/bash

echo
echo "---------------inicializando variables a utilizar en el script-------------------"
echo

#comando del interprete
python_command="python3"
#ruta del projecto
path_project=$(pwd)
#nombre del proyecto(la carpeta donde esta el proyecto)
name_project="resourceman"
#nombre de entorno
name_env="desarrollo"
#nombre de la configuracion de apache
name_config_apache="resourceman.conf"
#nombre del proceso demonio que correra el apache
name_daemon="resourceman"
#nombre de la base de datos
name_database="is2db"
#nombre del usuario de la base de datos
name_user_postgresql="postgres"
#contraseña del usuario de la base de datos
password_user_database="postgres"
#ruta de los entornos de virtualenvwrapper
path_WORKON_HOME=~/entornos


if [[ $python_command == "python" ]]
then
	pip_command="pip"
else
	pip_command="pip3"
fi

#bash dependencias $python_command
#$1=python_command
function dependencias() {
	#statements
	#$1=python_command
	echo
	echo "---------------instalando dependencias-------------------"
	echo
	$1=python_command
	# sudo apt-get install postgresql-9.5
	# sudo apt-get install postgresql-contrib-9.5
	sudo apt-get install rabbitmq-server
	sudo apt-get install "$1-pip" "$1-dev" libpq-dev
	sudo apt install aptitude apache2 apache2-dev

	if [[ $1 == "python3"  ]]
	then
		sudo apt install libapache2-mod-wsgi-py3
	else
		sudo apt install libapache2-mod-wsgi
	fi

}


#bash installVirtualenvwrapper $python_command $path_WORKON_HOME $pip_command
#$1=python_command
#$2=path_WORKON_HOME
#$3=mypip
function instalarVirtualenvwrapper() {
	#statements
	echo
	echo "---------------instalando virtualenvwrapper-------------------"
	echo
	#$1=python_command
	#$2=path_WORKON_HOME
	#$3=mypip

	$3 install --upgrade pip
	sudo $3 install virtualenvwrapper
	#echo "imprimiendo pip"
	#echo $3
	#echo "imprimiendo path_WORKON_HOME"
	#echo $2
	mkdir -p $2
	echo "
	export WORKON_HOME=$2
	export VIRTUALENVWRAPPER_PYTHON=`which $1`
	export VIRTUALENVWRAPPER_VIRTUALENV=`which virtualenv`
	source `which virtualenvwrapper.sh`
	export LC_ALL=
	" >> /etc/profile

	echo "
	export WORKON_HOME=$2
	export VIRTUALENVWRAPPER_PYTHON=`which $1`
	export VIRTUALENVWRAPPER_VIRTUALENV=`which virtualenv`
	source `which virtualenvwrapper.sh`
	export LC_ALL=
	" >> ~/.bashrc
}

#source `which virtualenvwrapper.sh`

#echo "imprimiendo WORKON_HOME"
#echo $WORKON_HOME

#bash CrearEntornoVirtual $path_project $name_env $python_command
#$1=path_project
#$2=name_env
#$3=python_command
function CrearEntornoVirtual() {
	#statements
	echo
	echo "---------------creando entorno virtual-------------------"
	echo
	#$1=path_project
	#$2=name_env
	#$3=python_command

	#source ~/.bashrc
	#source /etc/profile

	rmvirtualenv $2
	rm -R "$1/$2"
	mkvirtualenv -p `which $3` $2

}


#bash instalarRequerimientos $name_env $1 $path_project
#$1=name_env
#$2=$USER
#$3=path_project
function instalarRequerimientos() {
	#statements
	#$1=name_env
	#$2=$USER
	#$3=path_project
	echo
	echo "---------------instalando requerimientos en el entorno virtual-------------------"
	echo

	#source /etc/profile

	#workon $1
	pip install -r requirements.txt
	pip install --pre xhtml2pdf

	#echo "imprimiendo WORKON_HOME :   $WORKON_HOME"

	chown -R $2:$2 "$WORKON_HOME/$1"
	cp -R "$WORKON_HOME/$1" "$3/"
	chown -R $2:$2 "$3/$1"


}


#bash configApache $name_project $path_project $name_config_apache $name_daemon $name_env
#$1=name_project
#$2=path_project
#$3=name_config_apache
#$4=name_daemon
#$5=name_env
function configApache() {
	#statements
	#$1=name_project
	#$2=path_project
	#$3=name_config_apache
	#$4=name_daemon
	#$5=name_env

	echo
	echo "---------------configurando entorno de produccion-------------------"
	echo

	echo "
	<Directory $2/$1/$1 >
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory>

	WSGIScriptAlias / $2/$1/$1/wsgi.py
	WSGIDaemonProcess $4 python-home=$2/$5 python-path=$2/$1
	WSGIProcessGroup $4" > /etc/apache2/sites-available/$3
	a2enmod wsgi
	sitios=$(sudo ls /etc/apache2/sites-enabled/ )
	for site in $sitios
	do
		sudo a2dissite $site
	done
	a2ensite $3

}

#bash CrearBD $name_user_postgresql $password_user_database $name_database $path_project $name_project
#$1=name_user_postgresql
#$2=password_user_database
#$3=name_database
#$4=path_project
#$5=name_project
function CrearBD() {
	#statements
	#$1=name_user_postgresql
	#$2=password_user_database
	#$3=name_database
	#$4=path_project
	#$5=name_project
	echo
	echo "---------------eliminando y recreando la base de datos-------------------"
	echo

	#source /etc/profile
	#workon "desarrollo"
	mkdir -p "$4/fixtures"

	$4/$5/manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 7 > $4/fixtures/db.json

	sudo -u postgres psql -c "DROP DATABASE if exists $3;"
	sudo -u postgres psql -c "DROP USER if exists $1;"
	sudo -u postgres psql -c "CREATE DATABASE $3;"
	sudo -u postgres psql -c "CREATE USER $1 WITH PASSWORD '$2';"
	sudo -u postgres psql -c "GRANT ALL ON DATABASE $3  TO $1;"

}


#bash poblarBD $name_project $name_env $path_project
#$1=name_project
#$2=name_env
#$3=path_project
function poblarBD() {
	#statements
	#$1=name_project
	#$2=name_env
	#$3=path_project

	echo
	echo "---------------migrando y poblando la base de datos-------------------"
	echo
	#source /etc/profile

	#workon $2
	$3/$1/manage.py makemigrations
	$3/$1/manage.py migrate
	#echo 1
	# $3/$1/manage.py loaddata "$3/fixtures/db.json"
}

#bash reiniciarServidor
function reiniciarServidor() {
	#statements
	echo
	echo "---------------reiniciando el apache2-------------------"
	echo
		/etc/init.d/apache2 restart

}

dependencias $python_command

instalarVirtualenvwrapper $python_command $path_WORKON_HOME $pip_command
source /etc/profile

CrearEntornoVirtual $path_project $name_env $python_command
echo "nombre de entorno, usuario y ruta del proyecto"
echo $name_env $1 $path_project
instalarRequerimientos $name_env $1 $path_project

configApache $name_project $path_project $name_config_apache $name_daemon $name_env

CrearBD $name_user_postgresql $password_user_database $name_database $path_project $name_project

poblarBD $name_project $name_env $path_project

reiniciarServidor
