# Generated by Django 3.2 on 2022-12-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('user', 'Аутентифицированный пользователь'), ('moderator', 'Модератор')], default='user', max_length=20, verbose_name='Роль'),
        ),
    ]
