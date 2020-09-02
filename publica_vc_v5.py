# infotec_publica_vc.py
# Author: Álvaro Toriz
# Date created: Sep 1, 2020
# Date modified: Sep 1, 2020
# Converts vc_data file to vc_publishing html file, meaning we have a file with date, name, time, and URL of a videoconference and by text parsing we are going to get an HTML file to publish that data into a Moodle course.
import sys # import system communication library
print(sys.argv) # print all arguments
this_python_filename = sys.argv[0] # define variable for first argument wich is this code filename
print(this_python_filename) # print this code filename
vc_data_file = sys.argv[1] # define variable for second argument which is the input filename
print(vc_data_file) # print input filename
with open (vc_data_file, "r") as f1:
    data = f1.read().splitlines()
f1.close()
fecha = data[0].strip()
nombre = data[1].strip()
hora = data[2].strip()
url = data[3].strip()
f2 = open ('ensayo.html','w')
f2.write('<div style=\"background-color: lightgrey; padding: 20px;\">'
	+'<h3 style=\"text-align: center;\">'+nombre+'</h3>'
	+'<h4 style=\"text-align: center;\"><a href=\"'+url+'\" target=\"_blank\"><img src=\"http://aulavirtual.infotec.edu.mx/recursos/sitio/vc.png\" width=\"60\" height=\"50\" /></a> <a href=\"'+url+'\" target=\"_blank\">Videoconferencia '+fecha+' a las '+hora+'</a></h4>'
	+'<p>Requisitos para participar en la videoconferencia</p>'
	+'<ul>'
	+'<li> Computadora con cámara y micrófono</li>'
	+'<li>Aplicación BlueJeans</li>'
	+'<li>Audífonos (recomendable) o altavoces</li>'
	+'<li> Conexión estable a internet (de preferencia por cable ethernet)</li>'
	+'</ul>'
	+'<p style=\"text-align: center;\"></p>'
	+'<p>Las videoconferencias serán a través del sistema Blue Jeans. Revisa <strong><a href=\"http://aulavirtual.infotec.edu.mx/mod/page/view.php?id=17809\" target=\"_blank\">Cómo ingresar al sistema de videoconferencia Blue Jeans</a></strong> para que puedas conectarte sin contratiempos.</p>'
	+'</div>'
	+'<div style=\"background-color: lightblue; padding: 20px; text-align: center;\">'
	+'<h4><a href=\"'+url+'\" target=\"_blank\"> Enlace de videoconferencia '+nombre+', '+fecha+' a las '+hora+'</a></h4>'
	+'</div>'
+'')
f2.close()
