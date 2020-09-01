# infotec_publica_vc.py
import sys
print(sys.argv)
filename = sys.argv[0] 
print(filename)
vc_data = sys.argv[1] 
print(vc_data)
f = open ('holamundo.txt','w')
f.write('vc_data')
f.close()
f = open ('holamundo.txt','r')
mensaje = f.read()
print(mensaje)