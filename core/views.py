import boto3

from botocore.config import Config
from botocore.exceptions import ClientError
from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView

from .serializers import PresignedURLSerializer


class GetPresignedURLView(APIView):
    def post(self, request: Request) -> Response:
        serializer = PresignedURLSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        config = Config(
            signature_version='s3v4',
        )

        client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION_NAME,
            config=config
        )

        fields = {
            'acl': 'public-read',
            'Content-Type': serializer.data['type']
        }

        conditions = [
            {'acl': 'public-read'},
            {'Content-Type': serializer.data['type']}
        ]

        try:
            response = client.generate_presigned_post(
                Bucket=settings.AWS_S3_BUCKET_NAME,
                Conditions=conditions,
                Fields=fields,
                Key=serializer.data['object_name'],
            )

            return Response(response, status=HTTP_200_OK)
        except ClientError as e:
            return Response({'error': str(e)}, status=HTTP_503_SERVICE_UNAVAILABLE)
