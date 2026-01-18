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
    path('diabetes/low-gi-foods/', views.low_gi_foods, name='low_gi_foods'),
    path('diabetes/bread-alternatives/', views.bread_alternatives, name='bread_alternatives'),
    path('diabetes/carb-counting/', views.carb_counting, name='carb_counting'),
    path('diabetes/hypo-rule/', views.hypo_rule, name='hypo_rule'),
    path('diabetes/foot-care/', views.foot_care, name='foot_care'),
    path('diabetes/complications-prevention/', views.kidney_eye_care, name='kidney_eye_care'),
    path('diabetes/insulin-guide/', views.insulin_guide, name='insulin_guide'),
    path('diabetes/technology/', views.diabetes_tech, name='diabetes_tech'),
]