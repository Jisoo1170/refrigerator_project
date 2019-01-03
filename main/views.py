from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.db import IntegrityError
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def food_added(request, user_id):
    print('-'*100)
    print(request.POST.get("name"))
    print(request.POST.get("count"))
    print(request.POST.get("created_at"))
    try:
        name = request.POST.get("name")
        count = int(request.POST.get("count"))
        created_at = request.POST.get("created_at")
        
        created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d").date()
        expiray_date = created_at + datetime.timedelta(days=7)

        food.objects.create(name=name,count=count,created_at=created_at,expiray_date=expiray_date,user_id=user_id, status=1)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})
    # return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))

@csrf_exempt
def food_expiary(request, user_id, food_id):
    try:
        expiray_date = request.POST.get("expiary_date")
        expiray_date = datetime.datetime.strptime(expiray_date, "%Y-%m-%d").date()
        food.objects.filter(pk=food_id).update(expiray_date=expiray_date)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})

    # return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))

@csrf_exempt    
def food_created (request, user_id, food_id):
    try:
        created_at = request.POST.get("created_at")
        created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d").date()
        food.objects.filter(pk=food_id).update(created_at=created_at)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})

    # return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))

