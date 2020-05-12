from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'survey2'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    birthdate = models.StringField(
        label='¿Cuál es su edad? Por favor, use el formato años-meses (por ejemplo, 20-4).',
        widget=widgets.TextInput())

    gender = models.StringField(
        choices=['Masculino', 'Femenino', 'Otro'],
        label='¿Con que género se identifica?',
        widget=widgets.RadioSelect())

    ethnicity = models.StringField(
        choices=['Afro-Ecuatoriana', 'Mestiza', 'Asiatica', 'Indígena', 'Blanca', 'Prefiero no decir'],
        label='¿Con que etnia se identifica?',
        widget=widgets.RadioSelect())

    other_langs = models.StringField(
        label='¿Qué idiomas habla bien?',
        widget=widgets.TextInput())

    langs_used_weekly = models.StringField(
        label='¿Qué idiomas (incluyendo sus idiomas maternos y el Castellano) usa al menos una vez a la semana?',
        widget=widgets.TextInput())

    nationality = models.StringField(
        label='¿Cuál es su nacionalidad?',
        widget=widgets.TextInput())

    birthplace = models.StringField(
        label='¿Donde nació usted? (Ciudad, Provincia/Estado, País)',
        widget=widgets.TextInput())

    residence = models.StringField(
        label='¿En qué país reside?',
        widget=widgets.TextInput())

    bool_student = models.StringField(
        choices=['Sí','No'],
        label='¿Es usted estudiante?',
        widget=widgets.RadioSelect())

    profession = models.StringField(
        label='Si usted no es estudiante, ¿cuál es su profesión? Si es estudiante, escriba \'NA\' en la caja',
        widget=widgets.TextInput())

    education_level = models.StringField(
        choices=['Ninguno','Educación Inicial (Jardín)','Educación General Básica (Primaria)','Bachillerato (Secundaria)',
        'Algo de estudios universitarios (actualmente o pasado)','Instituto Técnico','Licenciatura o equivalente',
        'Maestría o equivalente','Doctorado'],
        label='¿Cuál es su nivel educativo?',
        widget=widgets.RadioSelect())

    phil_course_count = models.StringField(
        choices=['Nunca he tomado un curso de Economía',
                 'He tomado 1 o 2 cursos de Economía',
                 'He tomado más de 2 cursos de Economía, pero la Economía no es la disciplina en la que fui formado.',
                 'Estudio Economía y estoy por obtener una licenciatura en Economía.',
                 'Estudio Economía y tengo una licenciatura en Economía.',
                 'Estoy estudiando un posgrado en Economía.',
                 'Tengo un doctorado en Economía'],
        label='¿Cuántos cursos de Economía recibió durante sus estudios?',
        widget=widgets.RadioSelect())

    parents_income_level = models.StringField(
        choices=['400 o menos','401 a 800','801 a 1200','1201 a 1600',
        '1601 a 2000','2001 o más'],
        label='Hasta donde sabe, ¿cuál es el nivel de ingreso mensual conjunto de sus padres (en dólares)?',
        widget=widgets.RadioSelect())

    parents_edu_level = models.StringField(
        choices=['Ninguno','Educación Inicial (Jardín)','Educación General Básica (Primaria)','Bachillerato (Secundaria)',
        'Algunos estudios universitarios','Instituto Técnico','Licenciatura o equivalente',
        'Maestría o equivalente','Doctorado'],
        label='Hasta donde sabe, ¿cuál es el nivel educativo más alto que alcanzó alguno de sus padres (el que tenga más estudios)?',
        widget=widgets.RadioSelect())

    religion = models.StringField(
        choices=['Ninguna','Católica','Evangelista','Protestante (distinto de evangelista)',
                 'Mormona','Cristiana ortodoxa','Cristiana (otra)','Judía','Musulmana',
                 'Hinduísta','Budista','Sintoísta','Confucionista','Daoista','Jainista',
                 'Sikh','Atea o agnóstica','Otra'],
        label='¿Cuál es su afiliación religiosa actual? ',
        widget=widgets.RadioSelect())

    politics = models.StringField(
        choices=['Muy de izquierda','Izquierda','Centro-izquierda','Centro','Centro-derecha','Derecha','Muy de derecha'],
        label='En términos generales, ¿cuál es su inclinación política?',
        widget=widgets.RadioSelect())

    civil_status = models.StringField(
        choices=['Soltero','Casado','Divorciado','Viudo','Prefiero no decir'],
        label='¿Cuál es su estado civil?',
        widget=widgets.RadioSelect())
