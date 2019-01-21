from django.test import TestCase
import sys
print(sys.path)
path = "/Users/jisoo/Desktop/django_project/refrigerator/"
if path not in sys.path:
    sys.path.append(path)
print(sys.path)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "refrigerator.settings")
import json as simplejson
import django
django.setup()
from main.models import *

# all_recipe = recipe_food.objects.all()
# for recipe in all_recipe:
#     print(str(recipe.pk)+"__"+str(recipe.recipe_id))

# f = open('recipe_food.json', 'r')
# obj = simplejson.load(f)

# obj = obj.get('data')

# for o in obj:
#     recipe_id = o.get('RECIPE_ID')
#     irdnt_sn = o.get('IRDNT_SN')
#     irdnt_nm = o.get('IRDNT_NM')

#     new_receipt = recipe_food.objects.create(recipe_id=recipe_id, irdnt_sn=irdnt_sn, irdnt_nm=irdnt_nm)
#     print(new_receipt)

# f = open('recipe_how.json', 'r')
# obj = simplejson.load(f)
# obj = obj.get('data')

# for o in obj:
#     recipe_id = o.get('RECIPE_ID')
#     cooking_no = o.get('COOKING_NO')
#     cooking_dc = o.get('COOKING_DC')
#     stre_step_image_url = o.get('STRE_STEP_IMAGE_URL')

#     recipe_how.objects.create(recipe_id=recipe_id, cooking_no=cooking_no, cooking_dc=cooking_dc, stre_step_image_url=stre_step_image_url)
import json
f = open('recipe_info.json', 'r')
obj = json.load(f)
print(len(obj))
obj = obj.get('data')
for o in obj:
    recipe_id = o.get('RECIPE_ID')
    recipe_nm_ko = o.get('RECIPE_NM_KO')
    sumry = o.get('SUMRY')
    nation_nm = o.get('NATION_NM')
    cooking_time = o.get('COOKING_TIME')
    calorie = o.get('CALORIE')
    level_nm = o.get('LEVEL_NM')
    img_url = o.get('IMG_URL')
    det_url = o.get('DET_URL')

    recipe_info.objects.create(recipe_id=recipe_id, recipe_nm_ko=recipe_nm_ko, sumry=sumry, nation_nm=nation_nm,
        cooking_time=cooking_time, calorie=calorie, level_nm=level_nm, img_url=img_url, det_url=det_url)
