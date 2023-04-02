from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from post.models import Post


# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('titulo', 'autor', 'status', 'publicado', 'destaque')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    search_fields = ('titulo', 'corpo')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    ordering = ('-destaque', 'status', 'publicado')
    summernote_fields = ('corpo',)
