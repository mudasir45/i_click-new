# Generated by Django 4.1.3 on 2023-01-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IclickMain', '0007_alter_projectdetails_disc'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_reviews',
            name='projectid',
            field=models.IntegerField(default=45),
        ),
        migrations.AddField(
            model_name='project_reviews',
            name='review',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project_reviews',
            name='revid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]