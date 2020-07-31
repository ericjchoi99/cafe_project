from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser) : 
    phone_number = models.CharField(max_length = 10, null=True, blank =True) #null = 이 객체에 해당하는 속성이 데이터에 해당 x; 완전 비었다; 몰라도 된다는 뜻;undefined라고 뜸 /blank = 이 안에 데이터가 없다는 것을 명시; 안에 공란이 있다; 불러와도 공백이다~
    birth_day = models.DateField(default=timezone.now, null=True, blank =True)