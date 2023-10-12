from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import TodoModel
import urllib.request
import json



def index(request):
    return HttpResponse("Hello, world. ")


# 0. todo data front에 보내주기

# todo/sendtodo
def sendtododb(request):

    if request.method == 'GET':

        print("get_success_sendtododata")

        TodoDB = list(TodoModel.objects.all().values_list('id','status','title','content','due_date' ))

        print("전체 데이터: ", TodoDB)

        data = {
            'tdmaindata' : TodoDB
        }

        return JsonResponse(data)




# 1. 할일 생성

# todo/create

def todocreate(request):

    if request.method == 'POST':

        print("post_success_create")

        # 프론트에서 todo data 받아서 변수에 저장

        TodoPayload = json.loads(request.body)
        print("payload" , TodoPayload)
        tdstatus = TodoPayload["tdstatus"]
        tdtitle = TodoPayload["tdtitle"]
        tdcontent = TodoPayload["tdcontent"]
        tdduedate = TodoPayload["tdduedate"]


        print("todo data: " , tdstatus , tdtitle , tdcontent, tdduedate )


        # todo data저장

        new_todo = TodoModel.objects.create(status = tdstatus , title =tdtitle , content = tdcontent, due_date=tdduedate )

        print("새로운 todo저장되었습니다.")

        successdata = {
            'result' : True
        }

        return JsonResponse(successdata)
        


# 2. 할일 삭제

# todo/delete

def tododelete(request):

    if request.method == 'POST':

        # 삭제할 todo pk id받기
        TodoDeletePayload = json.loads(request.body)
        TodoPkId = TodoDeletePayload['todopkid']
        
        print('id:', TodoPkId)

        # 행 삭제하기

        deletetodo = TodoModel.objects.filter(id = TodoPkId)

        print("삭제될 행 추출" , deletetodo)

        GoDeleteToDo = deletetodo.delete()

        print("post_success_delete")

        data = {
            'success' : True
        }
        return JsonResponse(data)




        




# 3. 할일 수정

# todo/modify


def todomodify(request):

    if request.method == 'POST':

        print("post_success_modify")





