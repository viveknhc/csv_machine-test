
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from .models import User
from .serializers import UserSerializer

class UploadCSVView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')

        # Validate file type
        if not file or not file.name.endswith('.csv'):
            return Response({'error': 'Only .csv files are accepted.'}, status=status.HTTP_400_BAD_REQUEST)

        decoded_file = file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)
        valid_count, invalid_count = 0, 0
        errors = []

        for row in csv_reader:
            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                if not User.objects.filter(email=row['email']).exists():
                    serializer.save()
                    valid_count += 1
            else:
                invalid_count += 1
                errors.append({**row, 'errors': serializer.errors})

        return Response({
            'successfully_saved': valid_count,
            'rejected_records': invalid_count,
            'errors': errors
        }, status=status.HTTP_200_OK)
    