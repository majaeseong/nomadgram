# Generated by Django 2.0.9 on 2018-12-21 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181220_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
