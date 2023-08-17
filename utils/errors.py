from email import message
from django.http import JsonResponse

from rest_framework.response import Response


def handler404(request,exception):
    error_message = ("الصفحة غير موجودة")
    response=JsonResponse(data={"error":error_message})
    response.status_code=404
    
    return response


def handler500(request):
    error_message = ("خطأ داخلي في الخادم")
    response=JsonResponse(data={"error":error_message})
    response.status_code=500
    return response