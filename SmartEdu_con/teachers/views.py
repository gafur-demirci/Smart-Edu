from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teacher
from courses.models import Course

# Create your views here.
class TeacherListView(ListView):
    model = Teacher
    # paginate_by = 1
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    # queryset = Teacher.objects.all()
    # queryset = Teacher.objects.all()[:1]

    # def get_queryset(self):
    #     return Teacher.objects.all()[:2]

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available = True, teacher = self.kwargs['pk'])
        return context