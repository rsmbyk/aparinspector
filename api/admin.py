from django.contrib import admin

from api.models import Apar, InspectionReport, VerificationReport, PressureReport, QRCode

admin.site.register (Apar)
admin.site.register (InspectionReport)
admin.site.register (VerificationReport)
admin.site.register (PressureReport)
admin.site.register (QRCode)