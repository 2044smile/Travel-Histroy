from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Border
from .forms import BorderForm

def index(request):
    return render(request, 'border/index.html')

def border_search(request):
    br = Border.objects.all()

    b = request.GET.get('b','')

    if b:
        br = br.filter(title__icontains=b)

    return render(request, 'border/border_search.html', { 'border_search':br , 'b':b})


class borderListView(ListView):
    model = Border
    template_name = 'border/border.html'
    context_object_name = 'border'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(borderListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


# def border_new(request):
#     if request.method == "POST":
#         form = BorderForm(request.POST) # form 으로 넘겨받은 데이터를 받는다.
#         if form.is_valid(): # form 의 데이터가 올바른지 1차적으로 확인
#             post = form.save(commit=False)
#             post.save() # db에 저장
#             return redirect('/border')
#         return HttpResponse('실패')
#     elif request.method == 'GET':
#         form = BorderForm()
#         return render(request, 'border/border_new.html', {'form': form})
#     else:
#         pass

class BorderCreateView(CreateView):
    model = Border
    fields = ['title','author','text','photo']
    success_url = 'border/border.html'
    template_name = 'border/border_new.html'

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

def test(request):
    return render(request, 'test.html')