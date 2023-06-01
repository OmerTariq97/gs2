# Generated by Django 4.1.7 on 2023-04-14 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_singer_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='Singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sungby', to='api.singer'),
        ),
    ]