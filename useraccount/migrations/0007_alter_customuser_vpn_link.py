# Generated by Django 5.0.7 on 2024-07-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0006_alter_customuser_fragment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='vpn_link',
            field=models.TextField(blank=True),
        ),
    ]
