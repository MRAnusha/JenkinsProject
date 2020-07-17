import json

class Jsonbody(object):

    def __init__(self):
        pass

    def read_json_body(self,jsonfilepath):
        with open(jsonfilepath, 'r') as myfile:
            data = myfile.read()
            body = json.loads(data)
            return body

    def parse_nested_json_response(self,jsonresponse,nestedjsonkey,key):
        value = json.dumps(jsonresponse[nestedjsonkey][key])
        return value
       

    def parse_json_response(self,jsonresponse,key):
        value = json.dumps(jsonresponse[key])
        return value
