from django.shortcuts import render

def login_view(request):
    name_from_form = None
    if request.method == "POST":
        # هنا نستقبل "الاسم" الذي كتبه المستخدم في خانة my_name
        name_from_form = request.POST.get('my_name')
    
    return render(request, 'accounts/login.html', {'user_name': name_from_form})