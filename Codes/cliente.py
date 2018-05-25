import zmq
import SDtwitter
import SDdropbox
import SDtratamiento
import json
import time

#@author Corbacho_Sanchez_ManuelJesus Arias_Gómez-Calcerrada_JoséJoaquín
#@version 1.0

nombre_cuenta='Gato_directo'

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:1024")
socket.send_json("Preparado")

algo=socket.recv_json()
print("Recopilando tweets.. esto puede tardar un minuto")
SDtwitter.pointsfromtwitteraccount(nombre_cuenta)
time.sleep(30)
socket.send_json('data_'+nombre_cuenta+'.txt')
print("Enviado a Servidor")
mensaje=socket.recv_json()
print(mensaje)

SDtratamiento.plotpoints([nombre_cuenta])