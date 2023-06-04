from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':43,'b':123,'c':345}
    return render(request,'conditions.html',d)
def looping(request):
    d={'name':'manu'}
    return render(request,'looping.html',d)