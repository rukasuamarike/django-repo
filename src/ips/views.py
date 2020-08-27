from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
from .models import Ip
from .forms import IpForm, RawIpForm
# Create your views here.
def ip_create_view(request):
    form = RawIpForm()
    if request.method == "POST":
        form = RawIpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Ip.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, "ip/ip_create.html", context)

def dynamic_lookup_view(request,my_id):
    obj = Ip.objects.get(id=my_id)
    try:
        obj = Ip.objects.get(id=my_id)
    except Ip.DoesNotExist:
        raise Http404

    context = {
        "object":obj
    }
    return render(request,"ip/ip_details.html", context)
def ip_listview(request):
    queryset = Ip.objects.all
    context = {
        "object_list":queryset
    }
    return render(request,"ip/ip_list.html",context)
def ip_delete_view(request,id):
    obj = get_object_or_404(Ip,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object":obj
    }
    return render(request, "ip/ip_delete.html",context)

def ip_detail_view(request):
    obj = Ip.objects.get(id=1)
    context = {
        'object':obj
    }
    return render(request, "ip/ip_details.html" , context)