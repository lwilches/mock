from  services.ServiceManagerFake import ServiceManagerFake
import sys
from  services.QueueBd import QueueBd 
from  services.formatoOutputProvider import FormatoOutput , FormatoOutputJson , FormatoOutputJsonDynamo 

import json  

if __name__ == '__main__':

    crear_metadata = True  
   # if  sys.argv[1] == 'custumers':
   #     crear_metadata = True 
    #Crea servicio gestion  fakes 
    servicio = ServiceManagerFake( crear_metadata, FormatoOutputJsonDynamo())
    colaTareasSaveTel = QueueBd()
    #Abre la sesión
    if sys.argv[1] == 'custumers':
        servicio.crearArchivoCsvCustumers()
        
    elif sys.argv[1] == 'telefonos':
        servicio.crearArchivoCsvTelefonos(colaTareasSaveTel)
        colaTareasSaveTel.esperarfFinaliceSave()
    elif sys.argv[1] == 'direcciones':
        servicio.crearArchivoCsvDirecciones(colaTareasSaveTel)
        colaTareasSaveTel.esperarfFinaliceSave()

    elif sys.argv[1] == 'repeat':
        servicio.crearArchivoCsvCustumersExists('csv_custumers.csv' , 500)
    elif sys.argv[1] == 'to_json':
        servicio.crearArchivoCsvCustumersExistsFormatJson('csv_custumersjson.csv' , 500)
    elif sys.argv[1] == 'repeat_dir':
       servicio.crearArchivoCsvDireccionesCustumersExists('csv_custumers_direcciones1.csv')

    print('fin del trabajo')






