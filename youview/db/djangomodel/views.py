from django.shortcuts import render
from youview.db.djangomodel.models import Log

def create_error_log():
    Log.objects.create(remarks="CREATE")
