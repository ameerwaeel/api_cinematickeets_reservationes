"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register('guests',views.viewsets_guest)
router.register('movies',views.viewsets_movie)
router.register('reservationes',views.viewsets_reservation)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/jsonresponsenomodel/',views.no_rest_no_model),
    path('django/jsonresponsefrommodel/',views.no_rset_from_model),
    path('rest/fbv_list/',views.fbv_list),
    path('rest/fbv_pk/<int:pk>',views.fbv_pk),
    path('rest/cbv_list/',views.cbv_list.as_view()),
    path('rest/cbv_pk/<int:pk>/',views.cbv_pk.as_view()),
    path('rest/mixins_list/',views.mixins_list.as_view()),
    path('rest/mixins_pk/<int:pk>/',views.mixins_pk.as_view()),
    path('rest/generics_list/',views.generics_list.as_view()),
    path('rest/generics_pk/<int:pk>/',views.generics_pk.as_view()),
    path('rest/viewsets/',include(router.urls)),
    path('fbv/findmovie/',views.find_movie),
    path('fbv/new_reservation/',views.new_reservation),
    path('api_auth',include('rest_framework.urls')),
    path('api_token_auth',obtain_auth_token),
    path('rest/generics/post_pk/<int:pk>/',views.post_pk.as_view()),




    

    

    

    
]
