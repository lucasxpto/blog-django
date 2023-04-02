from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from stdimage import StdImageField
from dynamic_filenames import FilePattern

upload_to_pattern = FilePattern(
    filename_pattern='{model_name:.30}/{uuid:base32}{ext}')


class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publicado', destaque=False)

    def post_destacado(self):
        return super().get_queryset().filter(status='publicado', destaque=True)


class Post(models.Model):
    objects = models.Manager()
    publicados = PublicadosManager()

    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    corpo = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rascunho')
    criado = models.DateTimeField(auto_now_add=True)
    publicado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_autor')
    imagem = StdImageField('Imagem', upload_to=upload_to_pattern,
                           variations={'large': (700, 500), 'thumbnail': {'width': 300, 'height': 150, 'crop': True}},
                           delete_orphans=True, max_length=255)
    destaque = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.destaque:
            # Verificar se já existe um post em destaque
            destaque_existente = Post.objects.filter(destaque=True).exclude(pk=self.pk).first()

            # Se já existe um post em destaque, atualiza para destaque=False
            if destaque_existente:
                destaque_existente.destaque = False
                destaque_existente.save()

        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
