
from select import select
from selectors import SelectorKey
from xmlrpc.client import boolean


class DireccionContacto:
    def __init__(self,  id_persona , id_registro, cod_tipo_dir , direccion ,  cod_pais , cod_dpto ,  cod_cuidad, fec_alta    ) :
        self.id_persona = id_persona
        self.id_registro  = id_registro
        self.cod_tipo_dir = cod_tipo_dir
        self.direccion = direccion
        self.cod_pais = cod_pais
        self.cod_dpto = cod_dpto
        self.cod_ciudad = cod_cuidad
        self.fecha_alta = fec_alta

    def __str__(self) -> str:
        return (f'"{self.id_persona}","{self.id_registro}" , "{self.cod_tipo_dir}" ,  "{self.direccion}","{self.cod_pais}",  "{self.cod_dpto}" , "{self.cod_ciudad}" , "{self.fecha_alta}" ')

    def getArray (self):
        return self.id_persona ,  self.id_registro , self.cod_tipo_dir , self.direccion, self.cod_pais , self.cod_dpto , self.cod_ciudad , self.fecha_alta 
        


class TelefonoContacto:
    def  __init__(self,  id_persona , id_registro,cod_tipo_telef ,telefono  ,contacto_principal :boolean , fecha_alta ):
        self.id_persona = id_persona
        self.id_registro = id_registro 
        self.cod_tipo_telef = cod_tipo_telef 
        self.telefono = telefono 
        self.contacto_principal = contacto_principal ,  
        self.fecha_alta = fecha_alta
    
    def __str__(self) -> str:
        return (f'"{self.id_persona}","{self.id_registro}" , "{self.cod_tipo_telef}" ,  "{self.telefono}","{self.contacto_principal[0]}",  "{self.fecha_alta}" ')

    def getArray (self):
        return self.id_persona ,  self.id_registro , self.cod_tipo_telef , self.telefono, self.contacto_principal[0] , self.fecha_alta  



class CustumerInfo :

    def __init__(self , id_persona , nro_doc  , cod_tipo_doc ,nombre  , primer_apellido  ,segundo_apellido , nombre_completo  ,ciiu) :  
        self.id_persona  = id_persona
        self.nro_doc = nro_doc 
        self.cod_tipo_doc = cod_tipo_doc
        self.nombre = nombre  or ""
        self.primer_apellido = primer_apellido or ""
        self.segundo_apellido = segundo_apellido or ""
        self.nombre_completo = nombre_completo or ""
        self.ciiu =ciiu
    def __str__(self) -> str:
        return (f'"{self.id_persona}","{self.cod_tipo_doc}" , "{self.nro_doc}" ,  "{self.nombre}","{self.primer_apellido}",  "{self.segundo_apellido}" , "{self.nombre_completo}" , "{self.ciiu}" ')

    def getArray (self):
        return self.id_persona ,  self.cod_tipo_doc , self.nro_doc , self.nombre, self.primer_apellido , self.segundo_apellido , self.nombre_completo , self.ciiu 