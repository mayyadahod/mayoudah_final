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
    path('insulin-resistance/', views.insulin_resistance_index, name='insulin_resistance_index'),
    path('ir/what-is-it/', views.what_is_ir, name='what_is_ir'),
    path('ir/skin-signs/', views.ir_skin_signs, name='ir_skin_signs'),
    path('ir/homa-ir-test/', views.homa_ir_test, name='homa_ir_test'),
    path('ir/diet-plan/', views.ir_diet_plan, name='ir_diet_plan'),
    path('ir/exercise-guide/', views.ir_exercise_guide, name='ir_exercise_guide'),
    path('blood-pressure/', views.blood_pressure_index, name='blood_pressure_index'),
    path('bp/measure-right/', views.measure_bp_right, name='measure_bp_right'),
    path('bp/levels-chart/', views.bp_levels_chart, name='bp_levels_chart'),
    path('bp/dash-diet/', views.dash_diet, name='dash_diet'),
path('bp/salt-facts/', views.salt_and_bp, name='salt_and_bp'),
path('bp/emergency/', views.bp_emergency, name='bp_emergency'),
]