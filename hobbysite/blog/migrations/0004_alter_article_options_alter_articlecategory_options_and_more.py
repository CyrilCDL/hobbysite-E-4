# Generated by Django 5.0.3 on 2024-03-20 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.articlecategory'),
        ),
    ]
