   # ----------데이터 받아오기 연습-------------------


        # 1. start_data

        shop_startdata=shop_info.start_date.strftime(date_format)

        print(shop_startdata)

        # 1. end_data

        # 2. shopping_mall_name

        store_info= store_etc.objects.filter(id=3).first()

        shoppingmall_name = store_info.shop_name

        print("쇼핑몰명", shoppingmall_name)


        # 3. 별점 ,텍스트 ,포토 , 동영상 , 설문 
        
        rewards_info = option_reward.objects.filter(shop_id=shop_info,title="quick" , value="member").first()

        rewards_member_quick = rewards_info.reward

        print("멤버_퀵 : ", rewards_member_quick)



        #-------first를 쓰지않고  for문을 이용하여 값을 가져올때 ------------    
        # for i in rewards_info:
        #     i.reward

        #     print("i",i.reward , i.value)\

        #------------------------------------------------------------------