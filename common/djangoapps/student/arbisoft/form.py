from django import forms
from student.models import (
    CandidateProfile,
    CandidateCourse,
    CandidateExpertise,
    CandidateTechnology
)
from student.arbisoft import constants as arbi_constants


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = (
            'graduation_date',
            'phone_number',
            'cgpa',
            'position_in_class',
            'academic_projects',
            'extra_curricular_activities',
            'freelance_work',
            'accomplishment',
            'individuality_factor',
            'ideal_organization',
            'why_arbisoft',
            'expected_salary',
            'career_plan',
            'references',
            'other_studied_course',
            'other_technology',
        )
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'input-block', 'required': 'true'}),
            'graduation_date': forms.DateInput(attrs={'class': 'input-block', "type": "date", 'required': 'true'}),
            'cgpa': forms.NumberInput(attrs={'class': 'input-block', "type": "number", 'required': 'true'}),
            'position_in_class': forms.TextInput(attrs={'class': 'input-block', 'required': 'true'}),
            'academic_projects': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                       'required': 'true'}),
            'extra_curricular_activities': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                                 'required': 'true'}),
            'freelance_work': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                    'required': 'true'}),
            'accomplishment': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                    'required': 'true'}),
            'individuality_factor': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                          'required': 'true'}),
            'ideal_organization': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                        'required': 'true'}),
            'why_arbisoft': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                  'required': 'true'}),
            'expected_salary': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true'}),
            'career_plan': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                 'required': 'true'}),
            'references': forms.Textarea(attrs={'class': 'input-block', "type": "textarea", "rows": 4,
                                                'required': 'true'}),
            'other_studied_course': forms.TextInput(attrs={'class': 'input-inline',
                                                           'style': 'display: inline; width: 30%'}),
            'other_technology': forms.TextInput(attrs={'class': 'input-inline',
                                                       'style': 'display: inline; width: 30%'}),
        }


class CandidateCourseForm(forms.ModelForm):
    class Meta:
        model = CandidateCourse
        fields = ('studied_course',)
        labels = {
            'studied_course': "Check mark the courses you studied"
        }
        widgets = {
            'studied_course': forms.CheckboxSelectMultiple(
                attrs={'class': 'input-inline checkbox'}
            )
        }


class CandidateExpertiseForm(forms.ModelForm):
    class Meta:
        model = CandidateExpertise
        fields = (
            'expertise',
            'rank'
        )
        widgets = {
            'expertise': forms.HiddenInput(),
            'rank': forms.RadioSelect(
                choices=arbi_constants.EXPERTISE_RANKING
            )
        }


class CandidateTechnologyForm(forms.ModelForm):
    class Meta:
        model = CandidateTechnology
        fields = ('technology',)
        labels = {
            'technology': "Mark the technology you'd like to work on/learn"
        }
        widgets = {
            'technology': forms.CheckboxSelectMultiple(
                attrs={'class': 'input-inline checkbox'}
            )
        }
