# Generated by Django 2.2.16 on 2022-06-30 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Категория произведения')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Напишите комментарий', verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Жанр произведения')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите ревью', verbose_name='Текст ревью')),
                ('score', models.PositiveSmallIntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
            ],
            options={
                'verbose_name': 'Ревью',
                'verbose_name_plural': 'Ревью',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=160, verbose_name='Наименование произведения')),
                ('year', models.IntegerField(db_index=True, verbose_name='Дата создания произведения')),
                ('description', models.TextField(blank=True, verbose_name='Описание произведения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='title', to='reviews.Category', verbose_name='Категория произведения')),
                ('genre', models.ManyToManyField(blank=True, null=True, related_name='title', to='reviews.Genre', verbose_name='Жанр произведения')),
            ],
            options={
                'ordering': ('year',),
            },
        ),
    ]
