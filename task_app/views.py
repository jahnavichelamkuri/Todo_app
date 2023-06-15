from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.list import ListView
from .models import Task
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# def index(request):
#     return HttpResponse("Jahnavi")

# class TaskList(ListView):
#     model =Task

def create_task(request,user,task,description,status):
    Task.objects.create(user=user,task=task,description=description,status=status)

    response_data={"message":"insertion successfull"}
    return response_data


def delete_task(request):
    pass

def update_task(request):
    pass

def read_task(request):
    pass

class Todo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            type = self.request.GET.get('type')
            user = self.request.GET.get("user")
            task = self.request.GET.get("task")
            description= self.request.GET.get("description")
            status = self.request.GET.get("status")
            if type =="create":
                response = create_task(request)
            elif type == "update":
                response =update_task(request)
            elif type =="read":
                response = read_task(request)
            elif type =="delete":
                response = delete_task(request)
            return JsonResponse(response)
        except Exception as e:
            return Response({'error': str(e)})

    def post(self,request,*args,**kwargs):
        try:
            type = self.request.GET.get('type')
            print(type)
            user = self.request.GET.get("user")
            print(user)
            task = self.request.GET.get("task")
            description= self.request.GET.get("description")
            status = self.request.GET.get("status")
            if type =="create":
                response = create_task(request,user,task,description,status)
            elif type == "update":
                response =update_task(request)
            elif type =="read":
                response = read_task(request)
            elif type =="delete":
                response = delete_task(request)
            return JsonResponse(response)
        except Exception as e:
            return Response({'error': str(e)})
            

class DataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            token = request.META['HTTP_AUTHORIZATION'].split()[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            data = {"Userid":user_id}
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=401)
