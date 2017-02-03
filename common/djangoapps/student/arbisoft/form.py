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
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'graduation_date': forms.DateInput(attrs={'class': 'form-control', "type": "date"}),
            'cgpa': forms.NumberInput(attrs={'class': 'form-control', "type": "number"}),
            'position_in_class': forms.TextInput(attrs={'class': 'form-control'}),
            'academic_projects': forms.Textarea(attrs={'class': 'form-control'}),
            'extra_curricular_activities': forms.Textarea(attrs={'class': 'form-control'}),
            'freelance_work': forms.Textarea(attrs={'class': 'form-control'}),
            'accomplishment': forms.Textarea(attrs={'class': 'form-control'}),
            'individuality_factor': forms.Textarea(attrs={'class': 'form-control'}),
            'ideal_organization': forms.Textarea(attrs={'class': 'form-control'}),
            'why_arbisoft': forms.Textarea(attrs={'class': 'form-control'}),
            'expected_salary': forms.Textarea(attrs={'class': 'form-control'}),
            'career_plan': forms.Textarea(attrs={'class': 'form-control'}),
            'references': forms.Textarea(attrs={'class': 'form-control'}),
            'other_studied_course': forms.TextInput(attrs={'class': 'form-control'}),
            'other_technology': forms.TextInput(attrs={'class': 'form-control'}),
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
                attrs={'style': 'list-style:none;'}
            )
        }


class CandidateExpertiseForm(forms.ModelForm):
    class Meta:
        model = CandidateExpertise
        fields = (
            'expertise',
            'rank'
        )
        labels = {
            'expertise': "Mark the courses you are an expert at scale of 1 to 5, where 5 being expert and 1 being the least expert"
        }
        widgets = {
            'expertise': forms.RadioSelect(
                attrs={'style': 'list-style:none;'}
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
                attrs={'style': 'list-style:none;'}
            )
        }
