# Generated by Django 3.1.7 on 2021-03-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openseaitem', '0002_auto_20210315_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='openseaitem',
            name='image',
            field=models.ImageField(default='xxx', upload_to=''),
            preserve_default=False,
        ),
    ]