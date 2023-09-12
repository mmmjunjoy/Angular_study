
shop_service_additional_info = shop_service_additional.objects.filter(shop_id = shop_info)
premium_list = []
if shop_service_additional_info:
  for e in shop_service_additional_info:
    if e.status == "사용중" or  "설치요청":
      premium_list.append(e.name)


  if len(premium_list) != 0:
       for p in premium_list:
                    if p == "롤링위젯":
                        #롤링 html 나오게
                        print("롤링위젯 생성")
                    elif p == "브리핑위젯":
                        #브리핑  html 나오게
                        print("브리핑위젯 생성")
                    elif p == "세일즈티커":
                        #세일즈티커 html 나오게
                        print("세일즈티커 생성")
                    else:
                        print("없습니다. 끝")
  else :
      print("아무것도 신청안했습니다")