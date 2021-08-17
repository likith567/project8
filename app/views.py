from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'likith.html',context={'name':'likith','age':22})

def hello(request):
    return render(request,'nani.html',context={'name':'nani','age':23})