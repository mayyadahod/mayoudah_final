from django.shortcuts import render

def login_view(request):
    name_from_form = None
    if request.method == "POST":
        # هنا نستقبل "الاسم" الذي كتبه المستخدم في خانة my_name
        name_from_form = request.POST.get('my_name')
    
    return render(request, 'accounts/login.html', {'user_name': name_from_form})
def diabetes_index(request):
    return render(request, 'accounts/diabetes.html')

def diabetes_types(request):
    return render(request, 'accounts/articles/diabetes_types.html')
def diabetes_levels(request):
    return render(request, 'accounts/articles/diabetes_levels.html')

def hba1c_guide(request):
    return render(request, 'accounts/articles/hba1c_guide.html')

def low_gi_foods(request):
    return render(request, 'accounts/articles/low_gi_foods.html')
def bread_alternatives(request):
    return render(request, 'accounts/articles/bread_alternatives.html')
def carb_counting(request):
    return render(request, 'accounts/articles/carb_counting.html')
def hypo_rule(request):
    return render(request, 'accounts/articles/hypo_rule.html')

def foot_care(request):
    return render(request, 'accounts/articles/foot_care.html')

def kidney_eye_care(request):
    return render(request, 'accounts/articles/kidney_eye_care.html')
def insulin_guide(request):
    return render(request, 'accounts/articles/insulin_guide.html')

def diabetes_tech(request):
    return render(request, 'accounts/articles/diabetes_tech.html')
def insulin_resistance_index(request):
    return render(request, 'accounts/insulin_resistance.html')

def what_is_ir(request):
    return render(request, 'accounts/articles/what_is_ir.html')

def ir_skin_signs(request):
    return render(request, 'accounts/articles/ir_skin_signs.html')

def homa_ir_test(request):
    return render(request, 'accounts/articles/homa_ir_test.html')
def ir_diet_plan(request):
    return render(request, 'accounts/articles/ir_diet_plan.html')

def ir_exercise_guide(request):
    return render(request, 'accounts/articles/ir_exercise_guide.html')
def blood_pressure_index(request):
    return render(request, 'accounts/blood_pressure.html')
def measure_bp_right(request):
    return render(request, 'accounts/articles/measure_bp_right.html')

def bp_levels_chart(request):
    return render(request, 'accounts/articles/bp_levels_chart.html')
def dash_diet(request):
    return render(request, 'accounts/articles/dash_diet.html')

def salt_and_bp(request):
    return render(request, 'accounts/articles/salt_and_bp.html')

def bp_emergency(request):
    return render(request, 'accounts/articles/bp_emergency.html')
