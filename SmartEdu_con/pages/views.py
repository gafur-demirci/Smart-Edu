# from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course

# Class Based View (TemplateView) 
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available = True).order_by('-date')[:3]
        context['total_course'] = Course.objects.filter(available = True).count()
        return context
    
class AboutView(TemplateView):
    template_name = 'about.html'
class ContactView(TemplateView):
    template_name = 'contact.html'
    
""" 
from django.http import HttpResponse

# Function Based Views
# Index View
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Index Sayfasi</h1>")

# About View
def about(request):
    return render(request, 'about.html')

# Contact View
def contact(request):
    return render(request, 'contact.html')

"""