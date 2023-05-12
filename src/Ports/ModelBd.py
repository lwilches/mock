from enum import unique
from sqlite3 import Date
import string
from xmlrpc.client import Boolean
from sqlalchemy import  Column, Integer, String , Date, Boolean , ForeignKey  
from Ports.connectDb import Base
from sqlalchemy.orm import relationship 

class Custumer(Base) :
    __tablename__ = 'custumers'
    id_persona  = Column(Integer ,  primary_key=True)
    cod_tipo_doc = Column(Integer)
    id_salesforce = Column(String)
    nro_doc  = Column(String, unique=True)
    #telefonos =  relationship ('Telefonos', cascade='all, delete, delete-orphan')
    #direcciones =  relationship ('Direcciones', cascade='all, delete, delete-orphan')


class Telefonos(Base) :
    __tablename__ = 'custumers_tel'
    id_registro  = Column(String ,  primary_key=True)
    id_persona = Column(Integer, ForeignKey('custumers.id_persona'),nullable=False)


class Direcciones(Base) :
    __tablename__ = 'custumers_dir'
    id_registro  = Column(String ,  primary_key=True)
    id_persona = Column(Integer, ForeignKey('custumers.id_persona'), nullable=False)
