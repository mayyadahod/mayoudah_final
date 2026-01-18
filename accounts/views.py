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