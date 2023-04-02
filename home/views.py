from django.views.generic import TemplateView

from post.models import Post


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destaque'] = Post.publicados.post_destacado().first()
        context['posts'] = Post.publicados.all().order_by('-publicado')
        return context
