from django.shortcuts import render

def home(request):
    return render(request, 'thirdauth/home.html',
                    {'request': request, 'user': request.user})
