# Generated by Django 4.2.6 on 2023-10-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='topics',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]
