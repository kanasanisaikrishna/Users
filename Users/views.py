from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm

def Home(request):
    return render(request, 'home.html')

def Hello(request):
    return HttpResponse ("HELLO WORLD")

def Users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def User_details(request):
    user = None
    
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                pass
    
    return render(request, 'user_details.html', {'user': user})

def Add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_list')  # Redirect to the user list page after successful form submission
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})

