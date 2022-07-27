from django import forms
from .models import Student

# creating a form
class StudentForm(forms.ModelForm):
    # create meta class
    class Meta:
        model = Student
        fields = [
            "name", "age", "gender", "engineering_stream", "college", "place"
        ]
        
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'required': 'false'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'required': 'false'}),
            'engineering_stream': forms.Select(attrs={'class': 'form-control', 'required': 'false'}),
            'college': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
        }
        # fields = "__all__"
        