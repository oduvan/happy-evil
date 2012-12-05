from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from board.models import Post
from django.views.generic.edit import CreateView

class IndexView(ListView):
    template_name = 'index.html'
    model = Post

class RegistrationView(CreateView):
    template_name = 'registration/create.html'
    form_class = UserCreationForm

    def form_valid(self,form):
        user = form.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return HttpResponseRedirect(reverse('index'))