from django.core.management.base import BaseCommand
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response

class Command(BaseCommand):
    help = '커맨드에 대한 도움말을 적어줌'

 

    def handle(self, *args, **kwargs):
        
        userid = 'e4f4c27d-6810-4f8b-8c40-2034f7c3137a'

        url = 'https://api.channel.io/open/v4/users/@{}'.format(userid)

        headers = {'accept':'application/json' , 'x-access-key':'' , 'x-access-secret':''  }

        response = requests.get(url, headers=headers)

        print("응답" , response)
        
        items = response.json()

        print("응답 값" , items)

        # 필요한 값 추출 - profilemallId

        res = items['user']['profile']['mallId']
        
        print("----------------------------------------------------")
        print(" profile.mallID --> " ,res )





