from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class food(models.Model):
    TYPE1 = (
        ('1', '저장'),
        ('2', '대기중'),
        ('3', '삭제')
    )

    TYPE2 = (
        ('1', '개'),
        ('2', 'g'),
        ('3', 'ml')
    )

    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add = True)
    expiry_date = models.DateField(default = datetime.now().date())
    status = models.CharField(max_length=1 ,choices=TYPE1, default='1')
    unit = models.CharField(max_length=20 , default='개') 
   
    def __str__(self):
        return self.name

class recipe_info(models.Model):
    recipe_id = models.IntegerField(unique = True)
    recipe_nm_ko = models.CharField(max_length=800)
    sumry = models.CharField(max_length=800)
    nation_nm = models.CharField(max_length=800)
    cooking_time = models.CharField(max_length=800)
    calorie = models.CharField(max_length=800)
    level_nm = models.CharField(max_length=800)
    img_url = models.CharField(max_length=800)
    det_url = models.CharField(max_length=800)

    class Meta:
        ordering = ('recipe_id',)

    def __str__(self):
        return str(self.recipe_nm_ko)

class recipe_food(models.Model):
    recipe_id = models.ForeignKey(recipe_info)
    irdnt_sn = models.IntegerField(unique = True)
    irdnt_nm = models.CharField(max_length=800)

    class Meta:
        ordering = ('irdnt_sn',)

    def __str__(self):
        return str(self.irdnt_sn)

class recipe_how(models.Model):
    recipe_id = models.ForeignKey(recipe_info)
    cooking_no = models.IntegerField()
    cooking_dc = models.CharField(max_length=800)
    stre_step_image_url = models.CharField(max_length=800, null=True)
    
    class Meta:
        ordering = ('recipe_id',)

    def __str__(self):
        return str(self.recipe_id)

