# Generated by Django 4.1.5 on 2023-02-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_blog_status_alter_career_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_header',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='career_name',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
