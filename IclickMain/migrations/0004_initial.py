# Generated by Django 4.1.3 on 2023-01-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('IclickMain', '0003_delete_projectdetails_delete_userlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('stdid', models.IntegerField(primary_key=True, serialize=False)),
                ('project_id', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
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
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
