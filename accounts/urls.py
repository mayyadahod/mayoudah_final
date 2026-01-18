from django.urls import path
from . import views

urlpatterns = [
    # الرابط الرئيسي يشير الآن إلى login_view
    path('', views.login_view, name='login'), 
    
    # رابط فهرس السكري
    path('diabetes/', views.diabetes_index, name='diabetes_index'),
    path('diabetes/types/', views.diabetes_types, name='diabetes_types'),
    path('diabetes/levels/', views.diabetes_levels, name='diabetes_levels'),
    path('diabetes/hba1c/', views.hba1c_guide, name='hba1c_guide'),
]