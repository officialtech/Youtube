from django.shortcuts import render, HttpResponse, redirect
from .forms import AtricleModelForm

def create_data(request):
    if request.method == 'POST':
        form = AtricleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
        else:
            form = AtricleModelForm()
    return render(request, 'blog.html', {'form': AtricleModelForm()})


def success(request):
    return HttpResponse('<h1>Successfully Inserted</h1>')