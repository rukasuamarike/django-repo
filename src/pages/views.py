from django.http import HttpResponse
from django.shortcuts import render
from .models import Log
from .forms import LogForm, RawLogForm
# Create your views here.
def home_view(request):
    form = RawLogForm()
    if request.method == "POST":
        form = RawLogForm(request.POST)
        if form.is_valid():
            Log.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request,"home.html",context)
        # HttpResponse("<h1>Home</h1>")

def hello_world(request,*args, **kwargs):

    return render(request,"hello.html",{})

def panel(request,*args, **kwargs):
    my_context = {
        'my_text':'this is about me',
        'my_num':123,
        'my_list':[1,2,3,4,5,6],
        'my_bool':True
    }
    return render(request,"panel.html",my_context)
def log(request):
    logs = Log.objects.all
    context = {
        "log_list": logs
    }
    return render(request,'logs.html',context)