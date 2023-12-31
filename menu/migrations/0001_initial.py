# Generated by Django 4.2.4 on 2023-08-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(default='', max_length=200)),
                ('describe', models.TextField(default='', max_length=1000)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='menu_images/')),
                ('state', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Menu',
            },
        ),
    ]
