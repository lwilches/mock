import threading
import queue
from Ports.ModelBd import Custumer , Direcciones , Telefonos
from Ports.connectDb import Session, Base, Engine


# clase q procesa cola de tareas de grabacion / actualziacion  bd 
class QueueBd :

    def __init__(self):

        self.queueSaveRegistro = queue.Queue()
        self.session = Session()

        def workerSalvarBdRegistros():
            while True:
                item = self.queueSaveRegistro.get()
                if  isinstance(item, Telefonos) or isinstance(item, Direcciones)  :
                    self.session.add(item)
                    print(f'save  {item.id_registro}')
                else:
                    self.session.commit()
                    print(f'save commit')
                
                self.queueSaveRegistro.task_done()

        threading.Thread(target=workerSalvarBdRegistros, daemon=True).start()


    def registerWorker(self, metodo):
        #registra workr remoto
        threading.Thread(target=metodo, daemon=True).start()

    def esperarfFinaliceSave(self):
        self.queueSaveRegistro.join()

