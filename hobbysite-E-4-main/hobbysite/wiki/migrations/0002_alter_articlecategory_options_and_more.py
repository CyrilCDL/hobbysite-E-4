# Generated by Django 5.0.3 on 2024-03-20 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['-name']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='title',
        ),
    ]
