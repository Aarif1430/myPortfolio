from django.shortcuts import render, HttpResponse
from django.views import generic
import os

# Create your views here.

class IndexView(generic.ListView):
    template_name='portfolio/index.html'

    def get_queryset(self):
        return 'Hello World..!'

def pdf_download(request):
	with open('portfolio/storage/cv.pdf', 'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline;filename=cv.pdf'
		return response

def deploying_django_app_with_wsgi_in_apache(request):
    return render(request, template_name='blog/django_deploy_aws.html')

def linear_regression_in_new_fashion(request):
    return render(request, template_name='blog/linear_regression_in_new_fashion.html')
    
class blogView(generic.ListView):
    template_name='blog/post_list.html'

    def get_queryset(self):
        return 'Hello World..!'


class aboutView(generic.ListView):

    template_name='portfolio/about.html'
    def get_queryset(self):
        return 'Hello World..!'