from django.db import models

# Model for Doctor Specialisms
class Doctor_Specialism(models.Model):
    specialism_name = models.CharField('Specialism Name', max_length=250)
    specialism_description = models.CharField('Specialism Description', max_length=1000)
    
    def __str__(self):
        return self.specialism_name

# Model for Doctor Record, Doctor_Specialism value is linked one to one with the Doctor Specialism Model       
class Doctor_Record(models.Model):
    doctor_created_at = models.DateTimeField(auto_now_add=True)
    doctor_first_name = models.CharField('First Name', max_length=50)
    doctor_last_name = models.CharField('Last Name', max_length=50)
    doctor_email_address = models.EmailField('Email Address', max_length=100)
    doctor_specialism = models.ForeignKey(Doctor_Specialism, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return(f"{self.doctor_first_name} {self.doctor_last_name}")

# Model for Hospital Record, Hospital_Doctors value is linked one to many with the Doctor Record Model    
class Hospital_Record(models.Model):
    hospital_created_at = models.DateTimeField(auto_now_add=True)
    hospital_name = models.CharField('Name', max_length=250)
    hospital_address = models.CharField('Address', max_length=250)
    hospital_postcode = models.CharField('Postcode', max_length=250)
    hospital_email_address = models.EmailField('Email Address', max_length=250)
    hospital_phone_number = models.CharField('Phone Number', max_length=250)
    hospital_doctors = models.ManyToManyField(Doctor_Record, blank=True)

    def __str__(self):
        return self.hospital_name

