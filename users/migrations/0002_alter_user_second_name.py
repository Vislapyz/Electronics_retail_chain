# Generated by Django 5.1.1 on 2024-10-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="second_name",
            field=models.CharField(
                blank=True,
                help_text="Напишите Вашу фамилию",
                max_length=50,
                null=True,
                verbose_name="Фамилия",
            ),
        ),
    ]
