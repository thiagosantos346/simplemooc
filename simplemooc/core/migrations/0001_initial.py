# Generated by Django 2.2.3 on 2019-07-14 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de Início')),
                ('image', models.ImageField(upload_to='courses/image', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('upload_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em ')),
            ],
        ),
    ]
