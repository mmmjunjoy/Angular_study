



# 현상황은, product라는 모델에서 원하는 값을 추출하는 것이다.
# filter로 product와 외래키 관계인 , shop에 대해서 정보를 기입해준다.

product_id = product.objects.filter(shop_id = shop_info)


# 여러개의 행을 추출할수 있기에, 하나하나씩 행에 맞게 값을 추출하도록 한다. 

for i  in product_id:
  print("개별 넘버", i.product_no)
        

# 아래와 같은 코드를 이용해서 정보를 추출하려고 하면 오류가 생긴다.
  
#   AttributeError: 'QuerySet' object has no attribute 'product_no'
  
# # print("product_id 테스트",product_id.product_no )