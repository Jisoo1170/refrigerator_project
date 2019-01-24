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
    one_food = one_user.food_set.filter(status = 1)
    data = list(one_food.values('id','name','amount','created_at','expiry_date','unit','status'))
    # data = [{'id':obj.pk, 'name':obj.name, 'amount':obj.amount, 'created_at':obj.created_at,
    #         'expiry_date':obj.expiry_date, 'unit':obj.get_unit_display()} for obj in one_food ]
    data =  json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return HttpResponse(data, content_type='application/json')

def food_amount(request, user_id, food_id, amount):
    try:
    # amount = int(request.Post.get("amount"))
        food.objects.filter(pk=food_id).update(amount=amount)
# return JsonResponse({'status' : 'success', 'user_id' : user_id})
# return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})


def food_delete(request, user_id, food_id):
    try:
        food.objects.filter(pk=food_id).update(status=3)
    # return JsonResponse({'status' : 'success', 'user_id' : user_id})
    # return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})

@csrf_exempt
def food_added(request, user_id):
    # print('-'*100)
    # print(request.POST.get("name"))
    # print(request.POST.get("amount"))
    # print(request.POST.get("created_at"))
    try:
        name = eval(request.body.decode('utf-8')).get('name')
        amount = eval(request.body.decode('utf-8')).get('amount')
        created_at = eval(request.body.decode('utf-8')).get('created_at')
        
        created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d").date()
        expiry_date = created_at + datetime.timedelta(days=7)

        food.objects.create(name=name,amount=amount,created_at=created_at,expiry_date=expiry_date,user_id=user_id)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})
    # return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))

@csrf_exempt
def food_expiry(request, user_id, food_id):
    try:
        
        print(request.body)
        
        expiry_date = eval(request.body.decode('utf-8')).get('expiry_date')
        print(expiry_date)
        # expiry_date = request.POST.get("expiry_date")
        expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
        print(expiry_date)
        food.objects.filter(pk=food_id).update(expiry_date=expiry_date)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})

    # return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))

@csrf_exempt    
def food_created (request, user_id, food_id):
    try:
        # request.body.decode('utf-8')
        created_at = eval(request.body.decode('utf-8')).get('created_at')
        print(created_at)
        # created_at = request.POST.get("created_at")
        created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d").date()
        food.objects.filter(pk=food_id).update(created_at=created_at)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})

    # return HttpResponseRedirect(reverse('main:index', kwargs={'user_id': user_id}))

@csrf_exempt    
def food_unit (request, user_id, food_id):
    try:
        print(request.body)
        unit = eval(request.body.decode('utf-8')).get('unit')
        food.objects.filter(pk=food_id).update(unit=unit)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})

def food_deep (request, user_id):
    one_user = User.objects.get(pk=user_id)
    one_food = one_user.food_set.filter(status=2)

    data = list(one_food.values('id','name','amount','created_at','expiry_date','unit'))
    data =  json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return HttpResponse(data, content_type='application/json')

def deep_add (request, user_id, food_id):
    try:
        food.objects.filter(pk=food_id).update(status=1)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail","message": str(e)})

def deep_delete (request, user_id, food_id):
    try:
        food.objects.filter(pk=food_id).update(status=3)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail","message": str(e)})    

def search (request, search):
    r_id = recipe_food.objects.filter(irdnt_nm=search).values('recipe_id')
    recipes = recipe_info.objects.filter(recipe_id__in=r_id)
    # .values('recipe_nm_ko',
    #     'sumry','img_url','nation_nm','cooking_time','level_nm')
    data = [{'recipe_id':obj.recipe_id,'recipe_name':obj.recipe_nm_ko,'sumry':obj.sumry,'img_url':obj.img_url,
    'nation_nm':obj.nation_nm,'cooking_time':obj.cooking_time, 
    'recipes_ingredients': list(recipe_food.objects.filter(recipe_id=obj.pk).values('irdnt_nm'))}
    for obj in recipes]
    data =  json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return HttpResponse(data, content_type='application/json')

def recipe (request, recipe_id):
    obj = recipe_info.objects.get(pk=recipe_id)
    how = list(recipe_how.objects.filter(recipe_id=recipe_id).values('cooking_no','cooking_dc','stre_step_image_url'))
    recipe_ingredients = list(recipe_food.objects.filter(recipe_id=recipe_id).values('irdnt_nm'))
    data = {'recipe_id':recipe_id, 'recipe_nm_ko' : obj.recipe_nm_ko, 'recipe_ingredients':recipe_ingredients,
    'sumry':obj.sumry, 'img_url':obj.img_url,'nation_nm':obj.nation_nm,'cooking_time':obj.cooking_time, 
    'how':how}
    data =  json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def deep_receive (request, user_id):
    try:
        received_json_data = json.loads(request.body.decode("utf-8"))
        print(received_json_data)
        for o in received_json_data:
            name = o.get("name")
            print(name)
            print(food.objects.filter(user_id=user_id).filter(name=name).count())
            if food.objects.filter(user_id=user_id).filter(name=name).count() == 0:
                print(name)
                print(food.objects.filter(user_id=user_id).filter(name=name).count())
                food.objects.create(name=name,user_id=user_id, status=2)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status":"fail",'message': str(e)})
    # return HttpResponse(data, content_type='application/json')

def recommand(request, user_id):
    one = food.objects.filter(status=1).filter(expiry_date__gte=datetime.datetime.now().date()).order_by('expiry_date')[0]
    r_id = recipe_food.objects.filter(irdnt_nm=one.name).values('recipe_id')
    recipes = recipe_info.objects.filter(recipe_id__in=r_id)

    # .values('recipe_nm_ko',
    #     'sumry','img_url','nation_nm','cooking_time','level_nm')
    data = [{'recipe_id':obj.recipe_id,'recipe_name':obj.recipe_nm_ko,'sumry':obj.sumry,'img_url':obj.img_url,
    'nation_nm':obj.nation_nm,'cooking_time':obj.cooking_time, 
    'recipes_ingredients': list(recipe_food.objects.filter(recipe_id=obj.pk).values('irdnt_nm'))}
    for obj in recipes]
    data =  json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return HttpResponse(data, content_type='application/json')