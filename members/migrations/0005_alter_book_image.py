# Generated by Django 4.0.4 on 2022-04-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='static/images'),
        ),
    ]
