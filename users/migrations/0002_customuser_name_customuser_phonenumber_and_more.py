# Generated by Django 5.1.2 on 2024-10-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='phoneNumber',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
