import zmq
import SDtwitter
import SDdropbox
import SDtratamiento
import json
import time

#@author Corbacho_Sanchez_ManuelJesus Arias_Gómez-Calcerrada_JoséJoaquín
#@version 1.0

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:1024")

msg=socket.recv_json()
print("Un cliente esta preparado")
algo=1
socket.send_json(algo)

while True:
	nombre_fichero=socket.recv_json()
	print("Nombre fichero recibido", nombre_fichero)
	SDdropbox.uploadfiletodropbox(nombre_fichero)
	time.sleep(5)
	SDdropbox.downloaddropboxfile(nombre_fichero)
	time.sleep(5)
	socket.send_json("Enviado y descargado de dropbox")