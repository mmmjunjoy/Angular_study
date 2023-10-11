from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import TodoModel
import urllib.request
import json



def index(request):
    return HttpResponse("Hello, world. ")


# 0. ToDo Get API / todo data front에 보내주기

# todo/sendtodo
def sendtododb(request):

    if request.method == 'GET':

        print("get_success_sendtododata")

        # list 사용 : QuerySet 과 JSON 불일치 오류 해결
        TodoDB = list(TodoModel.objects.all().values_list("status","title","due_date"))

        print("전체 데이터: ", TodoDB)

        Data = {
            'statusft' : TodoDB
        }

        return JsonResponse(Data)




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

        print("post_success_delete")


        




# 3. 할일 수정

# todo/modify


def todomodify(request):

    if request.method == 'POST':

        print("post_success_modify")





