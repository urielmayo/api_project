# Generated by Django 4.1.1 on 2022-11-08 20:29

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
            name='AccesoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Accesory Category',
                'verbose_name_plural': 'Accesory Categories',
            },
        ),
        migrations.CreateModel(
            name='AccesoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Accesory Model',
                'verbose_name_plural': 'Accesory Models',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Dealer',
                'verbose_name_plural': 'Dealers',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dealer')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('in_stock', models.BooleanField()),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.color')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='api.dealer')),
                ('posts', models.ManyToManyField(to='api.post')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dealer')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lead',
                'verbose_name_plural': 'Leads',
            },
        ),
        migrations.CreateModel(
            name='Accesory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('in_stock', models.BooleanField()),
                ('year_of_compatibility', models.PositiveSmallIntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.accesorycategory')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accesories', to='api.dealer')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.accesorymodel')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.vehicle')),
            ],
            options={
                'verbose_name': 'Accesory',
                'verbose_name_plural': 'Accesories',
            },
        ),
    ]
