from django.db import models
from django.contrib.auth.models import User

class food(models.Model):
    TYPE1 = (
        ('1', '저장'),
        ('2', '대기중'),
        ('3', '삭제')
    )
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add = True)
    expiray_date = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=1 ,choices=TYPE1)
   
    def __str__(self):
        return self.name