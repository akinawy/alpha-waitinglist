from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import WaitingUser, PDFDownloadUser
from .serializers import WaitingUserSerializer, PDFDownloadUserSerializer
from .utils import send_email

class AddToWaitingListAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        language = request.data.get('language')
        if WaitingUser.objects.filter(email=email).exists():
            return Response({"message": "This email is already in the waiting list."},
                            status=status.HTTP_400_BAD_REQUEST)

        waiting_user = WaitingUser.objects.create(email=email, language=language)

        serializer = WaitingUserSerializer(waiting_user)

        return Response({"message": "User added to waiting list.", "user": serializer.data},
                        status=status.HTTP_201_CREATED)

class PDFDownloadUsersAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        language = request.data.get('language')
        if PDFDownloadUser.objects.filter(email=email).exists():
            return Response({"message": "This email already downloaded the pdf."},
                            status=status.HTTP_400_BAD_REQUEST)

        Pdfdownloader = PDFDownloadUser.objects.create(email=email, language=language)

        serializer = PDFDownloadUserSerializer(Pdfdownloader)
        send_email(email)
        return Response({"message": "PDF was sent successfully.", "user": serializer.data},
                        status=status.HTTP_201_CREATED)
