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
f1 = open (vc_data_file,'r') # open input filename for reading
mensaje = f1.read() # define variable for what I think is the 1st line of the input file
print(mensaje)
f1.close()
f2 = open ('result.html','w')
f2.write(mensaje)
f2.close()
f2 = open ('result.html','r')
contenido = f2.read()
print(contenido)
f2.close()