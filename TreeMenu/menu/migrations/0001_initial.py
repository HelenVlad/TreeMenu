# Generated by Django 5.0.4 on 2024-04-10 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_item', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('named_url', models.CharField(blank=True, max_length=255, null=True)),
                ('higher_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lower_level', to='menu.menuitems')),
            ],
        ),
    ]
