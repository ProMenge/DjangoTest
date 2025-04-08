from django.views import generic
from blog.models import Post
from django.views.generic import ListView
# Create your views here.

class PostView(ListView): 
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'