from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'