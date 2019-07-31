from django.shortcuts import render
from django.http import HttpResponse
from datetime import timezone
from django.shortcuts import redirect
from .models import Border
from .forms import BorderForm
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'border/index.html')

def border(request):
    br = Border.objects.all()
    context = {'title':br}

    return render(request, 'border/border.html', context)

def border_new(request):
    if request.method == "POST":
        form = BorderForm(request.POST) # form 으로 넘겨받은 데이터를 받는다.
        if form.is_valid(): # form 의 데이터가 올바른지 1차적으로 확인
            post = form.save(commit=False)
            post.save() # db에 저장
            return redirect('/border')
        return HttpResponse('fail')
    elif request.method == 'GET':
        form = BorderForm()
        return render(request, 'border/border_new.html', {'form': form})
    else:
        pass

def writing(request):
    return render(request, 'border/photo.html')

class BorderDeleteView(DeleteView):
    model = Border
    success_url = reverse_lazy('border')

class BorderUpdateView(UpdateView):
    model = Border
    fields = ['title', 'author','text']
    template_name_suffix = '_modify'
    success_url = reverse_lazy('border')

class BorderDetailView(DetailView):
    model = Border
