# Generated by Django 5.0.3 on 2024-03-26 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0003_autor_livro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={'verbose_name': 'Livro', 'verbose_name_plural': 'Livros'},
        ),
    ]
