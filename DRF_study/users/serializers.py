from django.contrib.auth.models import User

# django 의 기본 패스워드 검증 도구
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

# Token model
from rest_framework.authtoken.models import Token

# 이메일 중복 방지를 위해
from rest_framework.validators import UniqueValidator  




# 회원가입과 관련된 내용, 절차를 serializer 에서 구현되도록 진행

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required = True,
    validators = [UniqueValidator(queryset=User.objects.all())]
  )

 # write_only : 쓰기 전용,
 # required - True : 필수항목
  password = serializers.CharField(
    write_only = True,
    required = True,
    validators = [validate_password],
  )
  password2 = serializers.CharField(
    write_only = True,
    required = True,
  )

  class Meta:
    model = User
    fields = ('username', 'password', 'password2', 'email')
  
  def validate(self,data):
    if data['password'] != data['password2']:
      raise serializers.ValidationError(
        {"password" : "Password fields didn't match."}
      )
    
    return data
  
  def create(self, validated_data):
    user = User.objects.create_user(
      username= validated_data['username'],
      email = validated_data['email']
    )


    # set_password -> 비밀번호를 해싱해준다 (암호화)
    user.set_password(validated_data['password'])
    user.save()
    token = Token.objects.create(user= user)
    return user

