# Generated by Django 4.1.3 on 2023-01-22 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IclickMain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('stdid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('disc', models.CharField(max_length=500)),
                ('supervisor_name', models.CharField(max_length=50)),
                ('supervisor_qualif', models.CharField(max_length=50)),
                ('member1', models.CharField(max_length=50)),
                ('member2', models.CharField(max_length=50)),
                ('member3', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
            ],
        ),
    ]
