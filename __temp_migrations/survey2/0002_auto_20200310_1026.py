# Generated by Django 2.2.4 on 2020-03-10 15:26

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='bool_country',
        ),
        migrations.RemoveField(
            model_name='player',
            name='dialect',
        ),
        migrations.RemoveField(
            model_name='player',
            name='edu_countries',
        ),
        migrations.RemoveField(
            model_name='player',
            name='edu_langs',
        ),
        migrations.RemoveField(
            model_name='player',
            name='maternal_lang',
        ),
        migrations.RemoveField(
            model_name='player',
            name='other_countries',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rel_freq',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rel_import',
        ),
        migrations.AlterField(
            model_name='player',
            name='birthdate',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='¿Cuál es su edad? Por favor, use el formato años-meses (por ejemplo, 20-4).'),
        ),
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=otree.db.models.StringField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=10000, null=True, verbose_name='¿Con que género se identifica?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='phil_course_count',
            field=otree.db.models.StringField(choices=[('Nunca he tomado un curso de Economía', 'Nunca he tomado un curso de Economía'), ('He tomado 1 o 2 cursos de Economía', 'He tomado 1 o 2 cursos de Economía'), ('He tomado más de 2 cursos de Economía, pero la Economía no es la disciplina en la que fui formado.', 'He tomado más de 2 cursos de Economía, pero la Economía no es la disciplina en la que fui formado.'), ('Estudio Economía y estoy por obtener una licenciatura en Economía.', 'Estudio Economía y estoy por obtener una licenciatura en Economía.'), ('Estudio Economía y tengo una licenciatura en Economía.', 'Estudio Economía y tengo una licenciatura en Economía.'), ('Estoy estudiando un posgrado en Economía.', 'Estoy estudiando un posgrado en Economía.'), ('Tengo un doctorado en Economía', 'Tengo un doctorado en Economía')], max_length=10000, null=True, verbose_name='¿Cuántos cursos de Economía recibió durante sus estudios?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='religion',
            field=otree.db.models.StringField(choices=[('Ninguna', 'Ninguna'), ('Católica', 'Católica'), ('Evangelista', 'Evangelista'), ('Protestante (distinto de evangelista)', 'Protestante (distinto de evangelista)'), ('Mormona', 'Mormona'), ('Cristiana ortodoxa', 'Cristiana ortodoxa'), ('Cristiana (otra)', 'Cristiana (otra)'), ('Judía', 'Judía'), ('Musulmana', 'Musulmana'), ('Hinduísta', 'Hinduísta'), ('Budista', 'Budista'), ('Sintoísta', 'Sintoísta'), ('Confucionista', 'Confucionista'), ('Daoista', 'Daoista'), ('Jainista', 'Jainista'), ('Sikh', 'Sikh'), ('Atea o agnóstica', 'Atea o agnóstica'), ('Otra', 'Otra')], max_length=10000, null=True, verbose_name='¿Cuál es su afiliación religiosa actual? '),
        ),
    ]