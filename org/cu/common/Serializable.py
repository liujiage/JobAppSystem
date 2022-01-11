import json

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Serializable object
'''
class Serializable(object):
    # transfer object to JSON
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)