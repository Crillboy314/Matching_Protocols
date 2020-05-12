# Generated by Django 2.2.4 on 2020-03-09 05:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('incomplete_mean', '0002_player_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='birthdate',
            field=otree.db.models.StringField(choices=[('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001')], max_length=10000, null=True, verbose_name='¿En que año naciste ?'),
        ),
    ]
