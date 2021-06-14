import socket                                   #Импорт библиотеки Socket
from datetime import datetime, date, time
from configparser import ConfigParser

class LogServer(object):                        #Класс для работы с серверов по принятию логов
    
    def __init__(self,StringAdress='46.147.30.224', IntPort=4055):  #Конструктор от Адресса и Порта
        file='config.ini'
        config=ConfigParser()
        try:
            config.read(file)
        except:
            f=open(file,"x")
            f.write("[server]\n")
            f.write("adress=\n")
            f.write("port=")        
            f.close()
        try:    
            config.sections()
            self.StringAdress = config['server']['adress']
            self.IntPort=Int(config['server']['ip'])
        except:
            print('adress or port are empty in config.ini')
                                    #Инициализация

    def connect(self):    #Функция подключнения к серверу по адрессу и порту
        try:
            sock = socket.socket()                      #Инициализация сокета
            sock.settimeout(3)                         #Задаётся время ожидания
            sock.connect((self.StringAdress, self.IntPort))#Попытка коннекта
            print ("Good connection between client and server") #Сообщение об отсутствии ошибок
            sock.close()                            #Закрытие соединения
        except socket.timeout :                     #Если произошли какие-то ошибки - вывод сообщения
            print ("No connection between client and server") #Сообщение об ошибке
            sock.close()                            #Принудительное закрытие соединения

        
    
    def send(self,StringNameDef,StringTypeDef,StringMassageDef):                             #Функция для отправки сообщения серверу
        d=datetime.now()
        d=d.strftime("%y-%m-%d/%H:%M:%S")
        try:                                                
            sock = socket.socket()                              #Инициализация сокета
            sock.connect((self.StringAdress, self.IntPort))           #Попытка коннекта
            sock.send((StringNameDef+' '+StringTypeDef+' '+d+' '+StringMassageDef).encode())            #Попытка отправки сообщения с кодированием
            sock.close()                                    #Закрытие сокета
        except socket.timeout :                              #Если произошли какие-то ошибки - вывод сообщения
            print ("No connection between client and server")#Сообщение об ошибке
            sock.close()                                    #Принудительное закрытие соединения

 


