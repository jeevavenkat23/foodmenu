from django.shortcuts import render,redirect
from app1.models import *
from app1.forms import RootForm


# Create your views here.
# def show (request):
#     return render(request,'app1/index.html')

def show_Root(request):
    data=Root.objects.all()
    c={'allroot':data}
    return render(request,'app1/index.html',c)


def fis(request):
    if request.method == 'POST':
        form = RootForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_root')
    else:
        form = RootForm()

    return render(request, 'app1/fis.html', {'form': form})

def home(request):
    return render(request,'home.html')
def update(request,sno):
    s=Root.objects.get(sno=sno)
    form=RootForm(instance=s)
    dic={'form':form}
    if request.method=="POST":
        form=RootForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect(show_Root)

    return render(request,'app1/update.html',dic)        