from django.contrib import admin
from .models import Record, Doctor_Record, Hospital_Record, Doctor_Specialism

admin.site.register(Record)
admin.site.register(Doctor_Record)
admin.site.register(Hospital_Record)
admin.site.register(Doctor_Specialism)


