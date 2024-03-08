
# model끼리의 관계성 파악 후 ,

# 필요 컬럼 추출 방식

for review_item in review_list:
                    
                    # junbo - 카테고리no,명 추출 테스트


                    # no 추출
                    review_category_nos = review_item.product.category
                    
                    c_numbers = [num for num in review_category_nos.split('|') if num.isdigit()]
                    
                    c_nolist = []
                    for i in c_numbers:
                        c_nolist.append(i)

                    print("c_nolist", c_nolist)

                    print("[---------------------]")

                    # name추출
                    c_namelist = []
                    for i in c_numbers:
                        name = review_item.shop.category.filter( category_no = i)

                        for i in name:
                            nm = i.category_name
                            c_namelist.append(nm)
                    
                    print("c_namelist", c_namelist)
                        


                    return 0