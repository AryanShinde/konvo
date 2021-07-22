from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.
def homepage(request):
    return render(request, 'main/home.html')

def logout_view(request):
    logout(request)
    return redirect('home')