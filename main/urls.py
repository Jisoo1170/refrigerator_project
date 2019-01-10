from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'main/(?P<user_id>\d+)$', index, name="index"),

    url(r'(?P<user_id>\d+)/food/count/(?P<food_id>\d+)$', food_count, name="food_count"),
    url(r'(?P<user_id>\d+)/food/delete/(?P<food_id>\d+)$', food_delete, name="food_delete"),
    url(r'(?P<user_id>\d+)/food/added', food_added, name="food_added"),
    url(r'(?P<user_id>\d+)/food/expiary_date/(?P<food_id>\d+)$', food_expiary, name="food_expiray"),
    url(r'(?P<user_id>\d+)/food/created_at/(?P<food_id>\d+)$', food_created, name="food_created"),
    url(r'(?P<user_id>\d+)/food/unit/(?P<food_id>\d+)$', food_unit, name="food_unit"),
    
    url(r'main/(?P<user_id>\d+)/food_deep', food_deep, name="food_deep"),

    url(r'(?P<user_id>\d+)/deep/add/(?P<food_id>\d+)$',deep_add, name="deep_add"),
    url(r'(?P<user_id>\d+)/deep/delete/(?P<food_id>\d+)$', deep_delete, name="deep_delete")
    
    # url(r'(?P<user_id>\d+)/deep/receive/$', deep_receive, name="deep_receive")
]