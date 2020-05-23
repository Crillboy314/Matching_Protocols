# Generated by Django 2.2.4 on 2020-03-10 16:14

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey2', '0005_player_ethnicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='parents_income_level',
            field=otree.db.models.StringField(choices=[('400 o menos', '400 o menos'), ('401 a 800', '401 a 800'), ('801 a 1200', '801 a 1200'), ('1201 a 1600', '1201 a 1600'), ('1601 a 2000', '1601 a 2000'), ('2001 o más', '2001 o más')], max_length=10000, null=True, verbose_name='Hasta donde sabe, ¿cuál es el nivel de ingreso mensual conjunto de sus padres (en dólares)?'),
        ),
    ]