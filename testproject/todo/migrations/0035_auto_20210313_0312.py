# Generated by Django 3.1.7 on 2021-03-12 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0034_auto_20210313_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanclub',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='todo.user'),
        ),
    ]
