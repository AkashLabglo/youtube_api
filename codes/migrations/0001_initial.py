# Generated by Django 4.1.2 on 2022-12-14 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, null=True)),
                ('video', models.FileField(null=True, upload_to='media')),
                ('discretion', models.TextField(null=True)),
                ('likes_count', models.IntegerField(default=0)),
                ('comments_count', models.IntegerField(default=0)),
                ('is_public', models.BooleanField(default=False, help_text='0-Public, 1-Private')),
                ('monitaion', models.BooleanField(default=False, help_text='0-Off, 1-On')),
                ('is_adults', models.IntegerField(default=0, help_text='(0-All), (1-adults), (2-Kids)')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codes.category')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codes.video_upload')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codes.video_upload')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(max_length=500, null=True)),
                ('is_public', models.BooleanField(default=False, help_text='0-Public, 1-Private')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='codes.video_upload')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]