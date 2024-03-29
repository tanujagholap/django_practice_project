from django.shortcuts import render, redirect
from .forms import *
from .models import Create
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_url')
def create_view(request):
    template_name = 'app1/create.html'
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, template_name, context={'form': form})


@login_required(login_url='login_url')
def show_view(request):
    objs = Create.objects.all()
    context = {'objs': objs}
    return render(request, "app1/show.html", context)


@login_required(login_url='login_url')
def update_view(request, pk):
    template_name = 'app1/create.html'
    obj = Create.objects.get(id=pk)
    form = CreateForm(instance=obj)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, template_name, context={'form': form})


@login_required(login_url='login_url')
def delete_view(request, pk):
    template_name = 'app1/confirm.html'
    obj = Create.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, template_name)

