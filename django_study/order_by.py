

# order_by ?

# order_by('id')  -> id 에 대해서 오름차순

# order_by('-id')  -> id 에 대해서 내림차순
 


def orderbys():


  access_code = 12345
  info = models0.objects.filter(access_code = access_code)
  ticker_info = models1.objects.filter(shop = info).order_by('-id')[0]

