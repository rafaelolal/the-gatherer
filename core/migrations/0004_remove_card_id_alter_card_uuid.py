# Generated by Django 5.1.7 on 2025-03-25 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_card_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='id',
        ),
        migrations.AlterField(
            model_name='card',
            name='uuid',
            field=models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
