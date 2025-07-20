from django.core.serializers import serialize
import json
from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_http(self,json_data,status=200):
        return HttpResponse(json_data,content_type='applications/json',status=status)



class Serializers_mixins(object):
    def serialize(self,Quary_set):
        
        json_data=serialize('json',Quary_set)
        pdict=json.loads(json_data)
        final_list=[]
        for obj in pdict:
            emp_data=obj['fields']
            final_list.append(emp_data)
        json_data=json.dumps(final_list)
        return json_data