from xmlrpc.client import boolean
from modelo.Custumer  import CustumerInfo, TelefonoContacto, DireccionContacto
from faker import Faker



'''
Esta clase expone 3 metodos para crear los registros de clintes, telefonos y direccines fakes
* MakeCustumerFake -> crea anuevo clinte con informacion fake 
* MakeCustumerTelefFake -> crea telefono con informacion fake 
* MakeCustumerDirFake -> crea direccion  con informacion fake  
'''


class CustumerFakesManager :
    def __init__(self) :
        self.fake = Faker(['it_IT', 'en_US', 'es_CO'])
        
    #genera fake de custumer     
    def MakeCustumerFake(self):

        id_persona = self.fake.unique.random_int(min=11000, max=999999) 
        nro_doc   = self.fake.unique.random_int(min=110002000, max=999999999)   
        tipo_doc =self.fake.random_int(min=1, max=3)
        nombre_completo =""
        nombre=""
        primer_apellido =""
        segundo_apellido =""
        if tipo_doc == 3:
            nombre_completo = self.fake.company()   
        else: 
            nombre = self.fake.first_name()
            primer_apellido = self.fake.last_name()
            segundo_apellido  = self.fake.last_name()
        ciuu  = self.fake.random_int(min=11000, max=99999) 

        return  CustumerInfo(id_persona,nro_doc  , tipo_doc, nombre, primer_apellido, segundo_apellido ,  nombre_completo , ciuu      )

    # Genera un  nuevo registro de telefono 
    def MakeCustumerTelefFake(self, id_persona):
        cod_tipo_telef  = self.fake.random_element(elements=(1,2, 8,10,20))
        telefono = ""
        if cod_tipo_telef == 1 or  cod_tipo_telef == 2 :
            telefono = self.fake.phone_number()
        elif     cod_tipo_telef == 8 :
            telefono = self.fake.msisdn()
        else : 
            telefono = self.fake.ascii_safe_email()
        id_registro = self.fake.uuid4()
        contacto_principal:boolean  = True
        fecha_alta = self.fake.date()
        return  TelefonoContacto(id_persona, id_registro  , cod_tipo_telef , telefono  ,   contacto_principal  , fecha_alta   )

    # Genera un  nuevo registro de telefono 
    def MakeCustumerDirFake(self, id_persona):

        cod_tipo_dir   = self.fake.random_element(elements=(1,2))
        direccion =  self.fake.address()
        cod_pais = 1 
        cod_dpto =  5
        cod_municipio = self.fake.random_element(elements=(5001,5002,5004,5021,5030,5031,5034,5036,5038,5040,5042,5044,5045,5051,5055,5059,5079,5086,5088,5091,5093,5101,5107,5113,5120,5125,5129,5134,5138,5142,5145,5147,5148,5150,5154,5172,5190,5197,5206))
        fecha_alta = self.fake.date()
        id_registro = self.fake.uuid4()
        return DireccionContacto(  id_persona ,id_registro ,  cod_tipo_dir  , direccion ,cod_pais ,  cod_dpto ,  cod_municipio , fecha_alta )

