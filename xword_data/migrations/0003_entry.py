# Generated by Django 3.2.14 on 2022-07-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xword_data', '0002_alter_puzzle_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
