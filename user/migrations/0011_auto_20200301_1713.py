# Generated by Django 2.0.1 on 2020-03-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200301_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardcomment',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
    ]