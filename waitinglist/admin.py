from django.contrib import admin
from .models import WaitingUser, PDFDownloadUser, TookAssessment
admin.site.register(WaitingUser)
admin.site.register(PDFDownloadUser)
admin.site.register(TookAssessment)