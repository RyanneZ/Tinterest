# Generated by Django 4.0.5 on 2022-06-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='picture',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
