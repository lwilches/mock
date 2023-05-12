
from dataclasses import asdict
from dynamodb_json import json_util as json_dynamo 
import boto3
import json
from json import JSONEncoder


class FormatoOutput:
    def format(self, data ):
        raise Exception("NotImplementedException")



class FormatoOutputJson(FormatoOutput ) :
    def format(self , data ):
        return json.dumps(data, cls=CustomEncoder)



class FormatoOutputJsonDynamo(FormatoOutput ) :
    def format(self ,data ):
        
        
        jsonText   =  FormatoOutputJson().format(data)
        #json_obj = json.load(jsonText)
        with open('json1.json', 'w') as f:
            f.write(jsonText)
        
        records = ""
        with open('json1.json', 'r') as f:
            records =json.load(f)

  
 
        # Print the type of data variable
        print("Type:", type(records))


        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('tbl_info_persona')
        for record in  records :
            table.put_item(Item=record)

        return data  #json_dynamo.dumps(jsonText, as_dict= False )






class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


