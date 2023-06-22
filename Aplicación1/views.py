from django.shortcuts import render

# Create your views here.
def HolaMundo(request):
    return render(request,'HolaMundo.html',{})