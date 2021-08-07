from django.urls import path
from django.urls.resolvers import URLPattern
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
     path('category/<slug:category_name_slug>/', 
        views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('statistics/', views.statistics, name='statistics'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('the_fast_and_the_furious/', views.the_fast_and_the_furious, name='the_fast_and_the_furious'),
    path('the_expendables/', views.the_expendables, name='the_expendables'),
    path('deadpool/', views.deadpool, name='deadpool'),
    path('hangover/', views.hangover, name='hangover'),
    path('home_alone/', views.home_alone, name='home_alone'),
    path('minions/', views.minions, name='minions'),
    path('coco/', views.coco, name='coco'),
    path('titanic/', views.titanic, name='titanic'),
    path('black_panther/', views.black_panther, name='black_panther'),
    path('transformers/', views.transformers, name='transformers'),
    path('back_to_the_future/', views.back_to_the_future, name='back_to_the_future'),
    path('profile/',views.user_profile, name = "profile"),
    path('deleteuser/',views.delete_user, name = "deleteuser"),
]