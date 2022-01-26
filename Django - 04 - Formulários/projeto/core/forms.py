from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class Formulario(forms.Form):
  name = forms.CharField(max_length= 40, min_length=5)
  email = forms.EmailField(max_length=40, min_length=5)
  password = forms.CharField(widget=forms.PasswordInput())
  message = forms.CharField(widget=forms.TextInput())
  birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
  favorite_colors = forms.MultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices=FAVORITE_COLORS_CHOICES,
  )