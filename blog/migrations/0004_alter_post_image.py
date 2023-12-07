# Generated by Django 4.2.6 on 2023-10-09 21:08

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=blog.models.default_post_image, null=True, upload_to='post_images/'),
        ),
    ]