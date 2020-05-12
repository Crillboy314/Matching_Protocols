from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class DemographicsPageOne(Page):
    form_model = 'player'
    form_fields = ['birthdate',
                   'gender',
                   'ethnicity',
                   'other_langs',
                   'langs_used_weekly']

class DemographicsPageTwo(Page):
    form_model = 'player'
    form_fields = ['nationality',
                   'birthplace',
                   'residence']

class DemographicsPageThree(Page):
    form_model = 'player'
    form_fields = ['bool_student',              # Are you a student?
                   'profession',                # What is your profession?
                   'education_level',           # What is your education level?
                   'phil_course_count']

class DemographicsPageFour(Page):
    form_model = 'player'
    form_fields = ['parents_edu_level',
                   'parents_income_level',
                   'religion',
                   'politics',
                   'civil_status']

page_sequence = [
    DemographicsPageOne,
    DemographicsPageTwo,
    DemographicsPageThree,
    DemographicsPageFour
]
