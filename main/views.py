from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.db import IntegrityError
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse


def index(request, user_id):
    one_user = User.objects.get(pk=user_id)
    one_food = one_user.food_set.filter(status=1)

    data = list(one_food.values('id','name','count','created_at','expiray_date'))
    data =  json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return HttpResponse(data, content_type='application/json')

def food_count(request, user_id, food_id):
    # count = request.Post.get("count")
    count=3
    food.objects.filter(pk=food_id).update(count=count)
    # return JsonResponse({'status' : 'success', 'user_id' : user_id})
    return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))


def food_delete(request, user_id, food_id):
    food.objects.filter(pk=food_id).update(status=3)
    # return JsonResponse({'status' : 'success', 'user_id' : user_id})
    return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))

def food_added(reqeust, user_id):
    name = request.Post.get("name")
    count = int(request.Post.get("count"))
    created_at = reqeust.Post.get("created_at")
    created_at = datetime.strptime(created_at, "%Y-%m-%d").date()
    expiray_date = created_at + timedelta(days=7)

    food.objects.create(name=name,count=count,created_at=created_at,expiray_date=expiray_date,user_id=user_id)
    return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))


