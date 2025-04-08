from django.urls import path
from .views import AddToWaitingListAPIView, PDFDownloadUsersAPIView

urlpatterns = [
    path('waiting-users/', AddToWaitingListAPIView.as_view(), name='waiting-users'),
    path('send_pdf/', PDFDownloadUsersAPIView.as_view(), name='pdf-download'),

]
