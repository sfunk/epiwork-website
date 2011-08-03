from django import forms

class SurveyXmlForm(forms.Form):
    surveyxml = forms.CharField(required=True)

class SurveyTranslationAddForm(forms.Form):
    language = forms.CharField(label="Language code", max_length=3, required=True)
