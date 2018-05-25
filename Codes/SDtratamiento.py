import matplotlib.pyplot as plt
import numpy as np
#@author Corbacho_Sanchez_ManuelJesus Arias_Gómez-Calcerrada_JoséJoaquín
#@version 1.0
#Precondición: accounts es un vector/lista de strings que representa las cuentas
def plotpoints(accounts):
    N=len(accounts)
    points_matrix=np.empty(([5,N]))
    points_matrix=np.empty(([5,N]))##get the matrix empty
    i=0
    for iterator in accounts:
        j=0
        points=getpointsfromfile(iterator)
        for p in points:
            points_matrix[j][i]=points[j]
            j=j+1
        i=i+1
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ind = np.arange(N)                # the x locations for the groups
    width = 0.15                      # the width of the bars
    rectsPP = ax.bar(ind, points_matrix[0], width,
                color='blue',
                error_kw=dict(elinewidth=5,ecolor='blue'))
    rectsPSOE = ax.bar(ind+width, points_matrix[1], width,
                    color='red',
                    error_kw=dict(elinewidth=5,ecolor='red'))
    rectsPODEMOS = ax.bar(ind+width*2, points_matrix[2], width,
                color='purple',
                error_kw=dict(elinewidth=5,ecolor='purple'))
    rectsCs = ax.bar(ind+width*3, points_matrix[3], width,
                    color='orange',
                    error_kw=dict(elinewidth=5,ecolor='orange'))
    rectsIU = ax.bar(ind+width*4, points_matrix[4], width,
                color='green',
                error_kw=dict(elinewidth=5,ecolor='green'))
    ax.set_xlim(-width,len(ind)+width*5)
    ax.set_ylabel('Número de citas')
    ax.set_title('Cuenta de Twitter')
    xTickMarks = accounts
    ax.set_xticks(ind+width*2)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)
    # add a legend
    ax.legend( (rectsPP[0], rectsPSOE[0],rectsPODEMOS[0],rectsCs[0],rectsIU[0]), ('PP', 'PSOE', 'PODEMOS', 'Cs', 'IU') )
    plt.show()

#Precondicion:Existe el fichero "data_"+str(account)+".txt" y está formateado
    #por la funcion pointsfromtwitteraccount(Cuenta,afiliacion)
def getpointsfromfile(account):
    points=[0,0,0,0,0]
    with open("data_"+str(account)+".txt",'r') as fichero:
        fichero.readline()#leemos la primera linea que es la decha
        linea=fichero.readline()#Leemos la primera puntuacion
        i=0
        while not linea == "":
            cadenas=linea.split(": ",1)
            points[i]=float(cadenas[1])
            i=i+1
            linea=fichero.readline()
    return points
