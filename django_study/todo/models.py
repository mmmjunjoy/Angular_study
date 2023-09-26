from django.db import models
from django.conf import settings


# AUTH_USER_MODEL :  장고에서 인증 및 권한 부여 목적으로 사용할 사용자 모델을 나타내는 설정이다. 

#author : ForeignKey 필드가 된다.

# on_delete = models.CASCADE: (on_delete: ForeignKeyField가 바라보는 값이 삭제될때 해당 요소를 처리하는 방법을 지정해주는 것)
# 

class Todo(models.Model):
  title = models.TextField()
  completed = models.BooleanField(default=False)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
  )

