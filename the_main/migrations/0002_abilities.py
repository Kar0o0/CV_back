# Generated by Django 4.0.4 on 2022-06-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('experience', models.CharField(max_length=300, verbose_name='سابقه کار')),
                ('description', models.TextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'توانایی',
                'verbose_name_plural': 'توانایی ها',
            },
        ),
    ]
