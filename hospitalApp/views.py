from django.shortcuts import render
from .models import *
from .forms import patient_detailsForm
from django.http import HttpResponseRedirect
import os
import boto3
from pathlib import Path


# Create your views here.

def index(request):
    return render(request, 'index.html')

def downloads(request):
    # patitent details form
    
    if request.method == 'POST':
        form = patient_detailsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/downloads')
    else:
        form = patient_detailsForm()
    
    # patient details table
    patient_details_table = patient_details.objects.all()

    # create a s3 bucket and allow public access to upload files
            #upload it to an s3 bucket
    s3 = boto3.resource('s3')
    #create a bucket and make it public
    s3.create_bucket(Bucket='hospital-data-2147220')
    #upload all files in the documents folder to the s3 bucket
    for file in os.listdir('/home/joseph/Desktop/cc_exam/documents/documents'):
        s3.Object('hospital-data-2147220', file).put(Body=open('/'+file, 'rb'))
    #make the files public


        
    return render(request, 'downloads.html', {'form': form, 'patient_details_table': patient_details_table})
    
