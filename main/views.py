from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            if user.is_superuser or user.is_staff:
                return redirect('/admin')
            
            if user.groups.filter(name='Professor').exists():
                return redirect('prof:index')
            
            return redirect('student:index')
            

        return render(request, 'main/login.html', { 'wrong_cred_message': 'Error' })

    return render(request, 'main/login.html')


def logoutUser(request):
    logout(request)
    return render(request, 'main/logout.html',{ 'logout_message': 'Logged out Successfully' })