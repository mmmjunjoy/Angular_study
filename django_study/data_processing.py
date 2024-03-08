      
      
      
      
# 데이터가공  -> 추후 테스크 진행하기 위해.     

# 무분별한 텍스트를  -> 리스트 안에 담기  
      
for review_item in review_list:
                    
                    # junbo - 카테고리no,명 추출 테스트

                    review_category_nos = review_item.product.category

                    #  review_category_nos ->|80|10|30|50|17|  
                    #  이렇게 str 형식으로 추출된다. 
                    #  이렇게 되면 , 번호 각각에 대해 추후 데이터 작업을 하기 힘들기때문에 
                    #  번호들이 리스트에 담겨서 나오게끔 가공을 해줘야한다.

                    #  밑에가 그 작업이다.
                    #  1. | 기준으로 텍스트를 나누기
                    #  2. 나눠진 것들 중에서 숫자로만 이루어진 것만 리스트에 남기기  -> .isdigit()
                    
                    numbers = [num for num in review_category_nos.split('|') if num.isdigit()]


                    # -> 위 를 통해서

                    # numbers 는  -> ['80','10','30','50','17'] 이렇게 추출이 된다.

                    print("categorylist",numbers)