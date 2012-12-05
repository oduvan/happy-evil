from django.conf.urls import patterns,  url
from django.contrib.auth.decorators import login_required
from views import PostAddChoiceView, PostAddView

urlpatterns = patterns('',
    url(r'^add/$', login_required(PostAddChoiceView.as_view()), name='add_choice'),
    url(r'^add/(?P<type>\d+)/$', login_required(PostAddView.as_view()), name='add'),
)