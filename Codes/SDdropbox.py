import dropbox
import os
import os.path

#@author Corbacho_Sanchez_ManuelJesus Arias_Gómez-Calcerrada_JoséJoaquín
#@version 1.0
#https://www.dropbox.com/developers-v1/core/start/python
###############################################################################
###############################################################################
###############################################################################
def uploadfiletodropbox(filename):
    if os.path.exists(filename):
        access_token="..."
        cliente=dropbox.client.DropboxClient(access_token)
        archivo=open(filename,'rb')
        respuesta=cliente.put_file(filename,archivo)
        print(respuesta)
    else:
        print("No existe el archivo")
###############################################################################
###############################################################################
###############################################################################
def downloaddropboxfolder():
    access_token="..."
    cliente=dropbox.client.DropboxClient(access_token)
    metadatos_del_directorio = cliente.metadata('/')
    nombresdeficheros = [f['path'] for f in metadatos_del_directorio['contents'] if f['is_dir'] == False]
    for nombre in nombresdeficheros:
        nombre=nombre.replace('/','')
        if "data_" in nombre and ".txt" in nombre :
            fichero = cliente.get_file(str(nombre))
            fichero_de_salida = open(str(nombre), 'wb')
            fichero_de_salida.write(fichero.read())
            fichero_de_salida.close()
    return nombresdeficheros
###############################################################################
###############################################################################
###############################################################################
def downloaddropboxfile(fichero_a_bajar):
    access_token="..."
    cliente=dropbox.client.DropboxClient(access_token)
    metadatos_del_directorio = cliente.metadata('/')
    nombresdeficheros = [f['path'] for f in metadatos_del_directorio['contents'] if f['is_dir'] == False]
    for nombre in nombresdeficheros:
        if fichero_a_bajar in nombre :
            fichero = cliente.get_file(fichero_a_bajar)
            fichero_de_salida = open(fichero_a_bajar, 'wb')
            fichero_de_salida.write(fichero.read())
            fichero_de_salida.close()
            return "Archivo descargado con éxito"
    return "El fichero no existe"
