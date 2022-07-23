# Generated by Django 3.2.14 on 2022-07-23 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xword_data', '0003_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clue_text', models.CharField(max_length=512)),
                ('theme', models.BooleanField(default=False)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xword_data.entry')),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xword_data.puzzle')),
            ],
        ),
    ]