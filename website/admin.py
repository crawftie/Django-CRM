from django.contrib import admin
from .models import Doctor_Record, Hospital_Record, Doctor_Specialism

# Add MySQL DB's to Django Admin Page
admin.site.register(Doctor_Record)
admin.site.register(Hospital_Record)
admin.site.register(Doctor_Specialism)


