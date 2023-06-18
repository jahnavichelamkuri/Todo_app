from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.list import ListView
from .models import Task
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
from django.conf import settings
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

# def index(request):
#     return HttpResponse("Jahnavi")

# class TaskList(ListView):
#     model =Task

def create_task(request,user,task,description,status):
    Task.objects.create(user=user,task=task,description=description,status=status)

    response_data={"message":"successfull"}
    return response_data




def fetch_data(request, user):
    tasks = Task.objects.filter(user=user, status="In Progress")
    taskss = []
    for i in tasks:
        taskss.append(i.task)
        # print(task_list)

    response_data = {
        'task' : taskss
    }

    return response_data


def update_task(request,user,task,description,status,upload_file):
    ut=Task.objects.filter(user=user,task=task,status='In Progress').first()
    ut.description=description
    ut.status=status
    save_directory = 'taskfiles/'
    ut.file = default_storage.save(save_directory + upload_file.name, upload_file)
    ut.save()

    response_data={'message':"Task status updated successfully"}
    return response_data



def history_data(request,user):
   
    hd=Task.objects.filter(user=user,status="done")
    # print(hd)
    task_list=[]
    # print(task_list)
    status_list=[]
    for item in hd:
        task_list.append(item.task)
        # status_list.append(item['status'])
    response_data={"tasklist":task_list}
    return response_data

class Todo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            type = self.request.GET.get('type')
            user = self.request.GET.get("user")

            # print(user)
            task = self.request.GET.get("task")
            description= self.request.GET.get("description")
            status = self.request.GET.get("status")
            if type =="create":
                response = create_task(request)
            elif type == "update":
                response =update_task(request)
            elif type =="history":
                response = history_data(request)
            elif type =="fetch_data":
                response = fetch_data(request,user)
            return JsonResponse(response,safe=False)
        except Exception as e:
            return Response({'error': str(e)})

    def post(self,request,*args,**kwargs):
        print("POST")
        try:
            type = self.request.GET.get('type')
            print(type)
            user = self.request.GET.get("user")
            print(user)
            task = self.request.GET.get("task")
            description= self.request.GET.get("description")
            status = self.request.GET.get("status")
            upload_file= self.request.FILES.get('file')
            if type =="create":
                response = create_task(request,user,task,description,status)
            elif type == "update":
                response =update_task(request,user,task,description,status,upload_file)
            elif type =="history":
                response = history_data(request,user)
            elif type =="fetch_data":
                response = fetch_data(request)
            return JsonResponse(response,safe=False)
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