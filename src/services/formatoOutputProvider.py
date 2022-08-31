
from dynamodb_json import json_util as json_dynamo 

class FormatoOutput:
    def Format(data ):
        pass



class FormatoOutputJson(FormatoOutput ) :
    def Format(data ):
        return  data 



class FormatoOutputJsonDynamo(FormatoOutput ) :
    def Format(data ):
        return  json_dynamo.dumps(data)
