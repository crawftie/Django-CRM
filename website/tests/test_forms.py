from django.test import TestCase
from django.urls import reverse
from website.models import Doctor_Record, Doctor_Specialism, Hospital_Record
from website.Forms import AddDoctorRecordForm, AddSpecialismRecordForm, AddHospitalRecordForm

class FormTests(TestCase):
    def setUp(self):
        # Create a Doctor Specialism object to be associated with the Doctor_Record
        self.specialism = Doctor_Specialism.objects.create(
            specialism_name='Cardiology',
            specialism_description='Study of the heart and blood vessels'
        )
         # Create Doctor_Record objects to be associated with the Hospital_Record
        self.doctor1 = Doctor_Record.objects.create(
            doctor_first_name='James',
            doctor_last_name='Raynor',
            doctor_email_address='James.Raynor@StarCraft.com',
        )
        self.doctor2 = Doctor_Record.objects.create(
            doctor_first_name='Sarah',
            doctor_last_name='Kerrigan',
            doctor_email_address='Sarah.Kerrigan@StarCraft.com',
        )


    def test_add_doctor_record_form_valid(self):
        # Create a valid form data dictionary
        form_data = {
            'doctor_first_name': 'Tychus',
            'doctor_last_name': 'Findlay',
            'doctor_email_address': 'Tychus.Findlay@StarCraft.com',
            'doctor_specialism': self.specialism.id,
        }
        form = AddDoctorRecordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_add_specialism_record_form_valid(self):
        # Create a valid form data dictionary
        form_data = {
            'specialism_name': 'Cardiology',
            'specialism_description': 'Study of the heart and blood vessels',
        }
        form = AddSpecialismRecordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_add_hospital_record_form_valid(self):
        # Create a valid form data dictionary
        form_data = {
            'hospital_name': 'Korhal Hospital',
            'hospital_address': '123 Terran St',
            'hospital_postcode': 'SC2 2BW',
            'hospital_email_address': 'Korhal@StarCraft.com',
            'hospital_phone_number': '00000 111111',
            'hospital_doctors': [self.doctor1.id, self.doctor2.id],
        }
        form = AddHospitalRecordForm(data=form_data)
        self.assertTrue(form.is_valid())
