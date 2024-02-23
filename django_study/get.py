



# get ?

# get을 통한, 값 지정 

# type 을 가지고오는데, 없다면 , False로 기본값을 지정해준다.

# 추후, == 으로 가져온 값이 true인지 비교 연산

# 즉,  마지막으로 type에는  boolean값이 지정된다. 

def get(request):




  type = (request.POST.get('type' , False) == 'true')