# Generated by Django 3.2.3 on 2021-05-19 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='pizzashop_logo/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pizzashop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
