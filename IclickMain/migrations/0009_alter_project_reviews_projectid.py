# Generated by Django 4.1.3 on 2023-01-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IclickMain', '0008_project_reviews_projectid_project_reviews_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_reviews',
            name='projectid',
            field=models.IntegerField(),
        ),
    ]
