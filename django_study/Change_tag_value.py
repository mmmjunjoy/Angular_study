    def handle(self, *args, **options):
        print('test')



        # <!------ tag 실험하기 위해 ------->

        # 전체에 대한 status값 가져오기

        shop_tag = shop.objects.all().values('status')

        # print('shop_tag' , shop_tag)

        print('----------------------------------------------------------')

        # 추출된 mallid에 대해서만 status값 가져오기 
        # 원하는 결과값  -> dictionary 형태로 , {'1':'','2':'' ,'3':''}
        # list - 채널톡에서 추출한 mallID이다.
        
        list = ['doufabric','kicksewing','urbansteer','sh9193','dddd']
        result = {}
        for i in range(len(list)):
            mall_ids = list[i]

            shop_status = shop.objects.filter(mall_id = mall_ids).values('status')
            print("확인" , shop_status)
            

            # 쿼리셋 존재확인을 위해 -> exists() 사용 ,
            # 나중에 채널톡에서 가져온 데이터가 우리쪽 db에는 없을수도 있기 때문이다.
            
            if shop_status.exists():

                # dictionary형태에 값 추가하기 dict[key] = value 형식으로 한다.
                result[mall_ids] = shop_status[0]['status']
                print("result" , result)
        

        print('----------------------------------------------------------')

        # 채널톡 db와 비교하며, key값이 동일할 경우, 즉 업체의 값이 일차할경우 , 채널톡 컬럼의 status 에 
        # 알파리뷰 status데이터를 삽입한다.

        # 알파리뷰의 데이터이지만 - 채널톡 db라고 가정 -> channel_key

        channel_key  = channel.objects.all().values('mall_id')
        print('channel_key',channel_key[0]['mall_id'])

        print('channel_len' , len(channel_key))

        cnt = 0

        for key in result:

            for i in range(len(channel_key)):
           
                
                if key == channel_key[i]['mall_id']:

                    # 일치하면 채널톡 db  - profile.status 에 상태 업데이트

                    # channeltalkdb.update(profilestatus = result[key])

                    newstatus = shop.objects.all()
                    newstatus.update(status = result[key])
                    cnt+=1
                    print('update_cnt', cnt)

            print('key', key)

            print('res',result[key])

     

        # <!------ tag 실험하기 위해 ------->