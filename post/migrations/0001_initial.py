# Generated by Django 4.1.7 on 2023-04-02 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dynamic_filenames
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('corpo', models.TextField()),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunho', max_length=10)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('publicado', models.DateTimeField(auto_now=True)),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, max_length=255, upload_to=dynamic_filenames.FilePattern(filename_pattern='{model_name:.30}/{uuid:base32}{ext}'), variations={'large': (700, 500), 'thumbnail': {'crop': True, 'height': 150, 'width': 300}}, verbose_name='Imagem')),
                ('destaque', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_autor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]