# Generated by Django 4.2 on 2023-04-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=122)),
                ('Email', models.CharField(max_length=122)),
                ('Phone', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
