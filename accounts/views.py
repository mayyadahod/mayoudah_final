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
