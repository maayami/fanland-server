# Generated by Django 3.1.7 on 2021-03-12 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0035_auto_20210313_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='author_image',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='chat',
            name='author_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='chat',
            name='chatroom_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='todo.fanclub'),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='todo.user'),
        ),
    ]
