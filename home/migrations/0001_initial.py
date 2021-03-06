# Generated by Django 4.0.3 on 2022-04-04 15:30

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
                ('firstname', models.CharField(max_length=61)),
                ('lastname', models.CharField(max_length=61)),
                ('contact_num', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
