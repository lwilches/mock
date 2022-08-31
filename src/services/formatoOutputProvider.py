
from dataclasses import asdict
from dynamodb_json import json_util as json_dynamo 
import json

class FormatoOutput:
    def format(self, data ):
        raise Exception("NotImplementedException")



class FormatoOutputJson(FormatoOutput ) :
    def format(self , data ):
        return  json.dumps(data.__dict__)   



class FormatoOutputJsonDynamo(FormatoOutput ) :
    def format(self ,data ):
        return  json_dynamo.dumps(data.__dict__,as_dict= True )
