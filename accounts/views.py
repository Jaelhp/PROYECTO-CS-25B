from django.shortcuts import render
from django.contrib.auth.models import User, auth
def login_view(request):
    error = None # Por defecto, no hay error 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("Login exitoso")
            return render(request, 'accounts/home.html')
        else:
            error = "Credenciales invalidas"
            print(error)
            return render(request, 'accounts/login.html', {'error': error})
    else:
        return render(request, 'accounts/login.html', {'error': error})


def home_view(request):
    return render(request, 'accounts/home.html')