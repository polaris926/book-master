# Generated by Django 2.0.1 on 2020-02-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_messageboard_like_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectboard',
            options={'verbose_name': '收藏/点赞留言', 'verbose_name_plural': '收藏/点赞留言'},
        ),
        migrations.AddField(
            model_name='collectboard',
            name='is_like',
            field=models.BooleanField(default=False, verbose_name='是否点赞'),
        ),
    ]