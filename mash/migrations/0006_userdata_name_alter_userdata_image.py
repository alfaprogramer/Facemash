# Generated by Django 4.0.3 on 2024-05-01 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mash', '0005_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='name',
            field=models.CharField(default='sexy', max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mash.image'),
        ),
    ]