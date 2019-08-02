from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Border
from .forms import BorderForm

def index(request):
    return render(request, 'border/index.html')

def border(request):
    borders = Border.objects.all()

    paginator = Paginator(borders, 10) # page 10개 제한

    page = request.GET.get('page')  # ?page=1

    try:
        borders = paginator.page(page)
    except PageNotAnInteger:
        borders = paginator.page(1)
    except EmptyPage:
        borders = paginator.page(paginator.num_pages)

    return render(request, 'border/border.html', {'border':borders})




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