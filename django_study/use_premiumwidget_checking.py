# premium_list = []


        rolling_widget_status = False
        briefing_widget_status = False
        salesticker_widget_status = False

        if shop_service_additional_info:

            for e in shop_service_additional_info:
                #롤링위젯 체크
                if (e.name == "위젯1") and (e.status == "사용중" )  :
                    rolling_widget_status = True
                elif (e.name == "위젯1") and (e.status == "설치요청" )  :
                    rolling_widget_status = True

                #브리핑위젯 체크
                elif (e.name == "위젯2") and (e.status == "사용중" )  :
                    briefing_widget_status = True
                elif (e.name == "위젯2") and (e.status ==  "설치요청")  :
                    briefing_widget_status = True
                
                #세일즈티커 체크
                elif (e.name == "위젯3") and (e.status == "사용중"):
                    salesticker_widget_status = True
                elif (e.name == "위젯3") and (e.status == "설치요청"):
                    salesticker_widget_status = True
                   
                else:
                    continue
            


                
            print(rolling_widget_status,briefing_widget_status,salesticker_widget_status)
