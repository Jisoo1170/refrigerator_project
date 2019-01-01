from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'main/(?P<user_id>\d+)$', index, name="index"),

    url(r'food/count/(?P<food_id>\d+)$', food_count, name="food_count"),
    # url(r'food/delete/(?P<food_id>\d+)$', food_delete, name="food_delete"),
    # url(r'(?P<user_id>\d+)/food/added/$', food_added, name="food_added"),
    # url(r'(?P<user_id>\d+)/food/expiary_date/(?P<food_id>\d+)$', food_expiary, name="food_expiray"),
    # url(r'(?P<user_id>\d+)/food/created_at/(?P<food_id>\d+)$', food_created, name="food_created"),

    # url(r'main/foods_deep/(?P<user_id>\d+)$', deep, name="deep"),
    # url(r'(?P<user_id>\d+)/deep/add/(?P<food_id>\d+)$',deep_add, name="deep_add"),
    # url(r'(?P<user_id>\d+)/deep/delete/(?P<food_id>\d+)$', deep_delete, name="deep_delete"),  
]