from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.db import IntegrityError
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request, user_id):
    one_user = User.objects.get(pk=user_id)
    one_food = one_user.food_set.filter(status=1)

    data = list(one_food.values('id','name','count','created_at','expiray_date'))
    data =  json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return HttpResponse(data, content_type='application/json')

def food_count(request, food_id):
    count = request.Post.get("count")
    # count=1
    food.objects.filter(pk=food_id).update(count=count)

    return HttpResponse("success")