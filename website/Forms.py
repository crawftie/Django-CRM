from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from .models import Doctor_Specialism, Doctor_Record, Hospital_Record

# Form for signing up a new User of the system
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

from django import forms
from django.contrib.auth.forms import UserChangeForm

class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    # Add the superuser checkbox field
    is_superuser = forms.BooleanField(
        required=False,  # Optional field
        label="Make this user a superuser",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser']  # Include 'is_superuser' in the fields

    def __init__(self, *args, **kwargs):
        # Exclude the password field
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields.pop('password')

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/ -/_ only.</small></span>'


class UpdateUserPasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UpdateUserPasswordForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

User = get_user_model()

class AdminUpdateUserPasswordForm(forms.ModelForm):
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = []

    def save(self, commit=True):
        user = super(AdminUpdateUserPasswordForm, self).save(commit=False)
        new_password = self.cleaned_data['new_password']
        user.set_password(new_password)
        if commit:
            user.save()
        return user
# Form for creating / updating a Doctor Record
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

# Form for creating / updating a Doctor Specialism Record
class AddSpecialismRecordForm(ModelForm):
    class Meta:
        model = Doctor_Specialism
        fields = ('specialism_name', 'specialism_description')
        labels = {
            'specialism_name': '',
            'specialism_description': ''
        }
        widgets = {
            'specialism_name': forms.TextInput(attrs={"placeholder":"Specialism Name", "class":"form-control"}),
            'specialism_description': forms.TextInput(attrs={"placeholder":"Specialism Description", "class":"form-control"}),
        }

# Form for creating / updating a Hospital Record
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