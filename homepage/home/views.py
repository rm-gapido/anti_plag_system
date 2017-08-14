from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import utils
from .forms import DocumentForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'user_home.html')

def procedure(request):
    return render(request, 'user_procedure.html')

def document_title(request):

    if request.method == 'GET':
        pass
        # pprint('Accessing GET method ...')
        # form = DocumentForm()

    elif request.method == 'POST':
        doc_title = 'Sample'
        doc_type = 'T_WRITTEN'
        doc_pages = 10

        utils.create_dir(doc_title)
        # TODO: Magscan si raspi, tapos isave sa SCANNED_FILES_DIR ni utils.py

        utils.gen_pdf_from_dir(doc_title)


        # form = DocumentForm(request.POST)
        # print('Accessing POST method ...')
        # print(form)
        # utils.create_dir(form.document_title)

    return render (request, 'document-title.html', {})