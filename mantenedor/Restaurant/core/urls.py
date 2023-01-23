from django.urls import path  
from .views import home,form_plato,form_mod_plato,form_del_plato,form_reserva,form_mod_reserva,\
    form_del_reserva,reserva,form_bodega,form_del_bodega,form_mod_bodega,bodega,inicio,logout,loogin,\
    registroUsuario,\
    menu,\
    form_pedido, cosina, form_mod_pedido, form_del_pedido, form_receta, form_mod_receta, form_del_receta, receta, mesa

# from django.contrib.auth import logout



urlpatterns =[
    path('menu',menu,name="menu"),
    path('registroUsuario',registroUsuario,name='registroUsuario'),
    path('login',loogin,name='login'),

    path('logout',logout,name="logout"),
    path('',inicio,name="inicio"),
    path('home',home,name="home"),
    path('form-plato',form_plato,name='form_plato'),
    path('form-mod-plato/<id>',form_mod_plato,name='form_mod_plato'),
    path('form-del-plato/<id>',form_del_plato,name='form_del_plato'),


    path('reserva',reserva,name="reserva"),
    path('form-reserva',form_reserva,name='form_reserva'),
    path('form-mod-reserva/<id>',form_mod_reserva,name='form_mod_reserva'),
    path('form-del-reserva/<id>',form_del_reserva,name='form_del_reserva'),

    path('bodega',bodega,name="bodega"),
    path('form-bodega',form_bodega,name='form_bodega'),
    path('form-mod-bodega/<id>',form_mod_bodega,name='form_mod_bodega'),
    path('form-del-bodega/<id>',form_del_bodega,name='form_del_bodega'),

    path('form-pedido',form_pedido,name='form_pedido'),

    path('cosina',cosina,name='cosina'),
    path('form-mod-pedido/<id>',form_mod_pedido,name='form_mod_pedido'),
    path('form-del-pedido/<id>',form_del_pedido,name='form_del_pedido'),

    path('receta',receta,name='receta'),
    path('form-receta',form_receta,name='form_receta'),
    path('form-mod-receta/<id>',form_mod_receta,name='form_mod_receta'),
    path('form-del-receta/<id>',form_del_receta,name='form_del_receta'),
    
    
    path('mesa',mesa,name='mesa'),
    
    
    ]