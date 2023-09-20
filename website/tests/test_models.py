from django.test import TestCase
from website.models import Doctor_Specialism, Doctor_Record, Hospital_Record

class ModelTests(TestCase):
    def setUp(self):
        # Create a Doctor Specialism
        self.specialism = Doctor_Specialism.objects.create(
            specialism_name='Cardiology',
            specialism_description='Study of the heart and blood vessels'
        )

    def test_create_doctor_specialism(self):
        self.assertEqual(self.specialism.specialism_name, 'Cardiology')
        self.assertEqual(self.specialism.specialism_description, 'Study of the heart and blood vessels')

    def test_create_doctor_record(self):
        doctor = Doctor_Record.objects.create(
            doctor_first_name='John',
            doctor_last_name='Doe',
            doctor_email_address='john@example.com',
            doctor_specialism=self.specialism
        )
        self.assertEqual(doctor.doctor_first_name, 'John')
        self.assertEqual(doctor.doctor_last_name, 'Doe')
        self.assertEqual(doctor.doctor_email_address, 'john@example.com')
        self.assertEqual(doctor.doctor_specialism, self.specialism)

    def test_create_hospital_record(self):
        hospital = Hospital_Record.objects.create(
            hospital_name='City Hospital',
            hospital_address='123 Main St',
            hospital_postcode='12345',
            hospital_email_address='info@cityhospital.com',
            hospital_phone_number='555-123-4567',
        )
        self.assertEqual(hospital.hospital_name, 'City Hospital')
        self.assertEqual(hospital.hospital_address, '123 Main St')
        self.assertEqual(hospital.hospital_postcode, '12345')
        self.assertEqual(hospital.hospital_email_address, 'info@cityhospital.com')
        self.assertEqual(hospital.hospital_phone_number, '555-123-4567')
