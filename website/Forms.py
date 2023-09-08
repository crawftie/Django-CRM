from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Record, Doctor_Specialism, Doctor_Record, Hospital_Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class AddUserRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    opco = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OpCo", "class":"form-control"}), label="")
    department = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Department", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)

class AddDoctorRecordForm(ModelForm):
    class Meta:
        model = Doctor_Record
        fields = ('doctor_first_name', 'doctor_last_name', 'doctor_email_address', 'doctor_specialism')
        labels = {
                'doctor_first_name': '',
                'doctor_last_name': '',
                'doctor_email_address': '',
                'doctor_specialism': 'doctor_specialism'
        }
        widgets = {
                'doctor_first_name': forms.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),
                'doctor_last_name': forms.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}),
                'doctor_email_address': forms.EmailInput(attrs={"placeholder":"Email", "class":"form-control"}),
                'doctor_specialism': forms.Select(attrs={"placeholder":"Doctor Specialism", "class":"form-select"}),
        }

class AddSpecialismRecordForm(forms.ModelForm):
    specialism_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Specialism Name", "class":"form-control"}), label="")
    specialism_description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Specialism Description", "class":"form-control"}), label="")

    class Meta:
        model = Doctor_Specialism
        fields = ('specialism_name', 'specialism_description')
        exclude = ("user",)

class AddHospitalRecordForm(ModelForm):
        class Meta:
            model = Hospital_Record
            fields ={
                'hospital_name': '',
                'hospital_address': '',
                'hospital_postcode': '',
                'hospital_email_address': '',
                'hospital_phone_number': '',
                'hospital_doctors': ''
            }
            widgets ={
                'hospital_name': forms.TextInput(attrs={"placeholder":"Hospital Name", "class":"form-control"}),
                'hospital_address': forms.TextInput(attrs={"placeholder":"Hospital Address", "class":"form-control"}),
                'hospital_postcode': forms.TextInput(attrs={"placeholder":"Hospital Postcode", "class":"form-control"}),
                'hospital_email_address': forms.EmailInput(attrs={"placeholder":"Email", "class":"form-control"}),
                'hospital_phone_number': forms.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}),
                'hospital_doctors': forms.SelectMultiple(attrs={"placeholder":"Hospital Doctors", "class":"form-select"}),
            }