# Generated by Django 2.2.4 on 2020-03-10 15:35

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey2', '0003_auto_20200310_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='civil_status',
            field=otree.db.models.StringField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viudo', 'Viudo'), ('Prefiero no decir', 'Prefiero no decir')], max_length=10000, null=True, verbose_name='¿Cuál es su estado civil?'),
        ),
    ]
