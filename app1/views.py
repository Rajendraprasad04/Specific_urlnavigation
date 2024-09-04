from django.shortcuts import render

# Create your views here.
def cond(request):
    d={'a':5,'b':7}
    return render(request,'cond.html',d)


