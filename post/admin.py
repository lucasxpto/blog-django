from django.contrib import admin

from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'status', 'publicado', 'destaque')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    search_fields = ('titulo', 'corpo')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    ordering = ('status', 'publicado')
