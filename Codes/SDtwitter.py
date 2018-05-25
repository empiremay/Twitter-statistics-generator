import tweepy
from datetime import date, time, datetime
import os.path
import os
from datetime import date, time, datetime
#@author Corbacho_Sanchez_ManuelJesus Arias_Gómez-Calcerrada_JoséJoaquín
#@version 1.1
#http://tweepy.readthedocs.io/en/v3.5.0/auth_tutorial.html
#http://tweepy.readthedocs.io/en/v3.5.0/code_snippet.html

###############################################################################
###############################################################################
###############################################################################
def login():
    consumer_key="..."
    consumer_secret="..."
    access_token="..."
    access_token_secret="..."
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    API = tweepy.API(auth)
    return API
###############################################################################
###############################################################################
###############################################################################
def pointsfromtwitteraccount(account_id):#,left):
    counter=5000
    api=login()
    last_tuit_date=api.user_timeline(account_id)[0].created_at
    file=""
    newaccount=False
    #open/generate file and read date in format: dd/mm/yyyy/hh/mm/ss
    if os.path.exists('data_'+str(account_id)+'.txt'):
        file=open('data_'+str(account_id)+'.txt','a+') #open file
        file.seek(0) #pointer at the beggining of the file to read
        datestring=file.readline()
        oldest_desired_date=datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S%f\n') #https://stackoverflow.com/questions/5045210/how-to-remove-unconverted-data-from-a-python-datetime-object#5045386
        newaccount=False
    else:
        file=open('data_'+str(account_id)+'.txt','a+')
        oldest_desired_date=datetime.min
        file.write( str(last_tuit_date)+"\n" )
        file.write("PP: 0\n")
        file.write("PSOE: 0\n")
        file.write("PODEMOS: 0\n")
        file.write("C's: 0\n")
        file.write("IU: 0\n")
        file.seek(0)
        file.readline()
        newaccount=True
    points=[0,0,0,0,0]#new vector with ammount of cites : [PP PSOE PODEMOS C'S IU UP]
    for status in tweepy.Cursor(api.user_timeline, id = account_id, tweet_mode="extended").items(counter):
        #work in progress change print to print status and update date in the file
        tuit=status.full_text        #print(status.full_text+" "+status.created_at)
        if -1<(tuit.find("PP ")) or -1<(tuit.find("Partido Popular ")) or -1<(tuit.find("Mariano ")) or -1<(tuit.find("Rajoy ")) or -1<(tuit.find("Cifuentes ")):
            points[0]=points[0]+1
        if -1<(tuit.find("PSOE ")) or -1<(tuit.find("Partido Socialista ")) or -1<(tuit.find("Partido Socialista Obrero Español ")) or -1<(tuit.find("Pedro Sánchez ")) or -1<(tuit.find("Margarita Robles ")) or -1<(tuit.find("Susana Díaz ")) or -1<(tuit.find("Patxi Lopez ")):
            points[1]=points[1]+1
        if -1<(tuit.find("PODEMOS")) or -1<(tuit.find("Podemos ")) or -1<(tuit.find("Pablo Iglesias ")) or -1<(tuit.find("Irene Montero")) or -1<(tuit.find("Iñigo Errejón")) or -1<(tuit.find("Echenique")):
            points[2]=points[2]+1
        if -1<(tuit.find("CIUDADANOS"))  or -1<(tuit.find("C's")) or -1<(tuit.find("Albert Rivera")) or -1<(tuit.find("Rivera")) or -1<(tuit.find("Inés Arrimadas")) or -1<(tuit.find("Arrimadas")):
            points[3]=points[3]+1
        if -1<(tuit.find("IU")) or -1<(tuit.find("Izquierda Unida")) or -1<(tuit.find("Alberto Garzón")):
            points[4]=points[4]+1
        if  status.created_at<oldest_desired_date:
            break

    #if left==True:
    #    points[0]=-points[0]
    #else:
    #    for i in range(1,5):
    #        points[i]=-points[i]
    #A estas alturas points guarda las puntuaciones que se van a sumar/restar a cada partido
    file.close()
    aux_filename=file.name

    with open(aux_filename,'r') as file:
        with open(aux_filename+".tmp",'w') as file2:
            i=0
            linea=file.readline()
            while not linea == "":
            #for linea in file:
                if ": " in linea:
                    aux=linea.split(": ",1)
                    file2.write(linea.replace(aux[0]+": "+aux[1] , aux[0]+": "+str( points[i]+int(aux[1]) )+"\n" ) )
                    i=i+1
                else:
                    file2.write(str(last_tuit_date)+"\n")
                linea=file.readline()
            file2.close()
        file.close()
    if os.path.isfile(aux_filename):
        os.remove(aux_filename)
        os.rename(aux_filename+'.tmp',aux_filename)
    else:
        raise ValueError("file {} is not a file or dir.".format(aux))
    return points
###############################################################################
###############################################################################
###############################################################################
