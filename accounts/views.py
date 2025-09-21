from django.shortcuts import render

def login_view(request):
    error = None  # No mostramos nada por defecto

    if request.method == 'POST':
    
        error = 'Funcionalidad no implementada'

    return render(request, 'accounts/login.html', {'error': error})
