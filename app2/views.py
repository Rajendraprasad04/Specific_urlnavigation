from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'Rajendra'}
    return render(request,'loop.html',d)
