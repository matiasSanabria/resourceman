#! /bin/bash

#usamos crontab -l para listar las tareas pendientes y redireccionamos a un archivo
crontab -l >fic-tareas
#introducimos la tarea que queremos planificar en el archivo generado en el paso anterior
echo "14 18 * * * bash /home/$USER/is2/resolverSolicitudes.sh" >>fic-tareas
#instala las tareas del fichero en cron
crontab fic-tareas
