# Generated by Django 3.2.5 on 2021-07-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_testfieldsmoels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testfieldsmoels',
            name='error_messages',
            field=models.CharField(error_messages={'blank': 'INVALID!!11', 'null': 'NULL11!'}, max_length=500),
        ),
    ]