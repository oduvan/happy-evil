from django.views.generic.list import ListView
from board.models import Post

class IndexView(ListView):
    template_name = 'index.html'
    model = Post