from django.shortcuts import render
from youview.db.uv_djangomodel.models import Log

def create_error_log():
    Log.objects.create(remarks="CREATE")
