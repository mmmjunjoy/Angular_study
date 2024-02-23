


# get_or_create ??

# 위는 Django QuerySet API 중 하나이다.

# 일치하는 것이 있으면 반환하고 , 없으면 새로 생성하는 것이다.

class Leffe(models.Model):

  name = models.CharField(max_length=30)




# created 변수는 생성이 되었는지 안되었는지를 알 수 있다.
# true ,false로 반환 
  
obj, created = Leffe.objects.get_or_create(name = 'lefee')


