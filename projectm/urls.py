
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.EMP_CBV.as_view()),
    #path('apiall/',views.EMP_ALL.as_view()),
]
