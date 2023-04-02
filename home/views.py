from django.core.paginator import Paginator
from django.views.generic import TemplateView

from post.models import Post


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destaque'] = Post.publicados.post_destacado().first()
        post_list = Post.publicados.all().order_by('-publicado')
        paginator = Paginator(post_list, 5)
        page = self.request.GET.get('page')
        context['posts'] = paginator.get_page(page)
        return context
