# Generated by Django 4.1.1 on 2022-09-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
