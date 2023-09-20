User.objects.all()

user.objects.filter(activate = True)

queryset = User.objects.all()



#aggregate() -> 집계함수를 이용하여 연산 가능

#테이블의 전체 id개수 셀때 
User.objects.aggregate(Count('id'))

#UNION 
#쿼리셋의 결과를 합칠 수 있다
books = Book.objects.all()
ebooks = Ebook.objects.all()

books.union(ebooks)

# union 다른 사용법

data3 = union(books,ebooks)


#30세 이상 멤버 정보 가져오기

#gte : 이상의 의미
#gt: greater than : >
#lte : less than or equal : <=
#lt : less than : <

Member.objects.filter(age__gte=30)


