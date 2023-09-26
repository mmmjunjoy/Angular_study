#orm 으로 인해 , 성능이 나빠지는 이슈가 생기기도 한다고 함



# 이를 위해 orm을 사용할때 실행 쿼리문을 볼 수 있도록 창을 띄워놓자

#--------------------------------------------------------------
# mysql client에서
show processlist; # 현재 mysql에서 실행 중인 process 보기

show variables like 'general_log%'; # 현재 general_logs의 상태를 볼 수 있습니다.

set GLOBAL general_log='ON'; #general_log를 켤 때

set GLOBAL general_log='OFF'; #general_log를 끌 때


#--------------------------------------------------------------

# 나도 모르게 새로운 쿼리가 생성되기도 하는 이슈
# -> 1 + N 쿼리 문제 발생
# 이를 개선할 수 있는 4가지 방안

#간단한 db 모델 

class Member(models.Model):
	name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    detail = models.ForeignKey('MemberDetail', on_delete=SET_NULL)
    
	class Meta:
    	db_table = "member"
        
class MemberDetail(models.Model):
	address = models.CharField(max_length=32)
    
    class Meta:
    	db_table = "member_detail"

# 성능이 나빠지는 코드

def get_member_address_list():
	result = []

    member_list = Member.objects.filter(age__gte=30)

    for member in member_list:
        member_address = member.detail.address
        result.append(member_address)

    return result


# 1. select_related 사용


def get_member_address_list():
	result = []

    member_list = Member.objects.select_related('detail').filter(age>30)

    for member in member_list:
        member_address = member.detail.address
        result.append(member_address)

    return result

# 2. 매개변수를 넘겨줄떄 객체형태로 넘겨주자

class GetMemberInfo:
	
    # 특정 나이보다 큰 멤버들의 주소 정보를 가지고 오는 함수
    def get_member_address_list_from_age(age):
        result = []
        member_list = Member.objects.filter(age>30)

        for member in member_list:
            member_address = self.get_member_address(member.id)
            result.append(member_address)
	
    # 특정 멤버의 주소 정보를 가지고 오는 함수
    @staticmethod
    def get_member_address(member_id):
        member = Member.objects.get(id=member_id)
        member_address = member.detail.address
        return member_address
    

# select_relate포함 + member_id가 아닌 member로 넘겨준다


class GetMemberInfo:
	
    # 특정 나이보다 큰 멤버들의 주소 정보를 가지고 오는 함수
    def get_member_address_list_from_age(age):
        result = []
        member_list = Member.objects.select_related('detail').filter(age>30)

        for member in member_list:
            member_address = self.get_member_address(member)
            result.append(member_address)
	
    # 특정 멤버의 주소 정보를 가지고 오는 함수
    @staticmethod
    def get_member_address(member):
        member_address = member.detail.address
        return member_address




# 3. 필요한 부분에는 캐시를 적용

# 여기서는 , 캐시의 시간을 적절하게 세팅해줘야한다


# 4. 원시 sql문 적용하기

#  Manager.raw() 를 사용하여 원시 쿼리를 수행 -> 모델 인스턴스 반환



