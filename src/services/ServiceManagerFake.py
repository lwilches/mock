import imp
from select import select
#from socket import CAN_ISOTP
from modelo.Custumer  import CustumerInfo, TelefonoContacto, DireccionContacto
from services.CustumerFakesManager import  CustumerFakesManager
import csv
from Ports.connectDb import Session, Base, Engine
from Ports.ModelBd import Custumer , Direcciones , Telefonos
import threading
import queue
from  services.QueueBd import QueueBd 
from  services.formatoOutputProvider import FormatoOutput , FormatoOutputJson , FormatoOutputJsonDynamo 
from sqlalchemy import update
from sqlalchemy import bindparam

'''
Esta clase expone 3 metodos para crear los archivos
* crearArchivoCsvCustumers -> crea archivo de clites nuevos 
* crearArchivoCsvTelefonos -> crea archivo de clites nuevos 
* crearArchivoCsvTelefonos -> crea archivo de clites nuevos 
'''

class ServiceManagerFake:

    def __init__(self, create_metadata= False,  formatoJson : FormatoOutput = FormatoOutputJson()    ) -> None:
        #Crea la BD
        #if create_metadata:
        Base.metadata.create_all(Engine)
        self.session = Session()
        self.makerFakeCustumer  =CustumerFakesManager()
        self.formatoJson  =formatoJson 
    
        


    # funcion crea clientes nuevos desde 0 
    def crearArchivoCsvCustumers(self) :
        
        with open('csv_custumers.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            #se crea un millon de clientes 
            factor = 100000
            for _ in  range(10):
                for i in range(factor):
                    try:
                        custumerInfo = self.makerFakeCustumer.MakeCustumerFake()
                        custumerDb  =  Custumer(id_persona=  custumerInfo.id_persona  , cod_tipo_doc = custumerInfo.cod_tipo_doc ,  nro_doc = custumerInfo.nro_doc )
                        self.session.add(custumerDb)
                        print(f'indice:{i} data: {custumerInfo}'  )
                        writer.writerow( custumerInfo.getArray())
                    except Exception as e:
                        print(f' error en fila:{i} data: {custumerInfo} error: {str(e)}'  )
                self.session.commit()


     # funcion crea clientes a partir de bd 
    def crearArchivoCsvCustumersExists(self , nombre_file = 'csv_custumers.csv'  ,   maximo_registros =-1 ) :
    
        if  maximo_registros == -1 : 
            custumers  = self.session.query(Custumer).all()
        else: 
            custumers =     self.session.query(Custumer).limit(maximo_registros).all()

        with open(nombre_file, 'w', encoding='UTF8', newline='') as file:

            writer = csv.writer(file)


            razon  = 2000
            total =  len(custumers)
            iteraciones   = int(total/razon)
            minimo   = 0

            for i in range(iteraciones +1 ):
                custumers_group =custumers[0: 1:1]

                maximo =  razon * (i +1)
                if minimo  >=    len(custumers): 
                    custumers_group =custumers[len(custumers)::1]
                elif razon * i >=    len(custumers):
                    custumers_group =custumers[minimo::1]
                else :
                    custumers_group =custumers[minimo: maximo]

                minimo = maximo 

                #se crea un millon de clientes 
                for custumer in custumers_group:
                    try:
                        custumerInfo =  self.makerFakeCustumer.MakeCustumerFake(custumer.id_persona, custumer.nro_doc )
                        print(f'indice:{i} data: {custumerInfo}'  )
                        json  = self.formatoJson.format(custumerInfo)
                        writer.writerow( custumerInfo.getArray())
                    except Exception as e:
                        print(f' error en fila:{i} data: {custumerInfo} error: {str(e)}'  )

        self.__crearArchivosCsvTelefonosWithCustumers(custumers , 'csv_custumers_telefonos_cust.csv' , max_telefs =6 )
        self.__crearArchivosCsvDireccionesWithCustumers( custumers ,'csv_custumers_direcciones_cust.csv' , max_dirs =2 )


     # funcion crea clientes a partir de bd en formato json 
    def crearArchivoCsvCustumersExistsFormatJson(self , nombre_file = 'csv_custumers.csv'  ,   maximo_registros =-1 ) :
    
        if  maximo_registros == -1 : 
            custumers  = self.session.query(Custumer).all()
        else: 
            custumers =     self.session.query(Custumer).limit(maximo_registros).all()

        with open(nombre_file, 'w', encoding='UTF8', newline='') as file:
            
            writer = csv.writer(file)


            razon  = 2000
            total =  len(custumers)
            iteraciones   = int(total/razon)
            minimo   = 0

            for i in range(iteraciones +1 ):
                custumers_group =custumers[0: 1:1]

                maximo =  razon * (i +1)
                if minimo  >=    len(custumers): 
                    custumers_group =custumers[len(custumers)::1]
                elif razon * i >=    len(custumers):
                    custumers_group =custumers[minimo::1]
                else :
                    custumers_group =custumers[minimo: maximo]

                minimo = maximo 

                #se crea un millon de clientes 
                for custumer in custumers_group:
                    try:
                        custumerInfo =  self.makerFakeCustumer.MakeCustumerFake(custumer.id_persona, custumer.nro_doc )
                        telefono  = self.makerFakeCustumer.MakeCustumerTelefFake(custumer.id_persona) 
                        #direccion  = self.makerFakeCustumer.MakeCustumerDirFake(custumer.id_persona) 

                        custumerInfo.telefonosDto.append(telefono)  # telefono.getArray()
                        #custumerInfo.direccionDto = direccion #direccion.getArray()

                        json  = self.formatoJson.format(custumerInfo)
                        print(f'indice:{i} data: {custumerInfo}'  )
                        
                        writer.writerow( custumerInfo.getArray())
                    except Exception as e:
                        print(f' error en fila:{i} data: {custumerInfo} error: {str(e)}'  )

        self.__crearArchivosCsvTelefonosWithCustumers(custumers , 'csv_custumers_telefonos_cust.csv' , max_telefs =6 )
        self.__crearArchivosCsvDireccionesWithCustumers( custumers ,'csv_custumers_direcciones_cust.csv' , max_dirs =2 )


       # funcion crea clientes a partir de bd 
    def crearArchivoCsvDireccionesCustumersExists(self , nombre_file = 'csv_custumers_direcciones.csv'  ,   maximo_registros =-1 ) :
    
        
        finalizar = False
        cnt_commit =1  
        """
        with open('ClientesPocNews.txt', 'r', encoding='UTF8', newline='') as file:
            while True:
                line = file.readline()
               
                x = line.split(";")
                id_salesforce   = x[0].replace('"', '').strip()
                id_persona = x[0].strip()
                #custumer = self.session.query(Custumer).filter(Custumer.id_persona == id_persona).first()
                #if  custumer is not None :
                #    custumer.id_salesforce = id_salesforce

                stmt = (  update(Custumer)
                            .where(Custumer.id_persona == bindparam('b_id_persona') )
                            .values(id_salesforce= bindparam('b_id_salesforce') )
                )
                print(stmt)
                self.session.execute(stmt, [{'b_id_persona' :id_persona   , 'b_id_salesforce' :id_salesforce }])

                if not line:
                    finalizar = True 
                else :  
                    cnt_commit +=1 
                    
                if finalizar or cnt_commit == 10000 :
                    cnt_commit = 1
                    self.session.commit()  
                if finalizar:
                    break    
        """
        if  maximo_registros == -1 : 
            custumers  = self.session.query(Custumer).all()
        else: 
            custumers =     self.session.query(Custumer).limit(maximo_registros).all()
        self.__crearArchivosCsvDireccionesWithCustumers( custumers ,nombre_file  , max_dirs =2 )




    def __crearArchivosCsvTelefonosWithCustumers(self, custumers ,    nombre_file = 'csv_custumers_telefonos.csv' , max_telefs = 6 ,  colaTareasSaveBd : QueueBd  = None    ):

        razon  = 2000
        total =  len(custumers)
        iteraciones   = int(total/razon)
        minimo   = 0
        for i in range(iteraciones +1 ):
            custumers_group =custumers[0: 1:1]
            maximo =  razon * (i +1)
            if minimo  >=    len(custumers): 
                custumers_group =custumers[len(custumers)::1]
            elif razon * i >=    len(custumers):
                custumers_group =custumers[minimo::1]
            else :
                custumers_group =custumers[minimo: maximo]

            minimo = maximo 


            with open(nombre_file, 'a', encoding='UTF8', newline='') as file:
                writer = csv.writer(file)
                for custumer in custumers_group:
                    nroTelefonos  =  self.makerFakeCustumer.fake.random_int(min=1, max=max_telefs) 
                    for _ in range(nroTelefonos):
                        telefonoInfo = self.makerFakeCustumer.MakeCustumerTelefFake(custumer.id_persona) 
                        telfonoDb  =  Telefonos(id_persona=  custumer.id_persona  , id_registro=telefonoInfo.id_registro )
                        
                        if (colaTareasSaveBd ): colaTareasSaveBd.queueSaveRegistro.put(telfonoDb)

                        
                        writer.writerow( telefonoInfo.getArray())
                        print(f'id_persona:{ custumer.id_persona} data: {telefonoInfo}'  )

            if (colaTareasSaveBd ):  colaTareasSaveBd.queueSaveRegistro.put(True)
            

    # funcion crea telefonos de los clientes existentes
    def crearArchivoCsvTelefonos(self, colaTareasSaveBd : QueueBd):

        custumers  = self.session.query(Custumer).all()
        self.__crearArchivosCsvTelefonosWithCustumers(custumers , 'csv_custumers_telefonos.csv'  , colaTareasSaveBd  )



    def __crearArchivosCsvDireccionesWithCustumers(self, custumers ,    nombre_file = 'csv_custumers_direcciones.csv' , max_dirs = 2,  colaTareasSaveBd : QueueBd  = None    ):

        razon  = 2000
        total =  len(custumers)
        iteraciones   = int(total/razon)
        minimo   = 0

        for i in range(iteraciones +1 ):
            custumers_group =custumers[0: 1:1]

            maximo =  razon * (i +1)
            if minimo  >=    len(custumers): 
                custumers_group =custumers[len(custumers)::1]
            elif razon * i >=    len(custumers):
                custumers_group =custumers[minimo::1]
            else :
                custumers_group =custumers[minimo: maximo]

            minimo = maximo 

            with open(nombre_file, 'a', encoding='UTF8', newline='') as file:
                writer = csv.writer(file)
                for custumer in custumers_group:
                    nroDirecciones   =  self.makerFakeCustumer.fake.random_int(min=1, max=2) 
                    for _ in range(nroDirecciones):
                        direccionInfo = self.makerFakeCustumer.MakeCustumerDirFake(custumer.id_persona) 
                        direccionInfo.id_salesforce = custumer.id_salesforce 
                        direccionDb  =  Direcciones(id_persona=  custumer.id_persona  , id_registro=direccionInfo.id_registro )
                        if colaTareasSaveBd : colaTareasSaveBd.queueSaveRegistro.put(direccionDb)
                        writer.writerow( direccionInfo.getArray()) 
                        print(f'id_persona:{ custumer.id_persona} data: {direccionInfo}'  )
 #                   self.session.commit()

            if colaTareasSaveBd : colaTareasSaveBd.queueSaveRegistro.put(True)




    # funcion crea direcciones de los clientes nuievos 
    def   crearArchivoCsvDirecciones(self , colaTareasSaveBd : QueueBd): 
        custumers  = self.session.query(Custumer).all()
        self.__crearArchivosCsvTelefonosWithCustumers(custumers , 'csv_custumers_direcciones.csv'  , colaTareasSaveBd  )
        