from  services.ServiceManagerFake import ServiceManagerFake
import sys
from  services.QueueBd import QueueBd 

if __name__ == '__main__':

    crear_metadata = True  
   # if  sys.argv[1] == 'custumers':
   #     crear_metadata = True 
    #Crea servicio gestion  fakes 
    servicio = ServiceManagerFake( crear_metadata)
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

    print('fin del trabajo')






