# Generated by Django 5.0.7 on 2024-07-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_citysearchcount_alter_searchhistory_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='ip_address',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
    ]