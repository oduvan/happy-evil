from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from board.models import Post


class PostAddChoiceView(TemplateView):
    template_name = 'board/post_add_choice.html'

    def get_context_data(self,**kwargs):
        context = super(PostAddChoiceView,self).get_context_data(**kwargs)
        context.update({'types':Post.TYPE_CHOICES})
        return context


class PostAddView(CreateView):
    template_name = 'board/post_add.html'
    def get_form_class(self):
        try:
            return Post.TYPE_FORMS[int(self.kwargs['type'])]
        except KeyError:
            raise Http404

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.type = int(self.kwargs['type'])
        post.save()
        return HttpResponseRedirect(reverse('index'))