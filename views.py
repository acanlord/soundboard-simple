import requests
from django.http import HttpResponse
from django.shortcuts import render

# Uploads
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage




def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Check out some sounds</h1>
        <a href="/sound">Sound Test</a> <br />
        <a href="/uploads">Upload a file</a> <br />
    ''')


def sound(request):
    context = {}
    return render(request, 'sound.html', context) 


def uploads(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploads.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'uploads.html')
