from django.urls import path
from .views import home,form_plato,form_mod_plato,form_del_plato

urlpatterns =[
    path('',home,name="home"),
    path('form-plato',form_plato,name='form_plato'),
    path('form-mod-plato/<id>',form_mod_plato,name='form_mod_plato'),
    path('form-del-plato/<id>',form_del_plato,name='form_del_plato'),
]
