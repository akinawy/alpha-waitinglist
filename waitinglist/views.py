from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import WaitingUser, PDFDownloadUser, TookAssessment
from .serializers import WaitingUserSerializer, PDFDownloadUserSerializer
from .utils import send_email
import json

class AddToWaitingListAPIView(APIView):
    def post(self, request):

        email = request.data.get('email')
        language = request.data.get('language')
        if WaitingUser.objects.filter(email=email).exists():
            return Response({"message": "This email is already in the waiting list."},
                            status=status.HTTP_400_BAD_REQUEST)

        waiting_user = WaitingUser.objects.create(email=email, language=language)

        serializer = WaitingUserSerializer(waiting_user)
        send_email(email_address=email, reason="waiting list", language=language)

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
        send_email(email_address=email, reason="PDF Download", language=language)
        return Response({"message": "PDF was sent successfully.", "user": serializer.data},
                        status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def Webhook_handler(request):
    try:
        payload = json.loads(request.body)

        email = None
        for answer in payload.get('form_response', {}).get('answers', []):
            if answer.get('field', {}).get('ref') == 'email_ref':  # email field ref
                email = answer.get('text')
            if answer.get('field', {}).get('ref') == 'comment_ref':
                comment = answer.get('text')

        score = payload.get('form_response', {}).get('calculated', [])
        language = "EN" if payload.get('form_response', {}).get('form_id', []) == "W8HgAXB9" else "AR"

        if score and email:
            send_email(email_address=email, reason="send score", language=language, score=score)
        TookAssessment.objects.create(email=email, score=score, comment=comment, language=language)
        return Response({"status": "success", "message": "Data received"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"status": "error", "message": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )