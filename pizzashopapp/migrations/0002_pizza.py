# Generated by Django 3.2.3 on 2021-05-24 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pizza_images/')),
                ('price', models.IntegerField(default=0)),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.pizzashop')),
            ],
        ),
    ]