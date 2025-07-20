from django.shortcuts import render
from .models import Employee
from django.views import View
import json
from django.http import HttpResponse
from api.untils import is__json
from api.mixins import Serializers_mixins,HttpResponseMixin
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class EMP_CBV(HttpResponseMixin, Serializers_mixins, View):

    def get(self, request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=1)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'NOT found id, please enter valid ID'})
            return self.render_to_http(json_data, status=400)
        else:
            json_data = self.serialize([emp])
            return self.render_to_http(json_data, status=200)
   
    
    def post(self,request,*args,**kwargs):
        data=request.body
        Valid_json=is__json(data)
        if not Valid_json:
           json_data=json.dumps({'msg':'it not vaild'})
           return self.render_to_http(json_data,status=400)
        json_data=json.dumps({'msg':'it is  vaild Data' })
        return self.render_to_http(json_data)


        
        











'''
class EMP_ALL(View):
    def get(self,request,*agrs,**kwargs):

        Quary_set=Employee.objects.all()

        json_data=serialize('json',Quary_set,fields=('Ename','EJob'))
        pdict=json.loads(json_data)
        final_list=[]
        for obj in pdict:
           emp_data=obj['fields']
           final_list.append(emp_data)
        json_data=json.dumps(final_list,)
        return HttpResponse(json_data,content_type='applications/json')


class EMP_ALL(Serializers_mixins,View):
    def get(self,request,*agrs,**kwargs):

        Quary_set=Employee.objects.all()
        json_data=self.serialize(Quary_set)
        return HttpResponse(json_data,content_type='applications/json')'''