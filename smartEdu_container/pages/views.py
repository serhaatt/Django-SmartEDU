from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from courses.models import Course
from .forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from teachers.models import Teacher

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')
        context['total_course'] = Course.objects.filter(available=True).count()
        context['total_user'] = User.objects.all().count()
        context['total_teacher'] = Teacher.objects.all().count()
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(SuccessMessageMixin,FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'We received your message!'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def index(request):
#     return render(request,'index.html')

# def about(request):
#     return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')
