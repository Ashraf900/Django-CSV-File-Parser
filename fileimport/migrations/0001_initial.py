# Generated by Django 4.1 on 2022-08-24 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_year', models.CharField(max_length=400)),
                ('level', models.CharField(max_length=10)),
                ('question', models.CharField(max_length=2000)),
                ('option1', models.CharField(max_length=500)),
                ('option2', models.CharField(max_length=500)),
                ('option3', models.CharField(max_length=500)),
                ('option4', models.CharField(max_length=500)),
                ('explanation', models.CharField(max_length=1000)),
                ('answer', models.IntegerField()),
            ],
        ),
    ]
