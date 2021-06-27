import socket                                   #Импорт библиотеки Socket
from datetime import datetime, date, time       #Импорт библиотеки datetime
from configparser import ConfigParser           #Импорт библиотеки

class LogServer(object):                        #Класс для работы с серверов по принятию логов
    
    def __init__(self):                         #Конструктор от Адресса и Порта
        file='config.ini'                       #Присваивание значение переменной       
        config=ConfigParser()
        try:
            config.read(file)                   #Попытка прочитать файл конфигурации
        except:
            f=open(file,"x")                    #Если файл конфигурации отсутствует - создаём
            f.write("[server]\n")               
            f.write("adress=\n")                #Строка с адрессом серверной части
            f.write("port=")                    #Строка с портом сервера
            f.close()                           #Закрываем файл
        try:    
            config.sections()                   #Начало работы со строками конфига
            self.StringAdress = config['server']['adress']#Присвоение адресса сервера
            self.IntPort=int(config['server']['port'])#Присвоение порта
        except:
            print('adress or port are empty in config.ini')#Если конфиг файл пуст - сообщение об ошибке
                                      

    def connect(self):                          #Функция подключнения к серверу по адрессу и порту
        try:
            sock = socket.socket()              #Инициализация сокета
            sock.settimeout(3)                  #Задаётся время ожидания
            sock.connect((self.StringAdress, self.IntPort))#Попытка коннекта
            print ("Good connection between client and server") #Сообщение об отсутствии ошибок
            sock.close()                        #Закрытие соединения
        except socket.timeout :                 #Если произошли какие-то ошибки - вывод сообщения
            print ("No connection between client and server") #Сообщение об ошибке
            sock.close()                        #Принудительное закрытие соединения
            
            
     def config(self):                          #Функция подключнения к серверу по адрессу и порту
        f=open(file,"x")                    #Если файл конфигурации отсутствует - создаём
        f.write("[server]\n")               
        f.write("adress=\n")                #Строка с адрессом серверной части
        f.write("port=")                    #Строка с портом сервера
        f.close()                           #Закрываем файл

        
    
    def send(self,StringNameDef,StringTypeDef,StringMassageDef):#Функция для отправки сообщения серверу
        d=datetime.now()                        #Получение текущего время отправки
        d=d.strftime("%y-%m-%d/%H:%M:%S")       #Приведение к нужному типу
        try:                                                
            sock = socket.socket()              #Инициализация сокета
            sock.connect((self.StringAdress, self.IntPort))#Попытка коннекта
            sock.send((StringNameDef+'-'+StringTypeDef+'-'+d+'-'+StringMassageDef).encode())#Попытка отправки сообщения с кодированием
            sock.close()                        #Закрытие сокета
        except socket.timeout :                 #Если произошли какие-то ошибки - вывод сообщения
            print ("No connection between client and server")#Сообщение об ошибке
            sock.close()                        #Принудительное закрытие соединения

 


