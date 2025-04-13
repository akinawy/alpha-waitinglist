from django.contrib import admin
from .models import WaitingUser, PDFDownloadUser
admin.site.register(WaitingUser)
admin.site.register(PDFDownloadUser)